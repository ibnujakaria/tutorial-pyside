import sys
from PySide import QtGui, QtCore

# mendeklrasikan QtGui applikasi
app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
icon = QtGui.QIcon('../smile.png')

button = QtGui.QPushButton('Exit', window)
button.resize(button.sizeHint())
button.move(10, 10)
button.clicked.connect(QtCore.QCoreApplication.instance().quit)

window.resize(800, 600)
window.setWindowTitle('Belajar PySide')
window.setWindowIcon(icon)

# frameSize = window.frameSize()
# screenSize = QtGui.QDesktopWidget().screenGeometry()
# xPoint = screenSize.width() / 2 - frameSize.width() / 2
# yPoint = screenSize.height() / 2 - frameSize.height() / 2
# window.move(xPoint, yPoint)

frameWindow = window.frameGeometry()
centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
frameWindow.moveCenter(centerPoint)
window.move(frameWindow.topLeft())

window.show()

sys.exit(app.exec_())
