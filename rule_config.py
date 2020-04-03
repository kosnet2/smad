from PyQt5.QtWidgets import QWidget, QCheckBox, QTreeWidget, QTreeWidgetItem, QPushButton, QLabel, QDialog, QVBoxLayout, QApplication, QLineEdit, QDateTimeEdit
from PyQt5.QtCore import pyqtSlot, QDateTime, QDate, pyqtSignal
from PyQt5.QtGui import QFont
import os

class ScheduleItem(QWidget):
    deleted = pyqtSignal()
    schedulechanged = pyqtSignal('QDateTimeEdit', 'QDateTimeEdit', bool)

    def __init__(self, start, end, checked):
        super(ScheduleItem, self).__init__()
        self.createWidget(start, end, checked)

    def createWidget(self, start, end, checked):
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
        self.repetitive.setChecked(checked)
        self.repetitive.stateChanged.connect(self.scheduleChanged)

        # Delete button
        self.deleteBtn = QPushButton("Delete")
        self.deleteBtn.setFont(self.labelFont)
        self.deleteBtn.clicked.connect(self.delete)

        self.layout.addWidget(self.startLabel)
        self.layout.addWidget(self.startdt)
        self.layout.addWidget(self.endLabel)
        self.layout.addWidget(self.enddt)
        self.layout.addWidget(self.repetitive)
        self.layout.addWidget(self.deleteBtn)

        self.setLayout(self.layout)

    def delete(self):
        self.deleted.emit()

    def scheduleChanged(self):
        self.schedulechanged.emit(self.startdt, self.enddt, self.repetitive.isChecked())

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
                        self.addSubRule(ruleset, idx, rule.start, rule.end, rule.repetitive, rule.running)
                idx += 1

    def init_ui(self, ui):
        self.ui = ui # Probably Not needed
        self.treeWidget = self.ui.treeWidget
        self.treeWidget.setHeaderLabel("Available Configuration Files")
        self.topLevelItems = []
        self.parentChildren = {}

    def addRule(self, text):
        print('addRule called')
        topLevelItem = QTreeWidgetItem()
        index = len(self.topLevelItems)
        self.parentChildren[text] = []
        self.topLevelItems.append(QTreeWidgetItem())
        ruleButton = QPushButton(text)
        self.treeWidget.addTopLevelItem(topLevelItem)
        self.treeWidget.setItemWidget(topLevelItem, 0, ruleButton)
        ruleButton.clicked.connect(lambda: self.addSubRule(text, index))

    @pyqtSlot(bool)
    def addSubRule(self, parent, index, start=None, end=None, repetitive=None, running=None):
        child = QTreeWidgetItem()
        self.parentChildren[parent].append(child)
        self.treeWidget.topLevelItem(index).addChild(self.parentChildren[parent][-1])
        if start == None:
            now = QDateTime.currentDateTime()
            scheduleItem = ScheduleItem(now, now, True)
            self.data.addScheduledRule(parent, QDateTime.toString(now, "MMddyyhh:mm:ss"), QDateTime.toString(now, "MMddyyhh:mm:ss"), True, False)
        else:
            scheduleItem = ScheduleItem(QDateTime.fromString(start, "MMddyyhh:mm:ss"), QDateTime.fromString(end, "MMddyyhh:mm:ss"), True if repetitive == 'True' else False)
        self.treeWidget.setItemWidget(child, 0, scheduleItem)
        scheduleItem.schedulechanged.connect(lambda s, e, r : self.updateData(index, parent, child, s, e, r))
        scheduleItem.deleted.connect(lambda: self.removeSubRule(index, parent, child))
    
    def updateData(self, index, parent, child, startdt, enddt, repetitive):
        child_index = self.treeWidget.topLevelItem(index).indexOfChild(child)
        data_item = self.data.scheduled_rules[parent][child_index]
        data_item.start = QDateTime.toString(startdt.dateTime(), "MMddyyhh:mm:ss")
        data_item.end = QDateTime.toString(enddt.dateTime(), "MMddyyhh:mm:ss")
        data_item.repetitive = repetitive

    def removeSubRule(self, index, parent, child):
        child_index = self.treeWidget.topLevelItem(index).indexOfChild(child)
        self.data.removeScheduledRule(parent, child_index)
        self.treeWidget.topLevelItem(index).removeChild(child)

