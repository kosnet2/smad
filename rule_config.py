from PyQt5.QtWidgets import QWidget, QCheckBox, QTreeWidget, QTreeWidgetItem, QPushButton, QLabel, QDialog, QVBoxLayout, QApplication, QLineEdit, QDateTimeEdit
from PyQt5.QtCore import pyqtSlot, QDateTime, QDate, pyqtSignal
from PyQt5.QtGui import QFont
import os

class ScheduleItem(QWidget):
    deleted = pyqtSignal()
    schedulechanged = pyqtSignal('QDateTimeEdit', 'QDateTimeEdit', bool, bool)

    def __init__(self, start, end, rchecked, achecked):
        super(ScheduleItem, self).__init__()
        self.createWidget(start, end, rchecked, achecked)

    def createWidget(self, start, end, rchecked, achecked):
        self.layout = QVBoxLayout()
        self.labelFont = QFont()
        self.labelFont.setUnderline(True)
        
        # Start time
        self.startLabel = QLabel("Start")
        self.startLabel.setFont(self.labelFont)
        self.startdt = QDateTimeEdit(start)
        self.startdt.dateTimeChanged.connect(self.scheduleChanged)
        # End time
        self.endLabel = QLabel("End")
        self.endLabel.setFont(self.labelFont)
        self.enddt = QDateTimeEdit(end)
        self.enddt.dateTimeChanged.connect(self.scheduleChanged)
        # Repetitive
        self.repetitive = QCheckBox(None)
        self.repetitive.setText("Repetitive")
        self.repetitive.setToolTip("If selected, the detector will run based on days of the week and datetimes. \nE.g 04/06/20 00:00 - 05/06/20 00:00 (which is a Sunday) will run 24 hours every Sunday")
        self.repetitive.setChecked(rchecked)
        self.repetitive.stateChanged.connect(self.scheduleChanged)
        # Active
        self.active = QCheckBox(None)
        self.active.setText("Active")
        self.active.setToolTip("If not selected, this rule will never run")
        self.active.setChecked(achecked)
        self.setStyles()
        self.active.stateChanged.connect(self.scheduleChanged)

        # Delete button
        self.deleteBtn = QPushButton("Delete")
        self.deleteBtn.setFont(self.labelFont)
        self.deleteBtn.clicked.connect(self.delete)

        self.layout.addWidget(self.startLabel)
        self.layout.addWidget(self.startdt)
        self.layout.addWidget(self.endLabel)
        self.layout.addWidget(self.enddt)
        self.layout.addWidget(self.repetitive)
        self.layout.addWidget(self.active)
        self.layout.addWidget(self.deleteBtn)

        self.setLayout(self.layout)

    def delete(self):
        self.deleted.emit()

    def scheduleChanged(self):
        self.setStyles()
        self.schedulechanged.emit(self.startdt, self.enddt, self.repetitive.isChecked(), self.active.isChecked())
    
    def setStyles(self):
        if self.run 
        if self.active.isChecked() == True:
            self.setStyleSheet("background-color:lightgreen;")
        else:
            self.setStyleSheet("")

class RuleConfigWidget(QDialog):
    def __init__(self, ui, data):
        super(RuleConfigWidget, self).__init__()
        self.init_ui(ui)
        self.load_data(data)

    def load_data(self, data):
        self.data = data
        arr = os.listdir('smad_rules/')
        idx = 0
        for ruleset in arr:
            if ruleset.endswith('.smadconf'):
                self.addRule(ruleset)
                if ruleset in self.data.scheduled_rules:
                    for rule in self.data.getScheduledRulesByFile(ruleset):
                        self.addSubRule(ruleset, idx, rule.start, rule.end, rule.repetitive, rule.active, rule.running)
                idx += 1

    def init_ui(self, ui):
        self.ui = ui # Probably Not needed
        self.treeWidget = self.ui.treeWidget
        self.treeWidget.setHeaderLabel("Available Configuration Files")
        self.topLevelItems = []
        self.parentChildren = {}

    def updateRules(self):
        # save current data
        self.data.saveScheduledRules()
        
        # delete all data
        todelete = len(self.topLevelItems)
        for _ in range(todelete):
            self.treeWidget.takeTopLevelItem(0)
        self.topLevelItems = []
        self.parentChildren = {}

        # reinitialize
        self.init_ui(self.ui)
        self.load_data(self.data)

    def addRule(self, text):
        topLevelItem = QTreeWidgetItem()
        index = len(self.topLevelItems)
        self.parentChildren[text] = []
        self.topLevelItems.append(QTreeWidgetItem())
        ruleButton = QPushButton(text)
        self.treeWidget.addTopLevelItem(topLevelItem)
        self.treeWidget.setItemWidget(topLevelItem, 0, ruleButton)
        ruleButton.clicked.connect(lambda: self.addSubRule(text, index))

    @pyqtSlot(bool)
    def addSubRule(self, parent, index, start=None, end=None, repetitive=None, active=None, running=None):
        child = QTreeWidgetItem()
        self.parentChildren[parent].append(child)
        self.treeWidget.topLevelItem(index).addChild(self.parentChildren[parent][-1])
        if start == None:
            now = QDateTime.currentDateTime()
            scheduleItem = ScheduleItem(now, now, True, False)
            self.data.addScheduledRule(parent, QDateTime.toString(now, "MMddyyhh:mm:ss"), QDateTime.toString(now, "MMddyyhh:mm:ss"), True, False, False)
        else:
            startstr = QDateTime.fromString(start, "MMddyyhh:mm:ss")
            endstr = QDateTime.fromString(end, "MMddyyhh:mm:ss")
            rbool = True if repetitive == 'True' else False
            abool = True if active == 'True' else False
            scheduleItem = ScheduleItem(startstr, endstr, rbool, abool)
        self.treeWidget.setItemWidget(child, 0, scheduleItem)
        scheduleItem.schedulechanged.connect(lambda s, e, r, a : self.updateData(index, parent, child, s, e, r, a))
        scheduleItem.deleted.connect(lambda: self.removeSubRule(index, parent, child))
    
    def updateData(self, index, parent, child, startdt, enddt, repetitive, active):
        child_index = self.treeWidget.topLevelItem(index).indexOfChild(child)
        data_item = self.data.scheduled_rules[parent][child_index]
        data_item.start = QDateTime.toString(startdt.dateTime(), "MMddyyhh:mm:ss")
        data_item.end = QDateTime.toString(enddt.dateTime(), "MMddyyhh:mm:ss")
        data_item.repetitive = repetitive
        data_item.active = active

    def removeSubRule(self, index, parent, child):
        child_index = self.treeWidget.topLevelItem(index).indexOfChild(child)
        self.data.removeScheduledRule(parent, child_index)
        self.treeWidget.topLevelItem(index).removeChild(child)

