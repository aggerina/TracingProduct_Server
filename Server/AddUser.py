from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore    import pyqtSlot
#import mysql.connector as mdb
import MySQLdb as mdb
import mysql.connector
# import mariadb as mdb
from Server.Add_User_Main import Ui_MainWindow
import yaml

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

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.button.setEnabled(False)

        self.initWindow()

    def initWindow(self):
        self.lineedit1.setPlaceholderText('Please enter your UserID')
        self.lineedit2.setPlaceholderText('Please enter your Name')
        self.lineedit3.setPlaceholderText('Please enter your Family')
        self.lineedit4.setPlaceholderText('Please enter your Password')
        self.lineedit5.setPlaceholderText('Please enter your Password Again')

        self.lineedit1.textChanged.connect(self.newText)
        self.lineedit2.textChanged.connect(self.newText)
        self.lineedit3.textChanged.connect(self.newText)
        self.lineedit4.textChanged.connect(self.newText)

        self.button.clicked.connect(self.InsertData)




    # @pyqtSlot()
    def InsertData(self):


        mycursor = Bpms_Database.DB_save.cursor()

        sql = "INSERT INTO  Users(username, Personal_code , Last_Name, password) VALUES (%s, %s, %s, %s)"

        val = (f"{self.lineedit2.text()}", f"{self.lineedit1.text()}", f"{self.lineedit3.text()}", f"{self.lineedit4}")
        mycursor.execute(sql, val)

        Bpms_Database.DB_save.commit()

        print(mycursor.rowcount, "record inserted.")
        self.lineedit1.setText('')
        self.lineedit2.setText('')
        self.lineedit3.setText('')
        self.lineedit4.setText('')



        # con = mdb.connect('bpmsdatabese','BPMS', 'P@ssw0rd','photon')
        # with con:
        #     cur = con.cursor()
        #     cur.execute("INSERT INTO Employe(UserID, Tablename, Family, Posistion)"
        #                 "VALUES('%s', '%s', '%s', '%s' )"      %   (''.join(self.lineedit1.text()),
        #                                                             ''.join(self.lineedit2.text()),
        #                                                             ''.join(self.lineedit3.text()),
        #                                                             ''.join(self.lineedit4.text())))
        #     print(self.lineedit1.text())
        #     print(self.lineedit2.text())
        #     print(self.lineedit3.text())
        #     print(self.lineedit4.text())
        #     QMessageBox.about(self,"connection", "Data Inser successfuly")
        #
        # self.lineedit1.setText('')
        # self.lineedit2.setText('')
        # self.lineedit3.setText('')
        # self.lineedit4.setText('')
        # # self.initWindow()
        #





        #
        # with con:
        #     cur = con.cursor()
        #     cur.execute('''INSERT INTO Employe(UserID, Tablename , Family, Posistion )
        #                    VALUES ('%s', '%s', '%s', '%s' )''',
        #                     (self.lineedit1.text(),
        #                      self.lineedit2.text(),
        #                      self.lineedit3.text(),
        #                      self.lineedit4.text())
        #                 )
        #
        #     cur.close()
        #     self.close()
        #
        #
        #      QMessageBox.information(self, "Connection", "Data Inserted Successfully")
        #      con.close()




    def newText(self):
        if self.lineedit1.text() and self.lineedit2.text() and self.lineedit3.text():
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())