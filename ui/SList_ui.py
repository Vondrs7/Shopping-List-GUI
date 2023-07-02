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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_SList(object):
    def setupUi(self, SList):
        if not SList.objectName():
            SList.setObjectName(u"SList")
        SList.resize(1517, 831)
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
"QPushButton#Button_Filter{\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton#Button_Change{\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 2"
                        "0px;\n"
"font: 12pt \"FreeSans\";\n"
"}\n"
"\n"
"QPushButton#Button_Change_content{\n"
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
"QTableView#List{\n"
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
"border-color: rgb("
                        "255, 255, 255);\n"
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
"QPushButton:hover#Button_Filter{\n"
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
"\n"
"QPushButton:hover#Button_Change{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"QPushButton:hover#Button_Change_content{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 53);\n"
"}\n"
"\n"
"\n"
""
                        "QTableView:hover#List{\n"
"border: 3px solid rgb(255, 255, 255);\n"
"}")
        self.frame = QFrame(SList)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 1491, 811))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Label_error_message = QLabel(self.frame)
        self.Label_error_message.setObjectName(u"Label_error_message")
        self.Label_error_message.setGeometry(QRect(10, 790, 1201, 16))
        font = QFont()
        font.setFamilies([u"FreeSans"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.Label_error_message.setFont(font)
        self.Label_error_message.setStyleSheet(u"")
        self.Instructions = QLabel(self.frame)
        self.Instructions.setObjectName(u"Instructions")
        self.Instructions.setGeometry(QRect(550, 20, 351, 39))
        font1 = QFont()
        font1.setFamilies([u"FreeSans"])
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setItalic(False)
        self.Instructions.setFont(font1)
        self.Instructions.setStyleSheet(u"")
        self.User_text = QLabel(self.frame)
        self.User_text.setObjectName(u"User_text")
        self.User_text.setGeometry(QRect(20, 50, 101, 39))
        font2 = QFont()
        font2.setFamilies([u"FreeSans"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        self.User_text.setFont(font2)
        self.User_text.setStyleSheet(u"")
        self.User_selected = QLabel(self.frame)
        self.User_selected.setObjectName(u"User_selected")
        self.User_selected.setGeometry(QRect(110, 50, 341, 41))
        self.User_selected.setFont(font2)
        self.User_selected.setStyleSheet(u"")
        self.List = QTableWidget(self.frame)
        if (self.List.columnCount() < 11):
            self.List.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.List.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.List.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.List.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.List.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.List.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.List.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.List.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.List.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.List.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.List.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setForeground(brush);
        self.List.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.List.setObjectName(u"List")
        self.List.setGeometry(QRect(10, 90, 1211, 681))
        self.List.setStyleSheet(u"")
        self.Button_Cancel = QPushButton(self.frame)
        self.Button_Cancel.setObjectName(u"Button_Cancel")
        self.Button_Cancel.setGeometry(QRect(1260, 710, 200, 60))
        font3 = QFont()
        font3.setFamilies([u"FreeSans"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.Button_Cancel.setFont(font3)
        self.Button_Cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Cancel.setStyleSheet(u"")
        self.Button_Change = QPushButton(self.frame)
        self.Button_Change.setObjectName(u"Button_Change")
        self.Button_Change.setGeometry(QRect(1260, 640, 200, 60))
        self.Button_Change.setFont(font3)
        self.Button_Change.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Change.setStyleSheet(u"")
        self.Button_Delete = QPushButton(self.frame)
        self.Button_Delete.setObjectName(u"Button_Delete")
        self.Button_Delete.setEnabled(True)
        self.Button_Delete.setGeometry(QRect(1260, 300, 200, 60))
        self.Button_Delete.setFont(font3)
        self.Button_Delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Delete.setStyleSheet(u"")
        self.Button_Filter = QPushButton(self.frame)
        self.Button_Filter.setObjectName(u"Button_Filter")
        self.Button_Filter.setEnabled(True)
        self.Button_Filter.setGeometry(QRect(1260, 90, 200, 60))
        self.Button_Filter.setFont(font3)
        self.Button_Filter.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Filter.setStyleSheet(u"")
        self.Button_Create = QPushButton(self.frame)
        self.Button_Create.setObjectName(u"Button_Create")
        self.Button_Create.setEnabled(True)
        self.Button_Create.setGeometry(QRect(1260, 160, 200, 60))
        self.Button_Create.setFont(font3)
        self.Button_Create.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Create.setStyleSheet(u"")
        self.Button_Edit = QPushButton(self.frame)
        self.Button_Edit.setObjectName(u"Button_Edit")
        self.Button_Edit.setEnabled(True)
        self.Button_Edit.setGeometry(QRect(1260, 230, 200, 60))
        self.Button_Edit.setFont(font3)
        self.Button_Edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Edit.setStyleSheet(u"")
        self.Button_Change_content = QPushButton(self.frame)
        self.Button_Change_content.setObjectName(u"Button_Change_content")
        self.Button_Change_content.setGeometry(QRect(1260, 570, 200, 60))
        self.Button_Change_content.setFont(font3)
        self.Button_Change_content.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Change_content.setStyleSheet(u"")

        self.retranslateUi(SList)

        QMetaObject.connectSlotsByName(SList)
    # setupUi

    def retranslateUi(self, SList):
        SList.setWindowTitle(QCoreApplication.translate("SList", u"N\u00e1kupn\u00ed L\u00edstek JV", None))
        self.Label_error_message.setText("")
        self.Instructions.setText(QCoreApplication.translate("SList", u"N\u00e1kupn\u00ed L\u00edstek - JV", None))
        self.User_text.setText(QCoreApplication.translate("SList", u"U\u017eivatel:", None))
        self.User_selected.setText("")
        ___qtablewidgetitem = self.List.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SList", u"N\u00e1zev produktu", None));
        ___qtablewidgetitem1 = self.List.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SList", u"Cena (K\u010d)", None));
        ___qtablewidgetitem2 = self.List.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SList", u"Datum n\u00e1kupu", None));
        ___qtablewidgetitem3 = self.List.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SList", u"Mno\u017estv\u00ed", None));
        ___qtablewidgetitem4 = self.List.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SList", u"Jednotka", None));
        ___qtablewidgetitem5 = self.List.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SList", u"Sleva", None));
        ___qtablewidgetitem6 = self.List.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SList", u"N\u00e1zev obchodu", None));
        ___qtablewidgetitem7 = self.List.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("SList", u"M\u011bsto", None));
        ___qtablewidgetitem8 = self.List.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("SList", u"U\u017eivatel", None));
        ___qtablewidgetitem9 = self.List.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("SList", u"ID", None));
        ___qtablewidgetitem10 = self.List.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("SList", u"Pozn\u00e1mky", None));
        self.Button_Cancel.setText(QCoreApplication.translate("SList", u"Konec", None))
        self.Button_Change.setText(QCoreApplication.translate("SList", u"Zm\u011bnit u\u017eivatele", None))
        self.Button_Delete.setText(QCoreApplication.translate("SList", u"Smazat produkt", None))
        self.Button_Filter.setText(QCoreApplication.translate("SList", u"Filtrovat v\u00fdb\u011br", None))
        self.Button_Create.setText(QCoreApplication.translate("SList", u"P\u0159idat nov\u00fd produkt", None))
        self.Button_Edit.setText(QCoreApplication.translate("SList", u"Upravit produkt", None))
        self.Button_Change_content.setText(QCoreApplication.translate("SList", u"Zm\u011bnit zobrazen\u00ed", None))
    # retranslateUi

