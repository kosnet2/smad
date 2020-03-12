from PyQt5 import QtWidgets
import datetime
import threading
import subprocess
import select
import shlex
import os
import signal
# import re
import time

class FalcoThread(threading.Thread):
	def __init__(self, ui, rules):
		super(FalcoThread, self).__init__()
		self.ui = ui
		self.rules = rules
		self._stop_event = threading.Event()

	def run(self):
		# Create configuration file
		with open('smad_rules/auto_generated_rules.smadconf', 'w+') as f:
			f.write(self.rules)
		# Start Falco
		process = subprocess.Popen(shlex.split('falco -U -r smad_rules/auto_generated_rules.smadconf'), stdout=subprocess.PIPE)
		poll_obj = select.poll()
		poll_obj.register(process.stdout, select.POLLIN)

		while True:
			if self.stopped():
				process.terminate()
				os.wait()
				break
			if poll_obj.poll(0):
				output = process.stdout.readline()
				if output == b'' and process.poll() is not None:
					break
				if output:
					print(output)

	def stop(self):
		self._stop_event.set()

	def stopped(self):
		return self._stop_event.is_set()

	def addNotification(self, alert, details):
		values = [str(datetime.datetime.now()), alert.name, alert.filename, details]
		self.ui.notificationsTableWidget.insertRow(0)
		for i in range(self.ui.notificationsTableWidget.columnCount()):
			self.ui.notificationsTableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(values[i]))
