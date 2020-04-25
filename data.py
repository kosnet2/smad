from sysdig_commands import SysdigCommands
from collections import deque

# File responsible for handling application data
class Monitor:
	def __init__(self, command, metricType, name):
		self.command = command
		self.metricType = metricType
		self.alerts = []
		self.name = name

# Defines an alert set by the user on a specific Monitor
class Alert:
	def __init__(self, name, monitor, metrics, seconds, filename):
		self.name = name
		self.monitor = monitor
		self.metrics = metrics
		self.seconds = seconds
		self.filename = filename

# Defines a scheduled rule for the detector running using custom rules
class ScheduledRule:
	def __init__(self, start, end, repetitive, active, running):
		self.start = start
		self.end = end
		self.repetitive = repetitive
		self.active = active
		self.running = running

	def __eq__(self, other):
		if not isinstance(other, ScheduledRule):
			return NotImplemented
		return self.start == other.start and \
			   self.end == other.end and \
			   self.repetitive == other.repetitive and \
			   self.active == other.active and \
			   self.running == other.running

class Data:
	def __init__(self):
		self.sysdig_commands = SysdigCommands()
		self.monitors = {}
		self.alerts = []
		self.scheduled_rules = {}
		self.getScheduledRules()

	def getScheduledRules(self):
		try:
			with open('resources/scheduledRules.txt', 'r') as f:
				scheduledRules = f.read().split('\n')
				for line in scheduledRules:
					l = line.split(' ', 1)
					filename = l[0]
					if filename not in self.scheduled_rules:
						self.scheduled_rules[filename] = []
					scheduledRule = l[1].split(' ')

					start = scheduledRule[0]
					end = scheduledRule[1]
					repetitive = True if scheduledRule[2] == 'True' else False
					active = True if scheduledRule[3] == 'True' else False
					running = True if scheduledRule[4] == 'True' else False

					self.scheduled_rules[filename].append(ScheduledRule(start, end, repetitive, active, running))
		except Exception:
			return {}
	
	def saveScheduledRules(self):
		try:
			with open('resources/scheduledRules.txt', 'w') as f:
				for filename in self.scheduled_rules:
					for r in self.scheduled_rules[filename]:
						f.write(f'{filename} {r.start} {r.end} {r.repetitive} {r.active} {r.running}\n')

		except Exception as e:
			print('Caught exception while saving scheduled rules\n', e)

	def addScheduledRule(self, filename, start, end, repetitive, active, running):
		if filename not in self.scheduled_rules:
			self.scheduled_rules[filename] = []
		self.scheduled_rules[filename].append(ScheduledRule(start, end, repetitive, active, running))
	
	def removeScheduledRule(self, filename, index):
		self.scheduled_rules[filename][index].active = False
		self.scheduled_rules[filename].pop(index)

	def getScheduledRulesByFile(self, filename):
		return self.scheduled_rules[filename]

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
		self.monitors[name] = Monitor(commandDict['command'], commandDict['metricType'], name)

		# Add existing alerts to new monitor
		for alert in self.alerts:
			if alert.monitor == name:
				self.monitors[name].alerts.append(alert)

	def addAlert(self, name, monitor, metrics, seconds=0, filename=''):
		alert = Alert(name, monitor, metrics, seconds, filename)
		self.alerts.append(alert)
		self.monitors[monitor].alerts.append(alert)

	def editAlert(self, name, monitor, metrics, seconds, filename):
		index = [alert.name for alert in self.alerts].index(name)
		self.alerts[index].monitor = monitor
		self.alerts[index].metrics = metrics
		self.alerts[index].seconds = seconds
		self.alerts[index].filename = filename

	def removeMonitor(self, name):
		del self.monitors[name]

	def removeAlert(self, name):
		# Remove alert from alerts array
		i = 0
		for alert in self.alerts:
			if alert.name == name:
				del self.alerts[i]
				break
			i += 1

		# Remove alert from every monitor it is assigned to
		for monitor in self.monitors:
			i = 0
			for alert in self.monitors[monitor].alerts:
				if alert.name == name:
					del self.monitors[monitor].alerts[i]
					return
				i += 1
