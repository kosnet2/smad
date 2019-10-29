class Listeners:
	def __init__(self, ui):
		self.ui = ui
		self.registerListeners()

	def registerListeners(self):
		self.ui.cpuStartMonitorsPushButton.clicked.connect(lambda: startProcessMonitor())

    # Alerts
    def addAlert(self):
        if(self.groupBox_22.isChecked()==True):
            self.listWidget_6.addItem(self.generateQListItem("autogenerated Item"))
            self.textEdit_10.setText("added@email.com")
            self.displayInformationMessage('Something you didnt know man!')
            
    def deleteAlert(self):
        # UI
        self.listWidget_6.takeItem(self.listWidget_6.currentRow())
        self.displayErrorMessage(message='Oh no!')
        
        
    # Start Monitors
    def startProcessMonitor(self):
    	a = 1
        
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
