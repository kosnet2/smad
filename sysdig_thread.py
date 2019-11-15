import threading
import subprocess
import shlex
import os

class SysdigThread(threading.Thread):
	def __init__(self, name, monitor):
		super(SysdigThread, self).__init__()
		self.name = name
		self.monitor = monitor
		self._stop_event = threading.Event()

	def run(self):
		process = subprocess.Popen(shlex.split(self.monitor.command), stdout=subprocess.PIPE)
		while True:
			if self.stopped():
				process.kill()
				os.wait()
				break
			output = process.stdout.readline()
			if output == '' and process.poll() is not None:
				break
			if output:
				if self.name == 'cpu_top_processes':
					if len(self.monitor.alerts):
						line = output.strip().decode('utf-8')
						if '%' in line:
							cpu_usage = line[:line.index('%')]
							if (cpu_usage[0].isdigit() and float(cpu_usage) > 2):
								print(line)
			rc = process.poll()

	def stop(self):
		self._stop_event.set()

	def stopped(self):
		return self._stop_event.is_set()
