from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QPushButton, QAbstractItemView
from PyQt5.QtGui import QDropEvent
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot

class BlocksArea(QListWidget):
    newdrop = pyqtSignal()
    def __init__(self, type, parent=None):
        super(BlocksArea, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.setDropAction(Qt.MoveAction)
            event.accept()
            super(BlocksArea, self).dragEnterEvent(event)
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
            super(BlocksArea, self).dropEvent(event)
            event.accept()
            self.newdrop.emit()
        else:
            event.ignore()

    def addBlock(self, data):
        b = QListWidgetItem(data["prettyValue"])
        b.setData(Qt.UserRole, data)
        self.addItem(b)

    def removeAllBlocks(self):
        self.clear()
