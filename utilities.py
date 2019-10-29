from PyQt5 import QtCore, QtGui, QtWidgets

class Utilities:
	def showMessageBox(message, title, icon):
		msg = QtWidgets.QMessageBox()
		msg.setIcon(icon)
		msg.setText(message)
		msg.setWindowTitle(title)
		msg.exec_()
