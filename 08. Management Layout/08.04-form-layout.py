import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.resize(300, 200)
window.setWindowTitle('Tutorial PySide')

layout = QtGui.QFormLayout(window)

namaLineEdit = QtGui.QLineEdit()
emailLineEdit = QtGui.QLineEdit()
asalLineEdit = QtGui.QLineEdit()
submitBtn = QtGui.QPushButton('Submit')

layout.addRow('Nama', namaLineEdit)
layout.addRow('Email', emailLineEdit)
layout.addRow('Asal', asalLineEdit)
layout.addRow(submitBtn)

window.show()

sys.exit(app.exec_())
