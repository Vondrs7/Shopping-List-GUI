# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(497, 282)
        MainMenu.setStyleSheet(u"QLabel#Instructions {\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"FreeSans\";\n"
"}\n"
"\n"
"QWidget#MainMenu {\n"
"background-color: rgb(0, 0, 34);\n"
"}\n"
"\n"
"QPushButton#Button_Cancel{\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton:hover#Button_Cancel{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}")
        self.frame = QFrame(MainMenu)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 492, 263))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Instructions = QLabel(self.frame)
        self.Instructions.setObjectName(u"Instructions")
        self.Instructions.setGeometry(QRect(160, 10, 181, 39))
        font = QFont()
        font.setFamilies([u"FreeSans"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.Instructions.setFont(font)
        self.Instructions.setStyleSheet(u"")
        self.Button_Cancel = QPushButton(self.frame)
        self.Button_Cancel.setObjectName(u"Button_Cancel")
        self.Button_Cancel.setGeometry(QRect(80, 170, 360, 40))
        font1 = QFont()
        font1.setFamilies([u"FreeSans"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.Button_Cancel.setFont(font1)
        self.Button_Cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Cancel.setStyleSheet(u"")

        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"Form", None))
        self.Instructions.setText(QCoreApplication.translate("MainMenu", u"Hlavn\u00ed menu", None))
        self.Button_Cancel.setText(QCoreApplication.translate("MainMenu", u"Konec", None))
    # retranslateUi

