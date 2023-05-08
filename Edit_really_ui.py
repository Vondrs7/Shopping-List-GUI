# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Edit_really.ui'
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

class Ui_Edit_really(object):
    def setupUi(self, Edit_really):
        if not Edit_really.objectName():
            Edit_really.setObjectName(u"Edit_really")
        Edit_really.resize(731, 174)
        Edit_really.setStyleSheet(u"QWidget#Edit_really {\n"
"background-color: rgb(0, 0, 34);\n"
"}\n"
"\n"
"QLabel#Instructions {\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton#Button_Edit{\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton#Button_Back{\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton:hover#Button_Edit{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QPushButton:hover#Button_Back{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}")
        self.frame = QFrame(Edit_really)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 721, 161))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Instructions = QLabel(self.frame)
        self.Instructions.setObjectName(u"Instructions")
        self.Instructions.setGeometry(QRect(60, 20, 611, 31))
        self.Button_Edit = QPushButton(self.frame)
        self.Button_Edit.setObjectName(u"Button_Edit")
        self.Button_Edit.setGeometry(QRect(140, 90, 161, 41))
        self.Button_Back = QPushButton(self.frame)
        self.Button_Back.setObjectName(u"Button_Back")
        self.Button_Back.setGeometry(QRect(380, 90, 161, 41))

        self.retranslateUi(Edit_really)

        QMetaObject.connectSlotsByName(Edit_really)
    # setupUi

    def retranslateUi(self, Edit_really):
        Edit_really.setWindowTitle(QCoreApplication.translate("Edit_really", u"Form", None))
        self.Instructions.setText(QCoreApplication.translate("Edit_really", u"Opravdu si p\u0159ejete upravit tento produkt ?", None))
        self.Button_Edit.setText(QCoreApplication.translate("Edit_really", u"Upravit produkt", None))
        self.Button_Back.setText(QCoreApplication.translate("Edit_really", u"Zav\u0159\u00edt okno", None))
    # retranslateUi

