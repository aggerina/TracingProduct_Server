# import multiprocessing
# import socket
#
# def handle(connection, address):
#     import logging
#     logging.basicConfig(level=logging.DEBUG)
#     logger = logging.getLogger("process-%r" % (address,))
#     try:
#         logger.debug("Connected %r at %r", connection, address)
#         while True:
#             data = connection.recv(1024)
#             if data == "":
#                 logger.debug("Socket closed remotely")
#                 break
#             logger.debug("Received data %r", data)
#             connection.sendall(data)
#             logger.debug("Sent data")
#     except:
#         logger.exception("Problem handling request")
#     finally:
#         logger.debug("Closing socket")
#         connection.close()
#
# class Server(object):
#     def __init__(self, hostname, port):
#         import logging
#         self.logger = logging.getLogger("server")
#         self.hostname = hostname
#         self.port = port
#
#     def start(self):
#         self.logger.debug("listening")
#         self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.socket.bind((self.hostname, self.port))
#         self.socket.listen(1)
#
#         while True:
#             conn, address = self.socket.accept()
#             self.logger.debug("Got connection")
#             process = multiprocessing.Process(target=handle, args=(conn, address))
#             process.daemon = True
#             process.start()
#             self.logger.debug("Started process %r", process)
#
# if __name__ == "__main__":
#     import logging
#     logging.basicConfig(level=logging.DEBUG)
#     server = Server("0.0.0.0", 9000)
#     try:
#         logging.info("Listening")
#         server.start()
#     except:
#         logging.exception("Unexpected exception")
#     finally:
#         logging.info("Shutting down")
#         for process in multiprocessing.active_children():
#             logging.info("Shutting down process %r", process)
#             process.terminate()
#             process.join()
#     logging.info("All done")
#
#

import socket
import os
from _thread import *

ServerSideSocket = socket.socket()
host = '192.168.1.21'
port = 5050
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        print(data)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()