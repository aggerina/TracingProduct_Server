# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Reporter_Tracebility_04.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qt_material import  apply_stylesheet
import  pyodbc



class MssqlConnection(object):
    # try:

    server = '192.168.4.2\SEPIDAR'
    database = 'Sepidar04'
    username = 'bpms'
    password = 'aezakmiHESOYAM!@#321'
    cnxn_2 = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn_2.cursor()

##connect to database Tracebility
class Bpms_Database():
    try:

        with open("config.yaml", "r") as yamlfile:
            data_r = yaml.load(yamlfile, Loader=yaml.FullLoader)

        DB_save = mysql.connector.connect(
            host=data_r[0]['DATA_Setting']['HOST_SERVER'],
            user=data_r[0]['DATA_Setting']['USER_SERVER'],
            password=data_r[0]['DATA_Setting']['PASSWORD_SERVER'],
            database=data_r[0]['DATA_Setting']['DATABASE_SERVER'],

        )
    except:
        import sys

        ...

        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Critical)
        # msg.setText("ارتباط با دیتابیس  برقرار نشد  ")
        # msg.setWindowTitle("No Conecction")
        # msg.exec_()

    #
    #
    #
    #
    #
    # try:
    #     DB_save = mysql.connector.connect(
    #         host="192.168.1.91",
    #         user="BPMS",
    #         password="P@ssw0rd",
    #         database="photon"
    #     )
    #
    #
    # except:
    #     print("ارتباط با دیتابیس ردیابی  برقرار نشد")
    #     # msg = QMessageBox()
    #     # msg.setIcon(QMessageBox.Critical)
    #     # # msg.setStyle('fusion')
    #     # msg.setText("ارتباط با دیتابیس ردیابی  برقرار نشد")
    #     #
    #     # msg.setWindowTitle("No Conecction")
    #     # msg.exec_()



class Ui_Tracebility(object):
    def setupUi(self, Tracebility):
        if not Tracebility.objectName():
            Tracebility.setObjectName(u"Tracebility")
        Tracebility.resize(988, 754)
        self.actionSave_To_Excel = QAction(Tracebility)
        self.actionSave_To_Excel.setObjectName(u"actionSave_To_Excel")
        self.centralwidget = QWidget(Tracebility)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.tableWidget = QTableWidget(self.splitter)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        font = QFont()
        font.setFamily(u"B Nazanin")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(Qt.RightToLeft)
        self.splitter.addWidget(self.tableWidget)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(200, 700))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setMouseTracking(True)
        self.groupBox.setTabletTracking(True)
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_8 = QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_8, 7, 0, 1, 4)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 2)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 11, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 3, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_4, 3, 0, 1, 2)

        self.lineEdit_7 = QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_7, 9, 0, 1, 4)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 2, 1, 2)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 2)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_5, 4, 0, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 2)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 11, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 6, 2, 1, 2)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 8, 1, 1, 3)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 4, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 10, 2, 1, 2)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 10, 1, 1, 1)

        self.splitter.addWidget(self.groupBox)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        Tracebility.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Tracebility)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 988, 21))
        self.menusave_to_excel = QMenu(self.menubar)
        self.menusave_to_excel.setObjectName(u"menusave_to_excel")
        Tracebility.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Tracebility)
        self.statusbar.setObjectName(u"statusbar")
        Tracebility.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menusave_to_excel.menuAction())
        self.menusave_to_excel.addAction(self.actionSave_To_Excel)

        self.retranslateUi(Tracebility)

        QMetaObject.connectSlotsByName(Tracebility)
    # setupUi

    def retranslateUi(self, Tracebility):
        Tracebility.setWindowTitle(QCoreApplication.translate("Tracebility", u"MainWindow", None))
        self.actionSave_To_Excel.setText(QCoreApplication.translate("Tracebility", u"Save_To_Excel", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Tracebility", u"\u06a9\u062f \u0645\u062d\u0635\u0648\u0644 ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Tracebility", u"\u06a9\u062f \u0633\u0641\u0627\u0631\u0634", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Tracebility", u"\u06a9\u062f \u067e\u0631\u0633\u0646\u0644\u06cc \u0627\u067e\u0631\u0627\u062a\u0648\u0631", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Tracebility", u"\u06a9\u062f  OPC", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Tracebility", u"\u0634\u0645\u0627\u0631\u0647 \u0627\u06cc\u0633\u062a\u06af\u0627\u0647", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Tracebility", u"\u06a9\u062f \u0631\u062f\u06cc\u0627\u0628\u06cc ", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Tracebility", u"\u062a\u0627\u0631\u06cc\u062e ", None));
        self.groupBox.setTitle(QCoreApplication.translate("Tracebility", u"GroupBox", None))
        self.lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("Tracebility", u"\u06a9\u062f \u0645\u062d\u0635\u0648\u0644 ", None))
        self.lineEdit_2.setText("")
        self.label_2.setText(QCoreApplication.translate("Tracebility", u"\u06a9\u062f \u0633\u0641\u0627\u0631\u0634", None))
        self.label_6.setText(QCoreApplication.translate("Tracebility", u"\u062a\u0627\u0631\u06cc\u062e", None))
        self.label_4.setText(QCoreApplication.translate("Tracebility", u"\u0634\u0645\u0627\u0631\u0647 \u0627\u06cc\u0633\u062a\u06af\u0627\u0647", None))
        self.label_3.setText(QCoreApplication.translate("Tracebility", u"\u06a9\u062f \u067e\u0631\u0633\u0646\u0644", None))
        self.label_8.setText(QCoreApplication.translate("Tracebility", u"\u0634\u0631\u062d \u0645\u062d\u0635\u0648\u0644 ", None))
        self.label_7.setText(QCoreApplication.translate("Tracebility", u"\u0634\u0631\u062d \u0641\u0648\u0631\u0645\u0648\u0644 \u0633\u0627\u062e\u062a", None))
        self.label_5.setText(QCoreApplication.translate("Tracebility", u"\u06a9\u062f \u0631\u062f\u06cc\u0627\u0628\u06cc", None))
        self.label_9.setText(QCoreApplication.translate("Tracebility", u"\u0633\u0627\u0644 \u0645\u0627\u0644\u06cc ", None))
        self.menusave_to_excel.setTitle(QCoreApplication.translate("Tracebility", u"File", None))
    # retranslateUi
        ###
        ###Table Widh

        self.tableWidget.setColumnWidth(6, 300)

    def Feed_FiscalYear(self):
        try:
            with MssqlConnection.cnxn_2 as connection:
                cursor = connection.cursor()
                cursor.execute(f" select FiscalYearId, Title from FMK.FiscalYear ")
                self.FiscalYear = cursor.fetchall()

                # self.comboBox.
                # print(self.FiscalYear[0][1])
                # self.comboBox.addItems([f"{self.FiscalYear[0][1]}", f"{self.FiscalYear[1][1]}", f"{self.FiscalYear[2][1]}",f"{self.FiscalYear[3][1]}",
                #                        f"{self.FiscalYear[4][1]}", f"{self.FiscalYear[5][1]}", f"{self.FiscalYear[6][1]}"])
                for indx in range(len(self.FiscalYear)):
                    valu = self.FiscalYear[indx][1]
                    _ID = self.FiscalYear[indx][0]
                    self.comboBox.addItem(valu, userData=_ID)
                self.comboBox.setCurrentText(valu)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            # msg.setStyle('fusion')
            msg.setText("سال مالی بارگزاری نشد ")

            msg.setWindowTitle("No Conecction")
            msg.exec_()

        ################################################################################################

        ###  Get from user Order code  to start functions for read data order on Database

    def Get_Order_Code(self):
        try:

            if len(self.lineEdit_2.text()):
                with MssqlConnection.cnxn_2 as connection:
                    cursor = connection.cursor()

                    ##################################################################################################
                    ##### send query code of  productorder  to databese for given code of  ProducrFormula and
                    ##### FiscalYear and after thats state most be get refrence cods to next stat
                    cursor.execute(
                        f"select  ProductFormulaRef, ProductRef, Quantity,State ,FiscalYearRef from  WKO.ProductOrder"
                        f" where number={str(self.lineEdit_2.text())} and FiscalYearRef={self.comboBox.currentData()};")
                    mydata = cursor.fetchall()
                    ProductFormulaRef = mydata[0][0]
                    ProductRef = mydata[0][1]
                    self.Quantity = mydata[0][2]
                    self.Quantity = float(self.Quantity)
                    self.Quantity = int(self.Quantity)
                    self.Quantity = str(self.Quantity)

                    State = mydata[0][3]
                    FiscalYearRefmy = mydata[0][4]

                ####################################################################################################################
                cursor.execute(
                    f"select  Code, Title, ItemRef, ItemUnitRef, Quantity, IsActive from  WKO.ProductFormula "
                    f" where ProductFormulaID={str(ProductFormulaRef)};")
                ProductFormulaRef_DETAIL = cursor.fetchall()
                ProductFormulaRef_Code = ProductFormulaRef_DETAIL[0][0]
                ProductFormulaRef_Title = ProductFormulaRef_DETAIL[0][1]

                ProductFormulaRef_ItemRef = ProductFormulaRef_DETAIL[0][2]
                ProductFormulaRef_ItemUnitRef = ProductFormulaRef_DETAIL[0][3]
                ProductFormulaRef_Quantity = ProductFormulaRef_DETAIL[0][4]
                ProductFormulaRef_IsActive = ProductFormulaRef_DETAIL[0][5]

                #### get  title   fiscalyear from combobox  current data
                ############################################################################################################

                cursor.execute(
                    f"select   Title  from  FMK.FiscalYear  where FiscalYearID={str(self.comboBox.currentData())};")
                FiscalYearRef_Title = cursor.fetchall()
                # print("FiscalYearRef_Title", FiscalYearRef_Title)
                ## read  data from  inv item    code product  discription product
                #########################################################################################################
                cursor.execute(f"select Code  , Title   from  INV.Item "
                               f" where ItemID={str(ProductFormulaRef_ItemRef)};")
                ProductFormulaRef_ItemRef_detail = cursor.fetchall()
                ProductFormulaRef_ItemRef_Code = ProductFormulaRef_ItemRef_detail[0][0]
                ProductFormulaRef_ItemRef_Title = ProductFormulaRef_ItemRef_detail[0][1]

                ##########################set value on lineedite  for show order code detail
                self.lineEdit.setText(ProductFormulaRef_ItemRef_Code)
                # self.lineEdit_7.setText(str(self.Quantity))
                self.lineEdit_8.setText(ProductFormulaRef_ItemRef_Title)
                self.lineEdit_7.setText(str(ProductFormulaRef_Title))
                ##########  if len order code lawerthan of 1  clear  all lineEdit
            else:
                if len(self.lineEdit_2.text()) < 1:
                    ...

                    self.lineEdit_7.clear()
                    self.lineEdit.clear()
                    self.lineEdit_8.clear()
        except:

            msg = QtWidgets.QMessageBox()
            # msg.setIcon(QMessageBox.Critical)
            msg.setText("کد سفارش پیدا نشد")
            msg.setWindowTitle("خطا")
            msg.exec_()

            self.lineEdit_7.clear()
            self.lineEdit.clear()
            self.lineEdit_8.clear()

        ##########################################################################################################

        # cursor.execute(f"select   Code , Title, Itemref , Quantity  from  WKO.ProductFormula "
        #                f" where ProductFormulaID={str(Product_Order_ProductFormulaRef)};")
        # Data_ProductFormulaRef_from_product_Order = cursor.fetchall()
        # print(Data_ProductFormulaRef_from_product_Order)
        #
        #
        #
        # cursor.execute(f"select   Code , Title, Itemref , ItemRef, ItemUnitRef , BaseProductFormula ,Quantity   from  WKO.ProductFormula"
        #                f" where ProductFormulaID={str(Formul_BOM_Item_ProductFormulaRef)};")
        # Data_ProductFormulaRef_from_formul_BOM = cursor.fetchall()
        # print(Data_ProductFormulaRef_from_formul_BOM)

        ### reaad Code source store

    def Set_Time_combobox(self):
        from datetime import datetime, timedelta
        from dateutil.relativedelta import relativedelta

        TabelName = 'Save_Tracebility_'

        for i in range(12):
            TabelTime = f"{TabelName}{jalali_datetime.JalaliDatetime.now().year}-{i + 1}"
            print(TabelTime)

        # def get_forward_month_list():
        # now = datetime.now()
        #
        #     now = f"{jalali_datetime.JalaliDatetime.now().year}-{jalali_datetime.JalaliDatetime.now().month}"
        #     # return [(now + relativedelta(months=i)).strftime('%b') for i in range(12)]
        # print(get_forward_month_list())

        # for indx in range(len()):
        #     valu = self.FiscalYear[indx][1]
        #     _ID = self.FiscalYear[indx][0]
        #     self.comboBox.addItem(valu, userData=_ID)
        # self.comboBox.setCurrentText(valu)
        # jalali_datetime.JalaliDatetime.

    def curen_fisc(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml')
    Tracebility = QMainWindow()
    ui = Ui_Tracebility()
    ui.setupUi(Tracebility)
    Tracebility.show()
    sys.exit(app.exec_())


