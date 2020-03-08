# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from sysdig_thread import SysdigThread
import utilities as utils
from pyqtgraph import PlotWidget, plot
from random import randint

""" PLOTTING """
import sys
import numpy as np
import datetime
from PyQt5.QtCore import QTime, QTimer
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from collections import deque
import pytz

""" FALCO """
from falco_rules import FalcoRules
from falco_thread import FalcoThread

UNIX_EPOCH = datetime.datetime(1970, 1, 1, 0, 0)

def now_timestamp():
    return(int((datetime.datetime.now() - UNIX_EPOCH).total_seconds() * 1e6))

def int2dt(ts):
    return(datetime.datetime.utcfromtimestamp(float(ts)/1e6))

class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def tickStrings(self, values, scale, spacing):
        return [int2dt(value).strftime("%H:%M:%S") for value in values]

class FileDialog(QWidget):
    def __init__(self, type):
        super().__init__()
        self.title = 'Allo'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.type = type
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        if self.type == 'load_file':
            self.loadFileDialog()
        elif self.type == 'save_file':
            self.saveFileDialog()
        self.show()
    
    def loadFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "Load Anomaly Rules", "","SMAD configuration files (*.smadconf);;Text Files (*.txt)", options=options)
        if filename:
            # Do stuff here to load the file rules
            print(filename)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self,"Export Anomaly Rules","","SMAD configuration files (*.smadconf);;Text Files (*.txt)", options=options)
        if filename:
            # Do stuff here to export the file rules
            print(filename)


class Listeners:
    def __init__(self, ui, data):
        self.ui = ui
        self.data = data
        self.registerListeners()
        self.threads = {}
    
    def stopApplication(self, event):
		# Save monitors to file
        with open('resources/monitors.txt', 'w+') as f:
            f.write('\n'.join([monitor for monitor in self.data.monitors]))

        # Stop current threads
        for thread in self.threads:
            print(thread, 'is stopping from UI close event')
            self.threads[thread].stop()
            self.threads[thread].join()


    def registerListeners(self):
        # Monitors Button Listeners
        self.ui.monitorsStartMonitors.clicked.connect(lambda: self.startMonitors())
        self.ui.monitorsStopMonitorButton.clicked.connect(lambda: self.stopMonitor())
        self.ui.monitorsPlotMonitorButton.clicked.connect(lambda: self.visualizeMonitor())
        # Alerts Button Listeners
        self.ui.alertsSaveAlertPushButton.clicked.connect(lambda: self.saveAlert())
        self.ui.alertsDeleteAlertPushButton.clicked.connect(lambda: self.deleteAlert())
        self.ui.alertsEditAlertPushButton.clicked.connect(lambda: self.editAlert())
        self.ui.alertsChooseMonitorComboBox.currentIndexChanged.connect(lambda: self.enableMetrics())

        # Anomalies Button Listeners
        self.ui.anomaliesLoadRulesButton.clicked.connect(lambda: self.loadAnomalyRules())
        self.ui.anomaliesExportRulesButton.clicked.connect(lambda: self.exportAnomalyRules())
        self.ui.anomaliesDeployAnomalyDetectorButton.clicked.connect(lambda: self.deployAnomalyDetector())
    """""""""""""""
        ANOMALIES
    """""""""""""""
    def loadAnomalyRules(self):
        dialog = FileDialog('load_file')

    def exportAnomalyRules(self):
        dialog = FileDialog('save_file')

    def deployAnomalyDetector(self):
        # Read separate lines for all the text and checkbox fields
        # Should be the same idea as monitor loading functionalities
        rules = []
        invalidRules = []

        text = self.ui.anomaliesProgramExecutedTextEdit.toPlainText().strip()
        _rules = utils.getValidRules(text, 'program_executed_', 'process')
        
        rules.extend(_rules[0])
        invalidRules.extend(_rules[1])

        text = self.ui.anomaliesDirectoryFileOpensTextEdit.toPlainText().strip()
        _rules = utils.getValidRules(text, 'directory_file_open_', 'dir')

        rules.extend(_rules[0])
        invalidRules.extend(_rules[1])
        
        text = self.ui.anomaliesProcessFileOpensTextEdit.toPlainText().strip()
        _rules = utils.getValidRules(text, 'process_file_open_', 'process')

        rules.extend(_rules[0])
        invalidRules.extend(_rules[1])

        text = self.ui.anomaliesKnownUsersTextEdit.toPlainText().strip()
        _rules = utils.getValidRules(text, 'known_users_', 'user')

        rules.extend(_rules[0])
        invalidRules.extend(_rules[1])

        text = self.ui.anomalieUnknownUsersTextEdit.toPlainText().strip()
        _rules = utils.getValidRules(text, 'unknown_users_', 'user')

        rules.extend(_rules[0])
        invalidRules.extend(_rules[1])

        text = self.ui.anomaliesInboundIPTextEdit.toPlainText().strip()
        _rules = utils.getValidRules(text, 'inbound_ip_traffic_', 'ip')
        
        rules.extend(_rules[0])
        invalidRules.extend(_rules[1])
        
        text = self.ui.anomaliesOutboundIPTextEdit.toPlainText().strip()
        _rules = utils.getValidRules(text, 'outbound_ip_traffic_', 'ip')
        
        rules.extend(_rules[0])
        invalidRules.extend(_rules[1])
        
        text = self.ui.anomaliesMaliciousIPTextEdit.toPlainText().strip()
        _rules = utils.getValidRules(text, 'malicious_traffic_', 'ip')
        
        rules.extend(_rules[0])
        invalidRules.extend(_rules[1])

        if self.ui.anomaliesMongoDBCheckBox.isChecked():
            rules.append('inbound_mongodb_traffic')
        if self.ui.anomaliesHTTPCheckBox.isChecked():
            rules.append('inbound_http_traffic')
        if self.ui.anomaliesMySQLCheckBox.isChecked():
            rules.append('inbound_mysql_traffic')
        if self.ui.anomaliesKafkaCheckBox.isChecked():
            rules.append('inbound_kafka_traffic')
        
        # Create the falco configuration file
        # Start falco instance
        self.startFalco(rules)

        # self.startSysdig(monitors, self.ui.monitorsRunningMonitorsListWidget)

        # Display monitor Status
        self.displayRuleStatus(rules, invalidRules)
    
    """""""""""""""
        ALERTS
    """""""""""""""
    def enableMetrics(self):
        # Reset metrics before proceeding
        self.ui.alertsMetricUnitComboBox.clear()
        self.ui.alertsMetricValueSpinBox.setValue(0)
        self.ui.alertsMetricUnitComboBox.setEnabled(True)
        self.ui.alertsMetricValueSpinBox.setMinimum(0)
        self.ui.alertsMetricValueSpinBox.setMaximum(2147483647)
        
        monitor = self.ui.alertsChooseMonitorComboBox.currentText()
        if monitor != '':
            metricType = self.data.monitors[monitor].metricType
            
            if metricType == 'none':
                self.ui.alertsSetMetricWidget.setEnabled(False)
            else:
                self.ui.alertsSetMetricWidget.setEnabled(True)
    
                if metricType == 'percentage':
                    self.ui.alertsMetricValueSpinBox.setMaximum(100)
                    self.ui.alertsMetricUnitComboBox.addItem('%')
                elif metricType == 'time':
                    self.ui.alertsMetricUnitComboBox.addItem('s')
                    self.ui.alertsMetricUnitComboBox.addItem('ms')
                    self.ui.alertsMetricUnitComboBox.addItem('μs')
                    self.ui.alertsMetricUnitComboBox.addItem('m')
                elif metricType == 'number':
                    self.ui.alertsMetricUnitComboBox.addItem('Errors')
                elif metricType == 'size':
                    self.ui.alertsMetricUnitComboBox.addItem('B')
                    self.ui.alertsMetricUnitComboBox.addItem('KB')
                    self.ui.alertsMetricUnitComboBox.addItem('MB')
                    self.ui.alertsMetricUnitComboBox.addItem('GB')
    
    def saveAlert(self):
        # Get alert name, monitor and metrics
        alert = self.ui.alertsAlertNameTextEdit.toPlainText().strip()
        if len(alert) == 0:
            utils.showMessageBox('Alert name field must not be empty', 'Error', QtWidgets.QMessageBox.Critical)
            return
        monitor = self.ui.alertsChooseMonitorComboBox.currentText()

        metrics = ''
        if self.ui.alertsSetMetricWidget.isEnabled():
            metrics += self.ui.alertsMetricOperationComboBox.currentText() + ' '
            metrics += str(self.ui.alertsMetricValueSpinBox.value()) + ' '
            metrics += self.ui.alertsMetricUnitComboBox.currentText()
        
        # Get capture details
        captureTime = 0
        captureFilename = ''
        
        if self.ui.alertsCaptureGroupBox.isChecked():
            captureTime = self.ui.alertsCaptureDurationSpinBox.value()
            captureFilename = self.ui.alertsFileNameTextEdit.toPlainText().strip()
            if captureFilename == '':
                utils.showMessageBox('Capture filename field must not be empty', 'Error', QtWidgets.QMessageBox.Critical)
                return

        if self.ui.alertsListListWidget.findItems(alert, QtCore.Qt.MatchExactly):
            self.data.editAlert(alert, monitor, metrics, captureTime, captureFilename)
            utils.showMessageBox('Alert has been edited!', 'Success', QtWidgets.QMessageBox.Information)
        else:
            self.ui.alertsListListWidget.addItem(alert)
            self.data.addAlert(alert, monitor, metrics, captureTime, captureFilename)
            utils.showMessageBox('Alert has been added!', 'Success', QtWidgets.QMessageBox.Information)
        
        # Reset UI
        self.ui.alertsAlertNameTextEdit.setText('')
        self.ui.alertsFileNameTextEdit.setText('')
            
    def deleteAlert(self):
        idx = self.ui.alertsListListWidget.currentRow()
        if idx == -1:
            utils.showMessageBox('No alert selected', 'Error', QtWidgets.QMessageBox.Critical)
            return
        
        self.data.removeAlert(self.ui.alertsListListWidget.currentItem().text())
        self.ui.alertsListListWidget.takeItem(idx)

        utils.showMessageBox('Alert removed!', 'Success', QtWidgets.QMessageBox.Information)
    
    # TODO: There is a bug somewhere here
    def editAlert(self):
        idx = self.ui.alertsListListWidget.currentRow()
        if idx == -1:
            utils.showMessageBox('No alert selected', 'Error', QtWidgets.QMessageBox.Critical)
            return

        # Get alert by name
        alert = self.data.getAlert(self.ui.alertsListListWidget.currentItem().text())

        # Update UI with alert details
        self.ui.alertsAlertNameTextEdit.setText(alert.name)
        index = self.ui.alertsChooseMonitorComboBox.findText(alert.monitor, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ui.alertsChooseMonitorComboBox.setCurrentIndex(index)
            
        metrics = alert.metrics.split(' ')
        if len(metrics) == 0 :  # CASE - no metrics
            a = 10 # do nothing, for now..
        elif len(metrics) == 2: # CASE - missing last field
            op = metrics[0]
            th = metrics[1]
            idx = self.ui.alertsMetricOperationComboBox.findText(op)
            self.ui.alertsMetricOperationComboBox.setCurrentIndex(idx)
            self.ui.alertsMetricValueSpinBox.setValue(int(th))
        elif len(metrics) == 3: # CASE - all fields set
            op = metrics[0]
            th = metrics[1]
            un = metrics[2]
            idx = self.ui.alertsMetricOperationComboBox.findText(op)
            self.ui.alertsMetricOperationComboBox.setCurrentIndex(idx)
            self.ui.alertsMetricValueSpinBox.setValue(int(th))
            idx = self.ui.alertsMetricUnitComboBox.findText(un)
            self.ui.alertsMetricUnitComboBox.setCurrentIndex(idx)
            
        if alert.seconds > 0:
            self.ui.alertsCaptureGroupBox.setChecked(True)
            self.ui.alertsCaptureDurationSpinBox.setValue(alert.seconds)
            self.ui.alertsFileNameTextEdit.setText(alert.filename)
        else:
            self.ui.alertsCaptureGroupBox.setChecked(False)

    """""""""""""""
        MONITORS
    """""""""""""""
    # Start Monitors
    def startMonitors(self):
        monitorsChecked = any([self.ui.monitorsCpuProcessUsageCheckBox.isChecked(),
                               self.ui.monitorsProcessIOErrorsCheckBox.isChecked(),
                               self.ui.monitorsSystemCallErrorsCheckBox.isChecked(),
                               self.ui.monitorsFileIOErrorsCheckBox.isChecked(),
                               self.ui.monitorsFilesMostTimeSpentCheckBox.isChecked(),
                               self.ui.monitorsSystemCallsMostTimeSpentCheckBox.isChecked(),
                               self.ui.monitorsNetworkConnectionsBWCheckBox.isChecked(),
                               self.ui.monitorsProcessBWCheckBox.isChecked()])

        if not monitorsChecked:
            utils.showMessageBox('Please select at least one monitor', 'Error', QtWidgets.QMessageBox.Critical)
            return

        monitors = []
        invalidMonitors = []

        if self.ui.monitorsCpuProcessUsageCheckBox.isChecked():
            text = self.ui.monitorsCpuProcessUsageTextEdit.toPlainText().strip()
            if text == '':
                utils.showMessageBox('No processes entered', 'Error', QtWidgets.QMessageBox.Critical)
                return
            mntrs = utils.getValidMonitors(text, 'cpu_top_processes_', 'process')
            monitors.extend(mntrs[0])
            invalidMonitors.extend(mntrs[1])

        if self.ui.monitorsSystemCallErrorsCheckBox.isChecked():
            monitors.append('errors_top_system_calls_errors')
        if self.ui.monitorsFileIOErrorsCheckBox.isChecked():
            monitors.append('errors_top_file_errors')
        if self.ui.monitorsProcessIOErrorsCheckBox.isChecked():
            monitors.append('errors_top_processes')
        if self.ui.monitorsFilesMostTimeSpentCheckBox.isChecked():
            monitors.append('errors_files_most_time_spent')
        if self.ui.monitorsSystemCallsMostTimeSpentCheckBox.isChecked():
            monitors.append('errors_top_system_calls_errors_time')
        if self.ui.monitorsNetworkConnectionsBWCheckBox.isChecked():
            monitors.append('network_top_connections_bandwidth')
        if self.ui.monitorsProcessBWCheckBox.isChecked():
            monitors.append('network_top_processes_bandwidth')

        self.startSysdig(monitors, self.ui.monitorsRunningMonitorsListWidget)

        self.displayMonitorStatus(monitors, invalidMonitors)

        self.ui.monitorsCpuProcessUsageTextEdit.setPlainText('')

    def stopMonitor(self):
        idx = self.ui.monitorsRunningMonitorsListWidget.currentRow()
        if idx == -1:
            utils.showMessageBox('No monitor selected', 'Error', QtWidgets.QMessageBox.Critical)
            return

        text = self.ui.monitorsRunningMonitorsListWidget.currentItem().text()
        self.ui.monitorsRunningMonitorsListWidget.takeItem(idx)

        cbIdx = self.ui.alertsChooseMonitorComboBox.findText(text)
        self.ui.alertsChooseMonitorComboBox.removeItem(cbIdx)
        
        # Sysdig
        self.threads[text].stop()
        self.threads[text].join()
        # self.threads[text].stopPlot()
        del self.threads[text]

        self.data.removeMonitor(text)

        # Visualization
        # if self.ui.tmr:
        #     self.ui.tmr.stop()
        #     self.ui.graphWidget.clear()

        utils.showMessageBox('Monitor stopped!', 'Success', QtWidgets.QMessageBox.Information)


    """""""""""""""""""""
        VISUALIZATION
    """""""""""""""""""""

    def visualizeMonitor(self):
        idx = self.ui.monitorsRunningMonitorsListWidget.currentRow()
        if idx == -1:
            utils.showMessageBox('No monitor selected', 'Error', QtWidgets.QMessageBox.Critical)
            return

        text = self.ui.monitorsRunningMonitorsListWidget.currentItem().text()

        # Reset the graphWidget
        self.ui.graphWidget.clear()

        # Keep global time
        self.t = QTime()
        self.t.start()

        # Start plot data queues
        maxlen = 200
        self.ui.data_x = deque(maxlen=maxlen)
        self.ui.data_y = deque(maxlen=maxlen)
        for monitor in self.threads:
            self.threads[monitor].stopPlot()
        self.threads[text].startPlot()

        # Add line to plot
        self.ui.curve =self.ui.graphWidget.addPlot(title=text, axisItems={'bottom': TimeAxisItem(orientation='bottom')}).plot()

        # Keep timer
        self.ui.tmr = QTimer()
        self.ui.tmr.timeout.connect(lambda: self.update(text))
        self.ui.tmr.start(200)

    def update(self, monitorName):
        x = now_timestamp()
        self.ui.data_x.append(x)
        try:
            self.ui.curve.setData(x=list(self.ui.data_x), y=list(self.ui.data_y))
        except Exception as e:
            if len(self.ui.data_x) > len(self.ui.data_y):
                self.ui.data_x.pop()
            else:
                self.ui.data_y.pop()
        finally:
            self.ui.curve.setData(x=list(self.ui.data_x), y=list(self.ui.data_y))

    """""""""""""""
        SYSDIG
    """""""""""""""
    # Sysdig stuff here
    def startSysdig(self, monitors, listWidget):
        for name in monitors:
            if name not in self.data.monitors:
                self.data.addMonitor(name)
                monitor = self.data.monitors[name]
                
                # Start sysdig
                self.threads[name] = SysdigThread(name, monitor, self.ui)
                self.threads[name].start()
                
                self.ui.alertsChooseMonitorComboBox.addItem(name)
                listWidget.addItem(name)

    """""""""""""""
        FALCO
    """""""""""""""
    def startFalco(self, rules):

        falco_rules = FalcoRules()
        for rule in rules:
            falco_rules.setArgs(rule)

        rules = falco_rules.getRules()
        self.threads['falco'] = FalcoThread(self.ui, rules)
        self.threads['falco'].run()

    """""""""""""""
        UI HELPER
    """""""""""""""
    def displayMonitorStatus(self, monitors, invalidMonitors):
        if len(invalidMonitors) != 0:
            utils.showMessageBox('These monitors contain errors:\n\n--> '+ '\n--> '.join(invalidMonitors) +'\n\nConsult the docs for further info.','Warning', QtWidgets.QMessageBox.Warning)
        if len(monitors) != 0:    
            utils.showMessageBox('Monitors started:\n\n--> ' + '\n--> '.join(monitors), 'Success', QtWidgets.QMessageBox.Information)
        else:
            utils.showMessageBox('No monitors started!', 'Error', QtWidgets.QMessageBox.Critical)

    def displayRuleStatus(self, rules, invalidRules):
        if len(rules) != 0:    
            utils.showMessageBox('Rules set:\n\n--> ' + '\n--> '.join(rules), 'Success', QtWidgets.QMessageBox.Information)
        else:
            utils.showMessageBox('No rules were set!', 'Error', QtWidgets.QMessageBox.Critical)