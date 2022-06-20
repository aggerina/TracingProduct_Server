
from builtins import print

from Server.OPC_Managment.Style_BootStrap import Style, Style_Red
from  Server import  Setting_server

import pyodbc, re, sys, asyncio, mysql.connector
# from PyQt5.QtGui import *

import pandas as pd
from PyQt5.QtWidgets import QMessageBox , QMainWindow, QWidget, QSplitter, QPushButton, QTextEdit, QSpacerItem, QGroupBox,\
 QFormLayout, QSizePolicy, QFormLayout, QApplication, QLabel, QSpacerItem , QGridLayout ,QLineEdit, QTabWidget, QTableWidget,\
QAbstractItemView, QTableWidgetItem, QScrollArea, QHBoxLayout, QToolButton, QMenuBar, QMenu, QStatusBar, QAction, QFileDialog
from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication, pyqtSlot, QSize, QRect
from PyQt5.QtGui import QPalette, QBrush, QColor, QFont, QPixmap

from PyQt5 import QtCore, QtWidgets ,QtGui
import yaml
import csv
import os
from qt_material import apply_stylesheet
import qtawesome as QTA
import psycopg2
import uuid , shortuuid



## connect to database  Tracebility
class  Connect_To_server():
    try:
        with open("D:/photon_project/Tracebility_01/venv_new/Server/config.yaml", "r") as yamlfile:
            data_r = yaml.load(yamlfile, Loader=yaml.FullLoader)




        DB_save = mysql.connector.connect(

            host= data_r[0]['DATA_Setting']['HOST_SERVER'],
            user= data_r[0]['DATA_Setting']['USER_SERVER'],
            password= data_r[0]['DATA_Setting']['PASSWORD_SERVER'],
            database= data_r[0]['DATA_Setting']['DATABASE_SERVER'],


            # password=(f'"{str(Setting_date[2])}"'),
            # database="photon",

            # host="192.168.1.91",
            # user="BPMS",
            # password="P@ssw0rd",
            # database="photon"
        )
    except:
        import sys
        print('no connection managment opc')

        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Critical)
        # msg.setText("ارتباط با دیتابیس  برقرار نشد  ")
        # msg.setWindowTitle("No Conecction")
        # msg.exec_()

##connect to database Sepidar
class MssqlConnection(object):



    server = '192.168.4.2\SEPIDAR'
    database = 'Sepidar04'
    username = 'BPMS'
    password = 'aezakmiHESOYAM!@#321'
    cnxn_2 = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn_2.cursor()
        # cursor.execute("SET character_set_connection=utf8mb4;")
    # except:
    #     print("ارتباط با دیتابیس سپیدار برقرار نشد ")

        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Critical)
        # # msg.setStyle('fusion')
        # msg.setText("ارتباط با دیتابیس سپیدار برقرار نشد  ")
        #
        # msg.setWindowTitle("No Conecction")
        # msg.exec_()

class OPC_UI_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1245, 795)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setWindowTitle("MainWindow")
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.Admin_Page = QtWidgets.QWidget()
        self.Admin_Page.setObjectName("Admin_Page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Admin_Page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.Admin_Page)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        self.splitter_2.setFont(font)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        self.splitter.setFont(font)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tableWidget_show_resources = QtWidgets.QTableWidget(self.splitter)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        self.tableWidget_show_resources.setFont(font)
        self.tableWidget_show_resources.setMouseTracking(True)
        self.tableWidget_show_resources.setTabletTracking(True)
        self.tableWidget_show_resources.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget_show_resources.setAcceptDrops(True)
        self.tableWidget_show_resources.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_show_resources.setAutoFillBackground(True)
        self.tableWidget_show_resources.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_show_resources.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_show_resources.setDragEnabled(True)
        self.tableWidget_show_resources.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableWidget_show_resources.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tableWidget_show_resources.setAlternatingRowColors(True)
        self.tableWidget_show_resources.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_show_resources.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_show_resources.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_show_resources.setObjectName("tableWidget_show_resources")
        self.tableWidget_show_resources.setColumnCount(2)
        self.tableWidget_show_resources.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_show_resources.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_show_resources.setHorizontalHeaderItem(1, item)
        self.tableWidget_show_resources.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_show_resources.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_show_resources.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_show_resources.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_show_resources.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_show_resources.verticalHeader().setStretchLastSection(False)
        self.scrollArea = QtWidgets.QScrollArea(self.splitter)
        self.scrollArea.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 567, 570))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_Start_time = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Start_time.setObjectName("label_Start_time")
        self.gridLayout_5.addWidget(self.label_Start_time, 2, 5, 1, 1)
        self.label_Code_Order = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_Code_Order.setFont(font)
        self.label_Code_Order.setObjectName("label_Code_Order")
        self.gridLayout_5.addWidget(self.label_Code_Order, 0, 5, 1, 1)
        self.lable_StationNumber = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lable_StationNumber.setObjectName("lable_StationNumber")
        self.gridLayout_5.addWidget(self.lable_StationNumber, 1, 3, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout_5.addWidget(self.dateTimeEdit_2, 2, 4, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_5.addWidget(self.lineEdit_4, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 5, 1, 1)
        self.label_Count = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Count.setObjectName("label_Count")
        self.gridLayout_5.addWidget(self.label_Count, 0, 3, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_5.addWidget(self.dateTimeEdit, 2, 0, 1, 1)
        self.lineEdit_StationNumber = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_StationNumber.setObjectName("lineEdit_StationNumber")
        self.gridLayout_5.addWidget(self.lineEdit_StationNumber, 1, 0, 1, 1)
        self.lineEdit_Order_Code = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_Order_Code.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 194, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 161, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 64, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 86, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 192, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 194, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 161, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 64, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 86, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 192, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 64, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 194, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 161, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 64, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 86, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 64, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 64, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lineEdit_Order_Code.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        self.lineEdit_Order_Code.setFont(font)
        self.lineEdit_Order_Code.setAutoFillBackground(True)
        self.lineEdit_Order_Code.setObjectName("lineEdit_Order_Code")
        self.gridLayout_5.addWidget(self.lineEdit_Order_Code, 0, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 2, 3, 1, 1)
        self.tableWidget_Search_result = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_Search_result.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_Search_result.setObjectName("tableWidget_Search_result")
        self.tableWidget_Search_result.setColumnCount(3)
        self.tableWidget_Search_result.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Search_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Search_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Search_result.setHorizontalHeaderItem(2, item)
        self.gridLayout_5.addWidget(self.tableWidget_Search_result, 4, 0, 1, 6)
        self.lineEdit_code_Product = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_code_Product.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 194, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 161, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 64, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 86, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 192, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 194, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 161, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 64, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 86, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 192, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 64, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 194, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 161, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 64, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 86, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 64, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 64, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 129, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lineEdit_code_Product.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        self.lineEdit_code_Product.setFont(font)
        self.lineEdit_code_Product.setAutoFillBackground(True)
        self.lineEdit_code_Product.setObjectName("lineEdit_code_Product")
        self.gridLayout_5.addWidget(self.lineEdit_code_Product, 1, 4, 1, 1)
        self.pushButton_Instruction = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Instruction.setObjectName("pushButton_Instruction")
        self.gridLayout_5.addWidget(self.pushButton_Instruction, 3, 5, 1, 1)
        self.pushButton_PictureProduct = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_PictureProduct.setObjectName("pushButton_PictureProduct")
        self.gridLayout_5.addWidget(self.pushButton_PictureProduct, 3, 3, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tableWidget_operator_to_OPC = QtWidgets.QTableWidget(self.splitter)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        self.tableWidget_operator_to_OPC.setFont(font)
        self.tableWidget_operator_to_OPC.setMouseTracking(True)
        self.tableWidget_operator_to_OPC.setTabletTracking(True)
        self.tableWidget_operator_to_OPC.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget_operator_to_OPC.setAcceptDrops(True)
        self.tableWidget_operator_to_OPC.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_operator_to_OPC.setAutoFillBackground(True)
        self.tableWidget_operator_to_OPC.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_operator_to_OPC.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_operator_to_OPC.setDragEnabled(True)
        self.tableWidget_operator_to_OPC.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableWidget_operator_to_OPC.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tableWidget_operator_to_OPC.setAlternatingRowColors(True)
        self.tableWidget_operator_to_OPC.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_operator_to_OPC.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_operator_to_OPC.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_operator_to_OPC.setObjectName("tableWidget_operator_to_OPC")
        self.tableWidget_operator_to_OPC.setColumnCount(3)
        self.tableWidget_operator_to_OPC.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_operator_to_OPC.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_operator_to_OPC.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_operator_to_OPC.setHorizontalHeaderItem(2, item)
        self.tableWidget_operator_to_OPC.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_operator_to_OPC.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_operator_to_OPC.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_operator_to_OPC.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_operator_to_OPC.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_operator_to_OPC.verticalHeader().setStretchLastSection(False)
        self.groupBox = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 110))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setMouseTracking(True)
        self.groupBox.setTabletTracking(True)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_Save = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Save.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Save.setFont(font)
        self.pushButton_Save.setMouseTracking(True)
        self.pushButton_Save.setTabletTracking(True)
        self.pushButton_Save.setAutoFillBackground(True)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.gridLayout_3.addWidget(self.pushButton_Save, 0, 5, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_start.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setMouseTracking(True)
        self.pushButton_start.setTabletTracking(True)
        self.pushButton_start.setAutoFillBackground(True)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_3.addWidget(self.pushButton_start, 0, 1, 1, 1)
        self.pushButton_delete = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_delete.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setMouseTracking(True)
        self.pushButton_delete.setTabletTracking(True)
        self.pushButton_delete.setAutoFillBackground(True)
        self.pushButton_delete.setStyleSheet("")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout_3.addWidget(self.pushButton_delete, 0, 6, 1, 1)
        self.pushButton_read = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_read.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_read.setFont(font)
        self.pushButton_read.setMouseTracking(True)
        self.pushButton_read.setAutoFillBackground(True)
        self.pushButton_read.setObjectName("pushButton_read")
        self.gridLayout_3.addWidget(self.pushButton_read, 0, 0, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setMouseTracking(True)
        self.pushButton_stop.setTabletTracking(True)
        self.pushButton_stop.setAutoFillBackground(True)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout_3.addWidget(self.pushButton_stop, 0, 2, 1, 1)
        self.pushButton_start_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_start_3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_start_3.setFont(font)
        self.pushButton_start_3.setMouseTracking(True)
        self.pushButton_start_3.setTabletTracking(True)
        self.pushButton_start_3.setAutoFillBackground(True)
        self.pushButton_start_3.setObjectName("pushButton_start_3")
        self.gridLayout_3.addWidget(self.pushButton_start_3, 0, 3, 1, 1)
        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Admin_Page, "")
        self.Manage_Opc_Product = QtWidgets.QWidget()
        self.Manage_Opc_Product.setObjectName("Manage_Opc_Product")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Manage_Opc_Product)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.Manage_Opc_Product)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Manage_Opc_Product)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 162, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 243, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 202, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 108, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 162, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 208, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 162, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 243, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 202, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 108, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 162, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 208, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 162, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 243, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 202, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 108, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 162, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 162, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 162, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lineEdit_2.setPalette(palette)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.Manage_Opc_Product)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.splitter_3)
        self.groupBox_4.setAutoFillBackground(True)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget_3.setMaximumSize(QtCore.QSize(500, 16777215))
        self.tableWidget_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_3.setAutoFillBackground(True)
        self.tableWidget_3.setDragEnabled(True)
        self.tableWidget_3.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableWidget_3.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_3.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)
        self.gridLayout_6.addWidget(self.tableWidget_3, 0, 0, 1, 1)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_4.setAutoFillBackground(True)
        self.tableWidget_4.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        self.gridLayout_6.addWidget(self.tableWidget_4, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter_3)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_row_delete = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_row_delete.setMaximumSize(QtCore.QSize(16777215, 80))
        self.pushButton_row_delete.setAutoFillBackground(True)
        self.pushButton_row_delete.setObjectName("pushButton_row_delete")
        self.horizontalLayout.addWidget(self.pushButton_row_delete)
        self.pushButton_add_row = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_add_row.setMaximumSize(QtCore.QSize(16777215, 80))
        self.pushButton_add_row.setAutoFillBackground(True)
        self.pushButton_add_row.setObjectName("pushButton_add_row")
        self.horizontalLayout.addWidget(self.pushButton_add_row)
        self.pushButton_add_column = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_add_column.setMaximumSize(QtCore.QSize(16777215, 80))
        self.pushButton_add_column.setAutoFillBackground(True)
        self.pushButton_add_column.setObjectName("pushButton_add_column")
        self.horizontalLayout.addWidget(self.pushButton_add_column)
        self.pushButton_Save_opc = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_Save_opc.setMaximumSize(QtCore.QSize(16777215, 80))
        self.pushButton_Save_opc.setAutoFillBackground(True)
        self.pushButton_Save_opc.setObjectName("pushButton_Save_opc")
        self.horizontalLayout.addWidget(self.pushButton_Save_opc)
        self.toolButton_getData_FromSepidar = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_getData_FromSepidar.setMaximumSize(QtCore.QSize(16777215, 80))
        self.toolButton_getData_FromSepidar.setAutoFillBackground(True)
        self.toolButton_getData_FromSepidar.setObjectName("toolButton_getData_FromSepidar")
        self.horizontalLayout.addWidget(self.toolButton_getData_FromSepidar)
        self.pushButton_delete_rows = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_delete_rows.setMaximumSize(QtCore.QSize(16777215, 80))
        self.pushButton_delete_rows.setAutoFillBackground(True)
        self.pushButton_delete_rows.setObjectName("pushButton_delete_rows")
        self.horizontalLayout.addWidget(self.pushButton_delete_rows)
        self.gridLayout_4.addWidget(self.splitter_3, 1, 0, 1, 2)
        self.tabWidget.addTab(self.Manage_Opc_Product, "")
        self.Dispaly_Visio = QtWidgets.QWidget()
        self.Dispaly_Visio.setObjectName("Dispaly_Visio")
        self.groupBox_5 = QtWidgets.QGroupBox(self.Dispaly_Visio)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 1281, 721))
        self.groupBox_5.setAutoFillBackground(True)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.tabWidget.addTab(self.Dispaly_Visio, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1245, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 255, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 246, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 255, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 246, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 255, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 246, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.menubar.setPalette(palette)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 240, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 240, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 240, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        self.menuFile.setPalette(palette)
        self.menuFile.setObjectName("menuFile")
        self.menuOPC = QtWidgets.QMenu(self.menubar)
        self.menuOPC.setObjectName("menuOPC")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(190, 244, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 255, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 244, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 255, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 255, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        self.menuSetting.setPalette(palette)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_AS = QtWidgets.QAction(MainWindow)
        self.actionSave_AS.setObjectName("actionSave_AS")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionNew_OPC = QtWidgets.QAction(MainWindow)
        self.actionNew_OPC.setObjectName("actionNew_OPC")
        self.actionOpen_File_Visio = QtWidgets.QAction(MainWindow)
        self.actionOpen_File_Visio.setObjectName("actionOpen_File_Visio")
        self.actionNetwork_Setting = QtWidgets.QAction(MainWindow)
        self.actionNetwork_Setting.setObjectName("actionNetwork_Setting")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_AS)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionOpen_File_Visio)
        self.menuFile.addAction(self.actionExit)
        self.menuSetting.addAction(self.actionNetwork_Setting)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOPC.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_show_resources.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "شماره ایستگاه"))
        item = self.tableWidget_show_resources.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID پرسنل "))
        self.label_Start_time.setText(_translate("MainWindow", "تاریخ شروخ "))
        self.label_Code_Order.setText(_translate("MainWindow", "کد سفارش را وارد کنید "))
        self.lable_StationNumber.setText(_translate("MainWindow", "ایستگاه شروع"))
        self.label.setText(_translate("MainWindow", "کد محصول را وارد کنید "))
        self.label_Count.setText(_translate("MainWindow", "تعداد         "))
        self.label_6.setText(_translate("MainWindow", "تاریخ پایان "))
        item = self.tableWidget_Search_result.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "  BoMکد قطعه "))
        item = self.tableWidget_Search_result.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "شرح قطعه "))
        item = self.tableWidget_Search_result.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "تعداد"))
        self.pushButton_Instruction.setText(_translate("MainWindow", "اپلود دستورالعمل"))
        self.pushButton_PictureProduct.setText(_translate("MainWindow", "اپلود عکس محصول"))
        item = self.tableWidget_operator_to_OPC.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "مراحل ساخت "))
        item = self.tableWidget_operator_to_OPC.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "شماره ایستگاه"))
        item = self.tableWidget_operator_to_OPC.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "شماره پرسنل "))
        self.pushButton_Save.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_start.setText(_translate("MainWindow", "START"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_read.setText(_translate("MainWindow", "خواندن منابع "))
        self.pushButton_stop.setText(_translate("MainWindow", "STOP"))
        self.pushButton_start_3.setText(_translate("MainWindow", "START"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Admin_Page), _translate("MainWindow", "Tab 1"))
        self.label_4.setText(_translate("MainWindow", "  کد محصول "))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "مراحل ساخت "))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "شماره ایستگاه "))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "شماره پرسنل "))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "کد محصول "))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "شرح محصول"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "کد ردیابی"))
        self.pushButton_row_delete.setText(_translate("MainWindow", "پاک کردن ردیف"))
        self.pushButton_add_row.setText(_translate("MainWindow", "اضافه کردن ردیف "))
        self.pushButton_add_column.setText(_translate("MainWindow", "اضافه کردن ستون "))
        self.pushButton_Save_opc.setText(_translate("MainWindow", "ثبت OPC"))
        self.toolButton_getData_FromSepidar.setText(_translate("MainWindow", "بارگزاری تصویر "))
        self.pushButton_delete_rows.setText(_translate("MainWindow", "پاک کردن اطلاعات"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Manage_Opc_Product), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Dispaly_Visio), _translate("MainWindow", "Page"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOPC.setTitle(_translate("MainWindow", "OPC"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_AS.setText(_translate("MainWindow", "Save AS"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File_excel"))
        self.actionNew_OPC.setText(_translate("MainWindow", "New OPC"))
        self.actionOpen_File_Visio.setText(_translate("MainWindow", "Open_File_Visio"))
        self.actionNetwork_Setting.setText(_translate("MainWindow", "Network_Setting"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        ###### Call All StyleSheet
        self.tabWidget.setStyleSheet(Style())
        self.groupBox.setStyleSheet(Style())
        self.tableWidget_show_resources.setStyleSheet(Style())
        self.tableWidget_operator_to_OPC.setStyleSheet(Style())
        self.tableWidget_3.setStyleSheet(Style())
        self.pushButton_Save.setStyleSheet(Style())
        self.pushButton_delete.setStyleSheet(Style())
        self.pushButton_start.setStyleSheet(Style())
        self.pushButton_start_3.setStyleSheet(Style())
        self.pushButton_read.setStyleSheet(Style())
        self.pushButton_stop.setStyleSheet(Style())
        self.pushButton_stop.setStyleSheet(Style())

        self.pushButton_Save_opc.setStyleSheet(Style())
        self.pushButton_delete_rows.setStyleSheet(Style_Red())
        self.pushButton_add_column.setStyleSheet(Style())
        self.pushButton_add_row.setStyleSheet(Style())
        self.pushButton_row_delete.setStyleSheet(Style())
        self.toolButton_getData_FromSepidar.setStyleSheet(Style())

        self.lineEdit_code_Product.setStyleSheet(Style())
        self.lineEdit_2.setStyleSheet(Style())
        MainWindow.setStyleSheet(Style())

        # colomn set width

        self.tableWidget_4.setColumnWidth(0, 150)
        self.tableWidget_4.setColumnWidth(1, 300)
        self.tableWidget_4.setColumnWidth(2, 200)

        self.tableWidget_3.setColumnWidth(0, 200)
        self.tableWidget_3.setColumnWidth(1, 150)

        self.tableWidget_operator_to_OPC.setColumnWidth(0, 150)
        self.tableWidget_operator_to_OPC.setColumnWidth(1, 150)
        self.tableWidget_operator_to_OPC.setColumnWidth(2, 150)

        self.tableWidget_Search_result.setColumnWidth(0, 300)
        self.tableWidget_Search_result.setColumnWidth(1, 300)

        self.tableWidget_show_resources.setColumnWidth(0, 130)
        self.tableWidget_show_resources.setColumnWidth(1, 130)
        # font awosome
        icon_read = QTA.icon('fa.sticky-note-o', color='#00aeff')
        self.pushButton_read.setIcon(icon_read)
        icon_start = QTA.icon('fa.youtube-play', color='#00aeff')
        self.pushButton_start.setIcon(icon_start)
        icon_stop = QTA.icon('fa5s.stop', color='#00aeff')
        self.pushButton_stop.setIcon(icon_stop)
        icon_save = QTA.icon('fa5s.save', color='#00aeff')
        self.pushButton_Save.setIcon(icon_save)

        # icon_delete = QTA.icon('mdi.delete', color_on='red')

        icon_delete = QTA.icon('mdi.delete', color='#00aeff')
        self.pushButton_delete.setIcon(icon_delete)

        ########################## Calling Function
        self.toolButton_getData_FromSepidar.clicked.connect(self.Read_Product_Item_from_Sepidar)

        #### Read Pdf File
        self.pushButton_Instruction.clicked.connect(self.ReadFileInstruction)
        ####Read Picture Product
        self.pushButton_PictureProduct.clicked.connect(self.ReadFilePicutre)

        self.pushButton_Save.clicked.connect(self.Save_SQL_opc)
        self.pushButton_delete.clicked.connect(self.Delete_Value)
        self.pushButton_Save_opc.clicked.connect(self.Display_opc_list)

        self.pushButton_delete_rows.clicked.connect(self.Delete_opc)
        # self.pushButton_add_column.clicked.connect(self.Delete_opc)
        self.pushButton_add_row.clicked.connect(self.AddRow)
        self.pushButton_row_delete.clicked.connect(self.RemoveRow)
        # self.pushButton_add_column.clicked.connect(self.Read_File)
        self.actionOpen_File.triggered.connect(self.Read_File)
        self.lineEdit_2.textEdited.connect(self.Search_Code_Product)
        self.pushButton_read.clicked.connect(self.read_resourses)
        self.actionExit.triggered.connect(MainWindow.close)
        self.count = 0

        self.tableWidget_3.clicked.connect(self.Process_selected)

        ##############  LOAD Setting widget
        # Setting_UI = Setting_server.Ui_Setting_Network()
        # Setting_widget =  QWidget()
        # Setting_UI.setupUi(Setting_widget)
        #
        # self.actionNetwork_Setting.triggered.connect(lambda: Setting_widget.show())

    def Process_selected(self):
        asyncio.run(self.Cell_clected())
        ##Search Code Product From Database Sepidar

    def Search_Code_Product(self):
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.clear()
        self.tableWidget_4.clearContents()
        if len(self.lineEdit_2.text()) > 3:
            Cursor = MssqlConnection.cnxn_2.cursor()
            Cursor.execute(f"SELECT  Code,Title FROM INV.Item  WHERE Code  like  '{self.lineEdit_2.text()}%';")
            Prosuct_item = Cursor.fetchall()

            for row_number, row_data in enumerate(Prosuct_item):
                self.tableWidget_4.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget_4.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        ## Reac Product Item From Database Sepidar And Save to DataBase Tracebility

    def Read_Product_Item_from_Sepidar(self):
        DB_save_server = Connect_To_server.DB_save
        MY_curser = MssqlConnection.cnxn_2.cursor()
        MyCursor_server = Connect_To_server.DB_save.cursor()
        MY_curser.execute("SELECT  Code,Title FROM INV.Item;")
        all_product = MY_curser.fetchall()
        # print(all_product)

        # Q_Select = " select CodProduct from  Product"
        # MyCursor_server.execute(Q_Select)
        # Q_Product_code = MyCursor_server.fetchall()
        print("Started")

        c = 0
        # for i in enumerate(all_product):
        #     c = c + 1
        #     # print(i[1][0])
        #     # print(i[1][1])
        #     print(c)
        #     sql = f"INSERT INTO  Products(Product_id,  CodProduct, Discription, CodTracebility) VALUES ( %s, %s, %s, %s)"
        #     # f" where not EXISTS(select * from Product where  CodProduct= {i[1][1]})"
        #     Uid = uuid.uuid4()
        #     SU = shortuuid.encode(Uid)
        #
        #     val = (c, i[1][0], f"{i[1][1]}", SU[:7])
        #     MyCursor_server.execute(sql, val)
        # DB_save_server.commit()
        for i in enumerate(all_product):
            c = c + 1
            # print(i[1][0])
            # print(i[1][1])
            sql = f"INSERT INTO  InvProducts_part(PartNumber, discription) VALUES ( %s, %s)"
            # f" where not EXISTS(select * from Product where  CodProduct= {i[1][1]})"
            # Uid = uuid.uuid4()
            # SU = shortuuid.encode(Uid)

            val = ( int(i[1][0]), f"{i[1][1]}")
            print("type i[1][0]", i[1][0])
            print("type i[1][1]", i[1][1])

        #     MyCursor_server.execute(sql, val)
        #     print(c)
        # DB_save_server.commit()

        ## Append Column To Widget Opc

    async def Cell_clected(self):
        await asyncio.sleep(.10)

        for self.cell_opc_excel in self.tableWidget_3.selectedItems():
            # self.get_cell = self.cell_opc_excel.text()
            # self.rep_cell = self.get_cell.replace("*", " ")
            # self.spl_cell = self.rep_cell.split()
            self.remove_cell_selected()

        #
        # for self.cell_read_resorce in self.tableWidget_show_resources.selectedItems():
        #     # self.get_cell = self.cell_read_resorce.text()
        #     # self.rep_cell = self.get_cell.replace("*", " ")
        #     # self.spl_cell = self.rep_cell.split()
        #     self.remove_cell_selected()
        #
        #
        # for self.cell_opc_excel in self.tableWidget_3.selectedItems():
        #     # self.get_cell = self.cell_opc_excel.text()
        #     # self.rep_cell = self.get_cell.replace("*", " ")
        #     # self.spl_cell = self.rep_cell.split()
        #     self.remove_cell_selected()

    def remove_cell_selected(self):
        if self.cell_opc_excel.column() == 3:
            msg_Q = QMessageBox()
            msg_Q.setIcon(QMessageBox.Information)
            msg_Q.setText("برای پاک کردن ردیف  لطفا تایید کنید ")

            msg_Q.setWindowTitle("Delete dialog")
            msg_Q.setDetailedText("مقادیری که در ردیف  میباشد پاک میشود میشود")
            msg_Q.addButton(QMessageBox.Yes)
            msg_Q.addButton(QMessageBox.No)
            msg_Q.setDefaultButton(QMessageBox.Yes)
            return_value = msg_Q.exec_()
            if return_value == QMessageBox.Yes:
                self.tableWidget_3.removeRow(self.cell_opc_excel.row())
                # self.get_value_table_Product()

        # if self.cell_read_resorce.column() == 4:
        #     msg_Q = QMessageBox()
        #     msg_Q.setIcon(QMessageBox.Information)
        #     msg_Q.setText("برای پاک کردن ردیف  لطفا تایید کنید ")
        #
        #     msg_Q.setWindowTitle("Delete dialog")
        #     msg_Q.setDetailedText("مقادیری که در ردیف  میباشد پاک میشود میشود")
        #     msg_Q.addButton(QMessageBox.Yes)
        #     msg_Q.addButton(QMessageBox.No)
        #     msg_Q.setDefaultButton(QMessageBox.Yes)
        #     return_value = msg_Q.exec_()
        #     if return_value == QMessageBox.Yes:
        #         self.tableWidget_show_resources.removeRow(self.cell_opc_excel.row())

    def AddColumn(self):
        self.count_del = 0
        self.count = 0
        self.col_add = self.tableWidget_3.columnCount()

        self.tableWidget_3.insertColumn(self.col_add)
        self.count + 1
        self.count_del + 1
        ## Remove Column From Widget Opc

    def RemoveColumn(self):
        try:
            self.col_del = self.tableWidget_3.rowCount()

            self.tableWidget_3.removeColumn(self.count_del)
            self.count - 1
        except:
            msg = QMessageBox()
            msg.setText("ستونی برای پاک کردن نیست ")
            msg.setWindowTitle("خطا")
            msg.exec_()
        ## Add Row to widget Opc

    def AddRow(self):
        self.count_row = 0
        # self.count = 0
        self.row_add = self.tableWidget_3.rowCount()

        self.tableWidget_3.insertRow(self.row_add)
        self.tableWidget_3.setItem(self.tableWidget_3.rowCount() - 1, 3, QTableWidgetItem("حذف"))
        self.tableWidget_3.item(self.tableWidget_3.rowCount() - 1, 3).setIcon(QTA.icon('mdi.delete'))

        self.count + 1
        self.count_row + 1
        ## Remove row  from  Widget Opc

    def RemoveRow(self):
        try:
            self.row_del = self.tableWidget_3.rowCount()
            # self.tableWidget_3.removeRow(MYROW)
            self.tableWidget_3.removeRow(self.tableWidget_3.rowCount() - 1)

        except:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.warning)
            # msg.setStyle("fusion")
            msg.setText("ردیفی  برای پاک کردن نیست ")
            # msg.setInformativeText('More information')
            msg.setWindowTitle("خطا")
            msg.exec_()
        ## Get Opc List from  table opc_list and show data to table opc managment

    def Display_opc_list(self):
        try:

            model = self.tableWidget_3.model()
            self.data_SQL_opc_show = []

            for row in range(model.rowCount()):
                self.data_SQL_opc_show.append([])
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    self.data_SQL_opc_show[row].append(model.data(index))
            numrows = len(self.data_SQL_opc_show) - 1
            numcols = len(self.data_SQL_opc_show[0])

        except:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.warning)
            # msg.setStyle("fusion")
            msg.setText("دیتای در جدول نیست")
            # msg.setInformativeText('More information')
            msg.setWindowTitle("خطا")
            msg.exec_()
        try:

            self.tableWidget_operator_to_OPC.setColumnCount(numcols)
            self.tableWidget_operator_to_OPC.setRowCount(numrows)
            for row in range(numrows):
                for column in range(numcols):

                    if (self.data_SQL_opc_show[row][column]):
                        self.tableWidget_operator_to_OPC.setItem(row, column,
                                                                 QTableWidgetItem(
                                                                     (self.data_SQL_opc_show[row][column])))
                    else:
                        self.tableWidget_operator_to_OPC.setItem(row, column, QTableWidgetItem(
                            (self.data_SQL_opc_show[row][column])))
        except:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.warning)
            # msg.setStyle("fusion")
            msg.setText("عملیات نشان دادن دیتا در جدول  با موفقیت انجام نشد")
            # msg.setInformativeText('More information')
            msg.setWindowTitle("خطا")
            msg.exec_()
        ##read excel  file Opc from dialog Operator

    def Read_File(self):
        try:
            File = QFileDialog.getOpenFileName()
            File_path = File[0]

            #################################################################
            read_file = open(File_path, "r")
            Data_file = pd.read_excel(File_path)
            df = pd.DataFrame(Data_file, columns=['مراحل ساخت', 'ایستگاه کاری', 'پرسنل'])
            df_values = df.values.tolist()
            numrows = len(df_values)
            numcols = len(df_values[0])

        except:
            msg = QMessageBox()

            msg.setText("فایل انتخاب نشد")

            msg.setWindowTitle("خطا")
            msg.exec_()
        try:
            self.tableWidget_3.setColumnCount(4)
            self.tableWidget_3.setRowCount(numrows)
            for row in range(numrows):
                for column in range(numcols):

                    if (df_values[row][column]):
                        self.tableWidget_3.setItem(row, column,
                                                   QTableWidgetItem((f"{df_values[row][column]}")))

                self.tableWidget_3.setItem(row, 3, QTableWidgetItem('حذف'))
                self.tableWidget_3.item(row, 3).setIcon(QTA.icon('mdi.delete'))

        except:
            msg = QMessageBox()

            msg.setText("فایل نمایش داده نشد ")
            # msg.setInformativeText('More information')
            msg.setWindowTitle("خطا")
            msg.exec_()

    def ReadFileInstruction(self):
        try:
            File = QFileDialog.getOpenFileName()
            File_path = File[0]

            #################################################################
            with  open(File_path, "rb") as PdfFile:
                self.Instruction = PdfFile.read()





        except:
            msg = QMessageBox()

            msg.setText("فایل انتخاب نشد")

            msg.setWindowTitle("خطا")
            msg.exec_()

    def ReadFilePicutre(self):
        try:
            File = QFileDialog.getOpenFileName()
            File_path = File[0]

            #################################################################
            with  open(File_path, "rb") as PdfFile:
                self.ProductPicture = PdfFile.read()
                # print(PdfFile[:10])


        except:
            msg = QMessageBox()

            msg.setText("فایل انتخاب نشد")

            msg.setWindowTitle("خطا")
            msg.exec_()

    def Save_SQL_opc(self):
        DB_save = Connect_To_server.DB_save

        MyCursor = Connect_To_server.DB_save.cursor()
        ##  save start stationnumber to order code
        try:

            sqlt_1 = ('replace into `Station_to_Order`(`StationNumber`, `CodeOrder`) VALUES (%s, %s)')
            val_1 = (f"{int(self.lineEdit_StationNumber.text())}", f"{int(self.lineEdit_Order_Code.text())}")
            MyCursor.execute(sqlt_1, val_1)
            DB_save.commit()
        except:
            msg = QMessageBox()

            msg.setText("کد سفارش را وارد نکرده اید ")
            # msg.setInformativeText('More information')
            msg.setWindowTitle("خطا")
            msg.exec_()
        try:
            model = self.tableWidget_operator_to_OPC.model()
            self.data_SQL_opc = []
            ## Get CodeProduct From Related data save to DataBase
            MyCursor.execute(
                f" SELECT code_Product  FROM Opc_Product  WHERE code_Product='{self.lineEdit_code_Product.text()}' ")
            codeproduct = MyCursor.fetchall()

            for row in range(model.rowCount()):
                self.data_SQL_opc.append([])
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    self.data_SQL_opc[row].append(model.data(index))
            len_data_sql_opc = 0
            len_data_sql_opc = len(self.data_SQL_opc)

            roww = 0
            self.Station_number = 0
            self.Operator_Code = 0

            # for row in enumerate(self.data_SQL_opc):
            #     self.Order_Opc = str(self.data_SQL_opc[roww][0])
            #
            #
            #     self.Station_number = str(self.data_SQL_opc[roww][1])
            #     self.Operator_Code = str(self.data_SQL_opc[roww][2])
            #     roww += 1
            #     if roww > len_data_sql_opc:
            #         break
            #
            ################## get Product id   for validation data  checkeing  data from line edite
            qet_ref_product_id = f"SELECT Product_id FROM Products WHERE CodProduct='{str(self.lineEdit_code_Product.text())}' "
            MyCursor.execute(qet_ref_product_id)
            product_id_ref = MyCursor.fetchall()

            #         #####
            #         ####Inserte Data with loop
            #         #
            if codeproduct != []:
                sql_delete = f" DELETE FROM Opc_Product   where   code_Product='{self.lineEdit_code_Product.text()}';"

                MyCursor.execute(sql_delete)
                DB_save.commit()
                sql = "INSERT INTO  Opc_Product (P_id, code_Product,  Opc_Order, Order_code_Product, Instruction, 	picture) " \
                      " VALUES ( %s, %s, %s, %s, %s, %s)  "

                val = (f"{int(product_id_ref[0][0])}", f"{int(self.lineEdit_code_Product.text())}",
                       f"{str(self.data_SQL_opc)}",
                       f"{str(self.lineEdit_Order_Code.text())}",
                       self.Instruction,
                       self.ProductPicture)
                MyCursor.execute(sql, val)
                DB_save.commit()

                print('update')
                msg = QMessageBox()
                msg.setText("عملیات اپدیت  در دیتا بیس  انجام شد ")
                # msg.setInformativeText('More information')
                msg.setWindowTitle("موفق")
                msg.exec_()
                print('insert')
            else:
                sql = "INSERT INTO  Opc_Product (P_id, code_Product,  Opc_Order,  Order_code_Product, Instruction, 	picture) " \
                      " VALUES ( %s, %s, %s, %s , %s, %s)  "
                # try:
                val = (f"{int(product_id_ref[0][0])}", f"{int(self.lineEdit_code_Product.text())}",
                       f"{str(self.data_SQL_opc)}",
                       f"{str(self.lineEdit_Order_Code.text())}",
                       self.Instruction,
                       self.ProductPicture)

                MyCursor.execute(sql, val)
                DB_save.commit()
                msg = QMessageBox()

                msg.setText("عملیات ذخیره در دیتا بیس  انجام شد ")
                # msg.setInformativeText('More information')
                msg.setWindowTitle("موفق")
                msg.exec_()
                print('insert')

        except:
            msg = QMessageBox()

            msg.setText("احتمالا کد محصول وارد شده اشتباه است ")
            # msg.setInformativeText('More information')
            msg.setWindowTitle("خطا")
            msg.exec_()

        #
        # except:
        #     msg = QMessageBox()
        #     # msg.setIcon(QMessageBox.warning)
        #     # msg.setStyle("fusion")
        #     msg.setText("دیتای برای ثبت نیست")
        #     # msg.setInformativeText('More information')
        #     msg.setWindowTitle("خطا")
        #     msg.exec_()

    def Delete_opc(self):
        msg_Q = QMessageBox()
        msg_Q.setIcon(QMessageBox.Information)
        msg_Q.setText("برای پاک کردن اطلاعات   لطفا تایید کنید ")

        msg_Q.setWindowTitle("Delete dialog")
        msg_Q.setDetailedText("مقادیری که در فرم میباشد پاک میشود ")
        msg_Q.addButton(QMessageBox.Yes).setText('Opc')
        msg_Q.addButton(QMessageBox.Ok).setText('Product')
        msg_Q.addButton(QMessageBox.No)
        msg_Q.setDefaultButton(QMessageBox.Yes)
        return_value = msg_Q.exec_()
        if return_value == QMessageBox.Yes:
            self.tableWidget_3.clearContents()
            self.tableWidget_3.setRowCount(0)
        elif return_value == QMessageBox.Ok:
            self.tableWidget_4.clearContents()
            self.tableWidget_4.setRowCount(0)

    def Delete_Value(self):
        msg_Q = QMessageBox()
        msg_Q.setIcon(QMessageBox.Information)
        msg_Q.setText("برای پاک کردن اطلاعات   لطفا تایید کنید ")

        msg_Q.setWindowTitle("Delete dialog")
        msg_Q.setDetailedText("مقادیری که در فرم میباشد پاک میشود")
        msg_Q.addButton(QMessageBox.Yes).setText('Opc')
        msg_Q.addButton(QMessageBox.Ok).setText('resources')
        msg_Q.addButton(QMessageBox.No)
        msg_Q.setDefaultButton(QMessageBox.Yes)
        return_value = msg_Q.exec_()
        if return_value == QMessageBox.Yes:
            self.tableWidget_operator_to_OPC.clearContents()
            self.tableWidget_operator_to_OPC.setRowCount(0)
        elif return_value == QMessageBox.Ok:
            self.tableWidget_show_resources.clearContents()
            self.tableWidget_show_resources.setRowCount(0)

    def read_resourses(self):
        self.tableWidget_show_resources.clearContents()

        DB = Connect_To_server.DB_save

        Mycursor = Connect_To_server.DB_save.cursor()
        Mycursor.execute("select  CodeOperator,  Stationnumber from  Client_connected")
        list_live_resours = []
        live_resours = Mycursor.fetchall()
        print(type(live_resours))
        live_resours = list(live_resours)
        print(type(live_resours))

        self.tableWidget_show_resources.clearContents()
        self.tableWidget_show_resources.setRowCount(0)
        for row_number, row_data in enumerate(live_resours):

            self.tableWidget_show_resources.insertRow(row_number)
            #### GET  NAME OPERATOR   Width code operator

            # if len(self.lineEdit_4.text()) == 5:

            cursor = MssqlConnection.cnxn_2.cursor()
            cursor.execute(f"select  Title  from ACC.DL  where Code='{str(live_resours[row_number][0])} ' ;")

            self.Code_Operator_1 = cursor.fetchall()
            self.Code_Operator_1 = str(self.Code_Operator_1)
            self.Code_Operator_1 = self.Code_Operator_1.replace("(", "")
            self.Code_Operator_1 = self.Code_Operator_1.replace(")", "")
            self.Code_Operator_1 = self.Code_Operator_1.replace("[", "")
            self.Code_Operator_1 = self.Code_Operator_1.replace("]", "")
            self.Code_Operator_1 = self.Code_Operator_1.replace(",", "")
            self.Code_Operator_1 = self.Code_Operator_1.replace("'", "")
            self.Code_Operator_1 = self.Code_Operator_1.split()
            self.Code_Operator_3 = self.Code_Operator_1[1] + " " + self.Code_Operator_1[0]
            list_live_resours = []
            cc = [row_data[1], self.Code_Operator_3]
            list_live_resours.append(cc)
            print(list_live_resours[0])

            # row_data[0]  = self.Code_Operator_3
            for column_number, data in enumerate(list_live_resours[0]):
                ...

                self.tableWidget_show_resources.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def Save_resourses(self):
        DB = Connect_To_server.DB_save

        Mycursor = Connect_To_server.DB_save.cursor()
        Mycursor.execute(
            f"INSERT INTO `Opc_Resours`(`P_id`, `Device_Station`, `Operator_Station`) VALUES ([value-1],[value-2],[value-3])")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("material")
    MainWindow = QtWidgets.QMainWindow()
    apply_stylesheet(app, theme='light_blue.xml')
    # apply_stylesheet(app, theme='dark_purple.xml')
    ui = OPC_UI_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())




