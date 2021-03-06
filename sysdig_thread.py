from sysdig_commands import SysdigCommands
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QThread
from threading import Event, Lock
from collections import deque
import utilities as utils
import sys
import datetime
import subprocess
import select
import shlex
import os
import re
import time
import pyqtgraph as pg

class SysdigThread(QThread):
    def __init__(self, name, monitor, ui):
        QThread.__init__(self)
        self.sysdig_commands = SysdigCommands()
        self.ui = ui
        self.name = name
        self.monitor = monitor
        self._stop_event = Event()
        self.time_dict = {'ps': 10 ** -6, 'ns': 10 ** -3, 'μs': 1, 'us' : 1, 'ms': 10 ** 3, 's': 10 ** 6, 'm': 60 * (10 ** 6)}
        self.size_dict = {'B': 1, 'KB': 2 ** 10, 'MB': 2 ** 20, 'GB': 2 ** 30, 'TB': 2 ** 40, 'PB': 2 ** 50}

        # Visualization
        self.is_plotting = False
        self.timer = QTimer(self)

        self.pens = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
        self.penIndex = 0

    def getValues(self, line):
    	# Get space separated values from a line of output
        res = re.findall(r'[\S]+', line)
        return res if len(res) < 3 else [res[0], ' '.join(res[1:-1]), res[-1]]

    def run(self):
        process = subprocess.Popen(shlex.split(self.monitor.command), stdout=subprocess.PIPE)
        poll_obj = select.poll()
        poll_obj.register(process.stdout, select.POLLIN)   
        while True:
            if self.stopped():
                process.kill()
                os.wait()
                break
            if poll_obj.poll(0): # Check if thread has output
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break

                if output:
                    if self.monitor.metricType == 'none':
                        # Save directly to file if monitor has no metrics
                        filename = self.monitor.name.replace('/', '')
                        with open(f'smad_captures/none-metric-monitors/{filename}', 'ab+') as f:
                            f.write(output)

                            # Check for alerts with capture
                            for alert in self.monitor.alerts:
                                if alert.seconds:
                                    self.capture(alert.seconds, alert.filename)
                    else:
                        line = output.strip().decode('utf-8') # Convert bytes to string
                        if line[0].isdigit() and len(self.monitor.alerts):
                            if self.monitor.metricType == 'number' or self.monitor.metricType == 'percentage':
                                self.checkNumberMetric(self.getValues(line))
                            elif self.monitor.metricType == 'time':
                                self.checkTimeMetric(self.getValues(line))
                            elif self.monitor.metricType == 'size':
                                self.checkSizeMetric(self.getValues(line))

                        # Plotting
                        if line[0].isdigit() and self.is_plotting:
                            values = self.getValues(line)

                            # If new key encountered, create new plot
                            if values[1] not in self.ui.plots:
                                self.addPlot(values[1])

                            self.ui.plotsData[values[1]][0].append(utils.now_timestamp())

                            numValue = re.search('(\d+(?:\.\d+)?)',values[0]).groups()[0]
                            self.ui.plotsData[values[1]][1].append(float(numValue))

            rc = process.poll()

    def stopPlot(self):
        self.timer.stop()
        self.legend.scene().removeItem(self.legend)
        self.is_plotting = False
        self.ui.plotWidget.clear()

    def startPlot(self):
        self.legend = pg.LegendItem((100, 60), (70, 30))
        self.legend.setParentItem(self.ui.plotWidget.graphicsItem())
        self.timer.timeout.connect(self.update)
        self.timer.start(200)
        self.is_plotting = True

    def isPlotting(self):
        return self.is_plotting

    def addPlot(self, param):
        maxlen = 200
        self.ui.plots[param] = self.ui.plotWidget.plot(name=param, pen=pg.mkPen(color=self.pens[self.penIndex]), axisItems={'bottom': utils.TimeAxisItem(orientation='bottom')})
        self.legend.addItem(self.ui.plots[param], param)
        self.penIndex = (self.penIndex + 1) % len(self.pens)
        self.ui.plotsData[param] = [deque(maxlen=maxlen), deque(maxlen=maxlen)]

    def update(self):
        for param in self.ui.plots:
            self.ui.plots[param].setData(x=list(self.ui.plotsData[param][0]), y=list(self.ui.plotsData[param][1]))

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def checkNumberMetric(self, values):
        if self.name.startswith('cpu_top_processes'):
            value, processName, pid = values
            details = f'{value} from process {processName} ({pid})'
            value = float(value[:-1])
        elif self.name == 'errors_top_system_calls_errors':
            value, sysCall = values
            details = f'{value} Errors from syscall {sysCall}'
            value = int(value)
        elif self.name == 'errors_top_file_errors':
            value, filename = values
            details = f'{value} Errors from file {filename}'
            value = int(value)
        elif self.name == 'errors_top_processes':
            value, processName, pid = values
            details = f'{value} errors from process: {processName} ({pid})'
            value = int(value)

        for alert in self.monitor.alerts:
            op, threshold, unit = alert.metrics.split(' ')
            threshold = float(threshold)
            if (op == '<' and value < threshold) or (op == '>' and value > threshold) or (op == '=' and value == threshold):
                self.addNotification(alert, details)
        
    def checkTimeMetric(self, values):
        time, source = values
        if time[-2].isdigit():
            time, timeunit = time[:-1], time[-1:]
        else:
            time, timeunit = time[:-2], time[-2:]
        
        time = float(time) * self.time_dict[timeunit]

        if self.name == 'errors_files_most_time_spent':
            details = f'{time}{timeunit} in file {source}'
        elif self.name == 'errors_top_system_calls_errors_time':
            details = f'{time}{timeunit} in syscall {source}'

        for alert in self.monitor.alerts:
            op, value, unit = alert.metrics.split(' ')
            value = float(value) * self.time_dict[unit]
            if (op == '<' and time < value) or (op == '>' and time > value) or (op == '=' and time == value):
                self.addNotification(alert, details)

    def checkSizeMetric(self, values):
        if len(values) == 2:
            size, arg1 = values
            arg2 = 'unknown'
        else:
            size, arg1, arg2 = values
            
        if size[-1].isdigit():
            size += 'B'
        if size[-2].isdigit():
            size, sizeunit = size[:-1], size[-1:]
        else:
            size, sizeunit = size[:-2], size[-2:]
        
        size = float(size) * self.size_dict[sizeunit]

        if self.name == 'network_top_connections_bandwidth':
            details = f'{size}{sizeunit} from IP {arg2} ({arg1})'
        elif self.name == 'network_top_processes_bandwidth':
            details = f'{size}{sizeunit} from process {arg1} ({arg2})'

        for alert in self.monitor.alerts:
            op, value, unit = alert.metrics.split(' ')
            value = float(value) * self.size_dict[unit]
            if (op == '<' and size < value) or (op == '>' and size > value) or (op == '=' and size == value):
                self.addNotification(alert, details)

    def addNotification(self, alert, details):
        values = [str(datetime.datetime.now()), alert.name, alert.filename, details]

        # Insert blank row
        self.ui.notificationsTableWidget.insertRow(0)

        # Update new row
        for i in range(self.ui.notificationsTableWidget.columnCount()):
            self.ui.notificationsTableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(values[i]))
        if alert.seconds:
            self.capture(alert.seconds, alert.filename)

    def capture(self, seconds, filename):
        command = self.sysdig_commands.getCommand('capture')['command']
        command += f' -M {seconds}'

        # Start sysdig capture in a separate thread
        subprocess.run(args=shlex.split(command), stdout=open(f'smad_captures/{filename}', 'a+'))
