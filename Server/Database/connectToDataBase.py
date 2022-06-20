import yaml , mysql.connector
from khayyam import JalaliDatetime

# state_online = {"CodeOperator":"0"}
import psycopg2
class Bpms_Database():
    # def __init__(self):
    DATA_dic = []
    list_Stations = {'StationNumbers': []}
    list_operators    = {'CodeOperators': []}
    Dictionary_Barcode_tosave    = {}
    StastionNumber_Asign_toCodeOperator = {'StationNumbers':[], 'CodeOperators':[]}
    Befor_Tracebility_code  = 0


    try:
        with open("D:/photon_project/Tracebility_01/venv_new/Server/config.yaml", "r") as yamlfile:
            data_r = yaml.load(yamlfile, Loader=yaml.FullLoader)
        DB_save = mysql.connector.connect(
            host=data_r[0]['DATA_Setting']['HOST_SERVER'],
            user=data_r[0]['DATA_Setting']['USER_SERVER'],
            password=data_r[0]['DATA_Setting']['PASSWORD_SERVER'],
            database=data_r[0]['DATA_Setting']['DATABASE_SERVER'],
        )

    except:
        print("no conncted ")
        ...
#     def UpdateToDB(self, DATA_dic):
#         self.DATA_dic = DATA_dic
#         cursor =   Bpms_Database.DB_save.cursor()
#
#         TABLE_NAME = f"Save_Tracebility_{JalaliDatetime.now().year}-{JalaliDatetime.now().month}"
#
#
#         #### get opc-order
# #####   for dictionary recive from client
#         # sql_Opc_Order = f"select Opc_Order, Order_code_Product from Opc_Product where code_Product={int(DATA_dic['CodeProduct'])}"
#         #
#         # cursor.execute(sql_Opc_Order)
#         # Opc_Order_Data =   cursor.fetchall()
#
#         ### GET OPC_ORDER FROM TABLE RESULT
#         # self.DATA_dic["Opc_Order"] = Opc_Order_Data[0][0]
#         ### GET Order_code_Product FROM TABLE RESULT
#         # self.DATA_dic["Order_code_Product"] = Opc_Order_Data[0][1]
#
#         # print(DATA_dic["CodeProduct"])
#         SQL_1 = """CREATE TABLE if  NOT EXISTS `%s` (Code_Product INT(7) , Order_code_Product INT(7),Code_Operator INT(7), OPC_order TEXT, Station_number INT(2), Date_Time VARCHAR(40), Tracebility_code varchar (15) character set 'utf8' COLLATE 'utf8_persian_ci' )""" % (
#             TABLE_NAME)
#
#         cursor.execute(SQL_1)
#         Bpms_Database.DB_save.commit()
#
# ##########  Set Tracebility code To StationNumber
#
#
#         SQL_2 = f"SELECT 	* FROM `Station_to_Order` where `StationNumber`={int(self.DATA_dic['Stationnumber'])} ORDER BY ID DESC LIMIT 1;"
#         cursor.execute(SQL_2)
#         Station_to_order = cursor.fetchall()
#
#         if Station_to_order != []:
#             ####### Save Station_to_order to file for perevent  problemsome
#             with open('Station_to_Order.ptp', 'wt') as CodeOperatorFile2:
#                 CodeOperatorFile2.write(str(Station_to_order[0][2]))
#                 CodeOperatorFile2.close()
#         with open('Station_to_Order.ptp', 'r') as Station_to_Order:
#             self.Station_to_Order_code = str(Station_to_Order.read())
#
#
#         ##############Save Tracebility code  with Station number
#         try:
#             if self.DATA_dic['Stationnumber'] == Station_to_order[0][1] :
#                 if len(self.DATA_dic['Barcode']) > 6:
#                     SQL_3 = f"""REPLACE  INTO `Tracebility_code`(`TracebilityCode`) VALUES ({self.DATA_dic['Barcode']})"""
#                     Val_3 = f"{self.DATA_dic['Barcode']}"
#                     cursor.execute(SQL_3)
#                     Bpms_Database.DB_save.commit()
#         except:
#             print("not Station_to_order applyed")
#
#
#
#
#
#
#
# ############################## Classify  Barcode  StationNumbers
#         if self.DATA_dic['Stationnumber'] not in  Bpms_Database.list_Stations['StationNumbers']:
#             Bpms_Database.list_Stations['StationNumbers'].append(self.DATA_dic['Stationnumber'])
#         print(f"StationNumbers  {Bpms_Database.list_Stations['StationNumbers']}")
#         print(f"len  StationNumbers  {len(Bpms_Database.list_Stations['StationNumbers'])}")
#
#         for StationNumber in Bpms_Database.list_Stations['StationNumbers']:
#             if StationNumber == self.DATA_dic['Stationnumber']:
#                 print(f"StationNumber = {StationNumber}")
#                 ################################
#                 # self.DATA_dic["CodeOperator"] = state_online['CodeOperator']
#                 date_now = JalaliDatetime.now().strftime('%C')
#                 self.DATA_dic["DateTime"] = date_now
#
#
#                 if len (self.DATA_dic['Barcode']) > 6:
#                     self.DATA_dic['Tracebility_code'] = self.DATA_dic['Barcode']
#                     self.Befor_Tracebility_code = self.DATA_dic['Tracebility_code']
#                 # try:
#                 ## Asign code operator
#                 # if len(self.DATA_dic['Barcode'])   < 6:
#
#                     # self.DATA_dic["CodeOperator"] =  self.DATA_dic['Barcode']
#                     # state_online['CodeOperator'] = self.DATA_dic["CodeOperator"]
#                     # self.DATA_dic['Tracebility_code'] =  self.Befor_Tracebility_code
#                     # self.StastionNumber_Asign_toCodeOperator["CodeOperators"].append(self.DATA_dic["CodeOperator"])
#                     # self.StastionNumber_Asign_toCodeOperator["CodeOperators"] = list(set(self.StastionNumber_Asign_toCodeOperator["CodeOperators"]))
#                     # print(f"StastionNumber_Asign_toCodeOperator {self.StastionNumber_Asign_toCodeOperator['CodeOperators']}")
#                 # except:
#                 #     print("Operator Not Access ")
#
# ##############################################################################
#                 # if self.DATA_dic["CodeOperator"] not in Bpms_Database.list_operators['CodeOperators']:
#                 #     Bpms_Database.list_operators['CodeOperators'].append(self.DATA_dic['CodeOperator'])
#                 # print(f"CodeOperators  {Bpms_Database.list_operators['CodeOperators']}")
#                 # print(f"len  CodeOperators  {len(Bpms_Database.list_operators['CodeOperators'])}")
#                 if len(self.DATA_dic["CodeOperator"]) == 5:
#                     sql_connected_client = """INSERT IGNORE  INTO `Client_connected`( `CodeOperator`, `time`, `Stationnumber`) VALUES (%s,%s,%s)"""
#                     val_sql_connected_client = f"{self.DATA_dic['CodeOperator']}", f"{self.DATA_dic['DateTime']}", f"{self.DATA_dic['Stationnumber']}"
#                     cursor.execute(sql_connected_client, val_sql_connected_client)
#                     Bpms_Database.DB_save.commit()
#
#
#                 # print(f"state_online['CodeOperator']  ){state_online['CodeOperator']}")
#                 if len(self.DATA_dic["CodeOperator"]) == 5:
#                     if len(self.DATA_dic['Barcode']) > 6 :
#                         # self.DATA_dic["CodeOperator"] =  state_online['CodeOperator']
#
#
#                         sql =  "INSERT INTO `%s`" % TABLE_NAME +  "(`Code_Product`, `Order_code_Product`, `Code_Operator`, `OPC_order`, `Station_number`, `Date_Time`, `Tracebility_code`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#                         # print(TABLE_NAME)
#                         # sql =  "INSERT INTO `Save_Tracebility`(`Code_Product`,`Code_Order_Ref`, `Code_Operator`, `OPC_order`, `Station_number`, `Date_Time`) VALUES (%s, %s, %s, %s, %s, %s)"
#                         # val = f"{self.DATA_dic['CodeProduct']}", f"{self.DATA_dic['Order_code_Product']}",f"{self.DATA_dic['CodeOperator']}", f"{self.DATA_dic['Opc_Order']}" , f"{self.DATA_dic['0010']}", f"{self.DATA_dic['DateTime']}"
#                         val = f"{0}", f"{int(self.Station_to_Order_code)}",f"{self.DATA_dic['CodeOperator']}", f"{'null'}" , f"{self.DATA_dic['Stationnumber']}", f"{self.DATA_dic['DateTime']}" , f"{self.DATA_dic['Tracebility_code']}"
#                         cursor.execute(sql, val)
#                         Bpms_Database.DB_save.commit()
#                         print(f" from Code operator get data   = {self.DATA_dic['CodeOperator']}")
#
#                 # else:
#                 #     print(f"client not  access {self.DATA_dic['CodeOperator']}")
#                 #



    def Read_dataBase(self,Column_Name, TableName):
        cursor = Bpms_Database.DB_save.cursor()
        Bpms_Database_Read = cursor.execute(f"select {Column_Name} from {TableName} ")
        return Bpms_Database_Read


    def Search_dataBase(self,Column_Name, TableName, Data_Name):
        cursor = Bpms_Database.DB_save.cursor()
        Bpms_Database_Search = cursor.execute(f"select {Column_Name} from {TableName} where {Column_Name}={Data_Name}")
        return Bpms_Database_Search

    # def Read_dataBase_where(self,Column_Name, TableName, where):
    #     cursor = Bpms_Database.DB_save.cursor()
    #     Bpms_Database_Read = cursor.execute(f"select {Column_Name} from {TableName} where ")
    #     return Bpms_Database_Read







