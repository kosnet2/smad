from PyQt5 import QtCore, QtGui, QtWidgets
from utilities import Utilities as utils

class Listeners:
    def __init__(self, ui):
        self.ui = ui
        self.registerListeners()
    
    
    def registerListeners(self):
        # Monitors Button Listeners
        self.ui.cpuStartMonitorsPushButton.clicked.connect(lambda: self.startProcessMonitors())
        self.ui.cpuStopMonitorPushButton.clicked.connect(lambda: self.stopProcessMonitor())
        self.ui.errorsStartMonitorsPushButton.clicked.connect(lambda: self.startErrorsMonitors())
        self.ui.errorsStopMonitorPushButton.clicked.connect(lambda: self.stopErrorsMonitor())
        self.ui.networkStartMonitorsPushButton.clicked.connect(lambda: self.startNetworkMonitors())
        self.ui.networkStopMonitorPushButton.clicked.connect(lambda: self.stopNetworkMonitor())
        self.ui.securityStartMonitorsPushButton.clicked.connect(lambda: self.startSecurityMonitors())
        self.ui.securityStopMonitorPushButton.clicked.connect(lambda: self.stopSecurityMonitor())
        self.ui.appStartMonitorsPushButton.clicked.connect(lambda: self.startApplicationMonitors())
        self.ui.appStopMonitorPushButton.clicked.connect(lambda: self.stopApplicationMonitor())
        
        # Alerts Button Listeners
        self.ui.alertsAddAlertPushButton.clicked.connect(lambda: self.addAlert())
        self.ui.alertsListDeleteAlert.clicked.connect(lambda: self.deleteAlert())
        
        # Anomalies Button Listeners

    # Alerts
    def addAlert(self):
        # Get alert name, monitor and metrics
        alert = self.ui.alertsAlertNameTextEdit.toPlainText().strip()
        if len(alert) == 0:
            utils.showMessageBox('Alert name field must not be empty', 'Error', QtWidgets.QMessageBox.Critical)
            return
        monitor = self.ui.alertsChooseMonitorComboBox.currentText()
        
        metrics = self.ui.alertsSetMetricsTextEdit.toPlainText().strip()
        # TODO: Need to figure out logic
        if len(metrics) == 0:
            utils.showMessageBox('Metrics field must not be empty', 'Error', QtWidgets.QMessageBox.Critical)
            return

        # Get notifications
        notificationsChecked = any([self.ui.alertsEmailGroupBox.isChecked(),
                                    self.ui.alertsNotifyCheckBox.isChecked()])
    
        if not notificationsChecked:
            utils.showMessageBox('Please select at least one notification field', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        email = ''
        if self.ui.alertsEmailGroupBox.isChecked():
            email = self.ui.alertsEmailTextEdit.toPlainText().strip()
            if len(email) == 0:
                utils.showMessageBox('Email field must not be empty', 'Error', QtWidgets.QMessageBox.Critical)
                return

        notifications = self.ui.alertsNotifyCheckBox.isChecked()
        
        # Get capture details
        captureTime = 0
        captureFilename = ''
        
        if self.ui.alertsCaptureGroupBox.isChecked():
            captureTime = self.ui.alertsCaptureDurationSpinBox.value()
            captureFilename = self.ui.alertsFileNameTextEdit.toPlainText().strip()
            if captureFilename == '':
                utils.showMessageBox('Capture filename field must not be empty', 'Error', QtWidgets.QMessageBox.Critical)
                return

        if self.ui.alertsListListWidget.findItems(alert, QtCore.Qt.MatchExactly):
            utils.showMessageBox('Alert already exists', 'Duplicate alert', QtWidgets.QMessageBox.Critical)
            return
        
        self.ui.alertsListListWidget.addItem(alert)
        utils.showMessageBox('Alert added!', 'Success', QtWidgets.QMessageBox.Information)
        
        # Reset UI
        self.ui.alertsAlertNameTextEdit.setText('')
        self.ui.alertsSetMetricsTextEdit.setText('')
        self.ui.alertsEmailTextEdit.setText('')
        self.ui.alertsFileNameTextEdit.setText('')
        
        # Sysdig
            
    def deleteAlert(self):
        idx = self.ui.alertsListListWidget.currentRow()
        if idx == -1:
            utils.showMessageBox('No alert selected', 'Error', QtWidgets.QMessageBox.Critical)
        
        self.ui.alertsListListWidget.takeItem(idx)
        
        # Sysdig
        
    # Start Monitors
    def startProcessMonitors(self):
        monitorsChecked = any([self.ui.cpuProcessesGroupBox.isChecked(),
                               self.ui.cpuTopProcessesCheckBox.isChecked()])
    
        if not monitorsChecked:
            utils.showMessageBox('Please select at least one monitor', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        monitors = []
        if self.ui.cpuProcessesGroupBox.isChecked():
            text = self.ui.cpuProcessesTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No processes entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            processes = text.split('\n')
            # TODO: Implement naming logic for monitors
            monitors.extend(processes)

        if self.ui.cpuTopProcessesCheckBox.isChecked():
            monitors.append('cpu_top_processes')
        
        for monitor in monitors:
            idx = self.ui.alertsChooseMonitorComboBox.findText(monitor)
            if idx == -1:
                self.ui.alertsChooseMonitorComboBox.addItem(monitor)
                self.ui.cpuRunningMonitorsListWidget.addItem(monitor)
          
        # Start sysdig
        
        utils.showMessageBox('Monitor added!', 'Success', QtWidgets.QMessageBox.Information)
    	
    def startApplicationMonitors(self):
        monitorsChecked = any([self.ui.appHTTPGroupBox.isChecked(),
                               self.ui.appSQLGroupBox.isChecked()])
    
        if not monitorsChecked:
            utils.showMessageBox('Please select at least one monitor', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        monitors = []
        if self.ui.appHTTPGroupBox.isChecked():
            text = self.ui.appHTTPTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No request types entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            requestTypes = text.split('\n')
             # TODO: Implement naming logic for monitors
            monitors.extend(requestTypes)
        
        if self.ui.appSQLGroupBox.isChecked():
            text = self.ui.appSQLTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No query types entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            queryTypes = text.split('\n')
            # TODO: Implement naming logic for monitors
            monitors.extend(queryTypes)
        
        
        for monitor in monitors:
            idx = self.ui.alertsChooseMonitorComboBox.findText(monitor)
            if idx == -1:
                self.ui.alertsChooseMonitorComboBox.addItem(monitor)
                self.ui.appRunningMonitorsListWidget.addItem(monitor)
          
        # Start sysdig
        
        utils.showMessageBox('Monitor added!', 'Success', QtWidgets.QMessageBox.Information)        
    
    def startSecurityMonitors(self):
        monitorsChecked = any([self.ui.securityLoginShellsGroupBox.isChecked(),
                               self.ui.securityUserDirectoriesGroupBox.isChecked(),
                               self.ui.securityFileOpensGroupBox.isChecked()])
    
        if not monitorsChecked:
            utils.showMessageBox('Please select at least one monitor', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        monitors = []
        if self.ui.securityLoginShellsGroupBox.isChecked():
            text = self.ui.securityLoginShellsTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No login shell IDs entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            loginShellIds = text.split('\n')
            # TODO: Implement naming logic for monitors
            monitors.extend(loginShellIds)
        
        if self.ui.securityUserDirectoriesGroupBox.isChecked():
            text = self.ui.securityUserDirectoriesTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No users entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            users = text.split('\n')
             # TODO: Implement naming logic for monitors
            monitors.extend(users)
        
        if self.ui.securityFileOpensGroupBox.isChecked():
            text = self.ui.securityFileOpensTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No directories entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            directories = text.split('\n')
             # TODO: Implement naming logic for monitors
            monitors.extend(directories)
            
        for monitor in monitors:
            idx = self.ui.alertsChooseMonitorComboBox.findText(monitor)
            if idx == -1:
                self.ui.alertsChooseMonitorComboBox.addItem(monitor)
                self.ui.securityRunningMonitorsListWidget.addItem(monitor)
            
        # Start sysdig
        utils.showMessageBox('Monitor added!', 'Success', QtWidgets.QMessageBox.Information)        
    
    def startNetworkMonitors(self):
        monitorsChecked = any([self.ui.networkHostsGroupBox.isChecked(),
                               self.ui.networkTopProcessesCheckBox.isChecked(),
                               self.ui.networkTopClientsCheckBox.isChecked()])
    
        if not monitorsChecked:
            utils.showMessageBox('Please select at least one monitor', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        monitors = []
        if self.ui.networkHostsGroupBox.isChecked():
            text = self.ui.networkHostsTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No hosts entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            hosts = text.split('\n')
             # TODO: Implement naming logic for monitors
            monitors.extend(hosts)
        
        if self.ui.networkTopProcessesCheckBox.isChecked():
            monitors.append('network_top_processes')
            
        if self.ui.networkTopClientsCheckBox.isChecked():
            monitors.append('network_top_client_connections')
        
        for monitor in monitors:
            idx = self.ui.alertsChooseMonitorComboBox.findText(monitor)
            if idx == -1:
                self.ui.alertsChooseMonitorComboBox.addItem(monitor)
                self.ui.networkRunningMonitorsListWidget.addItem(monitor)
          
        # Start sysdig
        utils.showMessageBox('Monitor added!', 'Success', QtWidgets.QMessageBox.Information)            

    def startErrorsMonitors(self):
        monitorsChecked = any([self.ui.errorsProcessesGroupBox.isChecked(),
                               self.ui.errorsTopSystemCallsCheckBox.isChecked(),
                               self.ui.errorsSystemCallsTimeCheckBox.isChecked(),
                               self.ui.errorsTopFilesCheckBox.isChecked(),
                               self.ui.errorsTopProcessesCheckBox.isChecked(),
                               self.ui.errorsFileOpensCheckBox.isChecked(),
                               self.ui.errorsFilesTimeCheckBox.isChecked()])
       
        if not monitorsChecked:
            utils.showMessageBox('Please select at least one monitor', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        monitors = []
        if self.ui.errorsProcessesGroupBox.isChecked():
            text = self.ui.errorsProcessesTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No processes entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            processes = text.split('\n')
            # TODO: Implement naming logic for monitors
            monitors.extend(processes)
        
        if self.ui.errorsTopSystemCallsCheckBox.isChecked():
            monitors.append('errors_most_time_files_cat')
            
        if self.ui.errorsSystemCallsTimeCheckBox.isChecked():
            monitors.append('errors_top_system_calls')
        
        if self.ui.errorsTopFilesCheckBox.isChecked():
            monitors.append('errors_top_files')
        
        if self.ui.errorsTopProcessesCheckBox.isChecked():
            monitors.append('errors_top_processes')
        
        if self.ui.errorsFileOpensCheckBox.isChecked():
            monitors.append('errors_file_opens')
            
        if self.ui.errorsFilesTimeCheckBox.isChecked():
            monitors.append('errors_most_time_files')
            
        for monitor in monitors:
            idx = self.ui.alertsChooseMonitorComboBox.findText(monitor)
            if idx == -1:
                self.ui.alertsChooseMonitorComboBox.addItem(monitor)
                self.ui.errorsRunningMonitorsListWidget.addItem(monitor)
            
        # Start sysdig
        utils.showMessageBox('Monitor added!', 'Success', QtWidgets.QMessageBox.Information)        

    # Stop Monitors
    def stopProcessMonitor(self):
        idx = self.ui.cpuRunningMonitorsListWidget.currentRow()
        if idx == -1:
            utils.showMessageBox('No monitor selected', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        text = self.ui.cpuRunningMonitorsListWidget.currentItem().text()
        self.ui.cpuRunningMonitorsListWidget.takeItem(idx)
        
        cbIdx = self.ui.alertsChooseMonitorComboBox.findText(text)
        self.ui.alertsChooseMonitorComboBox.removeItem(cbIdx)
        
        # Sysdig
    
    def stopApplicationMonitor(self):
        idx = self.ui.appRunningMonitorsListWidget.currentRow()
        if idx == -1:
            utils.showMessageBox('No monitor selected', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        text = self.ui.appRunningMonitorsListWidget.currentItem().text()
        self.ui.appRunningMonitorsListWidget.takeItem(idx)
        
        cbIdx = self.ui.alertsChooseMonitorComboBox.findText(text)
        self.ui.alertsChooseMonitorComboBox.removeItem(cbIdx)
        # Sysdig
        
    def stopSecurityMonitor(self):
        idx = self.ui.securityRunningMonitorsListWidget.currentRow()
        if idx == -1:
            utils.showMessageBox('No monitor selected', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        text = self.ui.securityRunningMonitorsListWidget.currentItem().text() 
        self.ui.securityRunningMonitorsListWidget.takeItem(idx)
        
        cbIdx = self.ui.alertsChooseMonitorComboBox.findText(text)
        self.ui.alertsChooseMonitorComboBox.removeItem(cbIdx)
        
        # Sysdig
        
    def stopNetworkMonitor(self):
        idx = self.ui.networkRunningMonitorsListWidget.currentRow()
        if idx == -1:
            utils.showMessageBox('No monitor selected', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        text = self.ui.networkRunningMonitorsListWidget.currentItem().text() 
        self.ui.networkRunningMonitorsListWidget.takeItem(idx)
        
        cbIdx = self.ui.alertsChooseMonitorComboBox.findText(text)
        self.ui.alertsChooseMonitorComboBox.removeItem(cbIdx)
        
        # Sysdig
        
    def stopErrorsMonitor(self):
        idx = self.ui.errorsRunningMonitorsListWidget.currentRow()
        if idx == -1:
            utils.showMessageBox('No monitor selected', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        text = self.ui.errorsRunningMonitorsListWidget.currentItem().text()
        self.ui.errorsRunningMonitorsListWidget.takeItem(idx)
        
        cbIdx = self.ui.alertsChooseMonitorComboBox.findText(text)
        self.ui.alertsChooseMonitorComboBox.removeItem(cbIdx)
        
        # Sysdig