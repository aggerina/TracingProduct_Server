# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 81, 16))
        self.label.setObjectName("label")
        self.lineedit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit1.setGeometry(QtCore.QRect(140, 30, 171, 20))
        self.lineedit1.setObjectName("lineedit1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 81, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 190, 81, 16))
        self.label_5.setObjectName("label_5")
        self.lineedit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit2.setGeometry(QtCore.QRect(140, 70, 171, 20))
        self.lineedit2.setObjectName("lineedit2")
        self.lineedit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit3.setGeometry(QtCore.QRect(140, 110, 171, 20))
        self.lineedit3.setObjectName("lineedit3")
        self.lineedit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit4.setGeometry(QtCore.QRect(140, 150, 171, 20))
        self.lineedit4.setObjectName("lineedit4")
        self.lineedit4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit5.setGeometry(QtCore.QRect(140, 190, 171, 20))
        self.lineedit5.setObjectName("lineedit5")
        self.lineedit5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(94, 220, 181, 23))
        self.button.setObjectName("button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Personal code"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Family"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Confrim Password"))
        self.button.setText(_translate("MainWindow", "Subbmit"))