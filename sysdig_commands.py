#!/bin/python

# This class is responsible for the sysdig commands that will be executed.
# It has a set of predefined commands
# It will also be responsible for throwing exceptions in case an invalid sysdig
# command is issued.
from sysdig_fields import SysdigFields

f = SysdigFields()
class SysdigCommands:
    def __init__(self):
        a = 10
        self.staticCommands = {
                    'cpu_top_processes': 'sysdig command',
                    'errors_top_processes':'sysdig command',
                    'errors_top_system_calls':'sysdig command',
                    'network_top_processes':'sysdig command',
                    '...':'sysdig command',
                }



    ''' PUBLIC FUNCTIONS '''
    # Returns the specified dynamic command as part of a tuple
    # Returns a tuple of the type (0, "sysdig proc.name=cat")on success
    # or (-1, "Reason for error in args") otherwise
    def getDynamicCommand(self, *args):
        a = 10
    
    # Returns the specified static command as part of a tuple
    # Returns a tuple of the type (0, "sysdig proc.name=cat")on success
    # or (-1, "Reason for error in args") otherwise
    def getStaticCommand(self, *args):
        a = 10
    
    
    
    
    ''' PRIVATE FUNCTIONS '''
    # Returns True if process is a valid process on the linux machine
    # False otherwise
    def _isProcessValid(self, proc):
        a = 10
        
    # Returns True if ip is a valid IP of type "xxx.xxx.xxx.xxx"
    # False otherwise
    def _isIPValid(self, ip):
        a = 10
        
    # Returns True if the user exists on the linux machine
    # False otherwise
    def _isUserValid(self, user):
        a = 10
        
    # Returns True if the directory exists on the linux machin
    # False otherwise
    def _isDirValid(self, dir):
        a = 10
        
    # Returns True if the requsts is a valid HTTP request
    # False otherwise
    def _isHttpRequestValid(self, req):
        a = 10
        
    # Returns True if the query is a valid SQL query
    # False otherwise
    def _isSqlQueryValid(sql):
        a = 10
        
    def _isShellIdValid(id):
        a = 10
    