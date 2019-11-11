
# This class reprepresents an Alert set by the user on a specific Monitor
class Alerts:
    def __init__(self, name, monitor, metrics, *args):
        self.name = name
        self.monitor = monitor
        self.metrics = metrics # probably a dictionary
        self.email = ''
        self.notifications = False
        self.capture = False
        self.seconds = -1
        self.filename = ''
    
    def setEmailNotification(email):
        self.email = email
    
    def setNotificationsNotification():
        self.notifications = True
        
    def setCapture(seconds, filename):
        self.capture = True
        self.seconds = seconds
        self.filename = filename
    
    # This function is responsible for deploying the alert
    # It should start the process for finding anomalies on the
    # specific monitor outputs. 
    # In case something is wrong, a notification will be sent.
    # In case something is wrong, a capture file will be generated
    def deployAlert():
        a = 10
        
        
    