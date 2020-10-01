# The event loop that will read all data and emit the current rule taken into consideration

# A thread that will:
# - have access to the global ScheduledRules data
#       It should be able to modify the running state of the rule
#       It should be able to get start, end, repetitive and active modes of a rule

# - It should be able to emit a message with the name of the rule that needs to switched
#       The message will be the filename
#       It will be received from the listeners
#       Listeners will be responsible to stop/start the falco instance with the configuration file name specified
#       If a Scheduled Rule goes inactive and no other rule runs then a "Stop running message" should be emitted

from PyQt5.QtCore import QThread, QObject,pyqtSlot, QDateTime, QDate, pyqtSignal
from time import sleep
from threading import Event, Lock
from data import ScheduledRule
from copy import deepcopy
import os

class ContextSwitchHandler(QThread):
    scheduleswitched = pyqtSignal(str)

    def __init__(self, data):
        QThread.__init__(self)
        super(ContextSwitchHandler, self).__init__()
        self.data = data
        self._stop_event = Event()
        self.currRuleStr = 'None'
        self.currRuleObj = None

    def run(self):
        while True:
            if self.stopped():
                break 
            sleep(2)

            # There is no task running
            if self.currRuleObj == None:
                start = False
                for scheduledRule in self.data.scheduled_rules:
                    for rule in self.data.scheduled_rules[scheduledRule]:
                        if rule.active == True:
                            if rule.repetitive == True:
                                start = self.inRepetitiveScheduleRange(rule)
                            else: 
                                start = self.inOneTimeScheduleRange(rule)
                            if start:
                                self.startTask(scheduledRule, rule)
                                break
                    if start:
                        break
            # There is a task running
            else:
                stop = self.currRuleObj.active == False or self.currRuleObj.running == False
                if not stop:
                    if self.currRuleObj.repetitive == True:
                        stop = not self.inRepetitiveScheduleRange(self.currRuleObj)
                    else:
                        stop = not self.inOneTimeScheduleRange(self.currRuleObj)

                if stop == True:
                    self.stopTask()                

    def startTask(self, name, ruleObj):
        self.currRuleObj = ruleObj
        self.currRuleStr = name
        self.currRuleObj.running = True
        self.scheduleswitched.emit(self.currRuleStr)

    def stopTask(self):
        self.currRuleObj.running = False
        self.currRuleObj = None
        self.currRuleStr = 'None'
        self.scheduleswitched.emit(self.currRuleStr)

    def updateData(self, newData):
        self.rules = newData.copy()
        
    def stop(self):
        self._stop_event.set()

    def stopped(self):
        self._stop_event.is_set()

    def inRepetitiveScheduleRange(self, rule):
        start = QDateTime.fromString(rule.start, "MMddyyyyhh:mm:ss")
        end = QDateTime.fromString(rule.end, "MMddyyyyhh:mm:ss")
        now = QDateTime().currentDateTime()
        
        startTime = start.time()
        endTime = end.time()
        currTime = now.time()

        startDayOfWeek = start.date().dayOfWeek()
        endDayOfWeek = end.date().dayOfWeek()
        currDayOfWeek = now.date().dayOfWeek()
        
        duration = ((endDayOfWeek - startDayOfWeek) + 7) % 7
        curDuration = ((currDayOfWeek - startDayOfWeek) + 7) % 7

        # True if in valid range else False
        return not((curDuration > duration) or (curDuration == duration and (currTime < startTime or currTime >= endTime)))
    
    def inOneTimeScheduleRange(self, rule):
        startTime = QDateTime.fromString(rule.start, "MMddyyyyhh:mm:ss").toSecsSinceEpoch()
        endTime = QDateTime.fromString(rule.end, "MMddyyyyhh:mm:ss").toSecsSinceEpoch()
        now = QDateTime().currentSecsSinceEpoch()
        return not (now < startTime or now >= endTime)

class DataChangeHandler(QThread):
    datachanged = pyqtSignal(dict)
    
    def __init__(self, data):
        QThread.__init__(self)
        self.data = data
        self.previousData = deepcopy(self.data.scheduled_rules)
        self._stop_event = Event()

    def run(self):
        while(True):
            if self.stopped():
                break
            sleep(2)
            if self.hasDataChanged():
                # Update the data
                self.previousData = deepcopy(self.data.scheduled_rules)
                
                # Emit the change
                self.datachanged.emit(self.previousData)

    def hasDataChanged(self):
        # Overloaded comparison
        return self.previousData != self.data.scheduled_rules
    
    def stop(self):
        self._stop_event.set()

    def stopped(self):
        self._stop_event.is_set()