import pyodbc
class MssqlConnection(object):



    # try:


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
