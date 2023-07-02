# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Users_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_Users_menu(object):
    def setupUi(self, Users_menu):
        if not Users_menu.objectName():
            Users_menu.setObjectName(u"Users_menu")
        Users_menu.setWindowModality(Qt.NonModal)
        Users_menu.resize(509, 324)
        Users_menu.setContextMenuPolicy(Qt.DefaultContextMenu)
        Users_menu.setStyleSheet(u"QWidget#Users_menu {\n"
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
"font: 10pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton#Button_Select{\n"
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
"border-radius: 20px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QListWidget#Users{\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"FreeSans\";\n"
"border: 2px solid rgb(255, 255, 255);\n"
"background"
                        "-color: rgb(0, 0, 53);\n"
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
"QPushButton:hover#Button_Select{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QPushButton:hover#Button_Cancel{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QListWidget:hover#Users{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"}")
        self.aa = QFrame(Users_menu)
        self.aa.setObjectName(u"aa")
        self.aa.setGeometry(QRect(10, 10, 488, 311))
        self.aa.setFrameShape(QFrame.StyledPanel)
        self.aa.setFrameShadow(QFrame.Raised)
        self.Label_error_message = QLabel(self.aa)
        self.Label_error_message.setObjectName(u"Label_error_message")
        self.Label_error_message.setGeometry(QRect(40, 269, 411, 31))
        font = QFont()
        font.setFamilies([u"FreeSans"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.Label_error_message.setFont(font)
        self.Label_error_message.setStyleSheet(u"")
        self.Button_Select = QPushButton(self.aa)
        self.Button_Select.setObjectName(u"Button_Select")
        self.Button_Select.setEnabled(True)
        self.Button_Select.setGeometry(QRect(310, 120, 150, 40))
        font1 = QFont()
        font1.setFamilies([u"FreeSans"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.Button_Select.setFont(font1)
        self.Button_Select.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Select.setStyleSheet(u"")
        self.Button_Cancel = QPushButton(self.aa)
        self.Button_Cancel.setObjectName(u"Button_Cancel")
        self.Button_Cancel.setGeometry(QRect(310, 220, 150, 40))
        self.Button_Cancel.setFont(font1)
        self.Button_Cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Cancel.setStyleSheet(u"")
        self.Instructions = QLabel(self.aa)
        self.Instructions.setObjectName(u"Instructions")
        self.Instructions.setGeometry(QRect(140, 10, 221, 39))
        font2 = QFont()
        font2.setFamilies([u"FreeSans"])
        font2.setPointSize(24)
        font2.setBold(False)
        font2.setItalic(False)
        self.Instructions.setFont(font2)
        self.Instructions.setStyleSheet(u"")
        self.Users = QListWidget(self.aa)
        self.Users.setObjectName(u"Users")
        self.Users.setGeometry(QRect(30, 70, 256, 191))
        self.Button_Create = QPushButton(self.aa)
        self.Button_Create.setObjectName(u"Button_Create")
        self.Button_Create.setEnabled(True)
        self.Button_Create.setGeometry(QRect(310, 70, 150, 40))
        self.Button_Create.setFont(font1)
        self.Button_Create.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Create.setStyleSheet(u"")
        self.Button_Delete = QPushButton(self.aa)
        self.Button_Delete.setObjectName(u"Button_Delete")
        self.Button_Delete.setEnabled(True)
        self.Button_Delete.setGeometry(QRect(310, 170, 150, 40))
        self.Button_Delete.setFont(font1)
        self.Button_Delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Delete.setStyleSheet(u"")

        self.retranslateUi(Users_menu)

        QMetaObject.connectSlotsByName(Users_menu)
    # setupUi

    def retranslateUi(self, Users_menu):
        Users_menu.setWindowTitle(QCoreApplication.translate("Users_menu", u"N\u00e1kupn\u00ed L\u00edstek JV", None))
        self.Label_error_message.setText("")
        self.Button_Select.setText(QCoreApplication.translate("Users_menu", u"Vybrat", None))
        self.Button_Cancel.setText(QCoreApplication.translate("Users_menu", u"Konec", None))
        self.Instructions.setText(QCoreApplication.translate("Users_menu", u"V\u00fdb\u011br u\u017eivatele", None))
        self.Button_Create.setText(QCoreApplication.translate("Users_menu", u"Zalo\u017eit nov\u00fd", None))
        self.Button_Delete.setText(QCoreApplication.translate("Users_menu", u"Smazat", None))
    # retranslateUi

