# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smad.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(879, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.monitorsCpuProcessUsageCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.monitorsCpuProcessUsageCheckBox.setObjectName("monitorsCpuProcessUsageCheckBox")
        self.verticalLayout_3.addWidget(self.monitorsCpuProcessUsageCheckBox)
        self.monitorsCpuProcessUsageTextEdit = QtWidgets.QTextEdit(self.groupBox)
        self.monitorsCpuProcessUsageTextEdit.setObjectName("monitorsCpuProcessUsageTextEdit")
        self.verticalLayout_3.addWidget(self.monitorsCpuProcessUsageTextEdit)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.monitorsSystemCallErrorsCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.monitorsSystemCallErrorsCheckBox.setObjectName("monitorsSystemCallErrorsCheckBox")
        self.verticalLayout_4.addWidget(self.monitorsSystemCallErrorsCheckBox)
        self.monitorsFileIOErrorsCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.monitorsFileIOErrorsCheckBox.setObjectName("monitorsFileIOErrorsCheckBox")
        self.verticalLayout_4.addWidget(self.monitorsFileIOErrorsCheckBox)
        self.monitorsProcessIOErrorsCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.monitorsProcessIOErrorsCheckBox.setObjectName("monitorsProcessIOErrorsCheckBox")
        self.verticalLayout_4.addWidget(self.monitorsProcessIOErrorsCheckBox)
        self.monitorsFilesMostTimeSpentCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.monitorsFilesMostTimeSpentCheckBox.setObjectName("monitorsFilesMostTimeSpentCheckBox")
        self.verticalLayout_4.addWidget(self.monitorsFilesMostTimeSpentCheckBox)
        self.monitorsSystemCallsMostTimeSpentCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.monitorsSystemCallsMostTimeSpentCheckBox.setObjectName("monitorsSystemCallsMostTimeSpentCheckBox")
        self.verticalLayout_4.addWidget(self.monitorsSystemCallsMostTimeSpentCheckBox)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.monitorsNetworkConnectionsBWCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.monitorsNetworkConnectionsBWCheckBox.setObjectName("monitorsNetworkConnectionsBWCheckBox")
        self.verticalLayout_5.addWidget(self.monitorsNetworkConnectionsBWCheckBox)
        self.monitorsProcessBWCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.monitorsProcessBWCheckBox.setObjectName("monitorsProcessBWCheckBox")
        self.verticalLayout_5.addWidget(self.monitorsProcessBWCheckBox)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.monitorsStartMonitors = QtWidgets.QPushButton(self.tab_4)
        self.monitorsStartMonitors.setEnabled(True)
        self.monitorsStartMonitors.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.monitorsStartMonitors.setCheckable(False)
        self.monitorsStartMonitors.setObjectName("monitorsStartMonitors")
        self.verticalLayout_6.addWidget(self.monitorsStartMonitors)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.monitorsRunningMonitorsListWidget = QtWidgets.QListWidget(self.tab_5)
        self.monitorsRunningMonitorsListWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.monitorsRunningMonitorsListWidget.setMaximumSize(QtCore.QSize(16777215, 250))
        self.monitorsRunningMonitorsListWidget.setObjectName("monitorsRunningMonitorsListWidget")
        self.verticalLayout_7.addWidget(self.monitorsRunningMonitorsListWidget)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plotWidget = PlotWidget(self.groupBox_6)
        self.plotWidget.setObjectName("plotWidget")
        self.gridLayout_2.addWidget(self.plotWidget, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_6)
        self.widget = QtWidgets.QWidget(self.tab_5)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.monitorsPlotMonitorButton = QtWidgets.QPushButton(self.widget)
        self.monitorsPlotMonitorButton.setObjectName("monitorsPlotMonitorButton")
        self.horizontalLayout_3.addWidget(self.monitorsPlotMonitorButton)
        self.monitorsStopPlotMonitorButton = QtWidgets.QPushButton(self.widget)
        self.monitorsStopPlotMonitorButton.setEnabled(True)
        self.monitorsStopPlotMonitorButton.setObjectName("monitorsStopPlotMonitorButton")
        self.horizontalLayout_3.addWidget(self.monitorsStopPlotMonitorButton)
        self.monitorsStopMonitorButton = QtWidgets.QPushButton(self.widget)
        self.monitorsStopMonitorButton.setObjectName("monitorsStopMonitorButton")
        self.horizontalLayout_3.addWidget(self.monitorsStopMonitorButton)
        self.verticalLayout_7.addWidget(self.widget)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.alertsAlertDetailsGroupBox = QtWidgets.QGroupBox(self.tab_6)
        self.alertsAlertDetailsGroupBox.setObjectName("alertsAlertDetailsGroupBox")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.alertsAlertDetailsGroupBox)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.alertsTriggerGroupBox = QtWidgets.QGroupBox(self.alertsAlertDetailsGroupBox)
        self.alertsTriggerGroupBox.setObjectName("alertsTriggerGroupBox")
        self.formLayout_4 = QtWidgets.QFormLayout(self.alertsTriggerGroupBox)
        self.formLayout_4.setObjectName("formLayout_4")
        self.alertsAlertNameLabel = QtWidgets.QLabel(self.alertsTriggerGroupBox)
        self.alertsAlertNameLabel.setObjectName("alertsAlertNameLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.alertsAlertNameLabel)
        self.alertsAlertNameTextEdit = QtWidgets.QTextEdit(self.alertsTriggerGroupBox)
        self.alertsAlertNameTextEdit.setObjectName("alertsAlertNameTextEdit")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.alertsAlertNameTextEdit)
        self.alertsChooseMonitorLabel = QtWidgets.QLabel(self.alertsTriggerGroupBox)
        self.alertsChooseMonitorLabel.setObjectName("alertsChooseMonitorLabel")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.alertsChooseMonitorLabel)
        self.alertsChooseMonitorComboBox = QtWidgets.QComboBox(self.alertsTriggerGroupBox)
        self.alertsChooseMonitorComboBox.setObjectName("alertsChooseMonitorComboBox")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.alertsChooseMonitorComboBox)
        self.alertsSetMetricLabel = QtWidgets.QLabel(self.alertsTriggerGroupBox)
        self.alertsSetMetricLabel.setWordWrap(False)
        self.alertsSetMetricLabel.setIndent(-1)
        self.alertsSetMetricLabel.setObjectName("alertsSetMetricLabel")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.alertsSetMetricLabel)
        self.alertsSetMetricWidget = QtWidgets.QWidget(self.alertsTriggerGroupBox)
        self.alertsSetMetricWidget.setEnabled(True)
        self.alertsSetMetricWidget.setObjectName("alertsSetMetricWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.alertsSetMetricWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.alertsMetricDescription = QtWidgets.QLabel(self.alertsSetMetricWidget)
        self.alertsMetricDescription.setObjectName("alertsMetricDescription")
        self.horizontalLayout_4.addWidget(self.alertsMetricDescription)
        self.alertsMetricOperationComboBox = QtWidgets.QComboBox(self.alertsSetMetricWidget)
        self.alertsMetricOperationComboBox.setEnabled(True)
        self.alertsMetricOperationComboBox.setEditable(False)
        self.alertsMetricOperationComboBox.setObjectName("alertsMetricOperationComboBox")
        self.alertsMetricOperationComboBox.addItem("")
        self.alertsMetricOperationComboBox.addItem("")
        self.alertsMetricOperationComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.alertsMetricOperationComboBox)
        self.alertsMetricValueSpinBox = QtWidgets.QSpinBox(self.alertsSetMetricWidget)
        self.alertsMetricValueSpinBox.setMaximum(999999999)
        self.alertsMetricValueSpinBox.setObjectName("alertsMetricValueSpinBox")
        self.horizontalLayout_4.addWidget(self.alertsMetricValueSpinBox)
        self.alertsMetricUnitComboBox = QtWidgets.QComboBox(self.alertsSetMetricWidget)
        self.alertsMetricUnitComboBox.setObjectName("alertsMetricUnitComboBox")
        self.horizontalLayout_4.addWidget(self.alertsMetricUnitComboBox)
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.alertsSetMetricWidget)
        self.verticalLayout_23.addWidget(self.alertsTriggerGroupBox)
        self.alertsActionGroupBox = QtWidgets.QGroupBox(self.alertsAlertDetailsGroupBox)
        self.alertsActionGroupBox.setObjectName("alertsActionGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.alertsActionGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.alertsCaptureGroupBox = QtWidgets.QGroupBox(self.alertsActionGroupBox)
        self.alertsCaptureGroupBox.setCheckable(True)
        self.alertsCaptureGroupBox.setObjectName("alertsCaptureGroupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.alertsCaptureGroupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.alertsFileNameLabel = QtWidgets.QLabel(self.alertsCaptureGroupBox)
        self.alertsFileNameLabel.setObjectName("alertsFileNameLabel")
        self.gridLayout_8.addWidget(self.alertsFileNameLabel, 3, 0, 1, 1)
        self.alertsFileNameTextEdit = QtWidgets.QTextEdit(self.alertsCaptureGroupBox)
        self.alertsFileNameTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.alertsFileNameTextEdit.setObjectName("alertsFileNameTextEdit")
        self.gridLayout_8.addWidget(self.alertsFileNameTextEdit, 3, 1, 1, 1)
        self.alertsCaptureDurationLabel = QtWidgets.QLabel(self.alertsCaptureGroupBox)
        self.alertsCaptureDurationLabel.setObjectName("alertsCaptureDurationLabel")
        self.gridLayout_8.addWidget(self.alertsCaptureDurationLabel, 1, 0, 1, 1)
        self.alertsCaptureDurationSpinBox = QtWidgets.QSpinBox(self.alertsCaptureGroupBox)
        self.alertsCaptureDurationSpinBox.setMinimum(1)
        self.alertsCaptureDurationSpinBox.setMaximum(86400)
        self.alertsCaptureDurationSpinBox.setProperty("value", 60)
        self.alertsCaptureDurationSpinBox.setObjectName("alertsCaptureDurationSpinBox")
        self.gridLayout_8.addWidget(self.alertsCaptureDurationSpinBox, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.alertsCaptureGroupBox, 0, 0, 1, 1)
        self.verticalLayout_23.addWidget(self.alertsActionGroupBox)
        self.alertsSaveAlertPushButton = QtWidgets.QPushButton(self.alertsAlertDetailsGroupBox)
        self.alertsSaveAlertPushButton.setObjectName("alertsSaveAlertPushButton")
        self.verticalLayout_23.addWidget(self.alertsSaveAlertPushButton)
        self.horizontalLayout.addWidget(self.alertsAlertDetailsGroupBox)
        self.alertsListGroupBox = QtWidgets.QGroupBox(self.tab_6)
        self.alertsListGroupBox.setObjectName("alertsListGroupBox")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.alertsListGroupBox)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.alertsListListWidget = QtWidgets.QListWidget(self.alertsListGroupBox)
        self.alertsListListWidget.setObjectName("alertsListListWidget")
        self.verticalLayout_22.addWidget(self.alertsListListWidget)
        self.alertsAlertListButtons = QtWidgets.QHBoxLayout()
        self.alertsAlertListButtons.setObjectName("alertsAlertListButtons")
        self.alertsEditAlertPushButton = QtWidgets.QPushButton(self.alertsListGroupBox)
        self.alertsEditAlertPushButton.setObjectName("alertsEditAlertPushButton")
        self.alertsAlertListButtons.addWidget(self.alertsEditAlertPushButton)
        self.alertsDeleteAlertPushButton = QtWidgets.QPushButton(self.alertsListGroupBox)
        self.alertsDeleteAlertPushButton.setObjectName("alertsDeleteAlertPushButton")
        self.alertsAlertListButtons.addWidget(self.alertsDeleteAlertPushButton)
        self.verticalLayout_22.addLayout(self.alertsAlertListButtons)
        self.horizontalLayout.addWidget(self.alertsListGroupBox)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.verticalLayout_2.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.tab_8)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.anomaliesLoadRulesButton = QtWidgets.QPushButton(self.widget_2)
        self.anomaliesLoadRulesButton.setObjectName("anomaliesLoadRulesButton")
        self.horizontalLayout_5.addWidget(self.anomaliesLoadRulesButton)
        self.anomaliesExportRulesButton = QtWidgets.QPushButton(self.widget_2)
        self.anomaliesExportRulesButton.setObjectName("anomaliesExportRulesButton")
        self.horizontalLayout_5.addWidget(self.anomaliesExportRulesButton)
        self.verticalLayout.addWidget(self.widget_2)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.tab_8)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 819, 1074))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.anomaliesProgramExecutedGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.anomaliesProgramExecutedGroupBox.setCheckable(False)
        self.anomaliesProgramExecutedGroupBox.setChecked(False)
        self.anomaliesProgramExecutedGroupBox.setObjectName("anomaliesProgramExecutedGroupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.anomaliesProgramExecutedGroupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.anomaliesProgramExecutedTextEdit = QtWidgets.QTextEdit(self.anomaliesProgramExecutedGroupBox)
        self.anomaliesProgramExecutedTextEdit.setAutoFillBackground(False)
        self.anomaliesProgramExecutedTextEdit.setObjectName("anomaliesProgramExecutedTextEdit")
        self.horizontalLayout_6.addWidget(self.anomaliesProgramExecutedTextEdit)
        self.verticalLayout_27.addWidget(self.anomaliesProgramExecutedGroupBox)
        self.anomaliesDirectoryFileOpensGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.anomaliesDirectoryFileOpensGroupBox.setCheckable(False)
        self.anomaliesDirectoryFileOpensGroupBox.setChecked(False)
        self.anomaliesDirectoryFileOpensGroupBox.setObjectName("anomaliesDirectoryFileOpensGroupBox")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.anomaliesDirectoryFileOpensGroupBox)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.anomaliesDirectoryFileOpensTextEdit = QtWidgets.QTextEdit(self.anomaliesDirectoryFileOpensGroupBox)
        self.anomaliesDirectoryFileOpensTextEdit.setObjectName("anomaliesDirectoryFileOpensTextEdit")
        self.horizontalLayout_13.addWidget(self.anomaliesDirectoryFileOpensTextEdit)
        self.verticalLayout_27.addWidget(self.anomaliesDirectoryFileOpensGroupBox)
        self.anomaliesProcessFileOpensGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.anomaliesProcessFileOpensGroupBox.setCheckable(False)
        self.anomaliesProcessFileOpensGroupBox.setChecked(False)
        self.anomaliesProcessFileOpensGroupBox.setObjectName("anomaliesProcessFileOpensGroupBox")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.anomaliesProcessFileOpensGroupBox)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.anomaliesProcessFileOpensTextEdit = QtWidgets.QTextEdit(self.anomaliesProcessFileOpensGroupBox)
        self.anomaliesProcessFileOpensTextEdit.setObjectName("anomaliesProcessFileOpensTextEdit")
        self.horizontalLayout_16.addWidget(self.anomaliesProcessFileOpensTextEdit)
        self.verticalLayout_27.addWidget(self.anomaliesProcessFileOpensGroupBox)
        self.anomaliesKnownUsersGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.anomaliesKnownUsersGroupBox.setToolTipDuration(2)
        self.anomaliesKnownUsersGroupBox.setCheckable(False)
        self.anomaliesKnownUsersGroupBox.setChecked(False)
        self.anomaliesKnownUsersGroupBox.setObjectName("anomaliesKnownUsersGroupBox")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.anomaliesKnownUsersGroupBox)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.anomaliesKnownUsersTextEdit = QtWidgets.QTextEdit(self.anomaliesKnownUsersGroupBox)
        self.anomaliesKnownUsersTextEdit.setToolTipDuration(-1)
        self.anomaliesKnownUsersTextEdit.setObjectName("anomaliesKnownUsersTextEdit")
        self.horizontalLayout_17.addWidget(self.anomaliesKnownUsersTextEdit)
        self.verticalLayout_27.addWidget(self.anomaliesKnownUsersGroupBox)
        self.anomaliesUnknownUsersGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.anomaliesUnknownUsersGroupBox.setToolTipDuration(2)
        self.anomaliesUnknownUsersGroupBox.setCheckable(False)
        self.anomaliesUnknownUsersGroupBox.setChecked(False)
        self.anomaliesUnknownUsersGroupBox.setObjectName("anomaliesUnknownUsersGroupBox")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.anomaliesUnknownUsersGroupBox)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.anomalieUnknownUsersTextEdit = QtWidgets.QTextEdit(self.anomaliesUnknownUsersGroupBox)
        self.anomalieUnknownUsersTextEdit.setObjectName("anomalieUnknownUsersTextEdit")
        self.horizontalLayout_18.addWidget(self.anomalieUnknownUsersTextEdit)
        self.verticalLayout_27.addWidget(self.anomaliesUnknownUsersGroupBox)
        self.anomaliesInboundIPGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.anomaliesInboundIPGroupBox.setCheckable(False)
        self.anomaliesInboundIPGroupBox.setChecked(False)
        self.anomaliesInboundIPGroupBox.setObjectName("anomaliesInboundIPGroupBox")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.anomaliesInboundIPGroupBox)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.anomaliesInboundIPTextEdit = QtWidgets.QTextEdit(self.anomaliesInboundIPGroupBox)
        self.anomaliesInboundIPTextEdit.setObjectName("anomaliesInboundIPTextEdit")
        self.horizontalLayout_19.addWidget(self.anomaliesInboundIPTextEdit)
        self.verticalLayout_27.addWidget(self.anomaliesInboundIPGroupBox)
        self.anomaliesOutboundIPGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.anomaliesOutboundIPGroupBox.setCheckable(False)
        self.anomaliesOutboundIPGroupBox.setChecked(False)
        self.anomaliesOutboundIPGroupBox.setObjectName("anomaliesOutboundIPGroupBox")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.anomaliesOutboundIPGroupBox)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.anomaliesOutboundIPTextEdit = QtWidgets.QTextEdit(self.anomaliesOutboundIPGroupBox)
        self.anomaliesOutboundIPTextEdit.setObjectName("anomaliesOutboundIPTextEdit")
        self.horizontalLayout_20.addWidget(self.anomaliesOutboundIPTextEdit)
        self.verticalLayout_27.addWidget(self.anomaliesOutboundIPGroupBox)
        self.anomaliesMaliciousIPGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.anomaliesMaliciousIPGroupBox.setCheckable(False)
        self.anomaliesMaliciousIPGroupBox.setChecked(False)
        self.anomaliesMaliciousIPGroupBox.setObjectName("anomaliesMaliciousIPGroupBox")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.anomaliesMaliciousIPGroupBox)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.anomaliesMaliciousIPTextEdit = QtWidgets.QTextEdit(self.anomaliesMaliciousIPGroupBox)
        self.anomaliesMaliciousIPTextEdit.setObjectName("anomaliesMaliciousIPTextEdit")
        self.horizontalLayout_21.addWidget(self.anomaliesMaliciousIPTextEdit)
        self.verticalLayout_27.addWidget(self.anomaliesMaliciousIPGroupBox)
        self.groupBox_13 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.anomaliesMySQLCheckBox = QtWidgets.QCheckBox(self.groupBox_13)
        self.anomaliesMySQLCheckBox.setToolTipDuration(2)
        self.anomaliesMySQLCheckBox.setObjectName("anomaliesMySQLCheckBox")
        self.gridLayout_3.addWidget(self.anomaliesMySQLCheckBox, 0, 1, 1, 1)
        self.anomaliesMongoDBCheckBox = QtWidgets.QCheckBox(self.groupBox_13)
        self.anomaliesMongoDBCheckBox.setToolTipDuration(2)
        self.anomaliesMongoDBCheckBox.setObjectName("anomaliesMongoDBCheckBox")
        self.gridLayout_3.addWidget(self.anomaliesMongoDBCheckBox, 0, 0, 1, 1)
        self.anomaliesHTTPCheckBox = QtWidgets.QCheckBox(self.groupBox_13)
        self.anomaliesHTTPCheckBox.setToolTipDuration(2)
        self.anomaliesHTTPCheckBox.setObjectName("anomaliesHTTPCheckBox")
        self.gridLayout_3.addWidget(self.anomaliesHTTPCheckBox, 1, 0, 1, 1)
        self.anomaliesKafkaCheckBox = QtWidgets.QCheckBox(self.groupBox_13)
        self.anomaliesKafkaCheckBox.setToolTipDuration(2)
        self.anomaliesKafkaCheckBox.setObjectName("anomaliesKafkaCheckBox")
        self.gridLayout_3.addWidget(self.anomaliesKafkaCheckBox, 1, 1, 1, 1)
        self.verticalLayout_27.addWidget(self.groupBox_13)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea_5)
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_9)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setColumnCount(0)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout_4.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_9, "")
        self.verticalLayout_26.addWidget(self.tabWidget_3)
        self.anomaliesDeployAnomalyDetectorButton = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.anomaliesDeployAnomalyDetectorButton.setFont(font)
        self.anomaliesDeployAnomalyDetectorButton.setObjectName("anomaliesDeployAnomalyDetectorButton")
        self.verticalLayout_26.addWidget(self.anomaliesDeployAnomalyDetectorButton)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName("gridLayout")
        self.notificationsTableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.notificationsTableWidget.setColumnCount(4)
        self.notificationsTableWidget.setObjectName("notificationsTableWidget")
        self.notificationsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.notificationsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.notificationsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.notificationsTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.notificationsTableWidget.setHorizontalHeaderItem(3, item)
        self.notificationsTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.notificationsTableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.notificationsTableWidget.horizontalHeader().setHighlightSections(True)
        self.notificationsTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.notificationsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.notificationsTableWidget.verticalHeader().setDefaultSectionSize(30)
        self.notificationsTableWidget.verticalHeader().setMinimumSectionSize(21)
        self.notificationsTableWidget.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout.addWidget(self.notificationsTableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SMAD"))
        self.groupBox.setTitle(_translate("MainWindow", "CPU and Processes"))
        self.monitorsCpuProcessUsageCheckBox.setText(_translate("MainWindow", "Observe processes in terms of CPU usage"))
        self.monitorsCpuProcessUsageTextEdit.setPlaceholderText(_translate("MainWindow", "One process per line"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Performance and Errors"))
        self.monitorsSystemCallErrorsCheckBox.setText(_translate("MainWindow", "Observe top system calls returning errors"))
        self.monitorsFileIOErrorsCheckBox.setText(_translate("MainWindow", "Observe top files with I/O errors"))
        self.monitorsProcessIOErrorsCheckBox.setText(_translate("MainWindow", "Observe top processes with I/O errors"))
        self.monitorsFilesMostTimeSpentCheckBox.setText(_translate("MainWindow", "Observe files where most time has been spent"))
        self.monitorsSystemCallsMostTimeSpentCheckBox.setText(_translate("MainWindow", "Observe system calls where most time has been spent"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Network"))
        self.monitorsNetworkConnectionsBWCheckBox.setText(_translate("MainWindow", "Observe top network connections in terms of bandwidth"))
        self.monitorsProcessBWCheckBox.setText(_translate("MainWindow", "Observe top processes in terms of bandwidth"))
        self.monitorsStartMonitors.setText(_translate("MainWindow", "Start monitors"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Start monitors"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Visualization"))
        self.monitorsPlotMonitorButton.setText(_translate("MainWindow", "Plot monitor"))
        self.monitorsStopPlotMonitorButton.setText(_translate("MainWindow", "Stop plot"))
        self.monitorsStopMonitorButton.setText(_translate("MainWindow", "Stop monitor"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Running monitors"))
        self.alertsAlertDetailsGroupBox.setTitle(_translate("MainWindow", "Alert details"))
        self.alertsTriggerGroupBox.setTitle(_translate("MainWindow", "Trigger"))
        self.alertsAlertNameLabel.setText(_translate("MainWindow", "Alert name"))
        self.alertsAlertNameTextEdit.setPlaceholderText(_translate("MainWindow", "Alert name (eg. alert_x)"))
        self.alertsChooseMonitorLabel.setText(_translate("MainWindow", "Choose monitor"))
        self.alertsSetMetricLabel.setText(_translate("MainWindow", "Set metric"))
        self.alertsMetricDescription.setText(_translate("MainWindow", "Metric"))
        self.alertsMetricOperationComboBox.setItemText(0, _translate("MainWindow", ">"))
        self.alertsMetricOperationComboBox.setItemText(1, _translate("MainWindow", "<"))
        self.alertsMetricOperationComboBox.setItemText(2, _translate("MainWindow", "="))
        self.alertsActionGroupBox.setTitle(_translate("MainWindow", "Action"))
        self.alertsCaptureGroupBox.setTitle(_translate("MainWindow", "Set up capture"))
        self.alertsFileNameLabel.setText(_translate("MainWindow", "Filename"))
        self.alertsFileNameTextEdit.setPlaceholderText(_translate("MainWindow", "Meaningful filename"))
        self.alertsCaptureDurationLabel.setText(_translate("MainWindow", "Capture for (seconds)"))
        self.alertsSaveAlertPushButton.setText(_translate("MainWindow", "Save alert"))
        self.alertsListGroupBox.setTitle(_translate("MainWindow", "Alert list"))
        self.alertsEditAlertPushButton.setText(_translate("MainWindow", "Edit"))
        self.alertsDeleteAlertPushButton.setText(_translate("MainWindow", "Delete"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Alerts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Monitors"))
        self.label_7.setText(_translate("MainWindow", "Please configure the needed rules below or load from file.\n"
"Add multiples inputs for a rule in separate lines"))
        self.anomaliesLoadRulesButton.setText(_translate("MainWindow", "Load rules"))
        self.anomaliesExportRulesButton.setText(_translate("MainWindow", "Export rules"))
        self.anomaliesProgramExecutedGroupBox.setTitle(_translate("MainWindow", "Detect unexpected execution of a program"))
        self.anomaliesProgramExecutedTextEdit.setPlaceholderText(_translate("MainWindow", "i.e sudo"))
        self.anomaliesDirectoryFileOpensGroupBox.setTitle(_translate("MainWindow", "Detect failed file opens in directory"))
        self.anomaliesDirectoryFileOpensTextEdit.setPlaceholderText(_translate("MainWindow", "i.e. /etc"))
        self.anomaliesProcessFileOpensGroupBox.setTitle(_translate("MainWindow", "Detect failed file opens from process"))
        self.anomaliesProcessFileOpensTextEdit.setPlaceholderText(_translate("MainWindow", "i.e python3"))
        self.anomaliesKnownUsersGroupBox.setToolTip(_translate("MainWindow", "Monitor and detect system usage for specific known users"))
        self.anomaliesKnownUsersGroupBox.setTitle(_translate("MainWindow", "Detect directories visited by known users"))
        self.anomaliesKnownUsersTextEdit.setPlaceholderText(_translate("MainWindow", "i.e john"))
        self.anomaliesUnknownUsersGroupBox.setToolTip(_translate("MainWindow", "Provide the known users to identify unknown user activity"))
        self.anomaliesUnknownUsersGroupBox.setTitle(_translate("MainWindow", "Detect directories visited by unknown users"))
        self.anomalieUnknownUsersTextEdit.setPlaceholderText(_translate("MainWindow", "i.e john"))
        self.anomaliesInboundIPGroupBox.setTitle(_translate("MainWindow", "Detect inbound traffic related to IP"))
        self.anomaliesInboundIPTextEdit.setPlaceholderText(_translate("MainWindow", "i.e. 192.168.125.117"))
        self.anomaliesOutboundIPGroupBox.setTitle(_translate("MainWindow", "Detect outbound traffic related to IP"))
        self.anomaliesOutboundIPTextEdit.setPlaceholderText(_translate("MainWindow", "i.e 192.168.125.117"))
        self.anomaliesMaliciousIPGroupBox.setToolTip(_translate("MainWindow", "The list of malicious IPs should be updated frequently"))
        self.anomaliesMaliciousIPGroupBox.setTitle(_translate("MainWindow", "Detect traffic related to a malicious IP"))
        self.anomaliesMaliciousIPTextEdit.setPlaceholderText(_translate("MainWindow", "i.e. 192.168.125.117"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Detect unexpected inbound traffic on server"))
        self.anomaliesMySQLCheckBox.setToolTip(_translate("MainWindow", "Inbound traffic to MySQL server in an unknown port"))
        self.anomaliesMySQLCheckBox.setText(_translate("MainWindow", "MySQL unexpected inbound traffic"))
        self.anomaliesMongoDBCheckBox.setToolTip(_translate("MainWindow", "Inbound traffic to MongoDB server in an unknown port"))
        self.anomaliesMongoDBCheckBox.setText(_translate("MainWindow", "MongoDB unexpected inbound traffic"))
        self.anomaliesHTTPCheckBox.setToolTip(_translate("MainWindow", "Inbound traffic to HTTP server in an unknown port"))
        self.anomaliesHTTPCheckBox.setText(_translate("MainWindow", "HTTP server unexpected inbound traffic"))
        self.anomaliesKafkaCheckBox.setToolTip(_translate("MainWindow", "Inbound traffic to Kafka server in an unknown port"))
        self.anomaliesKafkaCheckBox.setText(_translate("MainWindow", "Kafka unexpected inbound traffic"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("MainWindow", "Detector"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "Scheduler"))
        self.anomaliesDeployAnomalyDetectorButton.setText(_translate("MainWindow", "Deploy Anomaly Detector"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Anomalies"))
        item = self.notificationsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Datetime"))
        item = self.notificationsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Alert name"))
        item = self.notificationsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "File name"))
        item = self.notificationsTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Notifications"))
from pyqtgraph import PlotWidget
