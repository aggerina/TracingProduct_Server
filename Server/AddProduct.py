
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog ,QTableView , QMainWindow, QPushButton
from PyQt5.QtWidgets import QMessageBox , QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtSql import *
#import MySQLdb as mdb
#from PySide2.QtCore  import pyqtSlot
import mysql.connector
import uuid
import qtawesome as QTA



#
# class Ui_Add_product(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi()



import sys


class DataBases():
    mydb = mysql.connector.connect(
        host="192.168.1.91",
        user="BPMS",
        password="P@ssw0rd",
        database="photon"
    )
class Ui_Add_product(object):
    def setupUi(self, Add_product):


        # self.setObjectName("Add_product")
        # self.resize(700, 400)
        # self.setMinimumSize(QtCore.QSize(700, 400))
        # self.setMaximumSize(QtCore.QSize(700, 400))
        # self.setAutoFillBackground(True)

        self.font = QFont()
        self.font.setFamily("B Nazanin")
        self.font.setPointSize(11)
        Add_product.setObjectName("Add_product")
        Add_product.resize(700, 400)
        Add_product.setMinimumSize(QtCore.QSize(700, 400))
        Add_product.setMaximumSize(QtCore.QSize(700, 400))
        Add_product.setAutoFillBackground(True)
        self.groupBoxaddproduct = QtWidgets.QGroupBox(Add_product)
        self.groupBoxaddproduct.setGeometry(QtCore.QRect(20, 10, 651, 371))
        self.groupBoxaddproduct.setAutoFillBackground(True)
        self.groupBoxaddproduct.setTitle("")
        self.groupBoxaddproduct.setObjectName("groupBoxaddproduct")
        # self.label_namepro = QtWidgets.QLabel(self.groupBoxaddproduct)
        # self.label_namepro.setGeometry(QtCore.QRect(550, 120, 81, 21))
        # self.label_namepro.setAutoFillBackground(True)
        # self.label_namepro.setObjectName("label_namepro")
        # self.label_codtraceabilitu = QtWidgets.QLabel(self.groupBoxaddproduct)
        # self.label_codtraceabilitu.setGeometry(QtCore.QRect(550, 200, 81, 21))
        # self.label_codtraceabilitu.setAutoFillBackground(True)
        # self.label_codtraceabilitu.setObjectName("label_codtraceabilitu")
        self.label_discription = QtWidgets.QLabel(self.groupBoxaddproduct)
        self.label_discription.setGeometry(QtCore.QRect(550, 285, 81, 21))
        self.label_discription.setAutoFillBackground(True)
        self.label_discription.setObjectName("label_discription")

        # self.lineEdit_ID = QtWidgets.QLineEdit(self.groupBoxaddproduct)
        # self.lineEdit_ID.setGeometry(QtCore.QRect(420, 120, 150, 20))
        # self.lineEdit_ID.setObjectName("lineEdit_namepro")

        # self.lineEdit_namepro = QtWidgets.QLineEdit(self.groupBoxaddproduct)
        # self.lineEdit_namepro.setGeometry(QtCore.QRect(420, 120, 150, 20))
        # self.lineEdit_namepro.setObjectName("lineEdit_namepro")

        self.lineEdit_codepro = QtWidgets.QLineEdit(self.groupBoxaddproduct)
        self.lineEdit_codepro.setGeometry(QtCore.QRect(420, 160, 150, 20))
        self.lineEdit_codepro.setObjectName("lineEdit_codepro")
        # self.label_orgpro = QtWidgets.QLabel(self.groupBoxaddproduct)
        # self.label_orgpro.setGeometry(QtCore.QRect(550, 240, 81, 21))
        # self.label_orgpro.setAutoFillBackground(True)
        # self.label_orgpro.setObjectName("label_orgpro")

        # self.lineEdit_codtraceabilitu = QtWidgets.QLineEdit(self.groupBoxaddproduct)
        # self.lineEdit_codtraceabilitu.setGeometry(QtCore.QRect(420, 200, 150, 20))
        # self.lineEdit_codtraceabilitu.setObjectName("lineEdit_codtraceabilitu")
        #
        # self.lineEdit_orgpro = QtWidgets.QLineEdit(self.groupBoxaddproduct)
        # self.lineEdit_orgpro.setGeometry(QtCore.QRect(420, 240, 150, 20))
        # self.lineEdit_orgpro.setObjectName("lineEdit_orgpro")

        self.label_codepro = QtWidgets.QLabel(self.groupBoxaddproduct)
        self.label_codepro.setGeometry(QtCore.QRect(550, 160, 81, 21))
        self.label_codepro.setAutoFillBackground(False)
        self.label_codepro.setObjectName("label_codepro")
        self.lineEdit_discription = QtWidgets.QLineEdit(self.groupBoxaddproduct)
        self.lineEdit_discription.setGeometry(QtCore.QRect(40, 280, 491, 31))
        self.lineEdit_discription.setObjectName("lineEdit_discription")


        ##SET pLACEHOLDER

        # self.lineEdit_namepro.setPlaceholderText('Please enter Product Name')
        self.lineEdit_codepro.setPlaceholderText('لطفا کد محصول را وارد کنید ')
        # self.lineEdit_codtraceabilitu.setPlaceholderText('لطفا کد رد یابی محصول را وارد کنید ')
        # self.lineEdit_orgpro.setPlaceholderText('لطفامحل استفاده محصول راواردکنید')
        self.lineEdit_discription.setPlaceholderText('لطفا مشخصات فنی محصول را وارد کنید ')
        ###  change value enable
        # self.lineEdit_namepro.textChanged.connect(self.newText)
        self.lineEdit_codepro.textChanged.connect(self.newText)
        # self.lineEdit_codtraceabilitu.textChanged.connect(self.newText)
        # self.lineEdit_orgpro.textChanged.connect(self.newText)
        self.lineEdit_discription.textChanged.connect(self.newText)

        ##picture
        self.pushButton_addpicture = QtWidgets.QPushButton(self.groupBoxaddproduct)
        self.pushButton_addpicture.setGeometry(QtCore.QRect(510, 320, 121, 31))
        self.pushButton_addpicture.setAutoFillBackground(True)
        self.pushButton_addpicture.setObjectName("pushButton_addpicture")

        self.pushButton_add_save = QtWidgets.QPushButton(self.groupBoxaddproduct)
        self.pushButton_add_save.setGeometry(QtCore.QRect(50, 340, 75, 23))
        self.pushButton_add_save.setAutoFillBackground(True)
        self.pushButton_add_save.setObjectName("pushButton_add_save")
        self.pushButton_add_save.setEnabled(False)

        self.label_picturepro = QtWidgets.QLabel(self.groupBoxaddproduct)
        self.label_picturepro.setGeometry(QtCore.QRect(20, 30, 321, 221))
        self.label_picturepro.setText("")
        self.label_picturepro.setObjectName("label_picturepro")

        self.retranslateUi(Add_product)


        icon_picture = QTA.icon('fa.picture-o')
        self.pushButton_addpicture.setIcon(icon_picture)

        icon_Save = QTA.icon('fa5s.save')
        self.pushButton_add_save.setIcon(icon_Save)
#############fonts set
        self.pushButton_add_save.setEnabled(False)
        icon_duplicate = QTA.icon('mdi.content-duplicate')
        self.lineEdit_codepro.setWindowIcon(icon_duplicate)
        self.lineEdit_discription.setFont(self.font)
        self.lineEdit_codepro.setFont(self.font)
        # self.lineEdit_codtraceabilitu.setFont(self.font)
        self.label_codepro.setFont(self.font)
        # self.label_codtraceabilitu.setFont(self.font)
        self.label_picturepro.setFont(self.font)
        self.pushButton_addpicture.setFont(self.font)
        self.pushButton_add_save.setFont(self.font)
        self.label_discription.setFont(self.font)


        ####signals
        self.pushButton_add_save.clicked.connect(self.InsertProduct)
        self.pushButton_addpicture.clicked.connect(lambda : self.AddPicture())
        self.lineEdit_codepro.textChanged.connect(self.find_already_code_product)
    def InsertProduct(self):
        mydb = DataBases.mydb
        mycursor = DataBases.mydb.cursor()
        sql = "INSERT INTO  Products( CodProduct, Discription, CodTracebility) VALUES ( %s, %s, %s)"
        val = ( f"{self.lineEdit_codepro.text()}",  f"{self.lineEdit_discription.text()}" , f"{str(hash(uuid.uuid4()))}")
        mycursor.execute(sql, val)
        print(mycursor.rowcount, "record inserted.")
        msg = QMessageBox()
        icon_info  = QTA.icon('ei.ok-sign')

        msg.setWindowIcon(icon_info)
        # msg.setStyle('fusion')
        msg.setText("ذخیره در دیتا بیس انجام شده ")
        msg.setWindowTitle("success Full")
        msg.exec_()
        mydb.commit()
        self.lineEdit_codepro.setText('')
        self.lineEdit_discription.setText('')
    def retranslateUi(self, Add_product):
        _translate = QtCore.QCoreApplication.translate
        Add_product.setWindowTitle(_translate("Add_product", "اضافه کردن محصول "))
        # self.label_namepro.setText(_translate("Add_product", " نام محصول"))
        # self.label_codtraceabilitu.setText(_translate("Add_product", " کد ردیابی "))
        self.label_discription.setText(_translate("Add_product", "شرح کالا "))
        # self.label_orgpro.setText(_translate("Add_product", " محل استفاده "))
        self.label_codepro.setText(_translate("Add_product", " کد محصول "))
        self.pushButton_addpicture.setText(_translate("Add_product", "بارگزاری عکس "))
        self.pushButton_add_save.setText(_translate("Add_product", "SAVE"))


    def find_already_code_product(self):
        try:

            mycursor_1 = DataBases.mydb.cursor()
            sql = f"select * from  Products where CodProduct={str(self.lineEdit_codepro.text())}"
            mycursor_1.execute(sql)
            self.already =  mycursor_1.fetchall()
            print(self.already)
            if self.already == []:
                if self.lineEdit_discription.text() and self.lineEdit_codepro.text():
                    self.pushButton_add_save.setEnabled(True)
                print("کد محصول تکراری نیست ")
                # self.newText

            else:
                self.Already_Product = False
                print("کد محصول تکراری میباشد ")
                # self.newText
                self.pushButton_add_save.setEnabled(False)
                icon_duplicate = QTA.icon('mdi.content-duplicate')
                self.lineEdit_codepro.windowIconChanged(icon_duplicate)
        except:
            ...

    def newText(self):
        if    self.lineEdit_discription.text() and self.lineEdit_codepro.text():
            if self.already == []:

                self.pushButton_add_save.setEnabled(True)
            else:
                self.pushButton_add_save.setEnabled(False)



    def SaveProduct(self):
        Sql_lineEdit_namepro        = self.lineEdit_namepro.text()
        print(Sql_lineEdit_namepro)

        SqllineEdit_codepro         = self.lineEdit_codepro.text()
        print(SqllineEdit_codepro)

        SqllineEdit_codtraceabilitu = self.lineEdit_codtraceabilitu.text()
        print(SqllineEdit_codtraceabilitu)

        SqllineEdit_discription     = self.lineEdit_discription.text()
        print(SqllineEdit_discription)

        SqllineEdit_orgpro          = self.lineEdit_orgpro.text()
        print(SqllineEdit_orgpro)


        self.lineEdit_namepro.clear()
        self.lineEdit_codepro.clear()
        self.lineEdit_discription.clear()
        self.lineEdit_codtraceabilitu.clear()
        self.lineEdit_orgpro.clear()

    class AddPicture(QWidget):

        def __init__(self):
            super().__init__()
            self.title = 'PyQt5 file dialogs - pythonspot.com'
            self.left = 10
            self.top = 10
            self.width = 640
            self.height = 480
            self.initUI()

        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)

            self.openFileNameDialog()
            self.openFileNamesDialog()
            self.saveFileDialog()

            self.show()

        def openFileNameDialog(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                      "All Files (*);;Python Files (*.py)", options=options)
            if fileName:
                print(fileName)

        def openFileNamesDialog(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                    "All Files (*);;Python Files (*.py)", options=options)
            if files:
                print(files)

        def saveFileDialog(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                      "All Files (*);;Text Files (*.txt)", options=options)
            if fileName:
                print(fileName)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle("Fusion")
    Add_product = QtWidgets.QDialog()
    ui = Ui_Add_product()
    ui.setupUi(Add_product)
    Add_product.show()
    ####SaveProduct


    sys.exit(app.exec_())
