import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.resize(300, 200)
window.setWindowTitle('Tutorial PySide')

layout = QtGui.QGridLayout(window)

btn1 = QtGui.QPushButton('Tombol 1')
btn2 = QtGui.QPushButton('Tombol 2')
btn3 = QtGui.QPushButton('Tombol 3')
btn4 = QtGui.QPushButton('Tombol 4')

layout.addWidget(btn1, 0, 0)
layout.addWidget(btn2, 0, 1)
layout.addWidget(btn3, 1, 0)
layout.addWidget(btn4, 1, 1)

window.show()

sys.exit(app.exec_())
