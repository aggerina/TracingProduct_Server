#
# from qt_material import apply_stylesheet
from PyQt5.QtCore import QStringListModel

#from dill.tests.test_selected import _d
import psycopg2
from queue import Queue
# from BarcodeReader import BarcodeReader
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import Setting_server
import yaml
import sys
import requests
import  urllib.request
import os
from pathlib import Path
import time
from  multiprocessing.connection import Listener
import datetime
from threading import Thread , Timer

import asyncio


time.sleep(1)
# from  multithreading import MultiThread


porotocol = "http://"

Operator = ''
StartOrder = False
BASE_DIR = Path(__file__).resolve().parent.parent
StateOrderToSend = True


from evdev import InputDevice, categorize, ecodes
# from  multiprocessing import Process
import time

from multiprocessing.connection import Client


# QueUe = Queue
# QueUe(maxsize=100)
QueUe = []

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # self.QueUe = Queue
        # self.QueUe(maxsize=100)
        # self.QueUe.put()
        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
        self.ListBarcodeRecived = []
        self.ListBarcodeExited = []
        self.Entery = True
        self.State = "Entery"
        # self.CountRecived = 0
        # self.CountExit = 0
        self.LastOrderCode = ''
        self.ReadSetting()
        self.USER_Logined = False
        uic.loadUi(self.CURRENT_DIR+'/'+'ClientApp_07.ui', self)
        self.showMaximized()
        # self.lineEdit_Operator.setReadOnly(True)
        self.label_ConnectionDatabase.setUpdatesEnabled(True)
        self.label_ProductPicture.setUpdatesEnabled(True)
        # self.label_PDF1.setUpdatesEnabled(True)
        # self.label_PDF2.setUpdatesEnabled(True)

        #####Setting UI
        self.tblBarcodes.setColumnWidth(0,80)
        self.tblBarcodes.setColumnWidth(1,100)
        self.tblBarcodes_Out.setColumnWidth(0,80)
        self.tblBarcodes_Out.setColumnWidth(1,100)

        self.table_Cuase.setColumnWidth(1,600)
        self.table_Cuase.setColumnWidth(0,80)
        self.table_BOM.setColumnWidth(1,600)
        self.table_BOM.setColumnWidth(0,80)
        self.tableBOM2_Exit.setColumnWidth(0,80)
        self.tableBOM2_Exit.setColumnWidth(1,500)
        self.tableBOM2_Exit.setColumnWidth(2,200)
        self.table_BOM_2.setColumnWidth(1,600)
        self.table_BOM_2.setColumnWidth(0,80)



        # Timers
        # self.timerNetwork = Timer(5, self.ConnectionTest)
        # self.timerNetwork.start()
        #
        # # processClock =  Thread(target=Window.ShowClock)
        # # processClock.start()
        # self.timerClock = Timer(1, self.ShowClock)
        # self.timerClock.start()

        # self.ListModelBarcode = QStringListModel(self.ListBarcodeRecived)

        #### Load Functions
        self.radioEntery.clicked.connect(self.RadioEntery)
        self.radioExit.clicked.connect(self.RadioExit)

        with open(f"{self.CURRENT_DIR}/LastOperator.ptp", 'r') as file:
            barcodestartUser = file.read()
            file.close()
        if len(barcodestartUser) == 7:
            self.GetResponseUser(barcodestartUser)

    # def getSelectedItem_1(self):
    #     Cause = []
    #
    #
    #
    #     # item = items[0]
    #     # return (item.data(0, Qt.DisplayRole), item.data(1, Qt.DisplayRole))
    #     print(item)
        self.tblBarcodes_Out.clicked.connect(self.Process_selected_EXIT)
        self.tblBarcodes.clicked.connect(self.Process_selected_Entry)
        self.table_BOM.clicked.connect(self.Process_selected_BOM2)
        self.table_Cuase.clicked.connect(self.Process_selected_BOM2_EXIT)
        self.tableBOM2_Exit.clicked.connect(self.Process_GetData)
        # try:
        # self.BTNSave.clicked.connect(self.PostRepairData(Operator=self.LastOperatorCode,Entery='', State=self.State, Exit=str(self.comboBox_Exit.currentText()), Product=self.Product[0]['Product_code'],
        #                                                  Station=self.StationNumber, Order=self.OrderData[0]['code'],
        #                                                 Description=str(self.lineEdit_RepairDescroption.text()),
        #                                                  tracebilityCode=self.TraceBilityCodeData['Tracebility_code']))
        #     print("successfuly")
        # except:
        #     print("error")

    def Process_selected_EXIT(self):
        asyncio.run(self.Cell_clected_Exit())

    def Process_selected_BOM2(self):
        asyncio.run(self.Cell_clected_BOM2())
    def Process_GetData(self):
        asyncio.run(self.Cell_clected_Data())

    async def Cell_clected_Data(self):
        await asyncio.sleep(.10)

        i = 0
        self.listDataCuase = ''
        self.lastDataCount = 0
        for self.cellData in self.tableBOM2_Exit.selectedItems():

            self.get_Data = self.cellData.text()
            self.listDataCuase = f"[{self.get_Data}]"
        #     print(self.cellData.row())
        #     self.listDataCuase.insert()
        #     if self.cellData.row() == self.lastDataCount:
        #         self.listDataCuase[i-1].append(self.get_Data)
        #     else:
        #         self.listDataCuase[i].append(self.get_Data)
        #
        #     i = i + 1
        #     self.lastDataCount = self.cellData.row()
        #
        # print(self.listDataCuase)





                #     # print(self.get_cellEntery)
        #     # self.rep_cell = self.get_cell.replace("*", " ")
        #     # self.spl_cell = self.rep_cell.split()
        # if self.cellBOM2.column() == 0:
        #     self.table_BOM_2.clearContents()
        #     self.table_BOM_2.setRowCount(0)
        #     response = requests.get(
        #         f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Products/{self.get_cellBOM2}/',
        #         timeout=2)
        #     BomData = response.json()
        #     try:
        #         # print(BomData['BOMS'][0])
        #         ListBOMS = BomData['BOMS']
        #
        #         Desc_BOMSData = []
        #
        #
        #         for i in range(len(ListBOMS)):
        #             Desc_BOMSData.append([ListBOMS[i]['PartNumber'], ListBOMS[i]['description']])
        #             # res = requests.get(
        #             #     f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Parts/{i}/',
        #             #     timeout=2)
        #             # BomData = res.json()
        #
        #
        #         for row in range(len(Desc_BOMSData)):
        #             self.table_BOM_2.insertRow(row)
        #
        #             for column in range(len(Desc_BOMSData[0])):
        #                 self.table_BOM_2.setItem(row, column, QtWidgets.QTableWidgetItem(Desc_BOMSData[row][column]))
        #     except:
        #         msg = QtWidgets.QMessageBox()
        #         msg.setIcon(QtWidgets.QMessageBox.Critical)
        #         msg.setText("BOM ندارد")
        #         msg.setWindowTitle("خطا")
        #         msg.exec_()
        #


    def Process_selected_BOM2_EXIT(self):
        asyncio.run(self.Cell_clected_BOM2_Exit())

    async def Cell_clected_BOM2_Exit(self):
        await asyncio.sleep(.10)


        for self.cellBOM2EXit in self.table_Cuase.selectedItems():
            self.get_cellBOM2EXit = self.cellBOM2EXit.text()

            # print(self.get_cellEntery)
            # self.rep_cell = self.get_cell.replace("*", " ")
            # self.spl_cell = self.rep_cell.split()
        if self.cellBOM2EXit.column() == 0:
            self.tableBOM2_Exit.clearContents()
            self.tableBOM2_Exit.setRowCount(0)
            response = requests.get(
                f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Products/{self.get_cellBOM2EXit}/',
                timeout=2)
            BomData = response.json()
            # print(BomData['BOMS'][0])
            try:
                ListBOMS = BomData['BOMS']

                Desc_BOMSData = []


                for i in range(len(ListBOMS)):
                    Desc_BOMSData.append([ListBOMS[i]['PartNumber'], ListBOMS[i]['description']])
                    # res = requests.get(
                    #     f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Parts/{i}/',
                    #     timeout=2)
                    # BomData = res.json()


                for row in range(len(Desc_BOMSData)):
                    self.tableBOM2_Exit.insertRow(row)

                    for column in range(len(Desc_BOMSData[0])):
                        self.tableBOM2_Exit.setItem(row, column, QtWidgets.QTableWidgetItem(Desc_BOMSData[row][column]))
            except:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("BOM ندارد ")
                msg.setWindowTitle("خطا")
                msg.exec_()



    def Process_selected_Entry(self):
            asyncio.run(self.Cell_clected_Entery())

    async def Cell_clected_BOM2(self):
        await asyncio.sleep(.10)


        for self.cellBOM2 in self.table_BOM.selectedItems():
            self.get_cellBOM2 = self.cellBOM2.text()

            # print(self.get_cellEntery)
            # self.rep_cell = self.get_cell.replace("*", " ")
            # self.spl_cell = self.rep_cell.split()
        if self.cellBOM2.column() == 0:
            self.table_BOM_2.clearContents()
            self.table_BOM_2.setRowCount(0)
            response = requests.get(
                f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Products/{self.get_cellBOM2}/',
                timeout=2)
            BomData = response.json()
            try:
                # print(BomData['BOMS'][0])
                ListBOMS = BomData['BOMS']

                Desc_BOMSData = []


                for i in range(len(ListBOMS)):
                    Desc_BOMSData.append([ListBOMS[i]['PartNumber'], ListBOMS[i]['description']])
                    # res = requests.get(
                    #     f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Parts/{i}/',
                    #     timeout=2)
                    # BomData = res.json()


                for row in range(len(Desc_BOMSData)):
                    self.table_BOM_2.insertRow(row)

                    for column in range(len(Desc_BOMSData[0])):
                        self.table_BOM_2.setItem(row, column, QtWidgets.QTableWidgetItem(Desc_BOMSData[row][column]))
            except:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("BOM ندارد")
                msg.setWindowTitle("خطا")
                msg.exec_()


    async def Cell_clected_Exit(self):
        await asyncio.sleep(.10)


        for self.cellExit in self.tblBarcodes_Out.selectedItems():
            self.get_cellExit = self.cellExit.text()

            # print(self.get_cellEntery)
            # self.rep_cell = self.get_cell.replace("*", " ")
            # self.spl_cell = self.rep_cell.split()
        if self.cellExit.column() == 1:
            self.table_Cuase.clearContents()
            self.table_Cuase.setRowCount(0)
            response = requests.get(
                f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Products/{self.get_cellExit}/',
                timeout=2)
            BomData = response.json()
            # print(BomData['BOMS'][0])
            ListBOMS = BomData['BOMS']

            Desc_BOMSData = []


            for i in range(len(ListBOMS)):
                Desc_BOMSData.append([ListBOMS[i]['PartNumber'], ListBOMS[i]['description']])
                # res = requests.get(
                #     f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Parts/{i}/',
                #     timeout=2)
                # BomData = res.json()


            for row in range(len(Desc_BOMSData)):
                self.table_Cuase.insertRow(row)

                for column in range(len(Desc_BOMSData[0])):
                    self.table_Cuase.setItem(row, column, QtWidgets.QTableWidgetItem(Desc_BOMSData[row][column]))

    async def Cell_clected_Entery(self):
        await asyncio.sleep(.10)


        for self.cellEntery in self.tblBarcodes.selectedItems():
            self.get_cellEntery = self.cellEntery.text()

            # print(self.get_cellEntery)
            # self.rep_cell = self.get_cell.replace("*", " ")
            # self.spl_cell = self.rep_cell.split()
        if self.cellEntery.column() ==1:
            self.table_BOM.clearContents()
            self.table_BOM.setRowCount(0)
            response = requests.get(
                f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Products/{self.get_cellEntery}/',
                timeout=2)
            BomData = response.json()
            # print(BomData['BOMS'][0])
            self.ListBOMS = BomData['BOMS']

            self.Desc_BOMSData = []


            for i in  range(len(self.ListBOMS)):


                self.Desc_BOMSData.append([self.ListBOMS[i]['PartNumber'],self.ListBOMS[i]['description']])
                # res = requests.get(
                #     f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Parts/{i}/',
                #     timeout=2)
                # BomData = res.json()


            for row in range(len(self.Desc_BOMSData)):
                self.table_BOM.insertRow(row)

                for column in range(len(self.Desc_BOMSData[0])):
                    self.table_BOM.setItem(row, column, QtWidgets.QTableWidgetItem(self.Desc_BOMSData[row][column]))



    def RadioEntery(self):
        self.Entery = True
        self.State = "Entery"


    def RadioExit(self):
        self.Entery = False
        self.State = "Exit"


    def ShowClock(self):

        # self.time = QtCore.QTime.currentTime()


        while True:

            # time.sleep(1)
            now = datetime.datetime.now()
            curenttime = now.strftime("%H:%M:%S")
            # curenttime = now.strftime("%H:%M")

            # text = time.toString('hh:mm:ss')
            # self.lcdClock.setText(text)
            self.lcdClock.setText(curenttime)
            time.sleep(1)


    def Exit(self):
        self.processBarcode.join()
        self.processBarcode.close()
        self.processGetBarcode.join()
        self.processGetBarcode.close()
        self.close()
    def ReadSetting(self):
        try:
            with open(f"{self.CURRENT_DIR}/config.yaml", "r") as yamlfile:
                self.data_r = yaml.load(yamlfile, Loader=yaml.FullLoader)

                self.PORT = self.data_r[0]['DATA_Setting']['send_port']
                self.Server_Address = self.data_r[0]['DATA_Setting']['Server_Address']
                self.DataBase_Name = self.data_r[0]['DATA_Setting']['DataBase_Name']
                self.USER_SERVER = self.data_r[0]['DATA_Setting']['USER_SERVER']
                self.PASSWORD_SERVER = self.data_r[0]['DATA_Setting']['PASSWORD_SERVER']
                self.DataBase_Address = self.data_r[0]['DATA_Setting']['DataBase_Address']
                self.StationNumber = self.data_r[0]['DATA_Setting']['StationNumber']
                self.DatabasePort = self.data_r[0]['DATA_Setting']['DatabasePort']
                self.BarcodeShutdown = self.data_r[0]['DATA_Setting']['BarcodeShutdown']
                self.BarcodeRestart = self.data_r[0]['DATA_Setting']['BarcodeRestart']

                self.BarcodeRepair = self.data_r[0]['DATA_Setting']['BarcodeRepair']
                self.BarcodeProdocer = self.data_r[0]['DATA_Setting']['BarcodeProdocer']
                yamlfile.close()
        except:
            print("ارتباط با دیتا بیس برقرار نشد ")
    def ReadStateOperator(self):
        with open(f"{self.CURRENT_DIR}/StateOperator.yaml", "r") as yamlfile:
            self.StateOperator = yaml.load(yamlfile, Loader=yaml.FullLoader)
            yamlfile.close()
            return self.StateOperator
    def WriteStateOperator(self, State):
        with open(f"{self.CURRENT_DIR}/StateOperator.yaml", "w") as yamlfile:
            Station = {
                'Operator': State
            }
            yaml.dump(Station, yamlfile)
            yamlfile.close()

    def ReadStateOrder(self):
        with open(f"{self.CURRENT_DIR}/StateOrder.yaml", "r") as yamlfile:
            self.StateOperator = yaml.load(yamlfile, Loader=yaml.FullLoader)
            yamlfile.close()
            return self.StateOperator
    def WriteStateOrder(self, State):
        with open(f"{self.CURRENT_DIR}/StateOrder.yaml", "w") as yamlfile:
            Order = {
                'Order': State
            }
            yaml.dump(Order, yamlfile)
            yamlfile.close()
    def GetResponseUser(self, barcode):
        self.Warning.clear()
        try:
            response = requests.get(
                f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Persons/{barcode}/get_Person/',
                timeout=2)
            if response.status_code == 200:
                self.USER_Logined = True
                self.Warning.clear()
                self.Warning.setStyleSheet(' background-color: #ffffff')
                data = response.json()
                self.LastOperatorCode = data['CodeOperator']
                pixmap = QtGui.QPixmap()
                with open(f"{self.CURRENT_DIR}/LastOperator.ptp", 'r') as file:
                    self.startoperator = file.read()
                    file.close()
                if self.startoperator == '0':
                    StartOrder = True
                if self.startoperator == barcode:
                    StartOrder = True
                try:
                    if StartOrder == True:
                        if data['Start'] == True:
                            with open(f"{self.CURRENT_DIR}/LastOperatorName.ptp", 'w') as file:
                                file.write(str(data['LastName']))
                                file.close()
                            with open(f"{self.CURRENT_DIR}/LastOperator.ptp", 'w') as file:
                                file.write(str(data['StartBarcode']))
                                file.close()
                            data['Image'] = porotocol + self.Server_Address + ":" + self.PORT + data['Image']
                            image = urllib.request.urlopen(data['Image']).read()
                            pixmap.loadFromData(image)
                            self.label_Picture.setPixmap(pixmap)
                            self.lineEdit_Operator.setText(str(data['Name'] + ' ' + data['LastName']))
                            self.lineEdit_CodeOperator.setText(str(data['CodeOperator']))
                except:
                    with open(f"{self.CURRENT_DIR}/LastOperatorName.ptp", 'r') as file:
                        lastOperatorName = file.read()
                        file.close()
                    self.Warning.setText(
                        f" توسط {lastOperatorName} ایستگاه مشغول کار است")
                if data['Start'] == False:
                    with open(f"{self.CURRENT_DIR}/LastOperator.ptp", 'r') as file:
                        operator = file.read()
                        file.close()
                    if operator == str(data['StartBarcode']):
                        StartOrder = True
                        self.Warning.clear()
                        self.label_Picture.clear()
                        self.lineEdit_Operator.clear()
                        self.lineEdit_OrderCode.clear()
                        self.lineEdit_ProductCode.clear()
                        self.lineEdit_ProductDescription.clear()
                        self.lineEdit_CodeOperator.clear()
                        self.lineEdit_OrderCount.clear()
                        self.Warning.clear()
                        self.label_PDF2.clear()
                        self.label_PDF1.clear()
                        self.label_ProductPicture.clear()
                        self.USER_Logined = False
                        self.ListBarcodeRecived = []
                        self.ListBarcodeExited = []
                        # self.CountRecived = 0
                        # self.CountExit = 0
                        self.LiRecive.clear()
                        self.LiExit.clear()
                        self.tblBarcodes.clearContents()
                        self.tblBarcodes.setRowCount(0)


                        # time.sleep(0.1)
                        with open(f"{self.CURRENT_DIR}/LastOperator.ptp", 'w') as file:
                            file.write('0')
                            file.close
                self.WriteStateOperator(data)
        except:
            self.label_connectionServer.setText("ارتباط با سرور برقرار نیست ")
            self.label_connectionServer.setStyleSheet(' background-color: #f0a6ad')
    def GetProductResponse(self, barcode):
        if self.USER_Logined == True:
            # self.ShowListBarcodeRecived()
            if self.Entery == True:

                if barcode in self.ListBarcodeRecived:

                    self.Warning.setText(f"بار کد {barcode} :قبلا استفاده شده ")
                    self.Warning.setStyleSheet(' background-color: #f0a6ad')
                    # time.sleep(1)
                    # self.Warning.clear()
                    # self.Warning.setStyleSheet('background-color: #ffffff')

                if barcode not in self.ListBarcodeRecived:
                    # self.tblBarcodes.insertRow(len(self.ListBarcodeRecived))
                    # self.tblBarcodes.setItem(len(self.ListBarcodeRecived), 0, QtWidgets.QTableWidgetItem(str(barcode)))
                    # self.tblBarcodes.setItem(len(self.ListBarcodeRecived), 1, QtWidgets.QTableWidgetItem(str('0000')))

                    # if len(self.ListBarcodeRecived) >110:
                    #
                    #
                    #     # self.ListBarcodeRecived.pop(0)
                    #     del self.ListBarcodeRecived[0:20]

                    self.Warning.clear()
                    self.Warning.setStyleSheet('background-color: #ffffff')
                    self.OrderData = None

                    try:
                        StateOrderToSend = False
                        response = requests.get(
                            f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Tracebility/{barcode}/',
                            timeout=2)
                        TraceBilityCodeData = response.json()
                        try:

                            self.OrderData = TraceBilityCodeData['order']

                            #
                            # self.tblBarcodes.setItem(len(self.ListBarcodeRecived), 1, QtWidgets.QTableWidgetItem(
                            #     str(self.OrderData[0]['Product'][0]['Product_code'])))
                            if self.OrderData is not None:


                                self.lineEdit_OrderCode.setText(self.OrderData[0]['code'])
                                self.lineEdit_ProductCode.setText(self.OrderData[0]['Product'][0]['Product_code'])
                                self.lineEdit_ProductDescription.setText(self.OrderData[0]['Product'][0]['title'])


                                # if self.OrderData is not None:
                                Product = self.OrderData[0]['Product']
                                if self.LastOrderCode != str(self.OrderData[0]['code']):

                                    try:
                                        pixmapimage = QtGui.QPixmap()
                                        image = urllib.request.urlopen(Product[0]['image']).read()
                                        pixmapimage.loadFromData(image)
                                        self.label_ProductPicture.setPixmap(pixmapimage)
                                    except:
                                        pass
                                    try:
                                        self.Image1 = QtGui.QImage()
                                        self.Image1.loadFromData(requests.get(Product[0][f'_1_{self.StationNumber}']).content)
                                        self.label_PDF1.setPixmap(QtGui.QPixmap(self.Image1))
                                        self.label_PDF1.show()
                                    except:
                                        pass
                                    try:
                                        self.Image2 = QtGui.QImage()
                                        self.Image2.loadFromData(requests.get(Product[0][f'_2_{self.StationNumber}']).content)
                                        self.label_PDF2.setPixmap(QtGui.QPixmap(self.Image2))
                                        self.label_PDF2.show()
                                    except:
                                        pass


                                self.LastOrderCode = str(self.OrderData[0]['code'])
                                # time.sleep(2)
                                self.PostTracebilityData(Operator=self.LastOperatorCode, Product=Product[0]['Product_code'],
                                                         Station=self.StationNumber, Order=self.OrderData[0]['code'],
                                                         tracebilityCode=TraceBilityCodeData['Tracebility_code'])

                                if self.StationNumber == "Repair":
                                    self.PostRepairData(Operator=self.LastOperatorCode,
                                                        Entery=str(self.comboBox_Entery.currentText()), State=self.State,
                                                        Exit='',
                                                        Product=Product[0]['Product_code'],
                                                        Station=self.StationNumber, Order=self.OrderData[0]['code'],
                                                        Description=str(self.lineEdit_RepairDescroption.text()),
                                                        tracebilityCode=TraceBilityCodeData['Tracebility_code'])

                                StateOrderToSend = True
                                self.lineEdit_OrderCount.setText(str(self.OrderData[0]['Count']))

                                self.tblBarcodes.insertRow(len(self.ListBarcodeRecived))
                                self.tblBarcodes.setItem(len(self.ListBarcodeRecived), 0,
                                                         QtWidgets.QTableWidgetItem(str(barcode)))
                                self.tblBarcodes.setItem(len(self.ListBarcodeRecived), 1,
                                                         QtWidgets.QTableWidgetItem(str(self.OrderData[0]['Product'][0]['Product_code'])))
                                # self.tblBarcodes.selectRow(len(self.ListBarcodeRecived))
                                # self.tblBarcodes.scrollToItem(len(self.ListBarcodeRecived))
                                # if self.tblBarcodes.rowCoun() > 10:
                                #     self.tblBarcodes.removeRow(1)


                                self.ListBarcodeRecived.append(barcode)
                                self.LiRecive.setText(str(len(self.ListBarcodeRecived)))
                            else:
                                self.Warning.setText("دیتای مربوط به این کد سفارش وجود ندارد ")
                                self.Warning.setStyleSheet(' background-color: #f0a6ad')
                        except:
                            self.Warning.setText("دیتای مربوط به این کد سفارش وجود ندارد ")
                            self.Warning.setStyleSheet(' background-color: #f0a6ad')
                        # # time.sleep(2)
                        # self.Warning.clear()
                        # self.Warning.setStyleSheet(' background-color: #ffffff')
                    except:
                        # time.sleep(0.1)
                        self.Warning.setText("ارتباط با سرور به مشکل خورده است ")
                        self.Warning.setStyleSheet(' background-color: #f0a6ad')
            if self.Entery == False:
                if barcode in self.ListBarcodeExited:

                    self.Warning.setText(f"بار کد {barcode} :قبلا استفاده شده ")
                    self.Warning.setStyleSheet(' background-color: #f0a6ad')
                    # time.sleep(1)
                    # self.Warning.clear()
                    # self.Warning.setStyleSheet('background-color: #ffffff')
                if barcode not  in self.ListBarcodeExited:


                    # self.tblBarcodes_Out.insertRow(len(self.ListBarcodeExited))
                    # self.tblBarcodes_Out.setItem(len(self.ListBarcodeExited), 0,QtWidgets.QTableWidgetItem(str(barcode)))
                    # self.tblBarcodes_Out.setItem(len(self.ListBarcodeExited), 1,QtWidgets.QTableWidgetItem(str(barcode)))




                    self.Warning.clear()
                    self.Warning.setStyleSheet('background-color: #ffffff')
                    self.OrderData = None

                    try:
                        StateOrderToSend = False
                        response = requests.get(
                            f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/Tracebility/{barcode}/',
                            timeout=2)
                        self.TraceBilityCodeData = response.json()
                        try:

                            self.OrderData = self.TraceBilityCodeData['order']


                            if self.OrderData is not None:

                                self.lineEdit_OrderCode.setText(self.OrderData[0]['code'])
                                self.lineEdit_ProductCode.setText(self.OrderData[0]['Product'][0]['Product_code'])
                                self.lineEdit_ProductDescription.setText(self.OrderData[0]['Product'][0]['title'])

                                # if self.OrderData is not None:
                                self.Product = self.OrderData[0]['Product']
                                if self.LastOrderCode != str(self.OrderData[0]['code']):

                                    try:
                                        pixmapimage = QtGui.QPixmap()
                                        image = urllib.request.urlopen(self.Product[0]['image']).read()
                                        pixmapimage.loadFromData(image)
                                        self.label_ProductPicture.setPixmap(pixmapimage)
                                    except:
                                        pass
                                    try:
                                        self.Image1 = QtGui.QImage()
                                        self.Image1.loadFromData(
                                            requests.get(self.Product[0][f'_1_{self.StationNumber}']).content)
                                        self.label_PDF1.setPixmap(QtGui.QPixmap(self.Image1))
                                        self.label_PDF1.show()
                                    except:
                                        pass
                                    try:
                                        self.Image2 = QtGui.QImage()
                                        self.Image2.loadFromData(
                                            requests.get(self.Product[0][f'_2_{self.StationNumber}']).content)
                                        self.label_PDF2.setPixmap(QtGui.QPixmap(self.Image2))
                                        self.label_PDF2.show()
                                    except:
                                        pass

                                self.LastOrderCode = str(self.OrderData[0]['code'])
                      
                                self.PostRepairData(Operator=self.LastOperatorCode,Entery='', State=self.State, Exit=str(self.comboBox_Exit.currentText()), Product=self.Product[0]['Product_code'],
                                                         Station=self.StationNumber, Order=self.OrderData[0]['code'],
                                                        Description=str(self.lineEdit_RepairDescroption.text()),
                                                         tracebilityCode=self.TraceBilityCodeData['Tracebility_code'])
                                StateOrderToSend = True
                                self.lineEdit_OrderCount.setText(str(self.OrderData[0]['Count']))
                                self.lineEdit_RepairDescroption.clear()
                                self.tblBarcodes_Out.insertRow(len(self.ListBarcodeExited))
                                self.tblBarcodes_Out.setItem(len(self.ListBarcodeExited), 0,
                                                             QtWidgets.QTableWidgetItem(str(barcode)))
                                self.tblBarcodes_Out.setItem(len(self.ListBarcodeExited), 1,
                                                             QtWidgets.QTableWidgetItem(str(self.OrderData[0]['Product'][0]['Product_code'])))

                                self.tblBarcodes.insertRow(len(self.ListBarcodeRecived))
                                self.tblBarcodes.setItem(len(self.ListBarcodeRecived), 0,
                                                         QtWidgets.QTableWidgetItem(str(barcode)))
                                self.tblBarcodes.setItem(len(self.ListBarcodeRecived), 1,
                                                         QtWidgets.QTableWidgetItem(
                                                             str(self.OrderData[0]['Product'][0]['Product_code'])))




                                self.ListBarcodeExited.append(barcode)
                                self.LiExit.setText(str(len(self.ListBarcodeExited)))

                                # self.tblBarcodes_Out.insertRow(len(self.ListBarcodeExited))
                                # self.tblBarcodes_Out.setItem(len(self.ListBarcodeExited), 0,
                                #                              QtWidgets.QTableWidgetItem(str(barcode)))
                                # self.tblBarcodes_Out.setItem(len(self.ListBarcodeExited), 1,
                                #                              QtWidgets.QTableWidgetItem(
                                #                                  str(self.OrderData[0]['Product'][0]['Product_code'])))


                            else:
                                self.Warning.setText("دیتای مربوط به این کد سفارش وجود ندارد############ ")
                                self.Warning.setStyleSheet(' background-color: #f0a6ad')

                        except:
                            self.Warning.setText("دیتای مربوط به این کد سفارش وجود ندارد ")
                            self.Warning.setStyleSheet(' background-color: #f0a6ad')
                        # # time.sleep(2)
                        # self.Warning.clear()
                        # self.Warning.setStyleSheet(' background-color: #ffffff')
                    except:
                        # time.sleep(0.1)
                        self.Warning.setText("ارتباط با سرور به مشکل خورده است ")
                        self.Warning.setStyleSheet(' background-color: #f0a6ad')


        else:
            # time.sleep(0.1)
            self.Warning.setStyleSheet(' background-color: #f0a6ad')
            self.Warning.setText("شما هنوز شروع به کار نکرده اید ")
    def GetBarcode(self):
        # self.listViewBarcode.setModel(self.ListModelBarcode)
        # address = ('localhost', 50000)
        # # listener = Listener(address, authkey=b'123456')
        # listener = Listener(address)
        # conn = listener.accept()
        # if QueUe.qsize() > 0 :
    # while True:
        try:
            if StateOrderToSend == True:
                massage = QueUe.pop(0)
                # massage = conn.recv()
                self.Barcode = massage
                if len(massage) == 6:
                    self.GetProductResponse( barcode=massage)
                if len(massage) == 7:
                    # ui.GetResponseUser(splitebarcode[1])
                    self.GetResponseUser( barcode=massage)
                if massage == str(self.BarcodeShutdown):
                    os.system('shutdown now')
                if massage == str(self.BarcodeRestart):
                    os.system('reboot')
                if massage == str(self.BarcodeProdocer):
                    self.tabWidget.setCurrentWidget(self.Prodocer)
                if massage == str(self.BarcodeRepair):
                    self.tabWidget.setCurrentWidget(self.Entry)


        except:
            pass

    def ConnectionTest(self):
        while True:



            try:
                connection = psycopg2.connect(database=self.DataBase_Name, user=self.USER_SERVER,
                                              password=self.PASSWORD_SERVER,
                                              host=self.DataBase_Address, port=self.DatabasePort)
                Cursore = connection.cursor()
                self.label_ConnectionDatabase.setText("ارتباط با دیتا بیس برقرار است ")
                self.label_ConnectionDatabase.setStyleSheet(' border-radius : 20px; background-color: #97ffa8')
            except:
                self.label_ConnectionDatabase.setText("ارتباط با دیتا بیس برقرار نیست")
                self.label_ConnectionDatabase.setStyleSheet(' border-radius : 20px; background-color: #f0a6ad')
            try:
                response = requests.get(url=porotocol + self.Server_Address + ":" + self.PORT, timeout=3)
                if response.status_code == 200 or response.status_code == 301:
                    self.label_connectionServer.setText("ارتباط با سرور برقرار است ")
                    self.label_connectionServer.setStyleSheet(' border-radius : 20px; background-color: #97ffa8')
                else:
                    self.label_connectionServer.setText("ارتباط با سرور برقرار نیست ")
                    self.label_connectionServer.setStyleSheet(' border-radius : 20px; background-color: #f0a6ad')
            except:
                self.label_connectionServer.setText("ارتباط با سرور برقرار نیست ")
                self.label_connectionServer.setStyleSheet(' border-radius : 20px; background-color: #f0a6ad')
            time.sleep(5)
    def PostTracebilityData(self, Operator, Station, Order, Product, tracebilityCode):
        Date = datetime.datetime.now().date()
        Time = datetime.datetime.now().time()


        try:

            requests.post(f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/TracebilityData/',
                          data={'Operator': Operator, 'Station': Station, 'Order': Order, 'Product': Product,
                                'tracebilityCode': tracebilityCode, 'Date': Date, 'Time': Time})

            self.Warning.setText(f" {self.Barcode} :بارکد دریافت شده ")
            # self.CountRecived = self.CountRecived + 1


            # time.sleep(1)
            # self.Warning.clear()
        except:

            self.Warning.setText(f" {self.Barcode}  :بارکد با مشکل رو به رو شده ")
            # time.sleep(1)

    def PostRepairData(self, Operator, Station, Order, Product,Entery,Exit,State, Description,    tracebilityCode):
        Date = datetime.datetime.now().date()
        Time = datetime.datetime.now().time()
        # self.getSelectedItem_1()

        try:

            requests.post(f'{porotocol + self.Server_Address + ":" + self.PORT}/rest/list/RepairProduct/',
                          data={'Operator': Operator,'Entery':Entery, 'Exit':Exit, 'State':State,'Description':Description, 'Station': Station, 'Order': Order, 'Product': Product,
                                'tracebilityCode': tracebilityCode, 'Date': Date, 'Time': Time})

            self.Warning.setText(f" {self.Barcode} :بارکد دریافت شده ")
            # self.CountExit = self.CountExit + 1


            # time.sleep(1)
            # self.Warning.clear()
        except:

            self.Warning.setText(f" {self.Barcode}  :بارکد با مشکل رو به رو شده ")
            # time.sleep(1)

    def BarcodeReader(self):
        import usb
        busses = usb.busses()
        # for bus in busses:
        #     device = bus.devices
        #     for dev in device:
        #         print(dev)
        #         print("Device:", dev.filename)
        #         print("  idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor))
        #         print("  idProduct: %d (0x%04x)" % (dev.idProduct, dev.idProduct))
        #         print("Manufacturer:", dev.iManufacturer)
        #         print("Serial:", dev.iSerialNumber)
        #         print("Product:", dev.iProduct)
        # time.sleep(5)
        # address = ('localhost', 50000)
        # # conn = Client(address, authkey=b'123456')
        # conn = Client(address)
        try:
            dev = InputDevice(f'/dev/input/event0')
        except:
            pass




        # Provided as an example taken from my own keyboard attached to a Centos 6 box:
        scancodes = {
            # Scancode: ASCIICode
            0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
            10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'q', 17: u'w', 18: u'e', 19: u'r',
            20: u't', 21: u'y', 22: u'u', 23: u'i', 24: u'o', 25: u'p', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
            30: u'a', 31: u's', 32: u'd', 33: u'f', 34: u'g', 35: u'h', 36: u'j', 37: u'k', 38: u'l', 39: u';',
            40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'z', 45: u'x', 46: u'c', 47: u'v', 48: u'b', 49: u'n',
            50: u'm', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 57: u' ', 100: u'RALT'
        }

        capscodes = {
            0: None, 1: u'ESC', 2: u'!', 3: u'@', 4: u'#', 5: u'$', 6: u'%', 7: u'^', 8: u'&', 9: u'*',
            10: u'(', 11: u')', 12: u'_', 13: u'+', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
            20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'{', 27: u'}', 28: u'CRLF', 29: u'LCTRL',
            30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u':',
            40: u'\'', 41: u'~', 42: u'LSHFT', 43: u'|', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
            50: u'M', 51: u'<', 52: u'>', 53: u'?', 54: u'RSHFT', 56: u'LALT', 57: u' ', 100: u'RALT'
        }
        # setup vars
        x = ''
        caps = False

        # grab provides exclusive access to the device
        dev.grab()

        # loop
        for event in dev.read_loop():
            if event.type == ecodes.EV_KEY:
                data = categorize(event)  # Save the event temporarily to introspect it
                if data.scancode == 42:
                    if data.keystate == 1:
                        caps = True
                    if data.keystate == 0:
                        caps = False
                if data.keystate == 1:  # Down events only
                    if caps:

                        key_lookup = u'{}'.format(capscodes.get(data.scancode)) or u'UNKNOWN:[{}]'.format(
                            data.scancode)  # Lookup or return UNKNOWN:XX
                    else:
                        key_lookup = u'{}'.format(scancodes.get(data.scancode)) or u'UNKNOWN:[{}]'.format(
                            data.scancode)  # Lookup or return UNKNOWN:XX
                    if (data.scancode != 42) and (data.scancode != 28):
                        x += key_lookup
                    if (data.scancode == 28):
                        # QueUe.put(x)
                        QueUe.append(x)
                        x = ''
                        if StateOrderToSend == True:
                            self.GetBarcode()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    Window = Ui_MainWindow()
    # apply_stylesheet(app, theme='light_yellow.xml')


    Window.show()

    # processGetBarcode = Thread(target=Window.GetBarcode)
    # processGetBarcode.start()


    processBarcode = Thread(target=Window.BarcodeReader)
    processBarcode.start()

    ThreadConnectionTest =  Thread(target=Window.ConnectionTest)
    ThreadConnectionTest.start()

    # timerNetwork = Timer(5, Window.ConnectionTest)
    # timerNetwork.start()


    processClock =  Thread(target=Window.ShowClock)
    processClock.start()
    # Timer(1, Window.ShowClock).start()
    # timerClock = Timer(1, Window.ShowClock)
    # timerClock.start()


    Setting = Setting_server.Ui_Setting_Network()
    Setting_widget = QtWidgets.QWidget()
    Setting.setupUi(Setting_widget)
    Window.actionNetworkSetting.triggered.connect(lambda: Setting_widget.show())
    app.exec_()



