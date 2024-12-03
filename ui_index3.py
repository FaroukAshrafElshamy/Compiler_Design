# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index3.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 623)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color:#040f13;\n"
"}\n"
"#Side_Menu{\n"
"	padding:5px;\n"
"	margin-right:5px;\n"
"	background-color:#071e26;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton{\n"
"	padding:10px 10px 10px 20px;\n"
"	background-color:#040f13;\n"
"	border-radius:5px;\n"
"	text-align:left;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color:rgb(162, 154, 154);\n"
"	color:balck;\n"
"}\n"
"\n"
"#Main_body{\n"
"	background-color:#071e26;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"#textBrowser, #TextExplain{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"#textEdit, #tabWidget, QTextBrowser{\n"
"	padding:5px;\n"
"	background-color:#040f13;\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(110, -1, -1, -1)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Showcard Gothic"])
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.main_program = QFrame(self.centralwidget)
        self.main_program.setObjectName(u"main_program")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_program.sizePolicy().hasHeightForWidth())
        self.main_program.setSizePolicy(sizePolicy1)
        self.main_program.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_program.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_program)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Side_Menu = QFrame(self.main_program)
        self.Side_Menu.setObjectName(u"Side_Menu")
        self.Side_Menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.Side_Menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Side_Menu)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.Side_Menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(100, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ExplainButton = QPushButton(self.frame_4)
        self.ExplainButton.setObjectName(u"ExplainButton")
        icon = QIcon()
        icon.addFile(u":/icon/resources/compiler (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ExplainButton.setIcon(icon)
        self.ExplainButton.setCheckable(True)
        self.ExplainButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.ExplainButton)

        self.EditorButton = QPushButton(self.frame_4)
        self.EditorButton.setObjectName(u"EditorButton")
        icon1 = QIcon()
        icon1.addFile(u":/icon/resources/code.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.EditorButton.setIcon(icon1)
        self.EditorButton.setCheckable(True)
        self.EditorButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.EditorButton)

        self.OutputButton = QPushButton(self.frame_4)
        self.OutputButton.setObjectName(u"OutputButton")
        icon2 = QIcon()
        icon2.addFile(u":/icon/resources/output.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.OutputButton.setIcon(icon2)
        self.OutputButton.setCheckable(True)
        self.OutputButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.OutputButton)

        self.HubButton = QPushButton(self.frame_4)
        self.HubButton.setObjectName(u"HubButton")
        icon3 = QIcon()
        icon3.addFile(u":/icon/resources/digital-nomad-hub.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HubButton.setIcon(icon3)
        self.HubButton.setCheckable(True)
        self.HubButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.HubButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.AboutButton = QPushButton(self.frame_4)
        self.AboutButton.setObjectName(u"AboutButton")
        icon4 = QIcon()
        icon4.addFile(u":/icon/resources/information.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AboutButton.setIcon(icon4)
        self.AboutButton.setCheckable(True)
        self.AboutButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.AboutButton)

        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)
        self.pushButton_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u":/icon/resources/power-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_6)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.Side_Menu)

        self.Main_body = QFrame(self.main_program)
        self.Main_body.setObjectName(u"Main_body")
        sizePolicy.setHeightForWidth(self.Main_body.sizePolicy().hasHeightForWidth())
        self.Main_body.setSizePolicy(sizePolicy)
        self.Main_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.Main_body.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Main_body)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.Main_page = QStackedWidget(self.Main_body)
        self.Main_page.setObjectName(u"Main_page")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_5 = QHBoxLayout(self.page)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.TextExplain = QTextBrowser(self.page)
        self.TextExplain.setObjectName(u"TextExplain")

        self.horizontalLayout_5.addWidget(self.TextExplain)

        self.Main_page.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")
        font1 = QFont()
        font1.setPointSize(11)
        self.textEdit.setFont(font1)
        self.textEdit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)
        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setCursorWidth(3)
        self.textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextEditable|Qt.TextInteractionFlag.TextEditorInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_6.addWidget(self.textEdit)

        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(5555555, 35))
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.fileName = QLabel(self.frame)
        self.fileName.setObjectName(u"fileName")

        self.horizontalLayout_8.addWidget(self.fileName)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.RunButton = QPushButton(self.frame)
        self.RunButton.setObjectName(u"RunButton")
        self.RunButton.setMinimumSize(QSize(100, 0))
        icon6 = QIcon()
        icon6.addFile(u":/icon/resources/sharpen2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.RunButton.setIcon(icon6)

        self.horizontalLayout_8.addWidget(self.RunButton)

        self.Open_file = QPushButton(self.frame)
        self.Open_file.setObjectName(u"Open_file")
        self.Open_file.setMinimumSize(QSize(100, 0))
        self.Open_file.setMaximumSize(QSize(100, 16777215))
        self.Open_file.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Open_file.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/icon/resources/open-folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Open_file.setIcon(icon7)
        self.Open_file.setCheckable(True)
        self.Open_file.setAutoExclusive(False)

        self.horizontalLayout_8.addWidget(self.Open_file)

        self.ClearButton = QPushButton(self.frame)
        self.ClearButton.setObjectName(u"ClearButton")
        self.ClearButton.setMinimumSize(QSize(100, 0))
        self.ClearButton.setMaximumSize(QSize(100, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/icon/resources/rubber.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ClearButton.setIcon(icon8)

        self.horizontalLayout_8.addWidget(self.ClearButton)

        self.Save_file = QPushButton(self.frame)
        self.Save_file.setObjectName(u"Save_file")
        self.Save_file.setMinimumSize(QSize(100, 0))
        self.Save_file.setMaximumSize(QSize(100, 16777215))
        icon9 = QIcon()
        icon9.addFile(u":/icon/resources/floppy-disk.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Save_file.setIcon(icon9)

        self.horizontalLayout_8.addWidget(self.Save_file)


        self.verticalLayout_6.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignBottom)

        self.Main_page.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.TextOutput = QTextBrowser(self.tab)
        self.TextOutput.setObjectName(u"TextOutput")

        self.verticalLayout_7.addWidget(self.TextOutput)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.textBrowser_2 = QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.horizontalLayout_9.addWidget(self.textBrowser_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.Main_page.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_3 = QVBoxLayout(self.page_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.page_4)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(25)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.Main_page.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_6 = QHBoxLayout(self.page_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.page_5)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_7.addWidget(self.textBrowser)


        self.horizontalLayout_6.addWidget(self.widget)

        self.Main_page.addWidget(self.page_5)

        self.horizontalLayout_4.addWidget(self.Main_page)


        self.horizontalLayout.addWidget(self.Main_body)


        self.verticalLayout.addWidget(self.main_program)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_6.toggled.connect(MainWindow.close)

        self.Main_page.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CodeX", None))
        self.ExplainButton.setText(QCoreApplication.translate("MainWindow", u" Explain", None))
        self.EditorButton.setText(QCoreApplication.translate("MainWindow", u" Editor", None))
        self.OutputButton.setText(QCoreApplication.translate("MainWindow", u" Output", None))
        self.HubButton.setText(QCoreApplication.translate("MainWindow", u" Hub", None))
        self.AboutButton.setText(QCoreApplication.translate("MainWindow", u" About", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"  Exit", None))
        self.TextExplain.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icon/resources/Com"
                        "pilerPhases-Photoroom.png\" /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Code", None))
        self.fileName.setText("")
        self.RunButton.setText(QCoreApplication.translate("MainWindow", u"  Run", None))
        self.Open_file.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.ClearButton.setText(QCoreApplication.translate("MainWindow", u" Clear", None))
        self.Save_file.setText(QCoreApplication.translate("MainWindow", u"  Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Lexical Analysis", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Syntax Analysis", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Soon... The Hub", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-fam"
                        "ily:'Inter','Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Inter','Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Inter','Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:14pt; color:#ffffff;\">This project is developed by CodeX team:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                        " text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Inter','Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:10pt; color:#ffffff;\">Farouk Ashraf Farouk Elshamy.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Inter','Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:10pt; color:#ffffff;\"> </span><span style=\" font-size:10pt; color:#ffffff;\">Khaled Abdo Abdelhamed Elmakhashen</span><span style=\" font-family:'Inter','Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:10pt; color:#ffffff;\">.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Mohamed Mostafa Mohamed Abd"
                        "elhamed.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Omar Mohamed Ahmed Shetewy.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">Supervisor: Dr.Heba Hamed.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">______________________</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style="
                        "\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright \u00a9 2024-CodeX</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

