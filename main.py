from listeners import Listeners
from load_data import LoadData
from sad_ui import *
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Set up listeners
    listeners = Listeners(ui)
    
    # Load data
    data = LoadData(ui)

    # Utilities
    
    MainWindow.showMaximized()
    sys.exit(app.exec_())