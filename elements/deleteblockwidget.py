from PyQt5.QtWidgets import QAbstractItemView
from elements.blocksarea import BlocksArea

class DeleteBlockWidget(BlocksArea):

    def __init__(self, type, parent=None):
        super(DeleteBlockWidget, self).__init__(parent)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)

    def dropEvent(self, event):
        if event.source() and event.source() !=  self:
            super(DeleteBlockWidget, self).dropEvent(event)
            self.clear()