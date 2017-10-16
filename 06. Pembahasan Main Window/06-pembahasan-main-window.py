import sys
from PySide import QtGui, QtCore

app = QtGui.QApplication(sys.argv)

mainWindow = QtGui.QMainWindow()
mainWindow.resize(800, 600)
mainWindow.setWindowTitle('Tutorial PySide')

# menjadikan text edit sebagai central widget
# textEdit = QtGui.QTextEdit("Tulis sesuatu di sini")
# mainWindow.setCentralWidget(textEdit)

# menjadikan calendar widget sebagai central widget
calendar = QtGui.QCalendarWidget()
mainWindow.setCentralWidget(calendar)

mainWindow.show()

sys.exit(app.exec_())
