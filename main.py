from listeners import Listeners
from data import Data
from sad_ui import *
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Load data
    data = Data()
    
    # Update UI
    ui.alertsListListWidget.addItems(data.alerts)

    for monitor in data.monitors:
        monitorType = monitor[:monitor.index('_')]
        
        ui.alertsChooseMonitorComboBox.addItem(monitor)

        if monitorType == 'cpu':
            ui.cpuRunningMonitorsListWidget.addItem(monitor)
        elif monitorType == 'errors':
            ui.errorsRunningMonitorsListWidget.addItem(monitor)
        elif monitorType == 'network':
            ui.networkRunningMonitorsListWidget.addItem(monitor)
        elif monitorType == 'security':
            ui.securityRunningMonitorsListWidget.addItem(monitor)
        elif monitorType == 'app':
            ui.appRunningMonitorsListWidget.addItem(monitor)

    # Set up listeners
    listeners = Listeners(ui, data)

    MainWindow.showMaximized()
    sys.exit(app.exec_())