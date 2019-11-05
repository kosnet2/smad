from PyQt5 import QtCore, QtGui, QtWidgets

class LoadData:
	def __init__(self, ui):
		self.ui = ui
		self.getMonitors()
		self.getAlerts()
		
	def getMonitors(self):
		self.monitors = ['cpu_stdout_cat', 'cpu_top_processes', 'errors_most_time_files_cat', 'errors_top_system_calls', 'errors_top_processes', 'network_top_processes', 'security_user_directories_root', 'app_http_requests']
		for monitor in self.monitors:
			monitorType = monitor[:monitor.index('_')]
			
			self.ui.alertsChooseMonitorComboBox.addItem(monitor)

			if monitorType == 'cpu':
				self.ui.cpuRunningMonitorsListWidget.addItem(monitor)
			elif monitorType == 'errors':
				self.ui.errorsRunningMonitorsListWidget.addItem(monitor)
			elif monitorType == 'network':
				self.ui.networkRunningMonitorsListWidget.addItem(monitor)
			elif monitorType == 'security':
				self.ui.securityRunningMonitorsListWidget.addItem(monitor)
			elif monitorType == 'app':
				self.ui.appRunningMonitorsListWidget.addItem(monitor)

	def getAlerts(self):
		self.alerts = ['alert_1', 'alert_2', 'alert_3', 'alert_4']
		self.ui.alertsListListWidget.addItems(self.alerts)
