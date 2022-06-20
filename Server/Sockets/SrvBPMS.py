SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096  # send 4096 bytes each time step
import psycopg2
import base64
import socket
from pathlib import Path
import sys
from Server.Database.DataBase_SQL import MssqlConnection
from translate import Translator
import time
import multiprocessing
import os
from _thread import *
from threading import Thread
import pyodbc, re, sys, asyncio, mysql.connector, datetime
import Server.Setting_server
import pandas as pd
import yaml
from khayyam import JalaliDatetime
import json
from Server.Database import connectToDataBase
from Server.Sockets import dictionary_binary

dataforsend = {'Barcode': '1154', 'code': '500'}
with open('D:/photon_project/Tracebility_01/venv_new/Server/Sockets/test.txt', 'rb') as datafile:
    filee = base64.b64encode(datafile.read())
    dataforsend['file'] = filee

list_Stations = {'StationNumbers': []}
DataBaseStart = False


class mserver(object):
    clients = []

    def __init__(self):
        Thread.__init__(self)

        print('init')
        self.curent_timee = datetime.datetime.now()

        start_value = 1
        BUFFER_SIZE = 1024
        recived_f = 'imgt_thread' + str(time.time()).split('.')[0] + '.jpg'

        DATA_dic = []

        list_operators = {'CodeOperators': []}
        Dictionary_Barcode_tosave = {}
        StastionNumber_Asign_toCodeOperator = {'StationNumbers': [], 'CodeOperators': []}
        Befor_Tracebility_code = 0

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

    def myprocess():

        process = multiprocessing.Process(target=mserver.ListenFun)
        process.start()

    def ListenFun():
        Connection_work = None
        with open("config.yaml", "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print(data[0]['DATA_Setting']['send_port'])

        with socket.socket() as ServerSideSocket:
            # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ServerSideSocket:

            host = socket.gethostbyname("pc-backup")
            print(host)
            LI_Port = int(data[0]['DATA_Setting']['send_port'])

            ThreadCount = 0
            try:
                ServerSideSocket.bind((host, LI_Port))
            except socket.error as e:
                print(str(e))
            print('Socket is listening..')
            ServerSideSocket.listen(100)

            def multi_threaded_client(connection):
                avoid_duplicate_1 = ['']
                avoid_duplicate_2 = ['']

                # while True:
                data_reciv = connection.recv(2048)
                # if not data_reciv:
                #     break

                # if data_reciv == b'0000':
                if data_reciv == b'0000':
                    connection.send(b'connection closed')
                    print("connection closed")
                    connection.close
                    Connection_close = True
                # if not Connection_close == True:

                # if data_reciv != b'':
                if data_reciv != b'0000':
                    ######################## Start Cominucation Between Server Client
                    # try:

                    # print(f"Data= {dict_recived}")
                    dict_recived = {}

                    try:
                        dict_recived = dictionary_binary.binary_to_dict(data_reciv)
                    except:
                        print("Data no Serializing")

                    if dict_recived['code'] == 200:
                        connection.send(dictionary_binary.dict_to_binary(dict_recived))
                    try:
                        if dict_recived['Barcode']:
                            ...
                    except:
                        dict_recived['Barcode'] = 0
                    print(f"Barcode recived {str(dict_recived['Barcode'])}")

                    if dict_recived["code"] == 105:
                        DataBaseStart = True
                        if len(str(dict_recived['Barcode'])) == 8:
                            ######### Split Barcode
                            Barcode = str(dict_recived['Barcode']).replace("*", " ")
                            Barcode = Barcode.split()
                            print(f"Barcode=== {Barcode}")
                            dict_recived['CodeOperator'] = Barcode[0]
                            Barcode = []
                            #
                            # cursor_SQL = MssqlConnection.cnxn_2.cursor()
                            # cursor_SQL.execute(f"select  Title  from ACC.DL  where Code='{str(dict_recived['CodeOperator'])} ' ;")
                            #
                            # Code_Operator_1 = cursor_SQL.fetchall()
                            mycursur = connectToDataBase.Bpms_Database.DB_save.cursor()
                            # mycursur.execute(f"select  LastName, Name , Image  from Employ_person where PersonalCode='{str(dict_recived['CodeOperator'])} ' ;")
                            mycursur.execute(
                                f"select  LastName, Name , Image  from Employ_person where PersonalCode='{str(dict_recived['CodeOperator'])} ' ;")
                            Code_Operator_1 = mycursur.fetchall()
                            print(f"Name Operator: {Code_Operator_1}")
                            Code_Operator_1 = str(Code_Operator_1)
                            Code_Operator_1 = Code_Operator_1.replace("(", "")
                            Code_Operator_1 = Code_Operator_1.replace(")", "")
                            Code_Operator_1 = Code_Operator_1.replace("[", "")
                            Code_Operator_1 = Code_Operator_1.replace("]", "")
                            Code_Operator_1 = Code_Operator_1.replace(",", "")
                            Code_Operator_1 = Code_Operator_1.replace("'", "")
                            Code_Operator_1 = Code_Operator_1.split()
                            Code_Operator_3 = Code_Operator_1[1] + " " + Code_Operator_1[0]
                            print(Code_Operator_1)
                            ############ conver operator image
                            # print(f"image Operator:  {Code_Operator_1[2]}")
                            # print(f"Path base {Path(__file__).resolve().parent.parent.parent/Code_Operator_1[2]}")
                            # with open(Path(__file__).resolve().parent.parent.parent/Code_Operator_1[2], 'rb') as OperatorImage:
                            #     dict_recived["OperatorImage"] =  base64.b64encode(OperatorImage.read())
                            #     OperatorImage.close()

                            # print(f"image Operator:  {Code_Operator_1[2]}")
                            # print(f"Path base {Path(__file__).resolve().parent.parent.parent / Code_Operator_1[2]}")
                            # pathfile = Path(__file__).resolve().parent.parent.parent / Code_Operator_1[2]
                            # connection.send(f"{Path(__file__).resolve().parent.parent.parent/Code_Operator_1[2]}"
                            #                 f"{SEPARATOR}"
                            #                 f"{os.path.getsize(Path(__file__).resolve().parent.parent.parent/Code_Operator_1[2])}"
                            #                 f"".encode())
                            # with open(Path(__file__).resolve().parent.parent.parent/Code_Operator_1[2], 'rb') as OperatorImage:
                            #     while True:
                            #         operatorimagebyte  = OperatorImage.read(BUFFER_SIZE)
                            #         if not operatorimagebyte:
                            #             break
                            #         connection.send(operatorimagebyte)

                            # Translate Name persion to english
                            # tranlator =  Translator(from_lang='Persian', to_lang='english')
                            # translation_Name_Operator = tranlator.translate(Code_Operator_3)
                            # with open('../Images/operator/20111.jpeg', 'rb') as picfile:
                            #     picfileread = base64.b64encode(picfile.read())

                            dict_recived['OperatorName'] = Code_Operator_3
                            dict_recived['code'] = 105
                            connection.send(dictionary_binary.dict_to_binary(dict_recived))
                            print(f"Data for send :  {dict_recived}")

                            # with open("../Images/operator/mostafa.png", 'rb') as picture:
                            #
                            #     operator_pic =  base64.b64encode(picture.read())
                    if dict_recived['code'] == 103:
                        ...

                    if DataBaseStart == True:
                        mserver.UpdateToDB(self=mserver, DATA_dic=dict_recived)
                        dict_recived = {}
                    # bin_recive_for_send = dictionary_binary.dict_to_binary(dict_recived)

                    # except:
                    #     print(" dict recived not ok ")

                    pdf_file = open("D:/photon_project/Tracebility_01/venv_new/Server/Sockets/pyforms-gui.pdf", "rb")
                    Listen_File = pdf_file.read(1024)
                    while (Listen_File):
                        Listen_File = pdf_file.read(1024)

                connection.close()

            while True:
                # if Ui_MainWindow().connection_work == True:
                Client, address = ServerSideSocket.accept()
                if address not in mserver.clients:
                    mserver.clients.append(Client)

                start_new_thread(multi_threaded_client, (Client,))
                # # process_2 =  multiProcessing.Process(target=multi_threaded_client, args=Client)
                # # process_2.start()
                # process_2 = start_new(multi_threaded_client)
                # process_2.start()
                ThreadCount += 1
                print('Thread Number: ' + str(ThreadCount))
                print(f"conncted client :{mserver.clients[ThreadCount - 1]}")
                print(f"conncted client  Count  :{len(mserver.clients)}")

            # ServerSideSocket.close()

        def Calculate_data_Tracebility():
            connectToDataBase.Bpms_Database.DATA_dic

    def UpdateToDB(self, DATA_dic):
        self.DATA_dic = DATA_dic
        cursor = self.DB_save.cursor()

        TABLE_NAME = f"Save_Tracebility_{JalaliDatetime.now().year}-{JalaliDatetime.now().month}"

        #### get opc-order
        #####   for dictionary recive from client
        # sql_Opc_Order = f"select Opc_Order, Order_code_Product from Opc_Product where code_Product={int(DATA_dic['CodeProduct'])}"
        #
        # cursor.execute(sql_Opc_Order)
        # Opc_Order_Data =   cursor.fetchall()

        ### GET OPC_ORDER FROM TABLE RESULT
        # self.DATA_dic["Opc_Order"] = Opc_Order_Data[0][0]
        ### GET Order_code_Product FROM TABLE RESULT
        # self.DATA_dic["Order_code_Product"] = Opc_Order_Data[0][1]

        # print(DATA_dic["CodeProduct"])
        SQL_1 = """CREATE TABLE if  NOT EXISTS `%s` (Code_Product INT(7) , Order_code_Product INT(7),Code_Operator INT(7), OPC_order TEXT, Station_number INT(2), Date_Time VARCHAR(40), Tracebility_code varchar (15) character set 'utf8' COLLATE 'utf8_persian_ci' )""" % (
            TABLE_NAME)
        # SQL_1 = f"CREATE TABLE if  NOT EXISTS Save_Tracebility{JalaliDatetime.now().year} (Code_Product INT , Order_code_Product INT,Code_Operator INT, OPC_order TEXT, Station_number INT, Date_Time VARCHAR, Tracebility_code varchar  )"
        cursor.execute(SQL_1)
        self.DB_save.commit()

        ##########  Set Tracebility code To StationNumber

        SQL_2 = f"SELECT 	* FROM Station_to_Order where StationNumber={int(self.DATA_dic['Stationnumber'])} ORDER BY ID DESC LIMIT 1;"
        cursor.execute(SQL_2)
        Station_to_order = cursor.fetchall()

        if Station_to_order != []:
            ####### Save Station_to_order to file for perevent  problemsome
            with open('Station_to_Order.ptp', 'wt') as CodeOperatorFile2:
                CodeOperatorFile2.write(str(Station_to_order[0][2]))
                CodeOperatorFile2.close()
        with open('Station_to_Order.ptp', 'r') as Station_to_Order:
            self.Station_to_Order_code = str(Station_to_Order.read())

        ##############Save Tracebility code  with Station number
        try:
            if self.DATA_dic['Stationnumber'] == self.Station_to_Order_code:
                if len(self.DATA_dic['Barcode']) > 6:
                    SQL_3 = f"""REPLACE  INTO Tracebility_code(TracebilityCode) VALUES ({self.DATA_dic['Barcode']})"""
                    Val_3 = f"{self.DATA_dic['Barcode']}"
                    cursor.execute(SQL_3)
                    self.DB_save.commit()
        except:
            print("not Station_to_order applyed")

        ############################## Classify  Barcode  StationNumbers
        if self.DATA_dic['Stationnumber'] not in list_Stations['StationNumbers']:
            list_Stations['StationNumbers'].append(self.DATA_dic['Stationnumber'])
        print(f"StationNumbers  {list_Stations['StationNumbers']}")
        print(f"len  StationNumbers  {len(list_Stations['StationNumbers'])}")

        for StationNumber in list_Stations['StationNumbers']:
            if StationNumber == self.DATA_dic['Stationnumber']:
                print(f"StationNumber = {StationNumber}")
                ################################
                # self.DATA_dic["CodeOperator"] = state_online['CodeOperator']
                date_now = JalaliDatetime.now().strftime('%C')
                self.DATA_dic["DateTime"] = date_now

                if len(self.DATA_dic['Barcode']) > 6:
                    self.DATA_dic['Tracebility_code'] = self.DATA_dic['Barcode']
                    self.Befor_Tracebility_code = self.DATA_dic['Tracebility_code']
                # try:
                ## Asign code operator
                # if len(self.DATA_dic['Barcode'])   < 6:

                # self.DATA_dic["CodeOperator"] =  self.DATA_dic['Barcode']
                # state_online['CodeOperator'] = self.DATA_dic["CodeOperator"]
                # self.DATA_dic['Tracebility_code'] =  self.Befor_Tracebility_code
                # self.StastionNumber_Asign_toCodeOperator["CodeOperators"].append(self.DATA_dic["CodeOperator"])
                # self.StastionNumber_Asign_toCodeOperator["CodeOperators"] = list(set(self.StastionNumber_Asign_toCodeOperator["CodeOperators"]))
                # print(f"StastionNumber_Asign_toCodeOperator {self.StastionNumber_Asign_toCodeOperator['CodeOperators']}")
                # except:
                #     print("Operator Not Access ")

                ##############################################################################
                # if self.DATA_dic["CodeOperator"] not in Bpms_Database.list_operators['CodeOperators']:
                #     Bpms_Database.list_operators['CodeOperators'].append(self.DATA_dic['CodeOperator'])
                # print(f"CodeOperators  {Bpms_Database.list_operators['CodeOperators']}")
                # print(f"len  CodeOperators  {len(Bpms_Database.list_operators['CodeOperators'])}")
                if len(self.DATA_dic["CodeOperator"]) == 5:
                    ...
                    # # sql_connected_client = """INSERT IGNORE  INTO `Client_connected`( `CodeOperator`, `time`, `Stationnumber`) VALUES (%s,%s,%s)  ON DUPLICATE KEY UPDATE (`CodeOperator`= {self.DATA_dic['CodeOperator']})"""
                    # sql_delete = f" DELETE FROM `Client_connected`   where   `Stationnumber`='{self.DATA_dic['CodeOperator']}';"
                    # sql_connected_client1 = """INSERT  INTO `Client_connected`( `CodeOperator`, `time`, `Stationnumber`) VALUES (%s,%s,%s)  """
                    # # sql_connected_client2 = """ALTER IGNORE TABLE   `Client_connected` add  UNIQUE INDEX u(`Stationnumber`)  """
                    # val_sql_connected_client = f"{self.DATA_dic['CodeOperator']}", f"{self.DATA_dic['DateTime']}", f"{self.DATA_dic['Stationnumber']}"
                    # cursor.execute(sql_delete)
                    # self.DB_save.commit()
                    # cursor.execute(sql_connected_client1, val_sql_connected_client)
                    # # cursor.execute(sql_connected_client2)
                    # self.DB_save.commit()

                # print(f"state_online['CodeOperator']  ){state_online['CodeOperator']}")
                if len(self.DATA_dic["CodeOperator"]) == 5:
                    if len(self.DATA_dic['Barcode']) > 6:
                        # self.DATA_dic["CodeOperator"] =  state_online['CodeOperator']

                        sql = "INSERT INTO `%s`" % TABLE_NAME + "(`Code_Product`, `Order_code_Product`, `Code_Operator`, `OPC_order`, `Station_number`, `Date_Time`, `Tracebility_code`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        # print(TABLE_NAME)
                        # sql =  "INSERT INTO `Save_Tracebility`(`Code_Product`,`Code_Order_Ref`, `Code_Operator`, `OPC_order`, `Station_number`, `Date_Time`) VALUES (%s, %s, %s, %s, %s, %s)"
                        # val = f"{self.DATA_dic['CodeProduct']}", f"{self.DATA_dic['Order_code_Product']}",f"{self.DATA_dic['CodeOperator']}", f"{self.DATA_dic['Opc_Order']}" , f"{self.DATA_dic['0010']}", f"{self.DATA_dic['DateTime']}"
                        val = f"{0}", f"{int(self.Station_to_Order_code)}", f"{self.DATA_dic['CodeOperator']}", f"{'null'}", f"{self.DATA_dic['Stationnumber']}", f"{self.DATA_dic['DateTime']}", f"{self.DATA_dic['Tracebility_code']}"
                        cursor.execute(sql, val)
                        self.DB_save.commit()
                        print(f" from Code operator get data   = {self.DATA_dic['CodeOperator']}")

                # else:
                #     print(f"client not  access {self.DATA_dic['CodeOperator']}")
                #










