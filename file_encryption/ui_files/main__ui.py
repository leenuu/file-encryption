# from os import error
from file_encryption.main import encryption_process
from PyQt5 import QtCore, QtWidgets
from . import login__ui

class Ui_main_widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_pro = encryption_process.encryption_pro()
        self.file_list = list()
        self.select_list = list()
        self.all_file_list = list()
        self.all_files = dict()

    def setupUi(self, main_dialog):
        main_dialog.setObjectName("main_dialog")
        main_dialog.resize(431, 407)
        self.pull_btn = QtWidgets.QPushButton(main_dialog)
        self.pull_btn.setGeometry(QtCore.QRect(180, 110, 75, 23))
        self.pull_btn.setObjectName("pull_btn")
        self.del_btn = QtWidgets.QPushButton(main_dialog)
        self.del_btn.setGeometry(QtCore.QRect(180, 220, 75, 23))
        self.del_btn.setObjectName("del_btn")
        self.push_btn = QtWidgets.QPushButton(main_dialog)
        self.push_btn.setGeometry(QtCore.QRect(180, 80, 75, 23))
        self.push_btn.setObjectName("push_btn")
        self.add_btn = QtWidgets.QPushButton(main_dialog)
        self.add_btn.setGeometry(QtCore.QRect(180, 190, 75, 23))
        self.add_btn.setObjectName("add_btn")
        self.login_btn = QtWidgets.QPushButton(main_dialog)
        self.login_btn.setGeometry(QtCore.QRect(180, 30, 75, 23))
        self.login_btn.setObjectName("login_btn")
        self.all_it = QtWidgets.QListWidget(main_dialog)
        self.all_it.setGeometry(QtCore.QRect(10, 30, 141, 351))
        self.all_it.setObjectName("all_it")
        self.select_it = QtWidgets.QListWidget(main_dialog)
        self.select_it.setGeometry(QtCore.QRect(280, 30, 141, 351))
        self.select_it.setObjectName("select_it")
        self.save_btn = QtWidgets.QPushButton(main_dialog)
        self.save_btn.setGeometry(QtCore.QRect(180, 330, 75, 23))
        self.save_btn.setObjectName("save_btn")
        self.refresh_btn = QtWidgets.QPushButton(main_dialog)
        self.refresh_btn.setGeometry(QtCore.QRect(180, 360, 75, 23))
        self.refresh_btn.setObjectName("refresh_btn")
        self.convert_btn = QtWidgets.QPushButton(main_dialog)
        self.convert_btn.setGeometry(QtCore.QRect(180, 300, 75, 23))
        self.convert_btn.setObjectName("convert_btn")

        self.login_btn.clicked.connect(self.login)
        self.add_btn.clicked.connect(self.add_list)
        self.del_btn.clicked.connect(self.del_list)
        self.pull_btn.clicked.connect(self.pull)
        self.push_btn.clicked.connect(self.psuh)
        self.refresh_btn.clicked.connect(self.refresh)
        self.save_btn.clicked.connect(self.save)
        self.convert_btn.clicked.connect(self.convert)

        self.btns_disabled(True)

        _translate = QtCore.QCoreApplication.translate
        main_dialog.setWindowTitle(_translate("main_dialog", "File Encryption"))
        self.pull_btn.setText(_translate("main_dialog","<<<"))
        self.del_btn.setText(_translate("main_dialog", "del"))
        self.push_btn.setText(_translate("main_dialog", ">>>"))
        self.add_btn.setText(_translate("main_dialog", "add"))
        self.login_btn.setText(_translate("main_dialog", "login"))
        self.save_btn.setText(_translate("main_dialog", "save"))
        self.refresh_btn.setText(_translate("main_dialog", "refresh"))
        self.convert_btn.setText(_translate("main_dialog", "convert"))

    def login(self):
        login_form = login__ui.Ui_login_dialog()
        login_form.exec_()
        if login_form.status == 1:
            print('pass')
            self.btns_disabled(False)
            self.load()
        else:
            print('closs')

    def btns_disabled(self, status):
        if status == True:
            self.login_btn.setDisabled(False)
        else:
            self.login_btn.setDisabled(True)
        self.add_btn.setDisabled(status)
        self.del_btn.setDisabled(status)
        self.pull_btn.setDisabled(status)
        self.push_btn.setDisabled(status)
        self.refresh_btn.setDisabled(status)
        self.save_btn.setDisabled(status)
        self.convert_btn.setDisabled(status)

    def load(self):
        try:
            self.main_pro.load_key()
            self.main_pro.load_file_data()
            self.all_files.update(self.main_pro.file_list)
            self.all_file_list.extend(list(self.all_files.keys()))
            self.refresh()

        except FileNotFoundError:
            pass

        except Exception as e: 
            print(e)

    def save(self):
        try:
            self.main_pro.file_list.update(self.all_files)
            # print(self.main_pro.file_list)
            self.main_pro.save_file_data()

        except Exception as e: 
            print(e)

    def psuh(self):     
        try:
            selected_it_num = self.all_it.currentRow()
            selected_it_name = self.all_it.currentItem().text()
            self.all_it.takeItem(selected_it_num)
            del self.file_list[self.file_list.index(selected_it_name)]
            self.select_it.clear()

            self.select_list.append(selected_it_name)
            for it in self.select_list:
                self.select_it.addItem(it)

            print('---------------------------------------------------------')
            print(f'select : {self.select_list}')
            print(f'file : {self.file_list}')
            print(f'all file : {self.all_file_list}')

        except Exception as e: 
            print(e)

    def pull(self):
        try:
            selected_it_num = self.select_it.currentRow()
            selected_it_name = self.select_it.currentItem().text()
            self.select_it.takeItem(selected_it_num)
            del self.select_list[self.select_list.index(selected_it_name)]
            self.all_it.clear()

            self.file_list.append(selected_it_name)
            for it in self.file_list:
                self.all_it.addItem(it)

            print('---------------------------------------------------------')
            print(f'select : {self.select_list}')
            print(f'file : {self.file_list}')
            print(f'all file : {self.all_file_list}')

        except Exception as e: 
            print(e)

    def add_list(self):
        try:
            files_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File') 
            data = self.main_pro.encode_cryption(files_path[0])
            filename = files_path[0].split('/')[len(files_path[0].split('/')) - 1]
            if filename in self.all_file_list:
                print('same files')
            
            else:
                self.file_list.append(filename)
                self.all_file_list.append(filename)
                self.all_files[filename] = {'files_path' : files_path[0] ,'data' : data}
                self.all_it.clear()
                for it in self.file_list:
                    self.all_it.addItem(it)

            print('---------------------------------------------------------')
            print(f'select : {self.select_list}')
            print(f'file : {self.file_list}')
            print(f'all file : {self.all_file_list}')
        
        except Exception as e: 
            print(e)

    def del_list(self):
        try:
            selected_it_num = self.all_it.currentRow()
            selected_it_name = self.all_it.currentItem().text()
            self.all_it.takeItem(selected_it_num)
            del self.file_list[self.file_list.index(selected_it_name)]
            del self.all_file_list[self.all_file_list.index(selected_it_name)]

            print('---------------------------------------------------------')
            print(f'select : {self.select_list}')
            print(f'file : {self.file_list}')
            print(f'all file : {self.all_file_list}')

        except Exception as e: 
            print(e)
    
    def refresh(self):

            self.select_it.clear()
            self.all_it.clear()
            for it in self.all_file_list:
                self.all_it.addItem(it)

            self.select_list.clear()
            self.file_list.clear()
            self.file_list.extend(self.all_file_list)

            print('---------------------------------------------------------')
            print(f'select : {self.select_list}')
            print(f'file : {self.file_list}')
            print(f'all file : {self.all_file_list}')

    def convert(self):
        try:
            for file in self.select_list:
                self.main_pro.decode_cryption(file, self.all_files[file]['data'])
            
            self.refresh()
        except Exception as e: 
            print(e)