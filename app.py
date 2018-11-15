from PyQt5.QtCore import pyqtSlot, Qt, QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QRadioButton, QDateTimeEdit, QLineEdit, QComboBox, QCheckBox, QSpinBox
from design import Ui_MainWindow
import os
import sys
from model import MainModel
from controller import MainController
from utils import createFileData, findItemsInLayout

# Architecture adapted from https: // github.com/AntoineGagne/design-3-glo/blob/f672ad453a78b64d17fa8de861a5d9e6b64af774/design/ui/views/main_view.py
# Style adapted from: https://github.com/RedFalsh/PyQt5_stylesheets/blob/master/PyQt5_stylesheets/style_navy.css
class MainView(QMainWindow):
    def __init__(self, model: MainModel, controller: MainController):
        super().__init__()
        self.controller = controller
        self.model = model
        self.currentBlock = ""

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.saveControls()
        self.setupButtons()
        self.model.subscribe_update_function(self.updateFilenames)

    def saveControls(self):
        self.controls = {
            "radioButtons": self.ui.centralwidget.findChildren(QRadioButton),
            "dateEdits": self.ui.centralwidget.findChildren(QDateTimeEdit),
            "selects": self.ui.centralwidget.findChildren(QComboBox),
            "textEdits": self.ui.centralwidget.findChildren(QLineEdit),
            "checkboxes": self.ui.centralwidget.findChildren(QCheckBox),
            "counters": self.ui.centralwidget.findChildren(QSpinBox)
        }

    def setupButtons(self):
        self.ui.Btn_Delete.clicked.connect(self.deleteFiles)
        self.ui.Btn_Confirm.clicked.connect(self.runRename)
        self.ui.Btn_AddBlock.clicked.connect(self.addBlockToBlocksArea)

        self.ui.Table_FilesList.filesdropped.connect(self.addFile)
        self.ui.listW_New_Pattern.newdrop.connect(self.updatePattern)
        self.ui.listW_New_Pattern.model().rowsRemoved.connect(self.updatePattern)

        # Connect controls to onChange function
        self.ui.Toolbox_BlockSettings.currentChanged.connect(self.onChange)

        for rb in self.controls["radioButtons"]:
            rb.clicked.connect(self.onChange)

        for de in self.controls["dateEdits"]:
            de.setDateTime(QDateTime.currentDateTime())
            de.editingFinished.connect(self.onChange)

        for sel in self.controls["selects"]:
            sel.currentIndexChanged.connect(self.onChange)

        for ed in self.controls["textEdits"]:
            ed.textChanged.connect(self.onChange)

        for cb in self.controls["checkboxes"]:
            cb.stateChanged.connect(self.onChange)

        for c in self.controls["counters"]:
            c.valueChanged.connect(self.onChange)

    def resetButtons(self):
        for de in self.controls["dateEdits"]:
            de.setDateTime(QDateTime.currentDateTime())

        for sel in self.controls["selects"]:
            sel.currentIndex =  0

        for ed in self.controls["textEdits"]:
            ed.clear()

        for c in self.controls["counters"]:
            c.blockSignals(True)
            c.setValue(c.minimum())
            c.blockSignals(False)

        for cb in self.controls["checkboxes"] + self.controls["radioButtons"]:
            cb.blockSignals(True)
            if cb.autoExclusive():
                cb.setAutoExclusive(False)
                cb.setChecked(False)
                cb.setAutoExclusive(True)
            else:
                cb.setChecked(False)
            cb.blockSignals(False)

        self.currentBlock = None
        self.ui.Btn_AddBlock.setEnabled(False)

    @pyqtSlot()
    def onChange(self):
        # Toggle active/inactive  fields according radiobuttons/checkboxes
        if type(self.sender()) == QCheckBox or type(self.sender()) ==  QRadioButton:
            parentLayout = self.sender().parentWidget().findChildren(QGridLayout)[0]
            for row in range(parentLayout.rowCount()):
                item = parentLayout.itemAtPosition(row, 0)
                dependentsInRow = findItemsInLayout(
                        parentLayout, row, row+1, 1, parentLayout.columnCount())
                if item and item.widget() and item.widget().isChecked():
                    [w.setEnabled(True) for w in dependentsInRow]
                else:
                    [w.setEnabled(False) for w in dependentsInRow]
        # Create new block value
        block = self.createBlock()
        self.currentBlock = block
        if self.currentBlock and len(self.currentBlock) > 0:
            self.ui.Btn_AddBlock.setEnabled(True)
            self.currentBlock = block
            self.displayPreview()
        else:
            self.ui.Btn_AddBlock.setEnabled(False)

    @pyqtSlot()
    def updatePattern(self):
        pattern = self.ui.listW_New_Pattern
        modelP = pattern.model()
        modelP.rowCount()
        patternList = []
        for i in range(pattern.count()):
            patternList.append(pattern.item(i).data(Qt.UserRole))
        self.controller.updatePattern(patternList)

    def displayPreview(self):
        block = self.currentBlock
        previewArea = self.ui.Lbl_PreviewBlock
        if block:
            previewArea.setText(block["prettyValue"])
        else:
            previewArea.setText("")

    def addBlockToBlocksArea(self):
        if self.currentBlock:
            self.ui.listW_BlocksArea.addBlock(self.currentBlock)
        self.resetButtons()

    def createBlock(self):
        if self.ui.Toolbox_BlockSettings.currentIndex() == 0:
            return self.createTextBlock()
        elif self.ui.Toolbox_BlockSettings.currentIndex() == 1:
            return self.createNumberBlock()
        else:
            pass

    def createTextBlock(self):
        if self.ui.RB_Text_exactText.isChecked():
            data = self.ui.Inp_Text_exactText.text()
            if len(data) > 0:
                block = {
                    "value": data,
                    "case": self.resolveCase(),
                    "separator": self.resolveSeparator()
                }
                block["prettyValue"] = self.createPrettyValue(block)
                return block
        elif self.ui.RB_Text_Date.isChecked():
            data = self.ui.Inp_Text_Date.date()
            dateformat = self.ui.Sel_Text_DateFormat.currentText()
            block = {
                "value": data.toString(dateformat),
                "case": self.resolveCase(),
                "separator": self.resolveSeparator()
            }
            block["prettyValue"] = self.createPrettyValue(block)
            return block
        elif self.ui.RB_Text_ParentFolder.isChecked():
            block = {
                "value": "ParentDir",
                "case": self.resolveCase(),
                "separator": self.resolveSeparator()
            }
            block["prettyValue"] = self.createPrettyValue(block)
            return block

        elif self.ui.RB_Text_OriginalName.isChecked():
            block = {
                "value": "OriginalName",
                "case": self.resolveCase(),
                "separator": self.resolveSeparator()
            }
            block["prettyValue"] = self.createPrettyValue(block)
            return block

        elif self.ui.RB_Text_Word.isChecked():
            wordIndex = self.ui.Inp_Word_index.value()
            separators = (self.ui.Inp_Word_Separators.text()) if self.ui.Inp_Word_Separators.text() else ""
            block = {
                "value": "Word:" + str(wordIndex) + ":" + separators,
                "case": self.resolveCase(),
                "separator": self.resolveSeparator()
            }
            block["prettyValue"] = self.createPrettyValue(block)
            return block
        else:
            pass

    def createNumberBlock(self):
        if self.ui.RB_Number_Counter.isChecked():
            count = self.ui.Inp_Numbering_StartFrom.value()
            zeroes = self.ui.Inp_Numbering_LeadingZeroes.value() + len(str(count))
            block = {
                "value": "Nr:" + str(count).zfill(zeroes),
                "case": None,
                "separator": self.resolveSeparator()
            }
            block["prettyValue"] = self.createPrettyValue(block)
            return block

        elif self.ui.RB_Number_Folder.isChecked():
            block = {
                "value": "Nr:Folder",
                "case": None,
                "separator": self.resolveSeparator()
            }
            block["prettyValue"] = self.createPrettyValue(block)
            return block

        elif self.ui.RB_Number_Items.isChecked():
            block = {
                "value": "Nr:All",
                "case": None,
                "separator": self.resolveSeparator()
            }
            block["prettyValue"] = self.createPrettyValue(block)
            return block
        else:
            pass

    def resolveCase(self):
        if self.ui.CB_Case_change.isChecked():
            sel = self.ui.Sel_Case
            if sel.currentText() == "lowercase":
                return "L"
            elif sel.currentText() == "UPPERCASE":
                return "U"
            elif sel.currentText() == "rEVERSE":
                return "R"
            else:
                return None
        else:
            return None

    def resolveSeparator(self):
        if self.ui.CB_Separators_include.isChecked():
            return self.ui.Inp_Separator.text()
        else:
            return None

    def createPrettyValue(self, block):
        previewString = block["value"]
        if block["separator"]:
           previewString += block["separator"]
        if block["case"]:
            if block["case"] == "L":
                previewString += u"\u2193"
            elif block["case"] == "U":
                previewString += u"\u2191"
            elif block["case"] == "R":
                previewString += u"\u2191\u2193"
            else:
                pass
        return previewString

    def updateFilenames(self):
        self.controller.updateFilenames()
        self.ui.Table_FilesList.updateFilenames(self.model.files)

    @pyqtSlot(str)
    def addFile(self, filepath):
        if os.path.isfile(filepath):
            if filepath not in self.model.files:
                file = createFileData(filepath)
                self.controller.addFile({filepath: file})
                self.ui.Table_FilesList.addFile(file)

    def deleteFiles(self):
        files = self.ui.Table_FilesList.checked.copy()
        for file in files:
            self.deleteFile(file)

    def deleteFile(self, filepath):
        if filepath in self.model.files:
            self.controller.deleteFile(filepath)
            self.ui.Table_FilesList.deleteFile(filepath)
            self.ui.Table_FilesList.checked.discard(filepath)

    def runRename(self):
        files = self.ui.Table_FilesList.checked.copy()
        if not files:
            self.ui.Lbl_Status.setText("No files selected")
            self.ui.Lbl_Status.setStyleSheet("color:red;")
        else:
            filesNameExists = 0
            filesNameNotDefined = 0
            for file in files:
                if self.model.files[file]["out"] and len(self.model.files[file]["out"]) > 0:
                    try:
                        newPath = os.path.join(os.path.dirname(
                            file), self.model.files[file]["out"] + self.model.files[file]["ext"])
                        os.rename(file, newPath)
                        self.deleteFile(file)
                    except FileExistsError:
                        filesNameExists += 1
                else:
                    filesNameNotDefined += 1
            if filesNameExists:
                self.ui.Lbl_Status.setText(
                    "%d files were not renamed, because another file with same name exists" % (filesNameExists))
                self.ui.Lbl_Status.setStyleSheet("color:red;")
            elif filesNameNotDefined:
                self.ui.Lbl_Status.setText(
                    "%d files were not renamed, because new name not defined" % (filesNameNotDefined))
                self.ui.Lbl_Status.setStyleSheet("color:red;")
            else:
                self.ui.Lbl_Status.setText("All files renamed successfully!")
                self.ui.Lbl_Status.setStyleSheet("color:green;")
                self.ui.listW_New_Pattern.removeAllBlocks()
                self.controller.resetPattern()

class RenamerApp(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.main_model = MainModel()
        self.main_controller = MainController(self.main_model)
        self.main_view = MainView(self.main_model, self.main_controller)
        self.main_view.show()

def main():
    app = RenamerApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()