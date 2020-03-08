
class FalcoRules:
    def __init__(self):
        self.falco_lists = {}
        self.falco_rules = {
            'program_executed': 
'''
- list: unexpected_programs
  items: {0}

- rule: The specified program is executed
  desc: An event will trigger every time you run the specified process
  condition: evt.type = execve and evt.dir = < and proc.name in (unexpected_programs)
  output: "(proc=%proc.name) run in (user=%user.name parent=%proc.pname cmdline=%proc.cmdline)" 
  priority: ERROR
  tags: [users]    
''',
            'process_file_open':
'''
- list: failing_processes
  items: {0}

- rule: The specified process gives failed file opens
  desc: An event will trigger every time the specified process cannot open a file
  condition: evt.type = openat and evt.failed = true and proc.name in (failing_processes)
  output: "File open error from proc=%proc.name run by user=%user.name with type=%evt.type on file=%fd.name"
  priority: ERROR
  tags: [filesystem]
''',
            'directory_file_open':
'''
- rule: File open in the specified directory
  desc: Get an event when a file is opened at the specified directory
  condition: evt.type=openat and fd.name contains {0}
  output: "File %fd.name opened from user %user.name"
  priority: WARNING
  tags: [filesystem]
''',
            'unknown_users':
'''
- list: known_users
  items: {0}

- rule: Directories visited from unknown users
  desc: Detect the directories that a user traverses using cd
  condition: evt.type=chdir and not user.name in (known_users)
  output: "Unknown user (user=%user.name) changed directory to (%evt.args)"
  priority: WARNING
  tags: [filesystem]
''',        
            'known_users':
'''
- list: users_to_monitor
  items: {0}

- rule: Directories visited from a known user
  desc: Detect the directories that the specified user traverses using cd
  condition: evt.type=chdir and user.name in (users_to_monitor)
  output: "Known user (user=%user.name) changed directory to (%evt.args)"
  priority: INFORMATIONAL
  tags: [filesystem]
''',
            'outbound_ip_traffic':
'''
- list: outbound_ip_list
  items: {0}

- rule: Spy outbound activities related to IP
  desc: Detect connections to specified IP
  condition: (outbound) and fd.sip in (outbound_ip_list) or fd.cip in (outbound_ip_list)
  output: "Connection to IP detected (command=%proc.cmdline connection=%fd.name user=%user.name)"
  priority: INFORMATIONAL
  tags: [network]
''',
            'inbound_ip_traffic':
'''
- list: inbound_ip_list
  items: {0}

- rule: Spy inbound activities related to IP
  desc: Detect connections from specified IP
  condition: (inbound) and fd.sip in (inbound_ip_list) or fd.cip in (inbound_ip_list)
  output: "Connection from IP detected (command=%proc.cmdline connection=%fd.name user=%user.name)"
  priority: INFORMATIONAL
  tags: [network]
''',
            'malicious_traffic':
'''
- list: malicious_ip_list
  items: {0}

- rule: Spy the specified IP
  desc: Detect connections to/from the specified IP
  condition: (inbound or outbound) and fd.sip in (malicious_ip_list) or fd.cip in (malicious_ip_list)
  output: "Suspicious connection to/from a malicious IP detected (command=%proc.cmdline connection=%fd.name user=%user.name)"
  priority: EMERGENCY
  tags: [network]
''',
            'inbound_mongodb_traffic':
'''
- macro: mongodb_server_port
  condition: fd.sport = 27017
- macro: mongodb_shardserver_port
  condition: fd.sport = 27018
- macro: mongodb_configserver_port
  condition: fd.sport = 27019
- macro: mongodb_webserver_port
  condition: fd.sport = 28017

- rule: Mongodb unexpected network inbound traffic
  desc: inbound network traffic to mongodb on a port other than the standard ports
  condition: >
    user.name = mongodb and inbound and not (mongodb_server_port or
    mongodb_shardserver_port or mongodb_configserver_port or mongodb_webserver_port)
  output: "Inbound network traffic to MongoDB on unexpected port (connection=%fd.name)"
  priority: WARNING
''',
            'inbound_http_traffic':
'''
- rule: HTTP server unexpected network inbound traffic
  desc: inbound network traffic to a http server program on a port other than the standard ports
  condition: proc.name in (http_server_binaries) and inbound and fd.sport != 80 and fd.sport != 443
  output: "Inbound network traffic to HTTP Server on unexpected port (connection=%fd.name)"
  priority: WARNING
''',
            'inbound_mysql_traffic':
'''
- rule: Mysql unexpected network inbound traffic
  desc: inbound network traffic to mysql on a port other than the standard ports
  condition: user.name = mysql and inbound and fd.sport != 3306
  output: "Inbound network traffic to MySQL on unexpected port (connection=%fd.name)"
  priority: WARNING
''',
            'inbound_kafka_traffic':
'''
- rule: Kafka unexpected network inbound traffic
  desc: inbound network traffic to kafka on a port other than the standard ports
  condition: user.name = kafka and inbound and fd.sport != 9092
  output: "Inbound network traffic to Kafka on unexpected port (connection=%fd.name)"
  priority: WARNING
'''
        }

    def setArgs(self, name):
        args = ''
        if name not in self.falco_rules:
            index = name.rfind('_')
            args = name[index + 1:]
            name = name[:index]

        if name not in self.falco_lists:
            self.falco_lists[name] = [args]
        else:
            self.falco_lists[name].append(args)

    def getRules(self):
        rules = ''
        for name in self.falco_lists:
            args = self.falco_lists[name]
            # non-parametric rules
            if len(args) == 0:
                rules += self.falco_rules[name] + '\n'
            # populating ip lists
            elif name.endswith('traffic'):
                args = str(list(map(lambda x: '\"' + x + '\"', args)))
                rules += self.falco_rules[name].format(args)
            # directory rules should be seperated
            elif name.startswith('directory'):
                for dir in args:
                  rules += self.falco_rules[name].format(dir)
            # the rest of the rules
            else:
              rules += self.falco_rules[name].format(args)

        return rules


    