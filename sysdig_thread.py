import threading
import subprocess
import shlex
import os
import re

class SysdigThread(threading.Thread):
    def __init__(self, name, monitor):
        super(SysdigThread, self).__init__()
        self.name = name
        self.monitor = monitor
        self._stop_event = threading.Event()
        self.time_dict = {'ps': 10 ** -6, 'ns': 10 ** -3, 'μs': 1, 'us' : 1, 'ms': 10 ** 3, 's': 10 ** 6, 'm': 60 * (10 ** 6)}
        self.size_dict = {'B': 1, 'KB': 2 ** 10, 'MB': 2 ** 20, 'GB': 2 ** 30, 'TB': 2 ** 40, 'PB': 2 ** 50}
        
    def run(self):
        process = subprocess.Popen(shlex.split(self.monitor.command), stdout=subprocess.PIPE)
        while True:
            if self.stopped():
                process.kill()
                os.wait()
                break
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                line = output.strip().decode('utf-8')
                if self.name == 'cpu_top_processes':
                    if '%' in line:
                        cpu_usage = line[:line.index('%')]
                        if cpu_usage[0].isdigit():
                            cpu_usage = float(cpu_usage)
                            for alert in self.monitor.alerts:
                                op, value, unit= alert.metrics.split(' ')
                                if op == '<' and cpu_usage < float(value):
                                    print(op, value, unit, 'Less bro', line)
                                elif op == '>' and cpu_usage > float(value):
                                    print(op, value, unit, 'Tis bigger', line)
                                elif  op == '=' and cpu_usage == float(value):
                                    print(op, value, unit, 'Equals man!', line)
                elif self.name == 'errors_top_system_calls_errors':
                    if line[0].isdigit():
                        num_errors, sys_call = re.findall(r'\w+', line)
                        num_errors = int(num_errors)
                        for alert in self.monitor.alerts:
                            # TODO: ADD ERRORS UNIT HERE LATER
                            op, value= alert.metrics.split(' ')
                            if op == '<' and num_errors < int(value):
                                print(op, value, 'Less bro', line)
                            elif op == '>' and num_errors > int(value):
                                print(op, value, 'Tis bigger', line)
                            elif  op == '=' and num_errors == int(value):
                                print(op, value, 'Equals man!', line)
                    
                elif self.name == 'errors_top_file_errors':
                    if line[0].isdigit():
                        num_errors, filename = re.findall(r'\w+', line)
                        num_errors = int(num_errors)
                        for alert in self.monitor.alerts:
                            # TODO: ADD ERRORS UNIT HERE LATER
                            op, value= alert.metrics.split(' ')
                            if op == '<' and num_errors < int(value):
                                print(op, value, 'Less bro', line)
                            elif op == '>' and num_errors > int(value):
                                print(op, value, 'Tis bigger', line)
                            elif  op == '=' and num_errors == int(value):
                                print(op, value, 'Equals man!', line)
                                    
                                    
                elif self.name == 'errors_files_most_time_spent':
                    if line[0].isdigit():
                        time, filename = re.findall(r'\w+', line)
                        if time[-2].isdigit():
                            time, timeunit = time[:-1], time[-1:]
                        else:
                            time, timeunit = time[:-2], time[-2:]
                        
                        time = float(time)
                        time *= self.time_dict[timeunit]
                        for alert in self.monitor.alerts:
                            op, value, unit = alert.metrics.split(' ')
                            value = float(value) * self.time_dict[unit]
                            if op == '<' and time < value:
                                print(op, value, 'Less bro', line)
                            elif op == '>' and time > value:
                                print(op, value, 'Tis bigger', line)
                            elif  op == '=' and time == value:
                                print(op, value, 'Equals man!', line)
                        
                elif self.name == 'errors_top_processes':
                    if line[0].isdigit():
                        num_errors, process, pid = re.findall(r'\w+', line)
                        num_errors = int(num_errors)
                        for alert in self.monitor.alerts:
                            # TODO: ADD ERRORS UNIT HERE LATER
                            op, value = alert.metrics.split(' ')
                            if op == '<' and num_errors < int(value):
                                print(op, value, 'Less bro', line)
                            elif op == '>' and num_errors > int(value):
                                print(op, value, 'Tis bigger', line)
                            elif  op == '=' and num_errors == int(value):
                                print(op, value, 'Equals man!', line)     
                                
                elif self.name == 'errors_top_system_calls_errors_time':
                    if line[0].isdigit():
                        time, syscall = re.findall(r'\w+', line)
                        if time[-2].isdigit():
                            time, timeunit = time[:-1], time[-1:]
                        else:
                            time, timeunit = time[:-2], time[-2:]
                        
                        time = float(time)
                        time *= self.time_dict[timeunit]
                        for alert in self.monitor.alerts:
                            op, value, unit = alert.metrics.split(' ')
                            value = float(value) * self.time_dict[unit]
                            if op == '<' and time < value:
                                print(op, value, 'Less bro', line)
                            elif op == '>' and time > value:
                                print(op, value, 'Tis bigger', line)
                            elif  op == '=' and time == value:
                                print(op, value, 'Equals man!', line)
                                
                elif self.name == 'network_top_connections_bandwidth':
                    if line[0].isdigit():
                        res = re.findall(r'[\S]+', line)
                        size, proto = res[0], res[1]
                        if len(res) == 2:
                            ip = res[1]
                        elif len(res) > 3:
                            size, proto, ip = res[0], ' '.join(res[1:-1]), res[-1]
                            
                        # make sure we get no erros on parsing
                        if size[-1].isdigit():
                            size += 'B'
                        if size[-2].isdigit():
                            size, sizeunit = size[:-1], size[-1:]
                        else:
                            size, sizeunit = size[:-2], size[-2:]
                        
                        size = float(size)
                        size *= self.size_dict[sizeunit]
                        for alert in self.monitor.alerts:
                            op, value, unit = alert.metrics.split(' ')
                            value = float(value) * self.size_dict[unit]
                            if op == '<' and size < value:
                                print(op, value, 'Less bro', line)
                            elif op == '>' and size > value:
                                print(op, value, 'Tis bigger', line)
                            elif  op == '=' and size == value:
                                print(op, value, 'Equals man!', line)     
                                
                elif self.name == 'network_top_processes_bandwidth':
                    if line[0].isdigit():

                        print(line)
                        res = re.findall(r'[\S]+', line)
                        size, proc, pid = res[0], ' '.join(res[1:-1]), res[-1]

                        # make sure we get no erros on parsing
                        if size[-1].isdigit():
                            size += 'B'
                        if size[-2].isdigit():
                            size, sizeunit = size[:-1], size[-1:]
                        else:
                            size, sizeunit = size[:-2], size[-2:]
                        size = float(size)
                        size *= self.size_dict[sizeunit]
                        for alert in self.monitor.alerts:
                            op, value, unit = alert.metrics.split(' ')
                            value = float(value) * self.size_dict[unit]
                            if op == '<' and size < value:
                                print(op, value, 'Less bro', line)
                            elif op == '>' and size > value:
                                print(op, value, 'Tis bigger', line)
                            elif  op == '=' and size == value:
                                print(op, value, 'Equals man!', line)  
                    
            rc = process.poll()

    def stop(self):	
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
