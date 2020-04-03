from PyQt5.QtWidgets import QWidget, QCheckBox, QTreeWidget, QTreeWidgetItem, QPushButton, QLabel, QDialog, QVBoxLayout, QApplication, QLineEdit, QDateTimeEdit
from PyQt5.QtCore import pyqtSlot, QDateTime, QDate, pyqtSignal
from PyQt5.QtGui import QFont
import os

class ScheduleItem(QWidget):
    deleted = pyqtSignal()
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
        # End time
        self.endLabel = QLabel("End")
        self.endLabel.setFont(self.labelFont)
        self.enddt = QDateTimeEdit(end)
        # Repetitive
        self.repetitive = QCheckBox(None)
        self.repetitive.setText("Repetitive")
        self.repetitive.setChecked(checked)
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

class RuleConfigWidget(QDialog):
    def __init__(self, ui):
        super(RuleConfigWidget, self).__init__()
        self.init_ui(ui)
        self.load_data()

    def load_data(self):
        arr = os.listdir('smad_rules/')
        for file in arr:
            self.addRule(file)

    def init_ui(self, ui):
        self.ui = ui # Probably Not needed
        self.treeWidget = self.ui.treeWidget
        self.treeWidget.setHeaderLabel("Available Configuration Files")
        self.topLevelItems = []
        self.parentChildren = {}

    def addRule(self, text):
        topLevelItem = QTreeWidgetItem()
        # TODO: Read the schedule from top of the file
        # to get its childen
        index = len(self.topLevelItems)
        self.parentChildren[text] = []
        self.topLevelItems.append(QTreeWidgetItem())
        ruleButton = QPushButton(text)
        self.treeWidget.addTopLevelItem(topLevelItem)
        self.treeWidget.setItemWidget(topLevelItem, 0, ruleButton)
        ruleButton.clicked.connect(lambda: self.addSubRule(text, index))

    @pyqtSlot(bool)
    def addSubRule(self, parent, index, start=None, end=None):
        child = QTreeWidgetItem()
        self.parentChildren[parent].append(child)
        self.treeWidget.topLevelItem(index).addChild(self.parentChildren[parent][-1])
        scheduleItem = ScheduleItem(QDateTime.currentDateTime(), QDateTime.currentDateTime(), True)
        self.treeWidget.setItemWidget(child, 0, scheduleItem)
        scheduleItem.deleted.connect(lambda: self.removeSubRule(index, child))
    
    @pyqtSlot()
    def removeSubRule(self, index, child):
        self.treeWidget.topLevelItem(index).removeChild(child)

