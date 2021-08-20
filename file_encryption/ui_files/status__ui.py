from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ok_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.status = 0

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(175, 130)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(50, 90, 75, 23))
        self.ok_btn.setObjectName("ok_btn")
        self.status_line = QtWidgets.QLabel(Dialog)
        self.status_line.setGeometry(QtCore.QRect(20, 10, 141, 61))
        self.status_line.setAlignment(QtCore.Qt.AlignCenter)
        self.status_line.setObjectName("status_line")

        self.ok_btn.clicked.connect(self.ok)

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ok_btn.setText(_translate("Dialog", "ok"))
        self.status_line.setText(_translate("Dialog", "Login Completed"))

    def ok(self):
        self.close()
        
class Ui_fail_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.status = 0

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(175, 130)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(50, 90, 75, 23))
        self.ok_btn.setObjectName("ok_btn")
        self.status_line = QtWidgets.QLabel(Dialog)
        self.status_line.setGeometry(QtCore.QRect(20, 10, 141, 61))
        self.status_line.setAlignment(QtCore.Qt.AlignCenter)
        self.status_line.setObjectName("status_line")

        self.ok_btn.clicked.connect(self.ok)

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ok_btn.setText(_translate("Dialog", "ok"))
        self.status_line.setText(_translate("Dialog", "Login Failed"))

    def ok(self):
        self.close()
