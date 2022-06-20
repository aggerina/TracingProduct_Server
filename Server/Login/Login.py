import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from Server.Database import connectToDataBase
# from Server import AddProduct, DeleteProduct, show_all_product ,Reporter_Tracebility_04
from Server.Main import  main_widget, app_main
# from Server.Main_start import  MainWindow as  MainWindow_start
# from Server.Main_start import  MainWindow
# from Server.Main_start import MainWindow as Main_start
from qt_material import apply_stylesheet


LOGIN_ACCESS = False

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("D:/photon_project/Tracebility_01/venv_new/Server/Login/welcomescreen.ui",self)
        # loadUi("welcomescreen.ui",self)
        self.login.clicked.connect(self.gotologin)
        # self.create.clicked.connect(self.gotocreate)


    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("D:/photon_project/Tracebility_01/venv_new/Server/Login/login.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user)==0 or len(password)==0:
            self.error.setText("Please input all fields.")

        else:
            try:
                cursor = connectToDataBase.Bpms_Database.DB_save.cursor()
                query = 'SELECT password FROM Users  WHERE username =\''+user+"\'"
                cursor.execute(query)
                result_pass = cursor.fetchone()[0]
            except:
                print("not  succefuli login")

            if result_pass == password:
                LOGIN_ACCESS = True
                print("Successfully logged in.")
                if LOGIN_ACCESS == True:
                    # sys.exit(app_main.exec_())
                    main_widget.show()

                    # app_Splash.exec_()
                    widget.close()
                #     ui_main_to_start = Ui_Main()
                #     window_main = QtWidgets.QMainWindow()
                #     ui_main_to_start.setupUi(window_main)
                #     window_main.show()

                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")

class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("createacc.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)

    def signupfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()

        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.error.setText("Please fill in all inputs.")

        elif password!=confirmpassword:
            self.error.setText("Passwords do not match.")
        else:
            conn = sqlite3.connect("shop_data.db")
            cur = conn.cursor()

            user_info = [user, password]
            cur.execute('INSERT INTO login_info (username, password) VALUES (?,?)', user_info)

            conn.commit()
            conn.close()

            fillprofile = FillProfileScreen()
            widget.addWidget(fillprofile)
            widget.setCurrentIndex(widget.currentIndex()+1)

class FillProfileScreen(QDialog):
    def __init__(self):
        super(FillProfileScreen, self).__init__()
        loadUi("fillprofile.ui",self)
        self.image.setPixmap(QPixmap('placeholder.png'))



# main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # apply_stylesheet(app,  theme='light_purple.xml')
    welcome = WelcomeScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(800)
    widget.setFixedWidth(600)
    widget.show()
    #
    # if LOGIN_ACCESS == True:
    #     ui_main_to_start = Ui_Main()
    #     window_main = QtWidgets.QMainWindow()
    #     ui_main_to_start.setupUi(window_main)
    #     window_main.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

