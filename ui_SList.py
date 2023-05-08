# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SList.ui'
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
from PySide6.QtWidgets import (QApplication, QColumnView, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_SList(object):
    def setupUi(self, SList):
        if not SList.objectName():
            SList.setObjectName(u"SList")
        SList.resize(1019, 609)
        SList.setStyleSheet(u"QWidget#SList {\n"
"background-color: rgb(0, 0, 34);\n"
"}\n"
"\n"
"QLabel#Instructions {\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#User_text {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#User_selected {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Label_error_message{\n"
"color: rgb(255, 0, 0);\n"
"font: 8pt \"FreeSans\";\n"
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
"QPushButton#Button_Delete{\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton#Button_Create{\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 2"
                        "0px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QColumnView#List{\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"FreeSans\";\n"
"border: 2px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"border-radius: 20px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"padding-top: 20px\n"
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
"QPushButton:hover#Button_Create{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QPushButton:hover#Button_Delete{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QPushButton:hover#Button_Edit{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QPushButton:hover#Button_Cancel{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
""
                        "\n"
"QColumnView:hover#List{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"}")
        self.frame = QFrame(SList)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 991, 591))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Label_error_message = QLabel(self.frame)
        self.Label_error_message.setObjectName(u"Label_error_message")
        self.Label_error_message.setGeometry(QRect(10, 570, 741, 16))
        font = QFont()
        font.setFamilies([u"FreeSans"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.Label_error_message.setFont(font)
        self.Label_error_message.setStyleSheet(u"")
        self.Button_Edit = QPushButton(self.frame)
        self.Button_Edit.setObjectName(u"Button_Edit")
        self.Button_Edit.setEnabled(True)
        self.Button_Edit.setGeometry(QRect(770, 160, 200, 60))
        font1 = QFont()
        font1.setFamilies([u"FreeSans"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.Button_Edit.setFont(font1)
        self.Button_Edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Edit.setStyleSheet(u"")
        self.Button_Cancel = QPushButton(self.frame)
        self.Button_Cancel.setObjectName(u"Button_Cancel")
        self.Button_Cancel.setGeometry(QRect(770, 300, 200, 60))
        self.Button_Cancel.setFont(font1)
        self.Button_Cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Cancel.setStyleSheet(u"")
        self.Instructions = QLabel(self.frame)
        self.Instructions.setObjectName(u"Instructions")
        self.Instructions.setGeometry(QRect(340, 10, 351, 39))
        font2 = QFont()
        font2.setFamilies([u"FreeSans"])
        font2.setPointSize(24)
        font2.setBold(False)
        font2.setItalic(False)
        self.Instructions.setFont(font2)
        self.Instructions.setStyleSheet(u"")
        self.Button_Create = QPushButton(self.frame)
        self.Button_Create.setObjectName(u"Button_Create")
        self.Button_Create.setEnabled(True)
        self.Button_Create.setGeometry(QRect(770, 90, 200, 60))
        self.Button_Create.setFont(font1)
        self.Button_Create.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Create.setStyleSheet(u"")
        self.Button_Delete = QPushButton(self.frame)
        self.Button_Delete.setObjectName(u"Button_Delete")
        self.Button_Delete.setEnabled(True)
        self.Button_Delete.setGeometry(QRect(770, 230, 200, 60))
        self.Button_Delete.setFont(font1)
        self.Button_Delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Delete.setStyleSheet(u"")
        self.List = QColumnView(self.frame)
        self.List.setObjectName(u"List")
        self.List.setGeometry(QRect(10, 90, 741, 471))
        self.User_text = QLabel(self.frame)
        self.User_text.setObjectName(u"User_text")
        self.User_text.setGeometry(QRect(20, 50, 101, 39))
        font3 = QFont()
        font3.setFamilies([u"FreeSans"])
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        self.User_text.setFont(font3)
        self.User_text.setStyleSheet(u"")
        self.User_selected = QLabel(self.frame)
        self.User_selected.setObjectName(u"User_selected")
        self.User_selected.setGeometry(QRect(110, 50, 341, 41))
        self.User_selected.setFont(font3)
        self.User_selected.setStyleSheet(u"")

        self.retranslateUi(SList)

        QMetaObject.connectSlotsByName(SList)
    # setupUi

    def retranslateUi(self, SList):
        SList.setWindowTitle(QCoreApplication.translate("SList", u"Form", None))
        self.Label_error_message.setText("")
        self.Button_Edit.setText(QCoreApplication.translate("SList", u"Upravit produkt", None))
        self.Button_Cancel.setText(QCoreApplication.translate("SList", u"Konec", None))
        self.Instructions.setText(QCoreApplication.translate("SList", u"N\u00e1kupn\u00ed L\u00edstek - JV", None))
        self.Button_Create.setText(QCoreApplication.translate("SList", u"P\u0159idat nov\u00fd produkt", None))
        self.Button_Delete.setText(QCoreApplication.translate("SList", u"Smazat produkt", None))
        self.User_text.setText(QCoreApplication.translate("SList", u"U\u017eivatel:", None))
        self.User_selected.setText("")
    # retranslateUi

