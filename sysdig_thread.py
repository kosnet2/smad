import threading
import subprocess
import shlex
import os

class SysdigThread(threading.Thread):
	def __init__(self, name, command):
		super(SysdigThread, self).__init__()
		self.name = name
		self.command = command
		self._stop_event = threading.Event()

	def run(self):
		process = subprocess.Popen(shlex.split(self.command), stdout=subprocess.PIPE)
		while True:
			if self.stopped():
				process.kill()
				os.wait()
				break
			output = process.stdout.readline()
			if output == '' and process.poll() is not None:
				break
			if output:
				print(output.strip())
			rc = process.poll()

	def stop(self):
		self._stop_event.set()

	def stopped(self):
		return self._stop_event.is_set()
