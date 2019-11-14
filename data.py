from PyQt5 import QtCore, QtGui, QtWidgets

# Defines an alert set by the user on a specific Monitor
class Alert:
    def __init__(self, name, monitor, metrics, notifications, email, seconds, filename):
        self.name = name
        self.monitor = monitor
        self.metrics = metrics # probably a dictionary
        self.email = email
        self.notifications = notifications
        self.seconds = seconds
        self.filename = filename

# File responsible for handling application data
class Data:
	def __init__(self):
		self.loadData()
		
	def loadData(self):
		self.monitors = {
			'cpu_stdout_cat': []
		}
		self.alerts = []

		for monitor in self.monitors:
			self.alerts.extend(self.monitors[monitor])

	def addMonitor(self, name):
		self.monitors[name] = []

		# Add existing alerts to new monitor
		for alert in self.alerts:
			if alert.monitor == name:
				self.monitors[name].append(alert)

	def addAlert(self, name, monitor, metrics, notifications=False, email='', seconds=0, filename=''):
		alert = Alert(name, monitor, metrics, notifications, email, seconds, filename)
		self.alerts.append(alert)
		self.monitors[monitor].append(alert)

	def removeMonitor(self, name):
		del self.monitors[name]

	def removeAlert(self, name):
		i = 0
		for alert in self.alerts:
			if alert.name == name:
				del self.alerts[i]
				break

		for monitor in self.monitors:
			i = 0
			for alert in self.monitors[monitor]:
				if alert.name == name:
					del self.monitors[monitor][i]
					return
				i += 1
