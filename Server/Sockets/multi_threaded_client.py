from khayyam import JalaliDatetime
from . import  dictionary_binary
from Database import connectToDataBase

def multi_threaded_connection(connection):
    date_now = JalaliDatetime.now().strftime('%C')

    BUFFER_SIZE = 1024
    connection.send(str.encode('Server is working:'))
    _start = "0011"
    _stop = "0012"
    _error = "0013"
    _warinig = "0014"
    retry = "0015"
    msg_5 = "0016"
    msg_7 = "0017"
    msg_8 = "0018"
    msg_9 = "0019"
    msg_10 = "00110"
    msg_11 = "00111"
    msg_12 = "00112"
    msg_13 = "00113"
    while True:
        global data_reciv
        # for clin in mserver.clients:

        data_reciv = connection.recv(4096)
        data_socket = data_reciv.decode('utf-8')
        if data_socket == '0000':
            connection.send(b'connection closed')
            print("connection closed")
            connection.close
            Connection_close = True
        # if not Connection_close == True:
        dict_recived = dictionary_binary.binary_to_dict(data_reciv.decode('utf-8'))
        # print(f"data_reciv{data_reciv}")
        # print(dict_recived)
        print(f"CodeProduct==[== {dict_recived['CodeProduct']} ==]")
        f = open("picture.txt", "w+")
        # f.write(dict_recived["picture"])

        # data = data_reciv.decode('utf-8')

        # print(dict_d["CodeProduct"])

        if dict_recived:
            dict_recived["DateTime"] = date_now

            data = {"CodeProduct": 110510, "CodeOperator": 20111,
                    "OPCorder": 4, "Stationnumber": 3, "DeviceNumber": 2,
                    "DateTime": "جمعه ۱۰ بهمن ۱۳۹۹ ۰۲:۱۱:۱۸ ب.ظ"}

            connectToDataBase.Bpms_Database.UpdateToDB(self=connectToDataBase.Bpms_Database, DATA_dic=dict_recived)
            connection.send(b"dict_recived")
            print("dict_recived Saved")

            # print(f"Riceve data str {dict_recived}")

        global response
        response = data_reciv.decode('utf-8')
        dict_response = response
        # print(dict_response)

        if response == _start:
            print("try to send file ")
            filename = 'IMG/6B.jpg'
            f = open(filename, 'rb')
            while True:
                l = f.read(BUFFER_SIZE)
                while (l):
                    connection.send(l)
                    # print('Sent ',repr(l))
                    l = f.read(BUFFER_SIZE)
                if not l:
                    f.close()
                    socket.close()

                    break

        if not data_reciv:
            break
    connection.close()
