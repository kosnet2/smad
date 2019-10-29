from sad_ui import *
from listeners import Listeners
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Set up listeners
    listeners = Listeners(ui)
    
    # Load data
       
    # Utilities
    
    MainWindow.showMaximized()
    sys.exit(app.exec_())