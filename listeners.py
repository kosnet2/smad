# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import utilities as utils

""" FILE_DIALOG """
from PyQt5.QtWidgets import QWidget, QFileDialog

""" VISUALIZATION """
import pyqtgraph as pg

""" SYSDIG """
from file_dialog import FileDialog
from collections import deque
from sysdig_thread import SysdigThread
from falco_rules import FalcoRules
from falco_thread import FalcoThread
from file_watcher_thread import FileWatcherThread

class Listeners:
    def __init__(self, ui, data):
        self.pens = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)] # Plotting colors
        self.penIndex = 0
        self.ui = ui
        self.data = data
        self.threads = {}
        self.registerListeners()
    
    def stopApplication(self, event):
		# Save monitors to file
        with open('resources/monitors.txt', 'w+') as f:
            f.write('\n'.join([monitor for monitor in self.data.monitors]))

        # Stop current threads
        for thread in self.threads:
            self.threads[thread].stop()
            self.threads[thread].wait()

    """""""""""""""""""""
     BUTTON REGISTRATION
    """""""""""""""""""""
    def registerListeners(self):
        # Monitors Button Listeners
        self.ui.monitorsStartMonitors.clicked.connect(lambda: self.startMonitors())
        self.ui.monitorsStopMonitorButton.clicked.connect(lambda: self.stopMonitor())
        self.ui.monitorsPlotMonitorButton.clicked.connect(lambda: self.visualizeMonitor())
        self.ui.monitorsStopPlotMonitorButton.clicked.connect(lambda: self.stopVisualizingMonitor())

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
        dialog = FileDialog('load_file', self.ui)

    def exportAnomalyRules(self):
        dialog = FileDialog('save_file', self.ui)

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
        
        # Start falco instance
        self.startFalco(rules, invalidRules)

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

        # Update metrics depending on monitor chosen
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
        if self.ui.alertsListListWidget.currentRow() == -1:
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
        idx = self.ui.alertsMetricOperationComboBox.findText(metrics[0])
        self.ui.alertsMetricOperationComboBox.setCurrentIndex(idx)
        self.ui.alertsMetricValueSpinBox.setValue(int(metrics[1]))

        # If last metric field is set
        if len(metrics) == 3:
            idx = self.ui.alertsMetricUnitComboBox.findText(metrics[2])
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

        # Start sysdig instances
        self.startSysdig(monitors, self.ui.monitorsRunningMonitorsListWidget)
        self.displayMonitorStatus(monitors, invalidMonitors)
        
        # Reset fields
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
       
        # Stop plotting if the monitor is plotting
        if self.threads[text].isPlotting():
            self.stopVisualizingMonitor()

        # Stop the sysdig thread
        self.threads[text].stop()
        self.threads[text].wait()
        del self.threads[text]

        # Clean user data
        self.data.removeMonitor(text)

        # Display message
        utils.showMessageBox('Monitor stopped!', 'Success', QtWidgets.QMessageBox.Information)


    """""""""""""""""""""
        VISUALIZATION
    """""""""""""""""""""
    def visualizeMonitor(self):
        if self.ui.monitorsRunningMonitorsListWidget.currentRow() == -1:
            utils.showMessageBox('No monitor selected', 'Error', QtWidgets.QMessageBox.Critical)
            return

        text = self.ui.monitorsRunningMonitorsListWidget.currentItem().text()

        # Reset plotting widget and stop already plotting monitors
        self.stopVisualizingMonitor()

        # Start plotting
        self.ui.plots = {}
        self.ui.plotsData = {}
        self.threads[text].startPlot()

    def stopVisualizingMonitor(self):
        for thread in self.threads:
            if isinstance(self.threads[thread], SysdigThread):
                if self.threads[thread].isPlotting():
                    self.threads[thread].stopPlot()
                    
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
    def startFalco(self, rules, invalidRules):
        falco_rules = FalcoRules()
        for rule in rules:
            falco_rules.setArgs(rule)

        if 'falco' in self.threads:
            self.threads['falco'].stop()
            self.threads['falco'].wait()

        self.threads['falco'] = FalcoThread(self.ui, falco_rules.getRules())
        self.threads['falco'].start()
        self.displayRuleStatus(rules, invalidRules)

        if 'file_watcher' in self.threads:
            self.threads['file_watcher'].stop()
            self.threads['file_watcher'].wait()

        self.threads['file_watcher'] = FileWatcherThread(self.ui, self.threads['falco'].get_events_file())
        self.threads['file_watcher'].start()

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
        events_file = self.threads['falco'].get_events_file()
        
        if len(rules) != 0:
            message  = 'Anomaly Detector Deployed with Custom + Default rules!\n\n--> '+ '\n--> '.join(rules) + '\n\nDetector alerts can be found in the Notifications tab\nor in the events file located at ' + events_file +'\n\nPlease consult the documentation for default rule information!'
            utils.showMessageBox(message, 'Success', QtWidgets.QMessageBox.Information)
        else:
            message = 'Anomaly Detector Deployed with Default rules!\n\n'+ 'Detector alerts can be found in the Notifications tab\nor in the events file located at ' + events_file + '\n\nPlease consult the documentation for default rule information!' 
            utils.showMessageBox(message, 'Success', QtWidgets.QMessageBox.Information)