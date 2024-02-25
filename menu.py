# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MENU.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(807, 565)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-10, 30, 701, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-image: url(:/img/parklioLicensePlateRecognition (2).jpg);\n"
"border-bottom-left-radius:50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 391, 430))
        self.label_2.setStyleSheet("background-color:white;\n"
"border-top-right-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(350, 60, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(350, 120, 341, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.exit = QtWidgets.QPushButton(self.widget)
        self.exit.setGeometry(QtCore.QRect(660, 429, 41, 31))
        self.exit.setStyleSheet("background-color:white;\n"
"border:none;")
        self.exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/power.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon)
        self.exit.setObjectName("exit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(420, 360, 61, 61))
        self.pushButton.setStyleSheet("QPushButton#pushButton{background-color: rgba(20, 146, 208, 255);\n"
"border-radius:30px;}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(112, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(112, 112, 112, 255);\n"
"}\n"
"\n"
"")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 360, 61, 61))
        self.pushButton_2.setStyleSheet("QPushButton{background-color: rgba(20, 146, 208, 255);\n"
"border-radius:30px;}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(112, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(112, 112, 112, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/video.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.exit.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Moroccan LPDR"))
        self.label_4.setText(_translate("Form", "Ce systéme de reconnaissance automatique \n"
"des plaques est efficace devient de plus en \n"
"plus une nécessite dans  la gestion de \n"
"plusieurs domaines  comme : \n"
"\n"
"     >> La circulation. \n"
" \n"
"     >>La sécurité routiére. \n"
" \n"
"     >>La gestion des parkings. \n"
" \n"
"     >> La poursuite de criminels."))

import icons
import img


