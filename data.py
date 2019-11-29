from sysdig_commands import SysdigCommands

# File responsible for handling application data
class Monitor:
	def __init__(self, command, metricType):
		self.command = command
		self.metricType = metricType
		self.alerts = []

# Defines an alert set by the user on a specific Monitor
class Alert:
    def __init__(self, name, monitor, metrics, notifications, email, seconds, filename):
        self.name = name
        self.monitor = monitor
        self.metrics = metrics
        self.email = email
        self.notifications = notifications
        self.seconds = seconds
        self.filename = filename

class Data:
	def __init__(self):
		self.sysdig_commands = SysdigCommands()
		self.monitors = {}
		self.alerts = []
		
	def saveData(self):
		# Save monitors to file
		with open('resources/monitors.txt', 'w+') as f:
			f.write('\n'.join([monitor for monitor in self.monitors]))

	def getSavedMonitors(self):
		try:
			with open('resources/monitors.txt', 'r') as f:
				monitors = f.read().split('\n') 
				return monitors[1:] if monitors[0] == '' else monitors
		except Exception:
			return []

	def getAlert(self, name):
		for alert in self.alerts:
			if alert.name == name:
				return alert

	def addMonitor(self, name):
		commandDict = self.sysdig_commands.getCommand(name)
		monitor = Monitor(commandDict['command'], commandDict['metricType'])
		self.monitors[name] = monitor

		# Add existing alerts to new monitor
		for alert in self.alerts:
			if alert.monitor == name:
				self.monitors[name].alerts.append(alert)

	def addAlert(self, name, monitor, metrics, notifications=False, email='', seconds=0, filename=''):
		alert = Alert(name, monitor, metrics, notifications, email, seconds, filename)
		self.alerts.append(alert)
		self.monitors[monitor].append(alert)

	def editAlert(self, name, monitor, metrics, notifications, email, seconds, filename):
		index = [alert.name for alert in self.alerts].index(name)
		self.alerts[index].monitor = monitor
		self.alerts[index].metrics = metrics
		self.alerts[index].notifications = notifications
		self.alerts[index].email = email
		self.alerts[index].seconds = seconds
		self.alerts[index].filename = filename

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
