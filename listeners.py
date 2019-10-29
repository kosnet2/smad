from PyQt5 import QtCore, QtGui, QtWidgets
from utilities import Utilities as utils

class Listeners:
    def __init__(self, ui):
        self.ui = ui
        self.registerListeners()
    
    
    def registerListeners(self):
        self.ui.cpuStartMonitorsPushButton.clicked.connect(lambda: self.startProcessMonitor())
        self.ui.alertsAddAlertPushButton.clicked.connect(lambda: self.addAlert())
        self.ui.alertsListDeleteAlert.clicked.connect(lambda: self.deleteAlert())

    # Alerts
    def addAlert(self):
        # UI
        # Get alert name
        alert = self.ui.alertsAlertNameTextEdit.toPlainText()
        if len(alert) == 0:
            utils.showMessageBox("Alert name field must not be empty", "Empty field", QtWidgets.QMessageBox.Critical)
            return
        
        # Get chosen monitor
        monitor = self.ui.alertsChooseMonitorComboBox.currentText()
        
        # Get metrics
        metrics = self.ui.alertsSetMetricsTextEdit.toPlainText()
        if len(metrics) == 0:
            utils.showMessageBox("Metrics field must not be empty", "Empty field", QtWidgets.QMessageBox.Critical)
            return
        
        # Get notification details
        email = ''
        notificationsChecked = self.ui.alertsEmailGroupBox.isChecked() or self.ui.alertsNotifyCheckBox.isChecked()
        if not notificationsChecked:
            utils.showMessageBox("Please select at least one notification field", "Empty field", QtWidgets.QMessageBox.Critical)
            return
        
        if self.ui.alertsEmailGroupBox.isChecked():
            email = self.ui.alertsEmailTextEdit.toPlainText()
            if len(email) == 0:
                utils.showMessageBox("Email field must not be empty", "Empty field", QtWidgets.QMessageBox.Critical)
                return

        notifications = self.ui.alertsNotifyCheckBox.isChecked()
        
        # Get capture details
        captureTime = 0
        captureFilename = ''
        
        if self.ui.alertsCaptureGroupBox.isChecked():
            captureTime = self.ui.alertsCaptureDurationSpinBox.value()
            
            captureFilename = self.ui.alertsFileNameTextEdit.toPlainText()
            if len(captureFilename) == 0:
                utils.showMessageBox("Capture file name field must not be empty", "Empty field", QtWidgets.QMessageBox.Critical)
                return
        
        # Add it to alert list
    
        if self.ui.alertsListListWidget.findItems(alert, QtCore.Qt.MatchExactly):
            utils.showMessageBox("Alert already exists", "Duplicate alert", QtWidgets.QMessageBox.Critical)
            return
        
        self.ui.alertsListListWidget.addItem(alert)
        print("add alert is valid")
        # Daemons
        
        
            
    def deleteAlert(self):
        # UI
        self.ui.alertsListListWidget.takeItem(self.alertsListListWidget.currentRow())
        # Daemons
        
    # Start Monitors
    def startProcessMonitor(self):
        if self.ui.cpuProcessesGroupBox.isChecked():
            text = self.ui.cpuProcessesTextEdit.toPlainText()
            if text == '':
                utils.showMessageBox('No processes entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            processes = text.split('\n')
			# Loop processes and start sysdig

        if self.ui.cpuTopProcessesCheckBox.isChecked():
            a = 1
            # Start sysdig
    	
        
    def startApplicationMonitor(self):
        a = 1
    
    def startSecurityMonitor(self):
        a = 1
        
    def startNetworkMonitor(self):
        a = 1

    def startPerformanceMonitor(self):
        a = 1
    

    # Stop Monitors
    def stopProcessMonitor(self):
        a = 1
        
    def stopApplicationMonitor(self):
        a = 1
    
    def stopSecurityMonitor(self):
        a = 1
        
    def stopNetworkMonitor(self):
        a = 1

    def stopPerformanceMonitor(self):
        a = 1
