

from PyQt5 import QtCore, QtGui, QtWidgets
import  mysql.connector

import qtawesome as QTA


class Ui_Form_show_all_product(object):
    def setupUi(self, Form_show_all_product):
        Form_show_all_product.setObjectName("Form_show_all_product")
        Form_show_all_product.resize(1005, 676)
        self.tableWidget = QtWidgets.QTableWidget(Form_show_all_product)
        self.tableWidget.setGeometry(QtCore.QRect(40, 10, 761, 541))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        # self.tableWidget.setRowCount(38)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.pushButtonSHOW = QtWidgets.QPushButton(Form_show_all_product)
        self.pushButtonSHOW.setGeometry(QtCore.QRect(590, 560, 141, 41))
        self.pushButtonSHOW.setObjectName("pushButton")

        self.retranslateUi(Form_show_all_product)
        QtCore.QMetaObject.connectSlotsByName(Form_show_all_product)




    def retranslateUi(self, Form_show_all_product):
        _translate = QtCore.QCoreApplication.translate
        Form_show_all_product.setWindowTitle(_translate("Form_show_all_product", "Form"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form_show_all_product", "id "))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form_show_all_product", " کد محصول"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form_show_all_product", "توضیحات"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form_show_all_product", "کد ردیابی "))
        self.pushButtonSHOW.setText(_translate("Form_show_all_product", "Refreash"))

        self.pushButtonSHOW.clicked.connect(self.ShowDAta)
        
        self.pushButtonSHOW.setIcon(QTA.icon('mdi.database-refresh'))



    def ShowDAta(self):
        mydb = mysql.connector.connect(
            host="192.168.1.91",
            user="BPMS",
            password="P@ssw0rd",
            database="photon"
        )

        mycursor = mydb.cursor()
        # sqlQry = "SELECT * FROM Product"
        # result =  mycursor.execute("SELECT * FROM Product")
        mycursor.execute("SELECT * FROM Products")
        result = mycursor.fetchall()


        self.tableWidget.setRowCount(0)
        for row_number, row_data  in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        mydb.commit()
        mydb.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle("Fusion")
    Form_show_all_product = QtWidgets.QWidget()
    ui = Ui_Form_show_all_product()
    ui.setupUi(Form_show_all_product)
    Form_show_all_product.show()
    sys.exit(app.exec_())
