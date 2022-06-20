import yaml , mysql.connector, pyodbc


class MssqlConnection(object):
    try:

        server = '192.168.4.2\SEPIDAR'
        database = 'Sepidar04'
        username = 'bpms'
        password = 'aezakmiHESOYAM!@#321'
        cnxn_2 = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn_2.cursor()

        # server = '192.168.1.24\CYBERGATESHAHO'
        # database = 'Sepidar04'
        # username = 'sa'
        # password = 'P@ssw0rdshaho123'
        # cnxn_2 = pyodbc.connect(
        #     'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        # cursor = cnxn_2.cursor()
    # # password = 'P@ssw0rdshaho1234'  bpms user

    except:
        print("زارت")


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



def Get_Order_Code(self):
    try:

        if len(self.lineEdit_20.text()):
            with MssqlConnection.cnxn_2 as connection:
                cursor = connection.cursor()

                ##################################################################################################
                ##### send query code of  productorder  to databese for given code of  ProducrFormula and
                ##### FiscalYear and after thats state most be get refrence cods to next stat
                cursor.execute(
                    f"select  ProductFormulaRef, ProductRef, Quantity,State ,FiscalYearRef from  WKO.ProductOrder"
                    f" where number={str(self.lineEdit_20.text())} and FiscalYearRef={self.comboBox.currentData()};")
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
            self.lineEdit_2.setText(ProductFormulaRef_ItemRef_Code)
            self.lineEdit_7.setText(str(self.Quantity))
            self.lineEdit_5.setText(ProductFormulaRef_ItemRef_Title)
            self.lineEdit_8.setText(str(ProductFormulaRef_Title))
            ##########  if len order code lawerthan of 1  clear  all lineEdit
        else:
            if len(self.lineEdit_20.text()) < 1:
                self.lineEdit_2.clear()
                self.lineEdit_7.clear()
                self.lineEdit_5.clear()
                self.lineEdit_8.clear()
    except:

        msg = QMessageBox()
        # msg.setIcon(QMessageBox.Critical)
        msg.setText("کد سفارش پیدا نشد")
        msg.setWindowTitle("خطا")
        msg.exec_()
        # self.lineEdit_20.clear()
        self.lineEdit_2.clear()
        self.lineEdit_7.clear()
        self.lineEdit_5.clear()
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
