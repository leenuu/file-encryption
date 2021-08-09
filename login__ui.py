from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, login_dialog):
        login_dialog.setObjectName("login_dialog")
        login_dialog.resize(431, 113)   
        self.status = QtWidgets.QLabel(login_dialog)
        self.status.setGeometry(QtCore.QRect(330, 20, 81, 71))
        self.status.setText("")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.login_btn = QtWidgets.QPushButton(login_dialog)
        self.login_btn.setGeometry(QtCore.QRect(220, 20, 91, 71))
        self.login_btn.setObjectName("login_btn")
        self.pass_line = QtWidgets.QLineEdit(login_dialog)
        self.pass_line.setGeometry(QtCore.QRect(20, 60, 181, 31))
        self.pass_line.setObjectName("pass_line")
        self.id_line = QtWidgets.QLineEdit(login_dialog)
        self.id_line.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.id_line.setObjectName("id_line")

        # self.retranslateUi(login_dialog)
        # QtCore.QMetaObject.connectSlotsByName(login_dialog)

        self.login_btn.clicked.connect(self.login)

    # def retranslateUi(self, login_dialog):
    #     _translate = QtCore.QCoreApplication.translate
    #     login_dialog.setWindowTitle(_translate("login_dialog", "Dialog"))
    #     self.login_btn.setText(_translate("login_dialog", "로그인"))

    def login(self):
        id = self.id_line.text()
        if id == '1':
            print("close")
            self.close()
