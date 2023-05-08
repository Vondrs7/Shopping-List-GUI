# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Choose_content.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListView,
    QPushButton, QSizePolicy, QWidget)

class Ui_Choose_content(object):
    def setupUi(self, Choose_content):
        if not Choose_content.objectName():
            Choose_content.setObjectName(u"Choose_content")
        Choose_content.resize(772, 520)
        Choose_content.setStyleSheet(u"QWidget#Choose_content {\n"
"background-color: rgb(0, 0, 34);\n"
"}\n"
"\n"
"QLabel#Instructions {\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Label_error_message{\n"
"color: rgb(255, 0, 0);\n"
"font: 8pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton#Button_show_all{\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton#Button_choose{\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton#Button_back{\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QListView#Content_list{\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"FreeSans\";\n"
"border: 2px solid rgb(255, 255, 255);\n"
"ba"
                        "ckground-color: rgb(0, 0, 53);\n"
"border-radius: 20px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"padding-top: 20px\n"
"}\n"
"\n"
"QPushButton:hover#Button_choose{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QPushButton:hover#Button_back{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QPushButton:hover#Button_show_all{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"\n"
"QListView:hover#Content_list{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"}")
        self.frame = QFrame(Choose_content)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 761, 511))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Content_list = QListView(self.frame)
        self.Content_list.setObjectName(u"Content_list")
        self.Content_list.setGeometry(QRect(20, 90, 521, 371))
        self.Instructions = QLabel(self.frame)
        self.Instructions.setObjectName(u"Instructions")
        self.Instructions.setGeometry(QRect(210, 20, 371, 39))
        font = QFont()
        font.setFamilies([u"FreeSans"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.Instructions.setFont(font)
        self.Instructions.setStyleSheet(u"")
        self.Button_show_all = QPushButton(self.frame)
        self.Button_show_all.setObjectName(u"Button_show_all")
        self.Button_show_all.setGeometry(QRect(560, 92, 181, 51))
        self.Button_choose = QPushButton(self.frame)
        self.Button_choose.setObjectName(u"Button_choose")
        self.Button_choose.setGeometry(QRect(560, 160, 181, 51))
        self.Button_back = QPushButton(self.frame)
        self.Button_back.setObjectName(u"Button_back")
        self.Button_back.setGeometry(QRect(560, 230, 181, 51))
        self.Label_error_message = QLabel(self.frame)
        self.Label_error_message.setObjectName(u"Label_error_message")
        self.Label_error_message.setGeometry(QRect(10, 490, 621, 20))
        font1 = QFont()
        font1.setFamilies([u"FreeSans"])
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        self.Label_error_message.setFont(font1)
        self.Label_error_message.setStyleSheet(u"")

        self.retranslateUi(Choose_content)

        QMetaObject.connectSlotsByName(Choose_content)
    # setupUi

    def retranslateUi(self, Choose_content):
        Choose_content.setWindowTitle(QCoreApplication.translate("Choose_content", u"Form", None))
        self.Instructions.setText(QCoreApplication.translate("Choose_content", u"Vybrat n\u00e1kup k zobrazen\u00ed", None))
        self.Button_show_all.setText(QCoreApplication.translate("Choose_content", u"Zobrazit v\u0161e", None))
        self.Button_choose.setText(QCoreApplication.translate("Choose_content", u"Potvrdit v\u00fdb\u011br", None))
        self.Button_back.setText(QCoreApplication.translate("Choose_content", u"Zp\u011bt", None))
        self.Label_error_message.setText("")
    # retranslateUi

