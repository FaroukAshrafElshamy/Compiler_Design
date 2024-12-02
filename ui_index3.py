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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTextBrowser, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 514)
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
"	padding:10px;\n"
"	padding-left:18px;\n"
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
"#textBrowser{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QWebEngineView{\n"
"	background-color:transparent;\n"
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

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setMinimumSize(QSize(100, 0))
        self.frame_5.setMaximumSize(QSize(150, 16777215))
        self.frame_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.AboutButton = QPushButton(self.frame_5)
        self.AboutButton.setObjectName(u"AboutButton")
        icon4 = QIcon()
        icon4.addFile(u":/icon/resources/information.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AboutButton.setIcon(icon4)
        self.AboutButton.setCheckable(True)
        self.AboutButton.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.AboutButton)

        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy3)
        self.pushButton_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u":/icon/resources/power-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.pushButton_6)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignmentFlag.AlignBottom)


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
        self.webEngineView = QWebEngineView(self.page)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.webEngineView)

        self.Main_page.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.Main_page.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.Main_page.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_3 = QVBoxLayout(self.page_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.page_4)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(25)
        self.label_2.setFont(font1)
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

