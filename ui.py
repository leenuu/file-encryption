from main__ui import Ui_main_widget
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_main_widget()
    ui.show()
    sys.exit(app.exec_())   