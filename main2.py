from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox, QMainWindow
from PyQt6.uic import loadUi
import sys
import mysql.connector

# xu ly
ddb = mysql.connector.connect(user='root', password='root', host='localhost')


class loginUi(QMainWindow):  # login window
    def __init__(self):
        super(loginUi, self).__init__()
        uic.loadUi('login.ui', self)
        self.SignIn.clicked.connect(self.login)
        self.SignUp.clicked.connect(self.register)

    def login(self):
        un = self.UserName.text()
        pw = self.UserPW.text()
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='TEST1')
        cs = db.cursor()
        cs.execute("select * from User where name = '" + un + "' and Password='" + pw + "'")
        kt = cs.fetchone()
        if kt:
            QMessageBox.information(self, "Loginouput", "Login success")
            cs.execute("select Usercol from User where name = '" + un + "' and Password='" + pw + "'")
            usercol = cs.fetchone()
            if (usercol[0] == "Doctor"):
                widget.setCurrentIndex(1)
            if (usercol[0] == "Patient"):
                widget.setCurrentIndex(2)
                widget.setFixedHeight(1000)
                widget.setFixedWidth(1000)

        else:
            QMessageBox.information(self, "Login Output", "Login fail")

    def register(self):
        widget.setCurrentIndex(3)


class doctorUi(QMainWindow):  # doctor window
    def __init__(self):
        super(doctorUi, self).__init__()
        uic.loadUi('doctor.ui', self)


class patientUi(QMainWindow):  # doctor window
    def __init__(self):
        super(patientUi, self).__init__()
        uic.loadUi('patient.ui', self)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        self.updateinf.clicked.connect(self.fillBang)

    def fillBang(self):
        DN = self.doctorname.text()
        Time = self.gioHen.time()


class formUi(QMainWindow):  # doctor window
    def __init__(self):
        super(formUi, self).__init__()
        uic.loadUi('formsignup.ui', self)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
Login_f = loginUi()
Doctor_f = doctorUi()
Patient_f = patientUi()
Form_f = formUi()
widget.addWidget(Login_f)
widget.addWidget(Doctor_f)
widget.addWidget(Patient_f)
widget.addWidget(Form_f)

widget.setCurrentIndex(0)
widget.setFixedHeight(602)
widget.setFixedWidth(804)
widget.show()
app.exec()
