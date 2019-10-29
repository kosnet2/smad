from sad_ui import *
from listeners import Listeners
import sys

def addAlert(message):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle('Error')
    msg.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    listeners = Listeners(ui)
    
    
    # Example
    # ui.networkStopMonitorPushButton.clicked.connect(lambda: addAlert('Boom'))
    # item = QtWidgets.QListWidgetItem()
    # item.setText('Test')
    # ui.alertsListListWidget.addItem(item)

    # Load data
    
    # Set up listeners
    
    # Utilities
    
    MainWindow.showMaximized()
    sys.exit(app.exec_())