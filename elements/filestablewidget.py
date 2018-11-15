from PyQt5.QtWidgets import QCheckBox, QAbstractItemView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from elements.cb_header import CB_Table_Header

class FilesTableWidget(QTableWidget):
    filesdropped = pyqtSignal(str)

    def __init__(self, type, parent=None):
        super(FilesTableWidget, self).__init__(parent)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.initUI()
        self.checked = set()
        self.dragoutside = False

    def initUI(self):
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setDropIndicatorShown(True)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        # add checkbox in header for selecting all items
        CB_Select_Header = CB_Table_Header(Qt.Horizontal, self)
        self.setHorizontalHeader(CB_Select_Header)
        CB_Select_Header.stateUpdated.connect(self.selectAllItems)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super(FilesTableWidget, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            super(FilesTableWidget, self).dragMoveEvent(event)

    def dropEvent(self, event):
        # Drag and drop rows inside the table
        if not event.isAccepted() and event.source() == self:
            drop_row = self.drop_on(event)
            rows = sorted(set(item.row() for item in self.selectedItems()))
            rows_to_move = [[QTableWidgetItem(self.item(row_index, column_index)) for column_index in range(1, self.columnCount())]
                            for row_index in rows]
            for row_index in reversed(rows):
                self.removeRow(row_index)
                if row_index < drop_row:
                    drop_row -= 1

            self.setSelectionMode(QAbstractItemView.MultiSelection)

            for row_index, data in enumerate(rows_to_move):
                row_index += drop_row
                self.insertRow(row_index)

                for column_index, column_data in enumerate(data):
                    self.setCheckbox(row_index)
                    self.setItem(row_index, column_index + 1, column_data)

                self.selectRow(row_index)
                event.accept()

            self.setSelectionMode(QAbstractItemView.ExtendedSelection)
            super().dropEvent(event)
        # Drop external files
        else:
            if event.mimeData().hasUrls():
                event.setDropAction(Qt.CopyAction)
                event.accept()
                for url in event.mimeData().urls():
                    filepath = str(url.toLocalFile())
                    self.filesdropped.emit(filepath)
            else:
                event.setDropAction(Qt.MoveAction)
                super(FilesTableWidget, self).dropEvent(event)

    # https: // github.com/myrrkel/pyzik/blob/d65dd1b89df1ac7620884e46ba70076d4e192fe7/src/tableWidgetDragRows.py
    def drop_on(self, event):
        index = self.indexAt(event.pos())
        if not index.isValid():
            return self.rowCount()
        return index.row() + 1 if self.is_below(event.pos(), index) else index.row()

    def is_below(self, pos, index):
        rect = self.visualRect(index)
        margin = 2
        if pos.y() - rect.top() < margin:
            return False
        elif rect.bottom() - pos.y() < margin:
            return True
        return rect.contains(pos, True) and not (int(self.model().flags(index)) & Qt.ItemIsDropEnabled) and pos.y() >= rect.center().y()

    @pyqtSlot(bool)
    def selectAllItems(self, isChecked):
        for row in range(self.rowCount()):
            ch = self.cellWidget(row, 0).findChild(QCheckBox)
            path = self.item(row, 4).text()
            if isChecked:
                ch.setCheckState(Qt.Checked)
                self.checked.add(path)
            else:
                ch.setCheckState(Qt.Unchecked)
                self.checked.discard(path)

    def onStateChanged(self):
        ch = self.sender()
        ix = self.indexAt(ch.parentWidget().pos())
        currItem = self.item(ix.row(), 4)
        if ch.isChecked():
            self.checked.add(currItem.text())
        else:
            self.checked.discard(currItem.text())

    def addFile(self, file):
        index = self.rowCount()
        self.insertRow(index)
        self.setCheckbox(index)
        self.setItem(index, 1, QTableWidgetItem(file["in"]))
        self.setItem(index, 2, QTableWidgetItem(file["out"]))
        self.setItem(index, 3, QTableWidgetItem(file["ext"][1:]))
        self.setItem(index, 4, QTableWidgetItem(file["path"]))

        # Because all files are checked by default, they should be added to prop
        self.checked.add(file["path"])

    def updateFilenames(self, files):
        for row in range(self.rowCount()):
            filepath = self.item(row, 4).text()
            newFileName = files[filepath]["out"]
            self.setItem(row, 2, QTableWidgetItem(newFileName))

    def setCheckbox(self, row):
        ch = QCheckBox(parent=self)
        ch.setCheckState(Qt.Checked)
        ch.clicked.connect(self.onStateChanged)

         # Following is needed in order to center cb in cell
        cell_widget = QWidget()
        lay_out = QHBoxLayout(cell_widget)
        lay_out.addWidget(ch)
        lay_out.setAlignment(Qt.AlignCenter)
        lay_out.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(lay_out)
        self.setCellWidget(row, 0, cell_widget)

    def deleteFile(self, file):
        res = self.findItems(file, Qt.MatchExactly)
        row = res[0].row()
        self.removeRow(row)