import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.resize(300, 200)
window.setWindowTitle('Tutorial PySide')

layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom, window)

btn1 = QtGui.QPushButton('Tombol 1')
btn2 = QtGui.QPushButton('Tombol 2')
btn3 = QtGui.QPushButton('Tombol 3')

layout.addWidget(btn1)
layout.addWidget(btn2)
layout.addWidget(btn3)

window.show()

sys.exit(app.exec_())
