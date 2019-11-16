# This class is responsible for the sysdig commands that will be executed.
# It has a set of predefined commands
# It will also be responsible for throwing exceptions in case an invalid sysdig command is issued.
class SysdigCommands:
    def __init__(self):
        self.sysdig_commands = {
            # Needs metrics
            'cpu_top_processes': {
                'command': 'sysdig --unbuffered -c topprocs_cpu',
                'metricType': 'percentage'
            },
            'errors_files_most_time_spent': {
                'command': 'sysdig --unbuffered -c topfiles_time',
                'metricType': 'time'
            },
            'errors_top_system_calls_errors': {
                'command': 'sysdig --unbuffered -c topscalls "evt.failed=true"',
                'metricType': 'number'
            },
            'errors_top_system_calls_errors_time': {
                'command': 'sysdig --unbuffered -c topscalls_time',
                'metricType': 'time'
            },
            'errors_top_file_errors': {
                'command': 'sysdig --unbuffered -c topfiles_errors',
                'metricType': 'number'
            },
            'errors_top_processes': {
                'command': 'sysdig --unbuffered -c topprocs_errors',
                'metricType': 'number'
            },
            'network_top_processes_bandwidth': {
                'command': 'sysdig --unbuffered -c topprocs_net',
                'metricType': 'size'
            },
            'network_top_connections_bandwidth': {
                'command': 'sysdig --unbuffered -c topconns',
                'metricType': 'size' 
            },
                    
            # Doesn't need metrics
            'errors_top_failed_file_opens': {
                'command': 'sysdig --unbuffered evt.type=openat and evt.failed=true and proc.name=',
                'metricType': 'none'
            },
            'cpu_stdout': {
                'command': 'sysdig --unbuffered -s 4096 -A -c stdout proc.name=',
                'metricType': 'none'
            },
            'network_spy_ip': {
                'command': 'sysdig --unbuffered -c spy_ip ',
                'metricType': 'none'
            },
            'security_commands_executed_by_id': {
                'command': 'sysdig --unbuffered -c spy_users proc.loginshellid=',
                'metricType': 'none'
            },
            'security_directories_visited_by_user': {
                'command': 'sysdig --unbuffered evt.type=chdir and user.name=',
                'metricType': 'none'
            },
            'security_file_opens_at': {
                'command': 'sysdig --unbuffered evt.type=openat and fd.name contains ',
                'metricType': 'none'
            },
            'application_request_of_type': {
                'command': 'sysdig --unbuffered -s 2000 -A -c echo_fds fd.port=80 and evt.buffer contains ',
                'metricType': 'none'
            },
            'application_queries_of_type': {
                'command': 'sysdig  --unbuffered -s 2000 -A -c echo_fds evt.buffer contains ',
                'metricType': 'none'
            }
        }

    def getCommand(self, name):
        arg = ''
        if name not in self.sysdig_commands:
            index = name.rfind('_')
            arg = name[index + 1:]
            name = name[:index]

        commandDict = dict(self.sysdig_commands[name])
        commandDict['command'] += arg
        return commandDict
        