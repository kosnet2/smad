from PyQt5.QtCore import QFileSystemWatcher, QObject, pyqtSlot, QThread
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QColor
import threading
import os
import subprocess
import datetime

class Event():
	def __init__(self, datetime, details):
		self.datetime = datetime
		self.details = details
		# For now these are the default settings for the below
		self.title = 'Anomaly Detector Event'
		self.filename=''

class FileWatcher(QObject):
	def __init__(self, ui, path):
		QObject.__init__(self)
		self._watcher = QFileSystemWatcher()
		self.ui = ui
		self._path = path
		self.set_watcher_path(self._path)

	def enable(self):
		self._watcher.fileChanged.connect(self._onFileChanged)

	def disable(self):
		self._watcher.fileChanged.disconnect(self._onFileChanged)

	def set_watcher_path(self, path):
		if self._watcher.files():
			self._watcher.removePaths(self._watcher.files())
		if path is not None and os.path.isfile(path):
			self._watcher.addPath(path)
		self._path = path

	@pyqtSlot()
	def _onFileChanged(self):
		if os.path.exists(self._path):
			# Get last line
			line = self.last_insert(self._path).decode('utf-8')[:-1]

			# Split datetime and event output and raise an event
			line = line.split(' ', 1)
			event = Event(str(datetime.datetime.now()), line[1])
			self.addNotification(event)

	def last_insert(self, path):
		return subprocess.check_output(['tail', '-1', path])

	def addNotification(self, event):
		def eventColor(details):
			if details.startswith('Warning'):
				return QColor(192, 192, 192)
			elif details.startswith('Error'):
				return QColor(255, 204, 204)
			elif details.startswith('Notice'):
				return QColor(255, 204, 229)
			elif details.startswith('Emergency'):
				return QColor(255, 102, 102)
			elif details.startswith('Informational'):
				return QColor(255, 229, 204)
			else:
				return QColor(255, 255, 255)
		values = [event.datetime, event.title, event.filename, event.details]
		self.ui.notificationsTableWidget.insertRow(0)
		for i in range(self.ui.notificationsTableWidget.columnCount()):
			rowItem = QTableWidgetItem(values[i])
			rowItem.setBackground(eventColor(event.details))
			self.ui.notificationsTableWidget.setItem(0, i, rowItem)

class FileWatcherThread(QThread):
	def __init__(self, ui, path):
		QThread.__init__(self)
		super(FileWatcherThread, self).__init__()
		self._file_watcher = FileWatcher(ui, path)

	def run(self):
		self._file_watcher.enable()

	def stop(self):
		self._file_watcher.disable()
