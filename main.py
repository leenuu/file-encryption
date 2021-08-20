from file_encryption.ui_files.main__ui import Ui_main_widget
from PyQt5 import QtWidgets
import sys
# import win32com.shell.shell as shell

if __name__ == "__main__":
    # pass
    # ASADMIN = 'asadmin'
    # if sys.argv[-1] != ASADMIN:
    #     script = os.path.abspath(sys.argv[0])
    #     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    #     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    #     sys.exit(0)
        
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_main_widget()
    ui.show()
    sys.exit(app.exec_())   
