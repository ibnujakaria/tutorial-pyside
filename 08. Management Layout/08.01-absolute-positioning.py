import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.resize(300, 200)
window.setWindowTitle('Tutorial PySide')

btn1 = QtGui.QPushButton('Tombol 1', window)
btn1.resize(280, 70)
btn1.move(10, 10)

btn2 = QtGui.QPushButton('Tombol 2', window)
btn2.resize(135, 100)
btn2.move(10, 90)

btn3 = QtGui.QPushButton('Tombol 3', window)
btn3.resize(135, 100)
btn3.move(155, 90)

window.show()

sys.exit(app.exec_())
