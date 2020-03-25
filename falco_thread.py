from PyQt5.QtCore import QThread
from threading import Event
from subprocess import Popen
import shlex
import os
from datetime import datetime

class FalcoThread(QThread):
	def __init__(self, ui, rules):
		QThread.__init__(self)
		self.ui = ui
		self.rules = rules
		self.events_file = 'smad_events/'+ datetime.now().strftime("%b_%d_%Y_%H:%M:%S") + '_smad_events.txt' 
		self._stop_event = Event()

	def run(self):
		# Create configuration file
		with open('smad_rules/user_generated_rules.yaml', 'w+') as f:
			f.write(self.rules)
		# Start Falco
		process = Popen(shlex.split('falco --unbuffered -r /etc/falco/falco_rules.yaml -r smad_rules/user_generated_rules.yaml -o stdout_output.enabled=false -o webserver.enabled=false -o file_output.enabled=true -o file_output.keep_alive=false -o file_output.filename="' + self.events_file + '"'))

		while True:
			if self.stopped():
				process.terminate()
				os.wait()
				break

	def stop(self):
		self._stop_event.set()

	def get_events_file(self):
		return self.events_file
		
	def stopped(self):
		return self._stop_event.is_set()
