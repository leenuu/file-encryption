from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.status = 0

    def setupUi(self, login_dialog):
        login_dialog.setObjectName("login_dialog")
        login_dialog.resize(431, 113)   
        self.status_line = QtWidgets.QLabel(login_dialog)
        self.status_line.setGeometry(QtCore.QRect(330, 20, 81, 71))
        self.status_line.setText("")
        self.status_line.setAlignment(QtCore.Qt.AlignCenter)
        self.status_line.setObjectName("status_line")
        self.login_btn = QtWidgets.QPushButton(login_dialog)
        self.login_btn.setGeometry(QtCore.QRect(220, 20, 91, 71))
        self.login_btn.setObjectName("login_btn")
        self.pass_line = QtWidgets.QLineEdit(login_dialog)
        self.pass_line.setGeometry(QtCore.QRect(20, 60, 181, 31))
        self.pass_line.setObjectName("pass_line")
        self.id_line = QtWidgets.QLineEdit(login_dialog)
        self.id_line.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.id_line.setObjectName("id_line")

        self.login_btn.clicked.connect(self.login)

        _translate = QtCore.QCoreApplication.translate
        login_dialog.setWindowTitle(_translate("login_dialog", "Dialog"))
        self.login_btn.setText(_translate("login_dialog", "로그인"))

    def login(self):
        _translate = QtCore.QCoreApplication.translate
        id = self.id_line.text()
        pass_word = self.pass_line.text()
        if id == '1' and pass_word == '1':
            self.status = 1
            print("close")
            self.close()

        else:
            self.status_line.setText(_translate("login_dialog", "faill"))

