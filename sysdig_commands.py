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
                    # Purely static
                    'cpu_top_processes': 'sudo sysdig -c topprocs_cpu',
                    'errors_files_most_time_spent':'sudo sysdig -c topfiles_time',
                    'errors_top_system_calls_errors': 'sudo sysdig -c topscalls "evt.failed=true"',
                    'errors_top_system_calls_times' : 'sudo sysdig -c topscalls_time',
                    'errors_top_file_errors': 'sudo sysdig -c topfiles_errors',
                    'errors_top_processes':'sudo sysdig -c topprocs_errors',
                    'network_top_processes_bandwidth' : 'sudo sysdig -c topprocs_net',
                    'network_top_connections_bandwidth': 'sudo sysdig -c topconns',
                    
                    
                    # Can be dynamic
                    'errors_top_failed_file_opens': 'sudo sysdig "evt.type=open and evt.failed=true"',
                    'cpu_stdout':'sudo sysdig -s4096 -A -c stdout',
                    'network_spy_ip':'sudo sysdig -c spy_ip',
                    'security_commands_executed_by_id':'sudo sysdig -c spy_users',
                    'security_directories_visited_by_user': 'sudo sysdig "evt.type=chdir"',
                    'security_file_opens_at' : 'sudo sysdig evt.type=open and fd.name contains ',
                    'application_request_of_type': 'sudo sysdig -s 2000 -A -c echo_fds fd.port=80 and evt.buffer contains',
                    'application_queries_of_type': '  sudo sysdig -s 2000 -A -c echo_fds evt.buffer contains ',
                }
        

    ''' PUBLIC FUNCTIONS '''
    # Returns the specified dynamic command as part of a tuple
    # Returns a tuple of the type (0, "sysdig proc.name=cat")on success
    # or (-1, "Reason for error in args") otherwise
    def getDynamicCommand(self, name, *args):
        command = ''
        if name in self.staticCommands:
            command += self.staticCommands[name] +' '+args
        else:
            #do some complicated chissllesss
            a = 10
        return command
    
    # Returns the specified static command as part of a tuple
    # Returns a tuple of the type (0, "sysdig proc.name=cat")on success
    # or (-1, "Reason for error in args") otherwise
    def getStaticCommand(self, name):
        return self.staticCommands[name]
    
    
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
    
