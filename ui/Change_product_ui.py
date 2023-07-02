# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Change_product.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Change_product(object):
    def setupUi(self, Change_product):
        if not Change_product.objectName():
            Change_product.setObjectName(u"Change_product")
        Change_product.resize(1181, 404)
        Change_product.setStyleSheet(u"QWidget#Change_product {\n"
"background-color: rgb(0, 0, 34);\n"
"}\n"
"\n"
"QLabel#Instructions {\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"FreeSans\";\n"
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
"QPushButton#Button_Save_Change{\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton:hover#Button_Back{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QPushButton:hover#Button_Save_Change{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QLabel#Text_name {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Text_price {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
""
                        "}\n"
"\n"
"QLabel#Text_date {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Text_amount {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Text_discount {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Text_unit {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Text_shop {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Text_city {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Text_comments {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLineEdit#Product_amount, \n"
"QLineEdit#Product_city,\n"
"QLineEdit#Product_comments,\n"
"QLineEdit#Product_date,\n"
"QLineEdit#Product_discount,\n"
"QLineEdit#Product_name,\n"
"QLineEdit#Product_price,\n"
"QLineEdit#Product_shop,\n"
"QLineEdit#Product_unit{\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"FreeSans\";\n"
"border: 2px solid rgb("
                        "255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"border-radius: 10px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover#Product_amount, \n"
"QLineEdit:hover#Product_city,\n"
"QLineEdit:hover#Product_comments,\n"
"QLineEdit:hover#Product_date,\n"
"QLineEdit:hover#Product_discount,\n"
"QLineEdit:hover#Product_name,\n"
"QLineEdit:hover#Product_price,\n"
"QLineEdit:hover#Product_shop,\n"
"QLineEdit:hover#Product_unit{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel#Message{\n"
"color: rgb(255, 0, 0);\n"
"font: 16pt \"FreeSans\";\n"
"}")
        self.frame = QFrame(Change_product)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1171, 391))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Instructions = QLabel(self.frame)
        self.Instructions.setObjectName(u"Instructions")
        self.Instructions.setGeometry(QRect(460, 10, 241, 39))
        font = QFont()
        font.setFamilies([u"FreeSans"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.Instructions.setFont(font)
        self.Instructions.setStyleSheet(u"")
        self.Product_name = QLineEdit(self.frame)
        self.Product_name.setObjectName(u"Product_name")
        self.Product_name.setGeometry(QRect(250, 70, 301, 31))
        self.Text_name = QLabel(self.frame)
        self.Text_name.setObjectName(u"Text_name")
        self.Text_name.setGeometry(QRect(40, 70, 161, 31))
        self.Message = QLabel(self.frame)
        self.Message.setObjectName(u"Message")
        self.Message.setGeometry(QRect(40, 270, 1091, 31))
        self.Button_Save_Change = QPushButton(self.frame)
        self.Button_Save_Change.setObjectName(u"Button_Save_Change")
        self.Button_Save_Change.setEnabled(True)
        self.Button_Save_Change.setGeometry(QRect(360, 300, 200, 60))
        font1 = QFont()
        font1.setFamilies([u"FreeSans"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.Button_Save_Change.setFont(font1)
        self.Button_Save_Change.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Save_Change.setStyleSheet(u"")
        self.Button_Back = QPushButton(self.frame)
        self.Button_Back.setObjectName(u"Button_Back")
        self.Button_Back.setEnabled(True)
        self.Button_Back.setGeometry(QRect(610, 300, 200, 60))
        self.Button_Back.setFont(font1)
        self.Button_Back.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Back.setStyleSheet(u"")
        self.Text_price = QLabel(self.frame)
        self.Text_price.setObjectName(u"Text_price")
        self.Text_price.setGeometry(QRect(40, 110, 161, 31))
        self.Text_date = QLabel(self.frame)
        self.Text_date.setObjectName(u"Text_date")
        self.Text_date.setGeometry(QRect(40, 190, 191, 31))
        self.Text_amount = QLabel(self.frame)
        self.Text_amount.setObjectName(u"Text_amount")
        self.Text_amount.setGeometry(QRect(590, 70, 161, 31))
        self.Text_unit = QLabel(self.frame)
        self.Text_unit.setObjectName(u"Text_unit")
        self.Text_unit.setGeometry(QRect(590, 110, 231, 31))
        self.Text_discount = QLabel(self.frame)
        self.Text_discount.setObjectName(u"Text_discount")
        self.Text_discount.setGeometry(QRect(40, 150, 161, 31))
        self.Text_comments = QLabel(self.frame)
        self.Text_comments.setObjectName(u"Text_comments")
        self.Text_comments.setGeometry(QRect(40, 230, 201, 31))
        self.Product_price = QLineEdit(self.frame)
        self.Product_price.setObjectName(u"Product_price")
        self.Product_price.setGeometry(QRect(250, 110, 301, 31))
        self.Product_discount = QLineEdit(self.frame)
        self.Product_discount.setObjectName(u"Product_discount")
        self.Product_discount.setGeometry(QRect(250, 150, 301, 31))
        self.Product_amount = QLineEdit(self.frame)
        self.Product_amount.setObjectName(u"Product_amount")
        self.Product_amount.setGeometry(QRect(840, 70, 301, 31))
        self.Product_unit = QLineEdit(self.frame)
        self.Product_unit.setObjectName(u"Product_unit")
        self.Product_unit.setGeometry(QRect(840, 110, 301, 31))
        self.Product_shop = QLineEdit(self.frame)
        self.Product_shop.setObjectName(u"Product_shop")
        self.Product_shop.setGeometry(QRect(840, 150, 301, 31))
        self.Product_comments = QLineEdit(self.frame)
        self.Product_comments.setObjectName(u"Product_comments")
        self.Product_comments.setGeometry(QRect(250, 230, 891, 31))
        self.Text_city = QLabel(self.frame)
        self.Text_city.setObjectName(u"Text_city")
        self.Text_city.setGeometry(QRect(590, 190, 161, 31))
        self.Text_shop = QLabel(self.frame)
        self.Text_shop.setObjectName(u"Text_shop")
        self.Text_shop.setGeometry(QRect(590, 150, 161, 31))
        self.Product_date = QLineEdit(self.frame)
        self.Product_date.setObjectName(u"Product_date")
        self.Product_date.setGeometry(QRect(250, 190, 301, 31))
        self.Product_city = QLineEdit(self.frame)
        self.Product_city.setObjectName(u"Product_city")
        self.Product_city.setGeometry(QRect(840, 190, 301, 31))

        self.retranslateUi(Change_product)

        QMetaObject.connectSlotsByName(Change_product)
    # setupUi

    def retranslateUi(self, Change_product):
        Change_product.setWindowTitle(QCoreApplication.translate("Change_product", u"N\u00e1kupn\u00ed L\u00edstek JV", None))
        self.Instructions.setText(QCoreApplication.translate("Change_product", u"Zm\u011bna produktu", None))
        self.Text_name.setText(QCoreApplication.translate("Change_product", u"N\u00e1zev produktu", None))
        self.Message.setText("")
        self.Button_Save_Change.setText(QCoreApplication.translate("Change_product", u"Upravit produkt", None))
        self.Button_Back.setText(QCoreApplication.translate("Change_product", u"Zav\u0159\u00edt okno", None))
        self.Text_price.setText(QCoreApplication.translate("Change_product", u"Cena (1ks/K\u010d)", None))
        self.Text_date.setText(QCoreApplication.translate("Change_product", u"Datum (dd.mm.rrrr)", None))
        self.Text_amount.setText(QCoreApplication.translate("Change_product", u"Mno\u017estv\u00ed", None))
        self.Text_unit.setText(QCoreApplication.translate("Change_product", u"Jednotka (ks,g,ml,cm,...)", None))
        self.Text_discount.setText(QCoreApplication.translate("Change_product", u"Sleva (ano/ne)", None))
        self.Text_comments.setText(QCoreApplication.translate("Change_product", u"Pozn\u00e1mky (voliteln\u00e9)", None))
        self.Text_city.setText(QCoreApplication.translate("Change_product", u"M\u011bsto", None))
        self.Text_shop.setText(QCoreApplication.translate("Change_product", u"N\u00e1zev obchodu", None))
    # retranslateUi

