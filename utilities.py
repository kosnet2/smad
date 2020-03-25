from PyQt5 import QtCore, QtGui, QtWidgets
from glob import glob
import os
import re
import datetime

""" PLOTTING """
import sys
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from collections import deque
import pytz
UNIX_EPOCH = datetime.datetime(1970, 1, 1, 0, 0)

# Function to get current UNIX_EPOCH to avoid calling datetime all the time
def getUnixEpoch():
    return UNIX_EPOCH

# Get current timestamp 
def now_timestamp():
    return(int((datetime.datetime.now() - getUnixEpoch()).total_seconds() * 1e6))

# Get time in seconds
def int2dt(ts):
    return(datetime.datetime.utcfromtimestamp(float(ts)/1e6))

# Custom time axis for showing timestamps
class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def tickStrings(self, values, scale, spacing):
        return [int2dt(value).strftime("%H:%M:%S") for value in values]

def showMessageBox(message, title, icon=QtWidgets.QMessageBox.Critical):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(icon)
    msg.setText(message)
    msg.setWindowTitle(title)
    msg.exec_()

def getValidRules(text, name, argType):
    def isValidArgType(argType, line):
        if argType == 'process':
            # Protection against command injection
            if re.search('[&|;#$]', line):
                return False
            stream = os.popen('command -v ' + line)
            if stream.read() == '':
                return False
        elif argType == 'ip':
            validIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
            if not re.match(validIpAddressRegex, line):
                return False
        elif argType == 'user':
            # Protection against command injection
            if re.match('[&|;#$]', line):
                return False
        elif argType == 'dir':
            # Protection against command injection
            if re.search('[&|;#$]', line):
                return False
            stream = os.popen('test -d '+ line +' && echo "yeap" || echo "nope"')
            output = stream.read()
            if 'nope' in output:
                return False

        return True

    # split multiline
    validRules = []
    invalidRules = []
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line != '' and isValidArgType(argType, line):
            validRules.append(name + line)
        else:
            invalidRules.append(name + line)

    return (validRules, invalidRules)

def getValidMonitors(text, name, argType):
    def isValidArgType(argType, line):
        # Validate linux commands
        if argType == 'process':
            # Protection against command injection
            if re.search('[&|;#$]', line):
                return False

            stream = os.popen('command -v ' + line)
            if stream.read() == '':
                return False
        # Validate ip addresses
        elif argType == 'ip':
            validIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
            if not re.match(validIpAddressRegex, line):
                return False
        # Validate login shell id exists
        elif argType == 'shellid':
            shellIds = [shellId.split('/')[-1] for shellId in glob('/dev/pts/*')]
            if line not in shellIds:
                return False
        # Validate linux user exists
        elif argType == 'user':
            # Protection against command injection
            if re.match('[&|;#$]', line):
                return False

            stream = os.popen('grep ' + line +' /etc/passwd')
            output = stream.read()
            if output == '':
                return False
        # Validate directory exists                 
        elif argType == 'dir':
            # Protection against command injection
            if re.search('[&|;#$]', line):
                return False

            stream = os.popen('test -d '+ line +' && echo "yeap" || echo "nope"')
            output = stream.read()
            if 'nope' in output:
                return False
        # Validate HTTP request type
        elif argType == 'request':
            validHTTPRequests = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
            if line not in validHTTPRequests:
                return False
        # Validate SQL request type
        elif argType == 'query':
            validSQLQueries = ['ALTER', 'CREATE','DROP','RENAME','TRUNCATE', 'DELETE', 'INSERT', 'UPDATE', 'GRANT', 'REVOKE', 'COMMIT', 'ROLLBACK', 'SAVEPOINT', 'SELECT']
            if line not in validSQLQueries:
                return False
            
        return True
        
    validMonitors = []
    invalidMonitors = []
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line != '' and isValidArgType(argType, line):
            validMonitors.append(name + line)
        else:
            invalidMonitors.append(name + line)
            
    return (validMonitors, invalidMonitors)
