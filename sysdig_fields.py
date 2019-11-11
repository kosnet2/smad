# This class defines the majority of sysdig fields in order to be used
# in another pieces of this software.
# For now " Containers, Kubernetes, Marathon, Span, Evtin " field classes
# have limited functionality. They might be added later
class SysdigFields: 

    class FileDescriptor:
        # the unique number identifying the file descriptor
        fd_num = 'fd.num'
        # type of FD. Can be 'file', 'directory', 'ipv4', 'ipv6', 'unix',
        # 'pipe', 'event', 'signalfd', 'eventpoll', 'inotify' or 'signal
        # fd'
        fd_type = 'fd.type'  
        # type of FD as a single character. Can be 'f' for file, 4 for IP
        # v4 socket, 6 for IPv6 socket, 'u' for unix socket, p for pipe, 
        # 'e' for eventfd, 's' for signalfd, 'l' for eventpoll, 'i' for i
        # notify, 'o' for unknown.
        fd_typechar = 'fd.typechar'
        # FD full name. If the fd is a file, this field contains the full
        # path. If the FD is a socket, this field contain the connection
        # tuple.
        fd_name = 'fd.name'         
        # If the fd is a file, the directory that contains it.
        fd_directory = 'fd.directory'    
        # If the fd is a file, the filename without the path.
        fd_filename = 'fd.filename'     
        #(FILTER ONLY) matches the ip address (client or server) of the fd.
        fd_ip = 'fd.ip'   
        # client IP address.
        fd_cip = 'fd.cip'          
        # server IP address.
        fd_sip = 'fd.sip'          
        # local IP address.
        fd_lip = 'fd.lip'
        # remote IP address
        fd_rip = 'fd.rip' 
        # (FILTER ONLY) matches the port (either client or server) of the
        # fd.
        fd_port = 'fd.port'         
        # for TCP/UDP FDs, the client port.
        fd_cport = 'fd.cport'        
        # for TCP/UDP FDs, server port.
        fd_sport = 'fd.sport'        
        # for TCP/UDP FDs, the local port.
        fd_lport = 'fd.lport'        
        # for TCP/UDP FDs, the remote port.
        fd_rport = 'fd.rport'        
        # the IP protocol of a socket. Can be 'tcp', 'udp', 'icmp' or 'raw'
        fd_l4proto = 'fd.l4proto'      
        # the socket family for socket events. Can be 'ip' or 'unix'.
        fd_sockfamily = 'fd.sockfamily'   
        # 'true' if the process owning this FD is the server endpoint in 
        # the connection.
        fd_is_server = 'fd.is_server'
        # a unique identifier for the FD, created by chaining the FD numb
        # er and the thread ID.
        fd_uid = 'fd.uid'          
        # chaining of the container ID and the FD name. Useful when tryin
        # g to identify which container an FD belongs to.
        fd_containername = 'fd.containername'
        # chaining of the container ID and the directory name. Useful whe
        # n trying to identify which container a directory belongs to.
        fd_containerdirectory = 'fd.containerdirectory'
        # (FILTER ONLY) matches the protocol (either client or server) of
        # the fd.                        
        fd_proto = 'fd.proto'        
        # for TCP/UDP FDs, the client protocol.
        fd_cproto = 'fd.cproto'       
        # for TCP/UDP FDs, server protocol.
        fd_sproto = 'fd.sproto'       
        # for TCP/UDP FDs, the local protocol.
        fd_lproto = 'fd.lproto'       
        # for TCP/UDP FDs, the remote protocol.
        fd_rproto = 'fd.rproto'       
        # (FILTER ONLY) matches the IP network (client or server) of the fd.
        fd_net = 'fd.net'          
        # (FILTER ONLY) matches the client IP network of the fd.
        fd_cnet = 'fd.cnet'         
        # (FILTER ONLY) matches the server IP network of the fd.
        fd_snet = 'fd.snet'         
        # (FILTER ONLY) matches the local IP network of the fd.
        fd_lnet = 'fd.lnet'         
        # (FILTER ONLY) matches the remote IP network of the fd.
        fd_rnet = 'fd.rnet'         
        # for TCP/UDP FDs, 'true' if the socket is connected.
        fd_connected = 'fd.connected'
        # True when an event changes the name of an fd used by this event
        # . This can occur in some cases such as udp connections where th
        # e connection tuple changes.
        fd_name_changed = 'fd.name_changed' 
        # Domain name associated with the client IP address.
        fd_cip_name = 'fd.cip.name'     
        # Domain name associated with the server IP address.
        fd_sip_name = 'fd.sip.name'     
        # Domain name associated with the local IP address.
        fd_lip_name = 'fd.lip.name'     
        # Domain name associated with the remote IP address.
        fd_rip_name ='fd.rip.name'     
        # device number (major/minor) containing the referenced file
        fd_dev = 'fd.dev'         
        # major device number containing the referenced file
        fd_dev_major = 'fd.dev.major'    
        # minor device number containing the referenced file
        fd_dev_minor = 'fd.dev.minor'    
        
    class Process:
        # the id of the process generating the event.
        proc_pid = 'proc.pid'
        # the first command line argument (usually the executable name or
        # a custom one).
        proc_exe = 'proc.exe'
        # the name (excluding the path) of the executable generating the 
        # event.
        proc_name = 'proc.name'
        # the arguments passed on the command line when starting the proc
        # ess generating the event.
        proc_args = 'proc.args'
        # the environment variables of the process generating the event.
        proc_env = 'proc.env'
        # full process command line, i.e. proc.name + proc.args.
        proc_cmdline = 'proc.cmdline'
        # full process command line, with exe as first argument, i.e. pro
        # c.exe + proc.args.
        proc_exeline = 'proc.exeline'
        # the current working directory of the event.
        proc_cwd = 'proc.cwd'
        # the number of threads that the process generating the event cur
        # rently has, including the main process thread.
        proc_nthreads = 'proc.nthreads'
        # the number of child threads that the process generating the eve
        # nt currently has. This excludes the main process thread.
        proc_nchilds = 'proc.nchilds'
        # the pid of the parent of the process generating the event.
        proc_ppid = 'proc.ppid'
        # the name (excluding the path) of the parent of the process gene
        # rating the event.
        proc_pname = 'proc.pname'
        # the full command line (proc.name + proc.args) of the parent of 
        # the process generating the event.
        proc_pcmdline = 'proc.pcmdline'
        # the pid of one of the process ancestors. E.g. proc.apid[1] retu
        # rns the parent pid, proc.apid[2] returns the grandparent pid, a
        # nd so on. proc.apid[0] is the pid of the current process. proc.
        # apid without arguments can be used in filters only and matches 
        # any of the process ancestors, e.g. proc.apid=1234.
        proc_apid = 'proc.apid'
        # the name (excluding the path) of one of the process ancestors. 
        # E.g. proc.aname[1] returns the parent name, proc.aname[2] retur
        # ns the grandparent name, and so on. proc.aname[0] is the name o
        # f the current process. proc.aname without arguments can be used
        # in filters only and matches any of the process ancestors, e.g.
        # proc.aname=bash.
        proc_aname = 'proc.aname'
        # the pid of the oldest shell among the ancestors of the current 
        # process, if there is one. This field can be used to separate di
        # fferent user sessions, and is useful in conjunction with chisel
        # s like spy_user.
        proc_loginshellid = 'proc.loginshellid'
        # number of nanoseconds since the process started.
        proc_duration = 'proc.duration'
        # number of open FDs for the process
        proc_fdopencount = 'proc.fdopencount'
        # maximum number of FDs the process can open.
        proc_fdlimit = 'proc.fdlimit'
        # the ratio between open FDs and maximum available FDs for the pr
        # ocess.
        proc_fdusage = 'proc.fdusage'
        # total virtual memory for the process (as kb).
        proc_vmsize = 'proc.vmsize'
        # resident non-swapped memory for the process (as kb).
        proc_vmrss = 'proc.vmrss'
        # swapped memory for the process (as kb).
        proc_vmswap = 'proc.vmswap'
        # number of major page faults since thread start.
        thread_pfmajor = 'thread.pfmajor'  
        # number of minor page faults since thread start.
        thread_pfminor = 'thread.pfminor'  
        # the id of the thread generating the event.
        thread_tid = 'thread.tid'    
        # 'true' if the thread generating the event is the main one in th
        # e process.
        thread_ismain = 'thread.ismain'
        # CPU time spent by the last scheduled thread, in nanoseconds. Ex
        # ported by switch events only.
        thread_exectime = 'thread.exectime' 
        # Total CPU time, in nanoseconds since the beginning of the captu
        # re, for the current thread. Exported by switch events only.
        thread_totexectime = 'thread.totexectime'
        # all the cgroups the thread belongs to, aggregated into a single
        # string.                        
        thread_cgroups = 'thread.cgroups'  
        # the cgroup the thread belongs to, for a specific subsystem. E.g
        # . thread.cgroup.cpuacct.
        thread_cgroup = 'thread.cgroup'
        # the id of the thread generating the event as seen from its curr
        # ent PID namespace.
        thread_vtid = 'thread.vtid'
        # the id of the process generating the event as seen from its cur
        # rent PID namespace.
        proc_vpid = 'proc.vpid'
        # the CPU consumed by the thread in the last second.
        thread_cpu = 'thread.cpu'      
        # the user CPU consumed by the thread in the last second.
        thread_cpu.user = 'thread.cpu.user'
        # the system CPU consumed by the thread in the last second.
        thread_cpu.system = 'thread.cpu.system'
        # For the process main thread, this is the total virtual memory f
        # or the process (as kb). For the other threads, this field is ze
        # ro.
        thread_vmsize = 'thread.vmsize'
        # For the process main thread, this is the resident non-swapped m
        # emory for the process (as kb). For the other threads, this fiel
        # d is zero.
        thread_vmrss = 'thread.vmrss'
        # the session id of the process generating the event.
        proc_sid = 'proc.sid'
        # the name of the current process's session leader. This is eithe
        # r the process with pid=proc.sid or the eldest ancestor that has
        # the same sid as the current process.
        proc_sname = 'proc.sname'
        # The controlling terminal of the process. 0 for processes withou
        # t a terminal.
        proc_tty = 'proc.tty'
        # The full executable path of the process.
        proc_exepath = 'proc.exepath'    
        # the process group id of the process generating the event, as se
        # en from its current PID namespace.
        proc_vpgid = 'proc.vpgid'     
        # true if this process is running as a part of the container's he
        # alth check.
        proc_is_container_healthcheck = 'proc.is_container_healthcheck'
        # true if this process is running as a part of the container's li
        # veness probe.
        proc_is_container_liveness_probe = 'proc.is_container_liveness_probe'
        # true if this process is running as a part of the container's re
        # adiness probe.
        proc_is_container_readiness_probe = 'proc.is_container_readiness_probe'

    class Event:
        # event number
        evt_num = 'evt.num'
        # event timestamp as a time string that including nanoseconds
        evt_time = 'evt.time'
        # event timestamp as a time string without nanoseconds
        evt_time_s = 'evt.time.s'
        # event timestamp as a time string that includes the date
        evt_datetime = 'evt.datetime'
        # event direction
        evt_dir = 'evt.dir'
        # event type
        evt_type = 'evt.type'
        # event category
        # Eg 'file' for file operations, 'net' for network operations
        # 'memory' for memory operations
        evt_category = 'evt.category'
        # number of CPU where the event happened
        evt_cpu = 'evt.cpu'
        # all the event arguments, aggregated into a single string.
        evt_args = 'evt.args'
        # for most events, this field returns the same value as evt.args.
        # However, for some events (like writes to /dev/log) it provides
        # higher level information coming from decoding the arguments.
        evt_info = 'evt.info'
        # event return value, as a string. If the event failed, the resul
        # t is an error code string (e.g. 'ENOENT'), otherwise the result
        # is the string 'SUCCESS'.
        evt_res = 'evt.res'
        # 'true' for events that returned an error status.
        evt_failed = 'evt.failed'
        # 'true' for events that read or write to FDs, like read(), send,
        # recvfrom(), etc.
        evt_is_io = 'evt.is_io'
        # 'true' for events that read from FDs, like read(), recv(), recv
        # from(), etc.
        evt_is_io_read = 'evt.is_io_read'        
        # 'true' for events that write to FDs, like write(), send(), etc.
        evt_is_io_write = 'evt.is_io_write'
        # 'r' for events that read from FDs, like read(); 'w' for events
        # that write to FDs, like write().
        evt_io_dir = 'evt.io_dir'
        # 'true' for events that make the thread wait, e.g. sleep(), sele
        # ct(), poll().
        evt_is_wait = 'evt.is_wait'
        # for events that make the thread wait (e.g. sleep(), select(), p
        # oll()), this is the time spent waiting for the event to return,
        # in nanoseconds.
        evt_wait_latency = 'evt.wait_latency'
        # 'true' for events that are writes to /dev/log.
        evt_is_syslog = 'evt.is_syslog'    
        # This filter field always returns 1 and can be used to count eve
        # nts from inside chisels.
        evt_count = 'evt.count' 
        # This filter field returns 1 for events that returned with an er
        # ror, and can be used to count event failures from inside chisels
        evt_count_error = 'evt.count.error'
        # This filter field returns 1 for events that returned with an er
        # ror and are related to file I/O, and can be used to count event
        # failures from inside chisels.
        evt_count_error_file = 'evt.count.error.file'
        # This filter field returns 1 for events that returned with an er
        # ror and are related to network I/O, and can be used to count ev
        # ent failures from inside chisels.
        evt_count_error_net = 'evt.count.error.net'
        # This filter field returns 1 for events that returned with an er
        # ror and are related to memory allocation, and can be used to co
        # unt event failures from inside chisels.
        evt_count_error_memory = 'evt.count.error.memory'
        # This filter field returns 1 for events that returned with an er
        # ror and are related to none of the previous categories, and can
        # be used to count event failures from inside chisels.
        evt_count_error_other ='evt.count.error.other'
        # This filter field returns 1 for exit events, and can be used to
        # count single events from inside chisels.
        evt_count_exit = 'evt.count.exit'
        # Absolute path calculated from dirfd and name during syscalls li
        # ke renameat and symlinkat. Use 'evt.abspath.src' or 'evt.abspat
        # h.dst' for syscalls that support multiple paths.
        evt_abspath = 'evt.abspath'
        # 'true' for open/openat events where the path was opened for reading
        evt_is_open_read = 'evt.is_open_read'
        # 'true' for open/openat events where the path was opened for writing
        evt_is_open_write = 'evt.is_open_write'
        # For system call events, the name of the system call.
        # Use this field instead of evt.type if you need to make
        # sure that the filtered value is actually a system call
        syscall_type = 'syscall.type'
    
    
    class User:
        # user ID.
        user_uid = 'user.uid'
        # user name.
        user_name = 'user.name'      
        # home directory of the user.
        user_homedir = 'user.homedir'    
        # user's shell.
        user_shell = 'user.shell'      
        # audit user id (auid).
        user_loginuid = 'user.loginuid'
        # audit user name (auid).
        user_loginname = 'user.loginname'  

        
    class Group:
        # group id
        group_gid = 'group.gid'
        # group name
        group_name = 'group.name'
    
    
    class SysLog:
        # facility as a string.
        syslog_facility_str = 'syslog.facility.str'
        # facility as a number (0-23).
        syslog_facility = 'syslog.facility'
        # severity as a string. Can have one of these values: emerg, aler
        # t, crit, err, warn, notice, info, debug
        syslog_severity_str = 'syslog.severity.str'
        # severity as a number (0-7).
        syslog_severity = 'syslog.severity' 
        # message sent to syslog.
        syslog_message = 'syslog.message'

        
    class Container:
        # the container id.
        container_id = 'container.id'
        # # the container name.
        container_name = 'container.name'  
        # the container image name (e.g. sysdig/sysdig:latest for docker).
        container_image = 'container.image'
        # the container image id (e.g. 6f7e2741b66b).
        container_image.id = 'container.image.id'
        # the container type, eg: docker or rkt
        container_type = 'container.type'
        # true for containers running as privileged, false otherwise
        container_privileged = 'container.privileged'
                        
    
    class FileDescriptorList:
        # for poll events, this is a comma-separated list of the FD numbe
        # rs in the 'fds' argument, returned as a string.
        fdlist_nums = 'fdlist.nums'     
        # for poll events, this is a comma-separated list of the FD names
        #  in the 'fds' argument, returned as a string.
        fdlist_names = 'fdlist.names'
        # for poll events, this is a comma-separated list of the client I
        # P addresses in the 'fds' argument, returned as a string.
        fdlist_cips = 'fdlist.cips'     
        # for poll events, this is a comma-separated list of the server I
        # P addresses in the 'fds' argument, returned as a string.
        fdlist_sips = 'fdlist.sips'     
        # for TCP/UDP FDs, for poll events, this is a comma-separated lis
        # t of the client TCP/UDP ports in the 'fds' argument, returned a
        # s a string.
        fdlist_cports = 'fdlist.cports'   
        # for poll events, this is a comma-separated list of the server T
        # CP/UDP ports in the 'fds' argument, returned as a string.
        fdlist_sports = 'fdlist.sports'   
        
        
    class Span:
        # ID of the span. This is a unique identifier that is used to mat
        # ch the enter and exit tracer events for this span. It can also 
        # be used to match different spans belonging to a trace.
        span_id = 'span.id'
        
    
        
    
        
    
        