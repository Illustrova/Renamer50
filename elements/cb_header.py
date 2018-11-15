from PyQt5.QtCore import Qt, pyqtSignal, QRect
from PyQt5.QtWidgets import QHeaderView, QStyle, QStyleOptionButton

# https: // stackoverflow.com/questions/9744975/pyside-pyqt4-adding-a-checkbox-to-qtablewidget-horizontal-column-header
class CB_Table_Header(QHeaderView):
    isOn = True
    stateUpdated = pyqtSignal(bool)

    def __init__(self, orientation, parent=None):
        QHeaderView.__init__(self, orientation, parent)
        self.setDefaultAlignment(Qt.AlignCenter)
        self.setSectionResizeMode(QHeaderView.Interactive)
        self.setDefaultSectionSize(250)

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        QHeaderView.paintSection(self, painter, rect, logicalIndex)
        painter.restore()
        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(10, 10, 10, 10)
            if self.isOn:
                option.state = QStyle.State_On
            else:
                option.state = QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)
        self.resizeSection(0, 34)
        self.resizeSection(3, 50)

    def mousePressEvent(self, event):
        self.isOn = not self.isOn
        self.updateSection(0)
        QHeaderView.mousePressEvent(self, event)
        self.stateUpdated.emit(self.isOn)