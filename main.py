from listeners import Listeners
from data import Data
from sad_ui import QtWidgets, Ui_MainWindow
import sys

def updateMonitorsUI(savedMonitors):
    for monitor in savedMonitors:
        if monitor == 'cpu_top_processes':
            ui.cpuTopProcessesCheckBox.setChecked(True)
        elif monitor[:10] == 'cpu_stdout':
            ui.cpuProcessesGroupBox.setChecked(True)
            text = ui.cpuProcessesTextEdit.toPlainText()
            if text == '':
                ui.cpuProcessesTextEdit.setText(monitor[11:])
            else:    
                ui.cpuProcessesTextEdit.setText(text + '\n' + monitor[11:])
        elif monitor == 'errors_top_system_calls_errors':
            ui.errorsTopSystemCallsCheckBox.setChecked(True)
        elif monitor == 'errors_top_system_calls_errors_time':
            ui.errorsSystemCallsTimeCheckBox.setChecked(True)
        elif monitor == 'errors_top_file_errors':
            ui.errorsTopFilesCheckBox.setChecked(True)
        elif monitor == 'errors_top_processes':
            ui.errorsTopProcessesCheckBox.setChecked(True)
        elif monitor[:28] == 'errors_top_failed_file_opens':
            ui.errorsFileOpensGroupBox.setChecked(True)
            text = ui.errorsFileOpensTextEdit.toPlainText()
            if text == '':
                ui.errorsFileOpensTextEdit.setText(monitor[29:])    
            else:
                ui.errorsFileOpensTextEdit.setText(text + '\n' + monitor[29:])
        elif monitor == 'network_top_processes_bandwidth': 
            ui.networkTopProcessesCheckBox.setChecked(True)
        elif monitor == 'network_top_connections_bandwidth': 
            ui.networkTopConnectionsCheckBox.setChecked(True)
        elif monitor[:14] == 'network_spy_ip':
            ui.networkHostsGroupBox.setChecked(True)
            text = ui.networkHostsTextEdit.toPlainText()
            if text == '':
                ui.networkHostsTextEdit.setText(monitor[15:])
            else:
                ui.networkHostsTextEdit.setText(text + '\n' + monitor[15:])
        elif monitor[:32] == 'security_commands_executed_by_id':
            ui.securityLoginShellsGroupBox.setChecked(True)
            text = ui.securityLoginShellsTextEdit.toPlainText()
            if text == '':
                ui.securityLoginShellsTextEdit.setText(monitor[33:])
            else:
                ui.securityLoginShellsTextEdit.setText(text + '\n' + monitor[33:])
        elif monitor[:36] == 'security_directories_visited_by_user':
            ui.securityUserDirectoriesGroupBox.setChecked(True)
            text = ui.securityUserDirectoriesTextEdit.toPlainText()
            if text == '':
                ui.securityUserDirectoriesTextEdit.setText(monitor[37:])
            else:
                ui.securityUserDirectoriesTextEdit.setText(text + '\n' + monitor[37:])
        elif monitor[:22] == 'security_file_opens_at':
            ui.securityFileOpensGroupBox.setChecked(True)
            text = ui.securityFileOpensTextEdit.toPlainText()
            if text == '':
                ui.securityFileOpensTextEdit.setText(monitor[23:])
            else:
                ui.securityFileOpensTextEdit.setText(text + '\n' + monitor[23:])
        elif monitor[:27] == 'application_request_of_type':
            ui.appHTTPGroupBox.setChecked(True)
            text = ui.appHTTPTextEdit.toPlainText()
            if text == '':
                ui.appHTTPTextEdit.setText(monitor[28:])
            else:
                ui.appHTTPTextEdit.setText(text + '\n' + monitor[28:])
        elif monitor[:27] == 'application_queries_of_type':
            ui.appSQLGroupBox.setChecked(True)
            text = ui.appSQLTextEdit.toPlainText()
            if text == '':
                ui.appSQLTextEdit.setText(monitor[28:])
            else:
                ui.appSQLTextEdit.setText(text + '\n' + monitor[28:])

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
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
