from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtCore import pyqtSignal

class FileDialog(QWidget):
    # Spawn a file dialog based on type parameter passed
    def __init__(self, type, ui):
        super().__init__()
        self.title = 'Allo'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.type = type
        self.ui = ui
        self.initUI()
        self.success = False

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        if self.type == 'load_file':
            self.loadFileDialog()
        elif self.type == 'save_file':
            self.saveFileDialog()
        self.show()
    
    def resetFields(self):
        self.ui.anomaliesProgramExecutedTextEdit.setPlainText('')
        self.ui.anomaliesDirectoryFileOpensTextEdit.setPlainText('')
        self.ui.anomaliesProcessFileOpensTextEdit.setPlainText('')
        self.ui.anomaliesKnownUsersTextEdit.setPlainText('')
        self.ui.anomalieUnknownUsersTextEdit.setPlainText('')
        self.ui.anomaliesInboundIPTextEdit.setPlainText('')
        self.ui.anomaliesOutboundIPTextEdit.setPlainText('')
        self.ui.anomaliesMaliciousIPTextEdit.setPlainText('')
        self.ui.anomaliesMongoDBCheckBox.setChecked(False)
        self.ui.anomaliesHTTPCheckBox.setChecked(False)
        self.ui.anomaliesMySQLCheckBox.setChecked(False)
        self.ui.anomaliesKafkaCheckBox.setChecked(False)

    def loadFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "Load Anomaly Rules", "","SMAD configuration files (*.smadconf)", options=options)
        if filename:
            # Read rules line by line and insert on corresponding ui_element
            # a ui_element can be a QTextEdit or a QCheckBox
            with open(filename, 'r') as f:
                line = f.readline()
                is_checkbox = False
                self.resetFields()
                while line:
                    if line.startswith('#'):
                        if line.startswith('# Program Executed'):
                            ui_element = self.ui.anomaliesProgramExecutedTextEdit
                            is_checkbox = False
                        elif line.startswith('# Directory File Open'):
                            ui_element = self.ui.anomaliesDirectoryFileOpensTextEdit
                            is_checkbox = False
                        elif line.startswith('# Process File Open'):
                            ui_element = self.ui.anomaliesProcessFileOpensTextEdit
                            is_checkbox = False
                        elif line.startswith('# Known Users'):
                            ui_element = self.ui.anomaliesKnownUsersTextEdit
                            is_checkbox = False
                        elif line.startswith('# Unknown Users'):
                            ui_element = self.ui.anomalieUnknownUsersTextEdit
                            is_checkbox = False
                        elif line.startswith('# Inbound Ip Traffic'):
                            ui_element = self.ui.anomaliesInboundIPTextEdit
                            is_checkbox = False
                        elif line.startswith('# Outbound Ip Traffic'):
                            ui_element = self.ui.anomaliesOutboundIPTextEdit
                            is_checkbox = False
                        elif line.startswith('# Malicious Ip Traffic'):
                            ui_element = self.ui.anomaliesMaliciousIPTextEdit
                            is_checkbox = False
                        elif line.startswith('# MongoDB Traffic'):
                            ui_element = self.ui.anomaliesMongoDBCheckBox
                            is_checkbox = True
                        elif line.startswith('# HTTP Traffic'):
                            ui_element = self.ui.anomaliesHTTPCheckBox
                            is_checkbox = True
                        elif line.startswith('# MySQL Traffic'):
                            ui_element = self.ui.anomaliesMySQLCheckBox
                            is_checkbox = True
                        elif line.startswith('# Kafka Traffic'):
                            ui_element = self.ui.anomaliesKafkaCheckBox
                            is_checkbox = True
                    else:
                        if is_checkbox:
                            ui_element.setChecked(True if line.strip() == 'True' else False)
                        else:
                            if line != '' or line != '\n':
                                ui_element.insertPlainText(line)

                    line = f.readline()
                self.success = True

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self,"Export Anomaly Rules","","SMAD configuration files (*.smadconf)", options=options)
        if filename:
            if not filename.endswith('.smadconf'):
                filename += '.smadconf'
            # Write the rule title followed by the parameters entered by the user
            # on various input fields
            with open(filename, 'w+') as f:
                f.write('# Program Executed\n' + self.ui.anomaliesProgramExecutedTextEdit.toPlainText().strip() + '\n')
                f.write('# Directory File Open\n' + self.ui.anomaliesDirectoryFileOpensTextEdit.toPlainText().strip() + '\n')
                f.write('# Process File Open\n' + self.ui.anomaliesProcessFileOpensTextEdit.toPlainText().strip() + '\n')
                f.write('# Known Users\n' + self.ui.anomaliesKnownUsersTextEdit.toPlainText().strip() + '\n')
                f.write('# Unknown Users\n' + self.ui.anomalieUnknownUsersTextEdit.toPlainText().strip() + '\n')
                f.write('# Inbound Ip Traffic\n' + self.ui.anomaliesInboundIPTextEdit.toPlainText().strip() + '\n')
                f.write('# Outbound Ip Traffic\n' + self.ui.anomaliesOutboundIPTextEdit.toPlainText().strip() + '\n')
                f.write('# Malicious Ip Traffic\n' + self.ui.anomaliesMaliciousIPTextEdit.toPlainText().strip() + '\n')
                f.write('# MongoDB Traffic\n' + str(self.ui.anomaliesMongoDBCheckBox.isChecked()) + '\n')
                f.write('# HTTP Traffic\n' + str( self.ui.anomaliesHTTPCheckBox.isChecked()) + '\n')
                f.write('# MySQL Traffic\n' + str(self.ui.anomaliesMySQLCheckBox.isChecked()) + '\n')
                f.write('# Kafka Traffic\n' + str(self.ui.anomaliesKafkaCheckBox.isChecked()) + '\n')
        self.ui.anomaliesOutboundIPTextEdit.setPlainText('')
        self.success = True
        self.filename = filename.split('/')[-1]
