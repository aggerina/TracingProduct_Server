# 
# import socket
# import Server_Gui_Bpms_26
# import time
# import multiProcessing
# import os
# from _thread import *
# from threading import Thread
# import pyodbc, pyodbc, re, sys, asyncio, mysql.connector, datetime
# import  Setting_server_5
# import pandas as pd
# import yaml
# 
# 
# # DATA_DICT = {Code_Product:'1101152',Version_Product:'1.01',Code_Operator:'210010'}
# class  Connect_To_server():
#     try:
#         with open("config.yaml", "r") as yamlfile:
#             data_r = yaml.load(yamlfile, Loader=yaml.FullLoader)
# 
# 
#         DB_save = mysql.connector.connect(
# 
#             host= data_r[0]['DATA_Setting']['HOST_SERVER'],
#             user= data_r[0]['DATA_Setting']['USER_SERVER'],
#             password= data_r[0]['DATA_Setting']['PASSWORD_SERVER'],
#             database= data_r[0]['DATA_Setting']['DATABASE_SERVER'],
#         )
#     except:
#         import sys
#         print('no connection')
# 
# 
# 
# class mserver(object):
#     # print(curent_timee.day)
#     print(datetime.datetime.now())
# 
# 
#     def __init__(self):
#         Thread.__init__(self)
# 
#         print('init')
#         self.curent_timee =  datetime.datetime.now()
# 
# 
#     start_value = 1
#     BUFFER_SIZE = 1024
#     recived_f = 'imgt_thread' + str(time.time()).split('.')[0] + '.jpg'
# 
#     # def myprocess(self,SendPort, RecivePort):
#     # def Get_Value(self):
#     # 
#     #     self.Send_Port =  Send_Port
#     #     self.Listen_Port = Listen_Port
#     #     print(f"Send_Port{self.Send_Port}")
#     #     print(f"Listen_Port{self.Listen_Port}")
#     #     return self.Listen_Port , self.Send_Port
# 
#         # return self.Send_Port
# 
# 
# 
#     def myprocess():
# 
# 
# 
#         process = multiProcessing.Process(target=mserver.ListenFun  )
#         process.start()
# 
# 
# 
# 
# 
# 
# 
#     def ListenFun():
# 
#         with open("config.yaml", "r") as yamlfile:
#             data = yaml.load(yamlfile, Loader=yaml.FullLoader)
#         print(data[0]['DATA_Setting']['send_port'])
# 
# 
# 
#         with socket.socket() as ServerSideSocket:
#             # ServerSideSocket = socket.socket()
#             host = socket.gethostbyname("pc-backup")
#             print(host)
#             LI_Port = int(data[0]['DATA_Setting']['send_port'])
# 
#             ThreadCount = 0
#             try:
#                 ServerSideSocket.bind((host, LI_Port))
#             except socket.error as e:
#                 print(str(e))
#             print('Socket is listening..')
#             ServerSideSocket.listen(100)
# 
#             def multi_threaded_client( connection):
#                 BUFFER_SIZE = 1024
#                 connection.send(str.encode('Server is working:'))
#                 _start = "0011"
#                 _stop = "0012"
#                 _error = "0013"
#                 _warinig = "0014"
#                 retry = "0015"
#                 msg_5 = "0016"
#                 msg_7 = "0017"
#                 msg_8 = "0018"
#                 msg_9 = "0019"
#                 msg_10 = "00110"
#                 msg_11 = "00111"
#                 msg_12 = "00112"
#                 msg_13 = "00113"
#                 while True:
#                     global data_reciv
#                     data_reciv = connection.recv(2048)
#                     print(data_reciv)
# 
#                     global response
#                     response =  data_reciv.decode('utf-8')
#                     # print(response)
# 
#                     dict_response =  response
#                     # print(dict(dict_response))
# 
#                     #
#                     if response == _start:
#                         print("try to send file ")
#                         filename = 'IMG/6B.jpg'
#                         f = open(filename, 'rb')
#                         while True:
#                             l = f.read(BUFFER_SIZE)
#                             while (l):
#                                 connection.send(l)
#                                 # print('Sent ',repr(l))
#                                 l = f.read(BUFFER_SIZE)
#                             if not l:
#                                 f.close()
#                                 sock.close()
#                                 break
# 
# 
# 
# 
# 
#                     # response = 'Server message: ' + data.decode('utf-8')
# 
#                     if not data_reciv:
#                         break
#                     # connection.sendall(str.encode("salaM"))
#                 connection.close()
# 
#             while True:
#                 Client, address = ServerSideSocket.accept()
#                 print('Connected to: ' + address[0] + ':' + str(address[1]))
#                 print('Connected to: ', address)
#                 print('Connected to: ', Client)
#                 start_new_thread(multi_threaded_client, (Client,))
#                 # # process_2 =  multiProcessing.Process(target=multi_threaded_client, args=Client)
#                 # # process_2.start()
#                 # process_2 = start_new(multi_threaded_client)
#                 # process_2.start()
#                 ThreadCount += 1
#                 print('Thread Number: ' + str(ThreadCount))
#             ServerSideSocket.close()
# 
# 
# 
# 
# 
# 
# 
# 
# 
#     # def ListenFun(SendPort,RecivPort):
#     # def ListenFun():
#     #     print('Listen_phase_1')
#     #     ServerSideSocket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     #     port = 2020
#     #     HOST = socket.gethostbyname("PC-BACKUP")
#     #     print('Listen_phase_2')
#     #
#     #
#     #     ServerSideSocket.bind((HOST, port ))
#     #     print('Listen_phase_3')
#     #
#     #     print('Listen_phase_4')
#     #     print("Listen")
#     #     ServerSideSocket.listen(5)
#     #     print("Listen_phase_5_bind_and_listen")
#     #
#     # def multi_threaded_client(connection):
#     #     connection.send(str.encode('Server is working:'))
#     #     while True:
#     #         data = connection.recv(2048)
#     #         print(data)
#     #         response = 'Server message: ' + data.decode('utf-8')
#     #         if not data:
#     #             break
#     #         connection.sendall(str.encode(response))
#     #     connection.close()
#     #
#     #     while True:
#     #         Client, address = ServerSideSocket.accept()
#     #         print('Connected to: ' + address[0] + ':' + str(address[1]))
#     #         start_new_thread(multi_threaded_client, (Client,))
#     #         ThreadCount += 1
#     #         print('Thread Number: ' + str(ThreadCount))
#     #     ServerSideSocket.close()
#     # multi_threaded_client()
# 
# 
# 
#             #
#             # conn, addr = ServerSideSocket.accept()
#             #
#             # time.sleep(.01)
#             #
#             # with conn:
#             #
#             #     print('Connected by', addr)
#             #     while True:
#             #
#             #
#             #
#             #
#             #         data     = conn.recv(1024)
#             #         # datastr =  print(input())
#             #         # datasend = conn.send()
#             #         if not data:
#             #             break
#             #
#             #         if data == b'exit':
#             #             print('exit prog')
#             #             break
#             #
#             #         dataint = int(data)
#             #         if dataint == 1:
#             #             print('error')
#             #
#             #         if dataint == 2:
#             #             print('warning')
#             #
#             #
#             #         dataprint = dataint * 2
#             #
#             #
#             #         # conn.sendall(data)
#             #         print(data)
#             #         datastr = str(dataprint)
#             #         print(datastr)
#             #         conn.sendall(datastr.encode('utf-8'))
#             #         conn.close()
#             #         time.sleep(1)
#             #
#             #
# 
# 
