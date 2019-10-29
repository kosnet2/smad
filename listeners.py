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
        isValid = True
        
        # Get alert name
        alert = self.ui.alertsAlertNameTextEdit.toPlainText()
        if len(alert) == 0:
            isValid = False
        
        # Get chosen monitor
        monitor = self.ui.alertsChooseMonitorComboBox.currentText()
        
        # Get metrics
        metrics = self.ui.alertsSetMetricsTextEdit.toPlainText()
        if len(metrics) == 0:
            isValid = False
        
        # Get notification details
        email = ''
        if self.ui.alertsEmailGroupBox.isChecked():
            email = self.ui.alertsEmailTextEdit.toPlainText()
            if len(email) == 0:
                isValid = False
        notifications = self.ui.alertsNotifyCheckBox.isChecked()
        
        # Get capture details
        captureTime = 0
        captureFilename = ''
        
        if self.ui.alertsCaptureGroupBox.isChecked():
            captureTime = self.ui.alertsCaptureDurationSpinBox.value()
            
            captureFilename = self.ui.alertsFileNameTextEdit.toPlainText()
            if len(captureFilename) == 0:
                isValid = False
        
        if isValid:
            print("add alert is valid")
            # add alert to UI list
            # call sysdig daemons 
            
            
    def deleteAlert(self):
        # UI
        self.listWidget_6.takeItem(self.listWidget_6.currentRow())
        self.displayErrorMessage(message='Oh no!')
        
        
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
