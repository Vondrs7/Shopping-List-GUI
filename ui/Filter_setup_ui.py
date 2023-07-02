# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Filter_setup.ui'
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

class Ui_Filter(object):
    def setupUi(self, Filter):
        if not Filter.objectName():
            Filter.setObjectName(u"Filter")
        Filter.resize(628, 723)
        Filter.setStyleSheet(u"QWidget#Filter {\n"
"background-color: rgb(0, 0, 34);\n"
"}\n"
"\n"
"QLabel#Instructions {\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Price {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Date {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Discount {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Amount{\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#City {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Unit {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Shop {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Comment {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QLabel#Product {\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton#Button_Search{\n"
"color: rgb(255,"
                        " 255, 255);\n"
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
"QPushButton:hover#Button_Search{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QPushButton:hover#Button_Back{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QLineEdit:hover#Product_choose,\n"
"QLineEdit:hover#Price_choose,\n"
"QLineEdit:hover#Date_choose,\n"
"QLineEdit:hover#Amount_choose,\n"
"QLineEdit:hover#Unit_choose,\n"
"QLineEdit:hover#Discount_choose,\n"
"QLineEdit:hover#Comment_choose,\n"
"QLineEdit:hover#City_choose,\n"
"QLineEdit:hover#Shop_choose{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QLineEdit#Product_choose,\n"
"QLineEdit"
                        "#Price_choose,\n"
"QLineEdit#Date_choose,\n"
"QLineEdit#Amount_choose,\n"
"QLineEdit#Unit_choose,\n"
"QLineEdit#Discount_choose,\n"
"QLineEdit#Comment_choose,\n"
"QLineEdit#City_choose,\n"
"QLineEdit#Shop_choose\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"FreeSans\";\n"
"border: 2px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"border-radius: 10px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"}\n"
"\n"
"\n"
"QLabel#Message{\n"
"color: rgb(255, 0, 0);\n"
"font: 16pt \"FreeSans\";\n"
"}")
        self.frame = QFrame(Filter)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 621, 701))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Instructions = QLabel(self.frame)
        self.Instructions.setObjectName(u"Instructions")
        self.Instructions.setGeometry(QRect(80, 20, 451, 39))
        font = QFont()
        font.setFamilies([u"FreeSans"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.Instructions.setFont(font)
        self.Instructions.setStyleSheet(u"")
        self.Product_choose = QLineEdit(self.frame)
        self.Product_choose.setObjectName(u"Product_choose")
        self.Product_choose.setGeometry(QRect(240, 100, 341, 31))
        self.Product = QLabel(self.frame)
        self.Product.setObjectName(u"Product")
        self.Product.setGeometry(QRect(40, 100, 161, 31))
        self.Message = QLabel(self.frame)
        self.Message.setObjectName(u"Message")
        self.Message.setGeometry(QRect(40, 550, 541, 31))
        self.Button_Search = QPushButton(self.frame)
        self.Button_Search.setObjectName(u"Button_Search")
        self.Button_Search.setEnabled(True)
        self.Button_Search.setGeometry(QRect(90, 600, 200, 60))
        font1 = QFont()
        font1.setFamilies([u"FreeSans"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.Button_Search.setFont(font1)
        self.Button_Search.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Search.setStyleSheet(u"")
        self.Button_Back = QPushButton(self.frame)
        self.Button_Back.setObjectName(u"Button_Back")
        self.Button_Back.setEnabled(True)
        self.Button_Back.setGeometry(QRect(320, 600, 200, 60))
        self.Button_Back.setFont(font1)
        self.Button_Back.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Back.setStyleSheet(u"")
        self.Price = QLabel(self.frame)
        self.Price.setObjectName(u"Price")
        self.Price.setGeometry(QRect(40, 150, 161, 31))
        self.Date = QLabel(self.frame)
        self.Date.setObjectName(u"Date")
        self.Date.setGeometry(QRect(40, 200, 201, 31))
        self.Amount = QLabel(self.frame)
        self.Amount.setObjectName(u"Amount")
        self.Amount.setGeometry(QRect(40, 250, 161, 31))
        self.Unit = QLabel(self.frame)
        self.Unit.setObjectName(u"Unit")
        self.Unit.setGeometry(QRect(40, 300, 161, 31))
        self.Discount = QLabel(self.frame)
        self.Discount.setObjectName(u"Discount")
        self.Discount.setGeometry(QRect(40, 350, 161, 31))
        self.Shop = QLabel(self.frame)
        self.Shop.setObjectName(u"Shop")
        self.Shop.setGeometry(QRect(40, 400, 161, 31))
        self.City = QLabel(self.frame)
        self.City.setObjectName(u"City")
        self.City.setGeometry(QRect(40, 450, 161, 31))
        self.Comment = QLabel(self.frame)
        self.Comment.setObjectName(u"Comment")
        self.Comment.setGeometry(QRect(40, 500, 161, 31))
        self.Price_choose = QLineEdit(self.frame)
        self.Price_choose.setObjectName(u"Price_choose")
        self.Price_choose.setGeometry(QRect(240, 150, 341, 31))
        self.Date_choose = QLineEdit(self.frame)
        self.Date_choose.setObjectName(u"Date_choose")
        self.Date_choose.setGeometry(QRect(240, 200, 341, 31))
        self.Amount_choose = QLineEdit(self.frame)
        self.Amount_choose.setObjectName(u"Amount_choose")
        self.Amount_choose.setGeometry(QRect(240, 250, 341, 31))
        self.Unit_choose = QLineEdit(self.frame)
        self.Unit_choose.setObjectName(u"Unit_choose")
        self.Unit_choose.setGeometry(QRect(240, 300, 341, 31))
        self.Discount_choose = QLineEdit(self.frame)
        self.Discount_choose.setObjectName(u"Discount_choose")
        self.Discount_choose.setGeometry(QRect(240, 350, 341, 31))
        self.City_choose = QLineEdit(self.frame)
        self.City_choose.setObjectName(u"City_choose")
        self.City_choose.setGeometry(QRect(240, 450, 341, 31))
        self.Comment_choose = QLineEdit(self.frame)
        self.Comment_choose.setObjectName(u"Comment_choose")
        self.Comment_choose.setGeometry(QRect(240, 500, 341, 31))
        self.Shop_choose = QLineEdit(self.frame)
        self.Shop_choose.setObjectName(u"Shop_choose")
        self.Shop_choose.setGeometry(QRect(240, 400, 341, 31))

        self.retranslateUi(Filter)

        QMetaObject.connectSlotsByName(Filter)
    # setupUi

    def retranslateUi(self, Filter):
        Filter.setWindowTitle(QCoreApplication.translate("Filter", u"N\u00e1kupn\u00ed L\u00edstek JV", None))
        self.Instructions.setText(QCoreApplication.translate("Filter", u"V\u00fdb\u011br filtru - porovn\u00e1vat podle:", None))
        self.Product.setText(QCoreApplication.translate("Filter", u"Produkt:", None))
        self.Message.setText(QCoreApplication.translate("Filter", u"TextLabel", None))
        self.Button_Search.setText(QCoreApplication.translate("Filter", u"Vyhledat", None))
        self.Button_Back.setText(QCoreApplication.translate("Filter", u"Zav\u0159\u00edt okno", None))
        self.Price.setText(QCoreApplication.translate("Filter", u"Cena:", None))
        self.Date.setText(QCoreApplication.translate("Filter", u"Datum (dd.mm.rrrr):", None))
        self.Amount.setText(QCoreApplication.translate("Filter", u"Mno\u017estv\u00ed:", None))
        self.Unit.setText(QCoreApplication.translate("Filter", u"Jednotka:", None))
        self.Discount.setText(QCoreApplication.translate("Filter", u"Sleva (ano/ne):", None))
        self.Shop.setText(QCoreApplication.translate("Filter", u"Obchod:", None))
        self.City.setText(QCoreApplication.translate("Filter", u"M\u011bsto:", None))
        self.Comment.setText(QCoreApplication.translate("Filter", u"Koment\u00e1\u0159:", None))
    # retranslateUi

