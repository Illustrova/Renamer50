# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'full.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1223, 620)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 800))
        self.centralwidget.setStyleSheet("QLabel, QRadioButton, QCheckBox, QComboBox, QTextEdit, QWidget, QSpinBox {\n"
"font-family: Arial;\n"
"font-size: 12px;\n"
"}\n"
"QPushButton {\n"
"font-family: Arial;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QLabel#Lbl_Word_Separators_Subtitle {\n"
"font-family: Arial;\n"
"font-size: 9px;\n"
"}\n"
"\n"
"QLabel#Lbl_Status {\n"
"font-weight:bold;\n"
"}\n"
"\n"
"\n"
"QListView#listW_New_Pattern {\n"
"border: 2px dashed rgb(180, 180, 180); \n"
"border-radius: 5px;\n"
"padding: 6px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QLabel#Lbl_PreviewBlock {\n"
"font-family: Arial;\n"
"}\n"
"\n"
"QListView::item {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(254, 255, 179, 230), stop:1 rgba(254, 255, 192, 230));\n"
"padding: 2px;\n"
"margin: 2px;\n"
"border: 1px solid rgb(238, 224, 71);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(255, 237, 172), stop:1 rgb(255, 246, 196));\n"
"color: rgb(116, 113, 25)\n"
"}\n"
"\n"
"QListView#listW_BlocksArea {\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(231, 237, 255), stop:1 rgb(226, 253, 255)); \n"
"border: 2px ridge  #50A3F0;\n"
"border-radius: 5px;\n"
"padding: 6px;\n"
"}\n"
"\n"
"#Lbl_PreviewBlock {\n"
"background-color:  rgb(240, 240, 240);\n"
"border: 0px;\n"
"}\n"
"\n"
"QListWidget#W_DeleteBlock {\n"
"border: 2px dashed rgb(220, 220, 220); \n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background: transparent;\n"
"background-image: url(res/trash2.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    border-bottom-left-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    color: #F0F0F0;\n"
"    min-width: 60px;\n"
"    min-height: 20px;\n"
"    padding: 3px 8px 3px 8px;\n"
"    margin:1px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 #489CEA); \n"
"}\n"
"\n"
"QToolBox::tab:selected, QToolBox::tab:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
"QPushButton#Btn_Confirm {\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    padding: 10px;    \n"
"    min-height: 10px;\n"
"    border-radius:5px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(33, 227, 110), stop:1 rgb(39, 175, 94)); \n"
"}\n"
"\n"
"QPushButton#Btn_Delete {\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    padding: 10px;    \n"
"    min-height: 10px;\n"
"    border-radius:5px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(253, 101, 98), stop:1 rgb(187, 48, 51)); \n"
"}\n"
"\n"
"QComboBox,QDateEdit{\n"
"    border-radius: 3px;\n"
"    padding: 1px 10px 1px 5px;\n"
"    border: 1px solid #50A3F0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down,QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 16px; \n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    border-left-color: #50A3F0;    \n"
"}\n"
"\n"
"QComboBox::down-arrow, QDateEdit::down-arrow {\n"
"  \n"
"image: url(res/arrow-down.png);\n"
"width: 9px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover,\n"
"QDateEdit::down-arrow:hover {\n"
"  \n"
"image: url(res/arrow-down-hover.png);\n"
"width: 9px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
".QLineEdit {\n"
"    border: 1px solid #50A3F0;\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"    background: none;\n"
"    selection-background-color: #0F7DBE;\n"
"}\n"
"\n"
".QGroupBox{\n"
"    border: 1px solid #50A3F0;\n"
"    border-radius: 5px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 12px;\n"
"    padding: 0px 5px 0px 5px;\n"
"    top:-2px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    padding: 10px;    \n"
"    min-height: 10px;\n"
"    border-radius:5px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 rgb(65, 113, 200)); \n"
"}\n"
"\n"
".QPushButton:hover{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 #489CEA);\n"
"}\n"
"\n"
".QPushButton:pressed{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#D4D4D4;\n"
"color: #909090;\n"
"}\n"
"\n"
"\n"
"QCheckBox {\n"
"    spacing: 2px; \n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    color: rgb(65, 113, 200);\n"
"}\n"
"\n"
"QRadioButton {\n"
"    spacing: 1px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 15px; \n"
"    height: 15px; \n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    width:15px; \n"
"    background-color:rgba(0,0,0,0%); \n"
"    padding-top:10px; \n"
"    padding-bottom:10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height:10px; \n"
"    background-color:rgba(0,0,0,0%); \n"
"    padding-left:10px; padding-right:10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    width:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 #489CEA); \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    height:10px;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 #489CEA); \n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    width:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    height:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical\n"
" {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal, QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    color: none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    color: none;\n"
"}\n"
"\n"
"\n"
"QScrollArea {\n"
"    border: 0px ; \n"
"}\n"
"\n"
"\n"
"QTableView {\n"
"    border: 1px solid #50A3F0; \n"
"    selection-background-color: #0F7DBE;\n"
"    selection-color: #F0F0F0;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    color: #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
"QTableView::item:hover {\n"
"    color: #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 #489CEA); \n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 5px; \n"
"    margin: 0px; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    padding:3px;\n"
"    margin:0px;\n"
"    color:#F0F0F0;\n"
"    border: 1px solid #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 #489CEA);\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Toolbox_BlockSettings = QtWidgets.QToolBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Toolbox_BlockSettings.sizePolicy().hasHeightForWidth())
        self.Toolbox_BlockSettings.setSizePolicy(sizePolicy)
        self.Toolbox_BlockSettings.setMinimumSize(QtCore.QSize(420, 260))
        self.Toolbox_BlockSettings.setMaximumSize(QtCore.QSize(420, 280))
        self.Toolbox_BlockSettings.setObjectName("Toolbox_BlockSettings")
        self.BlockText = QtWidgets.QWidget()
        self.BlockText.setGeometry(QtCore.QRect(0, 0, 420, 202))
        self.BlockText.setObjectName("BlockText")
        self.layoutWidget = QtWidgets.QWidget(self.BlockText)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 7, 411, 196))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.RB_Text_exactText = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RB_Text_exactText.sizePolicy().hasHeightForWidth())
        self.RB_Text_exactText.setSizePolicy(sizePolicy)
        self.RB_Text_exactText.setMinimumSize(QtCore.QSize(120, 25))
        self.RB_Text_exactText.setChecked(True)
        self.RB_Text_exactText.setObjectName("RB_Text_exactText")
        self.gridLayout_2.addWidget(self.RB_Text_exactText, 0, 0, 1, 1)
        self.Inp_Text_exactText = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Inp_Text_exactText.sizePolicy().hasHeightForWidth())
        self.Inp_Text_exactText.setSizePolicy(sizePolicy)
        self.Inp_Text_exactText.setObjectName("Inp_Text_exactText")
        self.gridLayout_2.addWidget(self.Inp_Text_exactText, 0, 1, 1, 2)
        self.RB_Text_Date = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RB_Text_Date.sizePolicy().hasHeightForWidth())
        self.RB_Text_Date.setSizePolicy(sizePolicy)
        self.RB_Text_Date.setMinimumSize(QtCore.QSize(120, 25))
        self.RB_Text_Date.setObjectName("RB_Text_Date")
        self.gridLayout_2.addWidget(self.RB_Text_Date, 1, 0, 1, 1)
        self.Inp_Text_Date = QtWidgets.QDateEdit(self.layoutWidget)
        self.Inp_Text_Date.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Inp_Text_Date.sizePolicy().hasHeightForWidth())
        self.Inp_Text_Date.setSizePolicy(sizePolicy)
        self.Inp_Text_Date.setMaximumSize(QtCore.QSize(110, 16777215))
        self.Inp_Text_Date.setCalendarPopup(True)
        self.Inp_Text_Date.setObjectName("Inp_Text_Date")
        self.gridLayout_2.addWidget(self.Inp_Text_Date, 1, 1, 1, 2)
        self.Sel_Text_DateFormat = QtWidgets.QComboBox(self.layoutWidget)
        self.Sel_Text_DateFormat.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sel_Text_DateFormat.sizePolicy().hasHeightForWidth())
        self.Sel_Text_DateFormat.setSizePolicy(sizePolicy)
        self.Sel_Text_DateFormat.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Sel_Text_DateFormat.setObjectName("Sel_Text_DateFormat")
        self.Sel_Text_DateFormat.addItem("")
        self.Sel_Text_DateFormat.addItem("")
        self.Sel_Text_DateFormat.addItem("")
        self.Sel_Text_DateFormat.addItem("")
        self.Sel_Text_DateFormat.addItem("")
        self.Sel_Text_DateFormat.addItem("")
        self.Sel_Text_DateFormat.addItem("")
        self.Sel_Text_DateFormat.addItem("")
        self.Sel_Text_DateFormat.addItem("")
        self.gridLayout_2.addWidget(self.Sel_Text_DateFormat, 1, 3, 1, 1)
        self.RB_Text_ParentFolder = QtWidgets.QRadioButton(self.layoutWidget)
        self.RB_Text_ParentFolder.setMinimumSize(QtCore.QSize(120, 25))
        self.RB_Text_ParentFolder.setObjectName("RB_Text_ParentFolder")
        self.gridLayout_2.addWidget(self.RB_Text_ParentFolder, 2, 0, 1, 1)
        self.RB_Text_OriginalName = QtWidgets.QRadioButton(self.layoutWidget)
        self.RB_Text_OriginalName.setMinimumSize(QtCore.QSize(120, 25))
        self.RB_Text_OriginalName.setObjectName("RB_Text_OriginalName")
        self.gridLayout_2.addWidget(self.RB_Text_OriginalName, 3, 0, 1, 1)
        self.RB_Text_Word = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RB_Text_Word.sizePolicy().hasHeightForWidth())
        self.RB_Text_Word.setSizePolicy(sizePolicy)
        self.RB_Text_Word.setMinimumSize(QtCore.QSize(150, 0))
        self.RB_Text_Word.setObjectName("RB_Text_Word")
        self.gridLayout_2.addWidget(self.RB_Text_Word, 4, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Lbl_Word_index = QtWidgets.QLabel(self.layoutWidget)
        self.Lbl_Word_index.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lbl_Word_index.sizePolicy().hasHeightForWidth())
        self.Lbl_Word_index.setSizePolicy(sizePolicy)
        self.Lbl_Word_index.setMinimumSize(QtCore.QSize(0, 11))
        self.Lbl_Word_index.setMaximumSize(QtCore.QSize(16777215, 11))
        self.Lbl_Word_index.setObjectName("Lbl_Word_index")
        self.verticalLayout_2.addWidget(self.Lbl_Word_index)
        self.Inp_Word_index = QtWidgets.QSpinBox(self.layoutWidget)
        self.Inp_Word_index.setEnabled(False)
        self.Inp_Word_index.setMinimumSize(QtCore.QSize(0, 22))
        self.Inp_Word_index.setMinimum(1)
        self.Inp_Word_index.setObjectName("Inp_Word_index")
        self.verticalLayout_2.addWidget(self.Inp_Word_index)
        spacerItem = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 4, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Lbl_Word_separators = QtWidgets.QLabel(self.layoutWidget)
        self.Lbl_Word_separators.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lbl_Word_separators.sizePolicy().hasHeightForWidth())
        self.Lbl_Word_separators.setSizePolicy(sizePolicy)
        self.Lbl_Word_separators.setMinimumSize(QtCore.QSize(0, 14))
        self.Lbl_Word_separators.setMaximumSize(QtCore.QSize(16777215, 14))
        self.Lbl_Word_separators.setObjectName("Lbl_Word_separators")
        self.verticalLayout_3.addWidget(self.Lbl_Word_separators)
        self.Inp_Word_Separators = QtWidgets.QLineEdit(self.layoutWidget)
        self.Inp_Word_Separators.setEnabled(False)
        self.Inp_Word_Separators.setMinimumSize(QtCore.QSize(0, 20))
        self.Inp_Word_Separators.setMaximumSize(QtCore.QSize(16777215, 22))
        self.Inp_Word_Separators.setObjectName("Inp_Word_Separators")
        self.verticalLayout_3.addWidget(self.Inp_Word_Separators)
        self.Lbl_Word_Separators_Subtitle = QtWidgets.QLabel(self.layoutWidget)
        self.Lbl_Word_Separators_Subtitle.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lbl_Word_Separators_Subtitle.sizePolicy().hasHeightForWidth())
        self.Lbl_Word_Separators_Subtitle.setSizePolicy(sizePolicy)
        self.Lbl_Word_Separators_Subtitle.setMinimumSize(QtCore.QSize(20, 14))
        self.Lbl_Word_Separators_Subtitle.setMaximumSize(QtCore.QSize(16777215, 14))
        self.Lbl_Word_Separators_Subtitle.setWordWrap(True)
        self.Lbl_Word_Separators_Subtitle.setObjectName("Lbl_Word_Separators_Subtitle")
        self.verticalLayout_3.addWidget(self.Lbl_Word_Separators_Subtitle)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 4, 2, 1, 2)
        self.Toolbox_BlockSettings.addItem(self.BlockText, "")
        self.BlockCount = QtWidgets.QWidget()
        self.BlockCount.setGeometry(QtCore.QRect(0, 0, 420, 202))
        self.BlockCount.setObjectName("BlockCount")
        self.layoutWidget1 = QtWidgets.QWidget(self.BlockCount)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 9, 408, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.RB_Number_Counter = QtWidgets.QRadioButton(self.layoutWidget1)
        self.RB_Number_Counter.setChecked(True)
        self.RB_Number_Counter.setObjectName("RB_Number_Counter")
        self.gridLayout_5.addWidget(self.RB_Number_Counter, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Lbl_Numbering_startFrom = QtWidgets.QLabel(self.layoutWidget1)
        self.Lbl_Numbering_startFrom.setObjectName("Lbl_Numbering_startFrom")
        self.gridLayout_3.addWidget(self.Lbl_Numbering_startFrom, 0, 0, 1, 1)
        self.Inp_Numbering_StartFrom = QtWidgets.QSpinBox(self.layoutWidget1)
        self.Inp_Numbering_StartFrom.setMaximum(999999999)
        self.Inp_Numbering_StartFrom.setObjectName("Inp_Numbering_StartFrom")
        self.gridLayout_3.addWidget(self.Inp_Numbering_StartFrom, 0, 1, 1, 1)
        self.Lbl_Numbering_LeadingZeroes = QtWidgets.QLabel(self.layoutWidget1)
        self.Lbl_Numbering_LeadingZeroes.setObjectName("Lbl_Numbering_LeadingZeroes")
        self.gridLayout_3.addWidget(self.Lbl_Numbering_LeadingZeroes, 1, 0, 1, 1)
        self.Inp_Numbering_LeadingZeroes = QtWidgets.QSpinBox(self.layoutWidget1)
        self.Inp_Numbering_LeadingZeroes.setObjectName("Inp_Numbering_LeadingZeroes")
        self.gridLayout_3.addWidget(self.Inp_Numbering_LeadingZeroes, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.RB_Number_Items = QtWidgets.QRadioButton(self.layoutWidget1)
        self.RB_Number_Items.setObjectName("RB_Number_Items")
        self.gridLayout_5.addWidget(self.RB_Number_Items, 1, 0, 1, 1)
        self.RB_Number_Folder = QtWidgets.QRadioButton(self.layoutWidget1)
        self.RB_Number_Folder.setObjectName("RB_Number_Folder")
        self.gridLayout_5.addWidget(self.RB_Number_Folder, 2, 0, 1, 1)
        self.Toolbox_BlockSettings.addItem(self.BlockCount, "")
        self.verticalLayout.addWidget(self.Toolbox_BlockSettings)
        self.Gr_Options = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Gr_Options.sizePolicy().hasHeightForWidth())
        self.Gr_Options.setSizePolicy(sizePolicy)
        self.Gr_Options.setMinimumSize(QtCore.QSize(420, 100))
        self.Gr_Options.setMaximumSize(QtCore.QSize(420, 120))
        self.Gr_Options.setObjectName("Gr_Options")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Gr_Options)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.CB_Separators_include = QtWidgets.QCheckBox(self.Gr_Options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CB_Separators_include.sizePolicy().hasHeightForWidth())
        self.CB_Separators_include.setSizePolicy(sizePolicy)
        self.CB_Separators_include.setObjectName("CB_Separators_include")
        self.gridLayout_4.addWidget(self.CB_Separators_include, 0, 0, 1, 1)
        self.CB_Case_change = QtWidgets.QCheckBox(self.Gr_Options)
        self.CB_Case_change.setObjectName("CB_Case_change")
        self.gridLayout_4.addWidget(self.CB_Case_change, 1, 0, 1, 1)
        self.Inp_Separator = QtWidgets.QLineEdit(self.Gr_Options)
        self.Inp_Separator.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Inp_Separator.sizePolicy().hasHeightForWidth())
        self.Inp_Separator.setSizePolicy(sizePolicy)
        self.Inp_Separator.setObjectName("Inp_Separator")
        self.gridLayout_4.addWidget(self.Inp_Separator, 0, 1, 1, 1)
        self.Sel_Case = QtWidgets.QComboBox(self.Gr_Options)
        self.Sel_Case.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sel_Case.sizePolicy().hasHeightForWidth())
        self.Sel_Case.setSizePolicy(sizePolicy)
        self.Sel_Case.setIconSize(QtCore.QSize(18, 16))
        self.Sel_Case.setFrame(True)
        self.Sel_Case.setObjectName("Sel_Case")
        self.Sel_Case.addItem("")
        self.Sel_Case.addItem("")
        self.Sel_Case.addItem("")
        self.gridLayout_4.addWidget(self.Sel_Case, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Lbl_PreviewBlock = QtWidgets.QLabel(self.Gr_Options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lbl_PreviewBlock.sizePolicy().hasHeightForWidth())
        self.Lbl_PreviewBlock.setSizePolicy(sizePolicy)
        self.Lbl_PreviewBlock.setMinimumSize(QtCore.QSize(100, 0))
        self.Lbl_PreviewBlock.setText("")
        self.Lbl_PreviewBlock.setAlignment(QtCore.Qt.AlignCenter)
        self.Lbl_PreviewBlock.setObjectName("Lbl_PreviewBlock")
        self.verticalLayout_4.addWidget(self.Lbl_PreviewBlock)
        self.Btn_AddBlock = QtWidgets.QPushButton(self.Gr_Options)
        self.Btn_AddBlock.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_AddBlock.sizePolicy().hasHeightForWidth())
        self.Btn_AddBlock.setSizePolicy(sizePolicy)
        self.Btn_AddBlock.setMinimumSize(QtCore.QSize(0, 30))
        self.Btn_AddBlock.setStyleSheet("")
        self.Btn_AddBlock.setObjectName("Btn_AddBlock")
        self.verticalLayout_4.addWidget(self.Btn_AddBlock)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addWidget(self.Gr_Options)
        self.listW_BlocksArea = BlocksArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listW_BlocksArea.sizePolicy().hasHeightForWidth())
        self.listW_BlocksArea.setSizePolicy(sizePolicy)
        self.listW_BlocksArea.setMinimumSize(QtCore.QSize(0, 80))
        self.listW_BlocksArea.setMaximumSize(QtCore.QSize(420, 200))
        self.listW_BlocksArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listW_BlocksArea.setFrameShape(QtWidgets.QFrame.Panel)
        self.listW_BlocksArea.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listW_BlocksArea.setFlow(QtWidgets.QListView.LeftToRight)
        self.listW_BlocksArea.setProperty("isWrapping", True)
        self.listW_BlocksArea.setModelColumn(0)
        self.listW_BlocksArea.setObjectName("listW_BlocksArea")
        self.verticalLayout.addWidget(self.listW_BlocksArea)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Lbl_NewFilename = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lbl_NewFilename.sizePolicy().hasHeightForWidth())
        self.Lbl_NewFilename.setSizePolicy(sizePolicy)
        self.Lbl_NewFilename.setMinimumSize(QtCore.QSize(0, 20))
        self.Lbl_NewFilename.setMaximumSize(QtCore.QSize(250, 20))
        self.Lbl_NewFilename.setIndent(1)
        self.Lbl_NewFilename.setObjectName("Lbl_NewFilename")
        self.gridLayout.addWidget(self.Lbl_NewFilename, 0, 0, 1, 1)
        self.W_DeleteBlock = DeleteBlockWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.W_DeleteBlock.sizePolicy().hasHeightForWidth())
        self.W_DeleteBlock.setSizePolicy(sizePolicy)
        self.W_DeleteBlock.setMinimumSize(QtCore.QSize(70, 0))
        self.W_DeleteBlock.setMaximumSize(QtCore.QSize(70, 16777215))
        self.W_DeleteBlock.setObjectName("W_DeleteBlock")
        self.gridLayout.addWidget(self.W_DeleteBlock, 0, 1, 2, 1)
        self.listW_New_Pattern = BlocksArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listW_New_Pattern.sizePolicy().hasHeightForWidth())
        self.listW_New_Pattern.setSizePolicy(sizePolicy)
        self.listW_New_Pattern.setMinimumSize(QtCore.QSize(340, 65))
        self.listW_New_Pattern.setMaximumSize(QtCore.QSize(340, 80))
        self.listW_New_Pattern.setAcceptDrops(True)
        self.listW_New_Pattern.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listW_New_Pattern.setFlow(QtWidgets.QListView.LeftToRight)
        self.listW_New_Pattern.setObjectName("listW_New_Pattern")
        self.gridLayout.addWidget(self.listW_New_Pattern, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.Line_Section_Separator = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Line_Section_Separator.sizePolicy().hasHeightForWidth())
        self.Line_Section_Separator.setSizePolicy(sizePolicy)
        self.Line_Section_Separator.setMinimumSize(QtCore.QSize(5, 0))
        self.Line_Section_Separator.setFrameShape(QtWidgets.QFrame.VLine)
        self.Line_Section_Separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line_Section_Separator.setObjectName("Line_Section_Separator")
        self.horizontalLayout_2.addWidget(self.Line_Section_Separator)
        self.Layout_right = QtWidgets.QVBoxLayout()
        self.Layout_right.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.Layout_right.setObjectName("Layout_right")
        self.Table_FilesList = FilesTableWidget(self.centralwidget)
        self.Table_FilesList.setMinimumSize(QtCore.QSize(12, 0))
        self.Table_FilesList.setAcceptDrops(True)
        self.Table_FilesList.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Table_FilesList.setMidLineWidth(-1)
        self.Table_FilesList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Table_FilesList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Table_FilesList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Table_FilesList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.Table_FilesList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Table_FilesList.setObjectName("Table_FilesList")
        self.Table_FilesList.setColumnCount(5)
        self.Table_FilesList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.Table_FilesList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_FilesList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_FilesList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_FilesList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_FilesList.setHorizontalHeaderItem(4, item)
        self.Table_FilesList.horizontalHeader().setVisible(True)
        self.Table_FilesList.horizontalHeader().setCascadingSectionResizes(False)
        self.Table_FilesList.horizontalHeader().setMinimumSectionSize(10)
        self.Table_FilesList.horizontalHeader().setSortIndicatorShown(True)
        self.Table_FilesList.horizontalHeader().setStretchLastSection(True)
        self.Table_FilesList.verticalHeader().setVisible(False)
        self.Table_FilesList.verticalHeader().setDefaultSectionSize(30)
        self.Table_FilesList.verticalHeader().setMinimumSectionSize(23)
        self.Layout_right.addWidget(self.Table_FilesList)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Btn_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Delete.setAutoFillBackground(False)
        self.Btn_Delete.setCheckable(False)
        self.Btn_Delete.setObjectName("Btn_Delete")
        self.horizontalLayout_5.addWidget(self.Btn_Delete)
        spacerItem2 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.Lbl_Status = QtWidgets.QLabel(self.centralwidget)
        self.Lbl_Status.setEnabled(True)
        self.Lbl_Status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Lbl_Status.setText("")
        self.Lbl_Status.setObjectName("Lbl_Status")
        self.horizontalLayout_5.addWidget(self.Lbl_Status)
        self.Btn_Confirm = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Confirm.sizePolicy().hasHeightForWidth())
        self.Btn_Confirm.setSizePolicy(sizePolicy)
        self.Btn_Confirm.setMinimumSize(QtCore.QSize(80, 30))
        self.Btn_Confirm.setObjectName("Btn_Confirm")
        self.horizontalLayout_5.addWidget(self.Btn_Confirm)
        self.Layout_right.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.Layout_right)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Toolbox_BlockSettings.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RB_Text_exactText.setText(_translate("MainWindow", "Exact text"))
        self.RB_Text_Date.setText(_translate("MainWindow", "Date"))
        self.Inp_Text_Date.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.Sel_Text_DateFormat.setItemText(0, _translate("MainWindow", "ddMMyy"))
        self.Sel_Text_DateFormat.setItemText(1, _translate("MainWindow", "yyMMdd"))
        self.Sel_Text_DateFormat.setItemText(2, _translate("MainWindow", "ddMMyyyy"))
        self.Sel_Text_DateFormat.setItemText(3, _translate("MainWindow", "yyyyMMdd"))
        self.Sel_Text_DateFormat.setItemText(4, _translate("MainWindow", "dd-MM-yy"))
        self.Sel_Text_DateFormat.setItemText(5, _translate("MainWindow", "yy-MM-dd"))
        self.Sel_Text_DateFormat.setItemText(6, _translate("MainWindow", "MMMM-d-yyyy"))
        self.Sel_Text_DateFormat.setItemText(7, _translate("MainWindow", "dd_MM_yy"))
        self.Sel_Text_DateFormat.setItemText(8, _translate("MainWindow", "yy_MM_dd"))
        self.RB_Text_ParentFolder.setText(_translate("MainWindow", "Directory name"))
        self.RB_Text_OriginalName.setText(_translate("MainWindow", "Original name"))
        self.RB_Text_Word.setText(_translate("MainWindow", "Word in current name"))
        self.Lbl_Word_index.setText(_translate("MainWindow", "Word index"))
        self.Lbl_Word_separators.setText(_translate("MainWindow", "Separators"))
        self.Lbl_Word_Separators_Subtitle.setText(_translate("MainWindow", "Use | to distinguish multiple separators"))
        self.Toolbox_BlockSettings.setItemText(self.Toolbox_BlockSettings.indexOf(self.BlockText), _translate("MainWindow", "Text"))
        self.RB_Number_Counter.setText(_translate("MainWindow", "Counter"))
        self.Lbl_Numbering_startFrom.setText(_translate("MainWindow", "Start from"))
        self.Lbl_Numbering_LeadingZeroes.setText(_translate("MainWindow", "Leading zeroes"))
        self.RB_Number_Items.setText(_translate("MainWindow", "Number of items in list"))
        self.RB_Number_Folder.setText(_translate("MainWindow", "Number of files in folder"))
        self.Toolbox_BlockSettings.setItemText(self.Toolbox_BlockSettings.indexOf(self.BlockCount), _translate("MainWindow", "Numbers"))
        self.Gr_Options.setTitle(_translate("MainWindow", "Options"))
        self.CB_Separators_include.setText(_translate("MainWindow", "Include separators"))
        self.CB_Case_change.setText(_translate("MainWindow", "Change case"))
        self.Sel_Case.setItemText(0, _translate("MainWindow", "lowercase"))
        self.Sel_Case.setItemText(1, _translate("MainWindow", "UPPERCASE"))
        self.Sel_Case.setItemText(2, _translate("MainWindow", "rEVERSE"))
        self.Btn_AddBlock.setText(_translate("MainWindow", "Add"))
        self.Lbl_NewFilename.setText(_translate("MainWindow", "Drop blocks here to create pattern:"))
        self.Table_FilesList.setSortingEnabled(True)
        item = self.Table_FilesList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Current filename"))
        item = self.Table_FilesList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New filename"))
        item = self.Table_FilesList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Filetype"))
        item = self.Table_FilesList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Path"))
        self.Btn_Delete.setText(_translate("MainWindow", "Delete selected"))
        self.Btn_Confirm.setText(_translate("MainWindow", "Rename"))

from elements.blocksarea import BlocksArea
from elements.deleteblockwidget import DeleteBlockWidget
from elements.filestablewidget import FilesTableWidget
