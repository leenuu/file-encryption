from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.sip import delete
from login__ui import Ui_login_dialog
from main import encryption_pro

class Ui_main_widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_pro = encryption_pro()
        self.file_list = list()
        self.selec_list = list()

    def setupUi(self, main_dialog):
        main_dialog.setObjectName("main_dialog")
        main_dialog.resize(431, 407)
        self.pull_btn = QtWidgets.QPushButton(main_dialog)
        self.pull_btn.setGeometry(QtCore.QRect(180, 160, 75, 23))
        self.pull_btn.setObjectName("pull_it")
        self.all_it = QtWidgets.QListWidget(main_dialog)
        self.all_it.setGeometry(QtCore.QRect(10, 40, 141, 291))
        self.all_it.setObjectName("all_it")
        self.select_it = QtWidgets.QListWidget(main_dialog)
        self.select_it.setGeometry(QtCore.QRect(280, 40, 141, 291))
        self.select_it.setObjectName("select_it")
        self.del_btn = QtWidgets.QPushButton(main_dialog)
        self.del_btn.setGeometry(QtCore.QRect(180, 260, 75, 23))
        self.del_btn.setObjectName("del_it")
        self.push_btn = QtWidgets.QPushButton(main_dialog)
        self.push_btn.setGeometry(QtCore.QRect(180, 130, 75, 23))
        self.push_btn.setObjectName("push_it")
        self.add_btn = QtWidgets.QPushButton(main_dialog)
        self.add_btn.setGeometry(QtCore.QRect(180, 230, 75, 23))
        self.add_btn.setObjectName("add_it")
        self.login_btn = QtWidgets.QPushButton(main_dialog)
        self.login_btn.setGeometry(QtCore.QRect(180, 40, 75, 23))
        self.login_btn.setObjectName("login_btn")

        self.login_btn.clicked.connect(self.login)
        self.add_btn.clicked.connect(self.add_list)
        self.del_btn.clicked.connect(self.del_list)
        self.pull_btn.clicked.connect(self.pull)
        self.push_btn.clicked.connect(self.psuh)

        _translate = QtCore.QCoreApplication.translate
        main_dialog.setWindowTitle(_translate("main_dialog", "Dialog"))
        self.pull_btn.setText(_translate("main_dialog","<<<"))
        self.del_btn.setText(_translate("main_dialog", "del"))
        self.push_btn.setText(_translate("main_dialog", ">>>"))
        self.add_btn.setText(_translate("main_dialog", "add"))
        self.login_btn.setText(_translate("main_dialog", "login"))

    def login(self):
        login_form = Ui_login_dialog()
        login_form.exec_()
        if login_form.status == 1:
            print('pass')
        else:
            print('closs')

    def load(self):
        pass
    
    def save(self):
        pass

    def psuh(self):
        try:
            selected_it_num = self.all_it.currentRow()
            selected_it_name = self.all_it.currentItem().text()
            self.all_it.takeItem(selected_it_num)
            del self.file_list[self.file_list.index(selected_it_name)]
            self.select_it.clear()

            self.selec_list.append(selected_it_name)
            for it in self.selec_list:
                self.select_it.addItem(it)

            print(f'select : {self.selec_list}')
            print(f'file : {self.file_list}')

        except:
            pass

    def pull(self):
        try:
            selected_it_num = self.select_it.currentRow()
            selected_it_name = self.select_it.currentItem().text()
            self.select_it.takeItem(selected_it_num)
            del self.selec_list[self.selec_list.index(selected_it_name)]
            self.all_it.clear()

            self.file_list.append(selected_it_name)
            for it in self.file_list:
                self.all_it.addItem(it)

            print(f'select : {self.selec_list}')
            print(f'file : {self.file_list}')

        except:
            pass

    def add_list(self):
        files = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File') 
        filename = files[0].split('/')[len(files[0].split('/')) - 1]
        self.file_list.append(filename)
        self.all_it.clear()
        for it in self.file_list:
            self.all_it.addItem(it)

        print(f'select : {self.selec_list}')
        print(f'file : {self.file_list}')

    def del_list(self):
        try:
            selected_it_num = self.all_it.currentRow()
            selected_it_name = self.all_it.currentItem().text()
            self.all_it.takeItem(selected_it_num)
            del self.file_list[self.file_list.index(selected_it_name)]

            print(f'select : {self.selec_list}')
            print(f'file : {self.file_list}')

        except:
            pass
