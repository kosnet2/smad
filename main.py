from PyQt5.QtCore import QFile, QTextStream
from listeners import Listeners
from smad import QtWidgets, Ui_MainWindow
from data import Data
import stylesheets.breeze_resources
import sys

def updateMonitorsUI(savedMonitors):
    for monitor in savedMonitors:
        if monitor[:17] == 'cpu_top_processes':
            ui.monitorsCpuProcessUsageCheckBox.setChecked(True)
            text = ui.monitorsCpuProcessUsageTextEdit
            if text.toPlainText() == '':
                text.setText(monitor[18:])
            else:
                text.setText(text.toPlainText() + '\n' + monitor[18:])
        elif monitor == 'errors_top_system_calls_errors':
            ui.monitorsSystemCallErrorsCheckBox.setChecked(True)
        elif monitor == 'errors_top_system_calls_errors_time':
            ui.monitorsSystemCallsMostTimeSpentCheckBox.setChecked(True)
        elif monitor == 'errors_top_file_errors':
            ui.monitorsFileIOErrorsCheckBox.setChecked(True)
        elif monitor == 'errors_top_processes':
            ui.monitorsProcessIOErrorsCheckBox.setChecked(True)
        elif monitor == 'errors_files_most_time_spent':
            ui.monitorsFilesMostTimeSpentCheckBox.setChecked(True)
        elif monitor == 'network_top_processes_bandwidth': 
            ui.monitorsProcessBWCheckBox.setChecked(True)
        elif monitor == 'network_top_connections_bandwidth': 
            ui.monitorsNetworkConnectionsBWCheckBox.setChecked(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    file = QFile(":/light.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Load data
    data = Data()

    # Update UI
    updateMonitorsUI(data.getSavedMonitors())

    # Set up listeners
    listeners = Listeners(ui, data)
    
    # Set close event listener
    MainWindow.closeEvent = listeners.stopApplication

    MainWindow.showMaximized()
    sys.exit(app.exec_())
