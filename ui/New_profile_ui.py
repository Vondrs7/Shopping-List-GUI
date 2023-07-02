# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'New_profile.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_NewProfile(object):
    def setupUi(self, NewProfile):
        if not NewProfile.objectName():
            NewProfile.setObjectName(u"NewProfile")
        NewProfile.resize(510, 281)
        NewProfile.setCursor(QCursor(Qt.ArrowCursor))
        NewProfile.setStyleSheet(u"QLabel#Instructions {\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"FreeSans\";\n"
"}\n"
"\n"
"QWidget#NewProfile {\n"
"background-color: rgb(0, 0, 34);\n"
"}\n"
"\n"
"QPushButton:hover#Button_Save_Continue{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QPushButton:hover#Button_Cancel{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QLineEdit:hover#Input_name{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel#Label_error_message{\n"
"color: rgb(255, 0, 0);\n"
"font: 8pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Label_Name{\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"FreeSans\";\n"
"}\n"
"\n"
"QLineEdit#Input_name{\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"FreeSans\";\n"
"border: 2px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"border-radius: 20px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton#Button_Save_Continue{\n"
"color: rgb(255, 255, 255);\n"
""
                        "border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton#Button_Cancel{\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font: 12pt \"FreeSans\";\n"
"}")
        self.horizontalLayout = QHBoxLayout(NewProfile)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(NewProfile)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Label_error_message = QLabel(self.frame)
        self.Label_error_message.setObjectName(u"Label_error_message")
        self.Label_error_message.setGeometry(QRect(169, 60, 261, 20))
        font = QFont()
        font.setFamilies([u"FreeSans"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.Label_error_message.setFont(font)
        self.Label_error_message.setStyleSheet(u"")
        self.Button_Save_Continue = QPushButton(self.frame)
        self.Button_Save_Continue.setObjectName(u"Button_Save_Continue")
        self.Button_Save_Continue.setEnabled(True)
        self.Button_Save_Continue.setGeometry(QRect(70, 130, 360, 40))
        font1 = QFont()
        font1.setFamilies([u"FreeSans"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.Button_Save_Continue.setFont(font1)
        self.Button_Save_Continue.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Save_Continue.setStyleSheet(u"")
        self.Button_Cancel = QPushButton(self.frame)
        self.Button_Cancel.setObjectName(u"Button_Cancel")
        self.Button_Cancel.setGeometry(QRect(70, 180, 360, 40))
        self.Button_Cancel.setFont(font1)
        self.Button_Cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Cancel.setStyleSheet(u"")
        self.Input_name = QLineEdit(self.frame)
        self.Input_name.setObjectName(u"Input_name")
        self.Input_name.setGeometry(QRect(150, 80, 280, 40))
        font2 = QFont()
        font2.setFamilies([u"FreeSans"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.Input_name.setFont(font2)
        self.Input_name.setStyleSheet(u"")
        self.Label_Name = QLabel(self.frame)
        self.Label_Name.setObjectName(u"Label_Name")
        self.Label_Name.setGeometry(QRect(80, 90, 62, 23))
        self.Label_Name.setFont(font2)
        self.Label_Name.setStyleSheet(u"")
        self.Instructions = QLabel(self.frame)
        self.Instructions.setObjectName(u"Instructions")
        self.Instructions.setGeometry(QRect(180, 10, 151, 39))
        font3 = QFont()
        font3.setFamilies([u"FreeSans"])
        font3.setPointSize(24)
        font3.setBold(False)
        font3.setItalic(False)
        self.Instructions.setFont(font3)
        self.Instructions.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(NewProfile)

        QMetaObject.connectSlotsByName(NewProfile)
    # setupUi

    def retranslateUi(self, NewProfile):
        NewProfile.setWindowTitle(QCoreApplication.translate("NewProfile", u"N\u00e1kupn\u00ed L\u00edstek JV", None))
        self.Label_error_message.setText("")
        self.Button_Save_Continue.setText(QCoreApplication.translate("NewProfile", u"Ulo\u017eit a pokra\u010dovat", None))
        self.Button_Cancel.setText(QCoreApplication.translate("NewProfile", u"Zav\u0159\u00edt okno", None))
        self.Label_Name.setText(QCoreApplication.translate("NewProfile", u"Jm\u00e9no:", None))
        self.Instructions.setText(QCoreApplication.translate("NewProfile", u"Nov\u00fd profil", None))
    # retranslateUi

