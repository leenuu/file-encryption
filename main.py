import ui_files
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
# import win32com.shell.shell as shell

if __name__ == "__main__":
    # ASADMIN = 'asadmin'
    # if sys.argv[-1] != ASADMIN:
    #     script = os.path.abspath(sys.argv[0])
    #     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    #     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    #     sys.exit(0)
        
    app = QtWidgets.QApplication(sys.argv)
    ui = ui_files.Ui_main_widget()
    ui.show()
    sys.exit(app.exec_())   
