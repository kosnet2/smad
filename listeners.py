from PyQt5 import QtCore, QtGui, QtWidgets
from utilities import Utilities as utils
from sysdig_thread import SysdigThread

class Listeners:
    def __init__(self, ui, data):
        self.ui = ui
        self.data = data
        self.registerListeners()
        self.threads = {}
    
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
        self.ui.alertsSaveAlertPushButton.clicked.connect(lambda: self.saveAlert())
        self.ui.alertsDeleteAlertPushButton.clicked.connect(lambda: self.deleteAlert())
        self.ui.alertsEditAlertPushButton.clicked.connect(lambda: self.editAlert())

        # Anomalies Button Listeners

    # Alerts
    def saveAlert(self):
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
            self.data.editAlert(alert, monitor, metrics, notifications, email, captureTime, captureFilename)
            utils.showMessageBox('Alert has been edited!', 'Success', QtWidgets.QMessageBox.Information)
        else:
            self.ui.alertsListListWidget.addItem(alert)
            self.data.addAlert(alert, monitor, metrics, notifications, email, captureTime, captureFilename)
            utils.showMessageBox('Alert has been added!', 'Success', QtWidgets.QMessageBox.Information)
        
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
            return
        
        self.data.removeAlert(self.ui.alertsListListWidget.currentItem().text())
        self.ui.alertsListListWidget.takeItem(idx)

        utils.showMessageBox('Alert removed!', 'Success', QtWidgets.QMessageBox.Information)
        
    def editAlert(self):
        idx = self.ui.alertsListListWidget.currentRow()
        if idx == -1:
            utils.showMessageBox('No alert selected', 'Error', QtWidgets.QMessageBox.Critical)
            return

        # Get alert by name
        alert = self.data.getAlert(self.ui.alertsListListWidget.currentItem().text())

        # Update UI with alert details
        self.ui.alertsAlertNameTextEdit.setText(alert.name)
        index = self.ui.alertsChooseMonitorComboBox.findText(alert.monitor, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ui.alertsChooseMonitorComboBox.setCurrentIndex(index)
        self.ui.alertsSetMetricsTextEdit.setText(alert.metrics)
        self.ui.alertsNotifyCheckBox.setChecked(alert.notifications)
        if alert.email != '':
            self.ui.alertsEmailGroupBox.setChecked(True)
            self.ui.alertsEmailTextEdit.setText(alert.email)
        else:
            self.ui.alertsEmailGroupBox.setChecked(False)
        if alert.seconds > 0:
            self.ui.alertsCaptureGroupBox.setChecked(True)
            self.ui.alertsCaptureDurationSpinBox.setValue(alert.seconds)
            self.ui.alertsFileNameTextEdit.setText(alert.filename)
        else:
            self.ui.alertsCaptureGroupBox.setChecked(False)

    # Start Monitors
    def startProcessMonitors(self):
        monitorsChecked = any([self.ui.cpuProcessesGroupBox.isChecked(),
                               self.ui.cpuTopProcessesCheckBox.isChecked()])
    
        if not monitorsChecked:
            utils.showMessageBox('Please select at least one monitor', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        monitors = []
        invalidMonitors = []
        if self.ui.cpuProcessesGroupBox.isChecked():
            text = self.ui.cpuProcessesTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No processes entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            mntrs = utils.getValidMonitors(text, 'cpu_stdout_', 'process')
            monitors.extend(mntrs[0])
            invalidMonitors.extend(mntrs[1])

        if self.ui.cpuTopProcessesCheckBox.isChecked():
            monitors.append('cpu_top_processes')
        
        self.startSysdig(monitors, self.ui.cpuRunningMonitorsListWidget)
        
        self.displayMonitorStatus(monitors, invalidMonitors)
        
        # Reset form
        self.ui.cpuProcessesTextEdit.setPlainText('')
            
    def startApplicationMonitors(self):
        monitorsChecked = any([self.ui.appHTTPGroupBox.isChecked(),
                               self.ui.appSQLGroupBox.isChecked()])
    
        if not monitorsChecked:
            utils.showMessageBox('Please select at least one monitor', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        monitors = []
        invalidMonitors = []
        if self.ui.appHTTPGroupBox.isChecked():
            text = self.ui.appHTTPTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No request types entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            mntrs = utils.getValidMonitors(text, 'application_request_of_type_', 'request')
            monitors.extend(mntrs[0])
            invalidMonitors.extend(mntrs[1])
        
        if self.ui.appSQLGroupBox.isChecked():
            text = self.ui.appSQLTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No query types entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            mntrs = utils.getValidMonitors(text, 'application_queries_of_type_', 'query')
            monitors.extend(mntrs[0])
            invalidMonitors.extend(mntrs[1])
        
        self.startSysdig(monitors, self.ui.appRunningMonitorsListWidget)
        
        self.displayMonitorStatus(monitors, invalidMonitors)       
        
        # Reset form
        self.ui.appHTTPTextEdit.setPlainText('')
        self.ui.appSQLTextEdit.setPlainText('')

    def startSecurityMonitors(self):
        monitorsChecked = any([self.ui.securityLoginShellsGroupBox.isChecked(),
                               self.ui.securityUserDirectoriesGroupBox.isChecked(),
                               self.ui.securityFileOpensGroupBox.isChecked()])
    
        if not monitorsChecked:
            utils.showMessageBox('Please select at least one monitor', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        monitors = []
        invalidMonitors = []
        if self.ui.securityLoginShellsGroupBox.isChecked():
            text = self.ui.securityLoginShellsTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No login shell IDs entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            mntrs = utils.getValidMonitors(text, 'security_commands_executed_by_id_', 'shellid') 
            monitors.extend(mntrs[0])
            invalidMonitors.extend(mntrs[1])
        
        if self.ui.securityUserDirectoriesGroupBox.isChecked():
            text = self.ui.securityUserDirectoriesTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No users entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            mntrs = utils.getValidMonitors(text, 'security_directories_visited_by_user_', 'user')
            monitors.extend(mntrs[0])
            invalidMonitors.extend(mntrs[1])
        
        if self.ui.securityFileOpensGroupBox.isChecked():
            text = self.ui.securityFileOpensTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No directories entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            mntrs = utils.getValidMonitors(text, 'security_file_opens_at_', 'dir')
            monitors.extend(mntrs[0])
            invalidMonitors.extend(mntrs[1])
        
        self.startSysdig(monitors, self.ui.securityRunningMonitorsListWidget)
        
        self.displayMonitorStatus(monitors, invalidMonitors)

        # Reset form
        self.ui.securityLoginShellsTextEdit.setPlainText('')
        self.ui.securityUserDirectoriesTextEdit.setPlainText('')
        self.ui.securityFileOpensTextEdit.setPlainText('')
    
    def startNetworkMonitors(self):
        monitorsChecked = any([self.ui.networkHostsGroupBox.isChecked(),
                               self.ui.networkTopProcessesCheckBox.isChecked(),
                               self.ui.networkTopConnectionsCheckBox.isChecked()])
    
        if not monitorsChecked:
            utils.showMessageBox('Please select at least one monitor', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        monitors = []
        invalidMonitors = []
        if self.ui.networkHostsGroupBox.isChecked():
            text = self.ui.networkHostsTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No hosts entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            mntrs = utils.getValidMonitors(text, 'network_spy_ip_', 'ip')
            monitors.extend(mntrs[0])
            invalidMonitors.extend(mntrs[1])
        
        if self.ui.networkTopProcessesCheckBox.isChecked():
            monitors.append('network_top_processes_bandwidth')
            
        if self.ui.networkTopConnectionsCheckBox.isChecked():
            monitors.append('network_top_connections_bandwidth')
        
        self.startSysdig(monitors, self.ui.networkRunningMonitorsListWidget)
        
        self.displayMonitorStatus(monitors, invalidMonitors)
        
        # Reset form
        self.ui.networkHostsTextEdit.setPlainText('')
        
    def startErrorsMonitors(self):
        monitorsChecked = any([self.ui.errorsFileOpensGroupBox.isChecked(),
                               self.ui.errorsTopSystemCallsCheckBox.isChecked(),
                               self.ui.errorsSystemCallsTimeCheckBox.isChecked(),
                               self.ui.errorsTopFilesCheckBox.isChecked(),
                               self.ui.errorsTopProcessesCheckBox.isChecked(),
                               self.ui.errorsFilesTimeCheckBox.isChecked()])
       
        if not monitorsChecked:
            utils.showMessageBox('Please select at least one monitor', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        monitors = []
        invalidMonitors = []
        if self.ui.errorsFileOpensGroupBox.isChecked():
            text = self.ui.errorsFileOpensTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No processes entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            mntrs = utils.getValidMonitors(text, 'errors_top_failed_file_opens_', 'process')
            monitors.extend(mntrs[0])
            invalidMonitors.extend(mntrs[1])
        
        if self.ui.errorsTopSystemCallsCheckBox.isChecked():
            monitors.append('errors_top_system_calls_errors')
            
        if self.ui.errorsSystemCallsTimeCheckBox.isChecked():
            monitors.append('errors_top_system_calls_errors_time')
        
        if self.ui.errorsTopFilesCheckBox.isChecked():
            monitors.append('errors_top_file_errors')
        
        if self.ui.errorsTopProcessesCheckBox.isChecked():
            monitors.append('errors_top_processes')
  
        if self.ui.errorsFilesTimeCheckBox.isChecked():
            monitors.append('errors_files_most_time_spent')

        self.startSysdig(monitors, self.ui.errorsRunningMonitorsListWidget)

        self.displayMonitorStatus(monitors, invalidMonitors)
        
        # Reset form
        self.ui.errorsFileOpensTextEdit.setPlainText('')

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
        self.threads[text].stop()
        self.threads[text].join()
        del self.threads[text]

        self.data.removeMonitor(text)

        utils.showMessageBox('Monitor stopped!', 'Success', QtWidgets.QMessageBox.Information)
    
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
        
        
    # Sysdig stuff here
    def startSysdig(self, monitors, listWidget):
        for name in monitors:
            if name not in self.data.monitors:
                self.data.addMonitor(name)
                monitor = self.data.monitors[name]
                
                # Start sysdig
                self.threads[name] = SysdigThread(name, monitor)
                self.threads[name].start()
                
                self.ui.alertsChooseMonitorComboBox.addItem(name)
                listWidget.addItem(name)
                
    def displayMonitorStatus(self, monitors, invalidMonitors):
        if len(invalidMonitors) != 0:
            utils.showMessageBox('These monitors contain errors:\n\n--> '+ '\n--> '.join(invalidMonitors) +'\n\nConsult the docs for further info.','Warning', QtWidgets.QMessageBox.Warning)
        if len(monitors) != 0:    
            utils.showMessageBox('Monitors started:\n\n--> ' + '\n--> '.join(monitors), 'Success', QtWidgets.QMessageBox.Information)
        else:
            utils.showMessageBox('No monitors started!', 'Error', QtWidgets.QMessageBox.Critical)