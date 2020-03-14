import threading
import subprocess
import shlex
import os

class FalcoThread(threading.Thread):
	def __init__(self, ui, rules):
		super(FalcoThread, self).__init__()
		self.ui = ui
		self.rules = rules
		self._stop_event = threading.Event()

	def run(self):
		# Create configuration file
		with open('smad_rules/user_generated_rules.yaml', 'w+') as f:
			f.write(self.rules)
		# Start Falco
		process = subprocess.Popen(shlex.split('falco --unbuffered -r /etc/falco/falco_rules.yaml -r smad_rules/user_generated_rules.yaml -o stdout_output.enabled=false -o webserver.enabled=false -o file_output.enabled=true -o file_output.keep_alive=false -o file_output.filename="smad_rules/.falco_events.txt"'))

		while True:
			if self.stopped():
				process.terminate()
				os.wait()
				break
				
	def stop(self):
		self._stop_event.set()

	def stopped(self):
		return self._stop_event.is_set()
