from PyQt5 import QtCore, QtGui, QtWidgets
from login__ui import Ui_login_dialog

class Ui_main_widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, main_dialog):
        main_dialog.setObjectName("main_dialog")
        main_dialog.resize(431, 407)
        self.pull_int = QtWidgets.QPushButton(main_dialog)
        self.pull_int.setGeometry(QtCore.QRect(180, 160, 75, 23))
        self.pull_int.setObjectName("pull_int")
        self.all_it = QtWidgets.QListView(main_dialog)
        self.all_it.setGeometry(QtCore.QRect(10, 40, 141, 291))
        self.all_it.setObjectName("all_it")
        self.add_2 = QtWidgets.QPushButton(main_dialog)
        self.add_2.setGeometry(QtCore.QRect(180, 260, 75, 23))
        self.add_2.setObjectName("add_2")
        self.selec_it = QtWidgets.QListView(main_dialog)
        self.selec_it.setGeometry(QtCore.QRect(280, 40, 141, 291))
        self.selec_it.setObjectName("selec_it")
        self.push_it = QtWidgets.QPushButton(main_dialog)
        self.push_it.setGeometry(QtCore.QRect(180, 130, 75, 23))
        self.push_it.setObjectName("push_it")
        self.add = QtWidgets.QPushButton(main_dialog)
        self.add.setGeometry(QtCore.QRect(180, 230, 75, 23))
        self.add.setObjectName("add")
        self.login_btn = QtWidgets.QPushButton(main_dialog)
        self.login_btn.setGeometry(QtCore.QRect(180, 40, 75, 23))
        self.login_btn.setObjectName("login_btn")

        self.login_btn.clicked.connect(self.login)

        # _translate = QtCore.QCoreApplication.translate
        # main_dialog.setWindowTitle(_translate("main_dialog", "Dialog"))
        # self.pull_int.setText(_translate("main_dialog", "<<<"))
        # self.add_2.setText(_translate("main_dialog", "del"))
        # self.push_it.setText(_translate("main_dialog", ">>>"))
        # self.add.setText(_translate("main_dialog", "add"))
        # self.login.setText(_translate("main_dialog", "login"))

    def login(self):
        login_form = Ui_login_dialog()
        login_form.exec_()
