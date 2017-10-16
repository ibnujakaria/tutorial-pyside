import sys
from PySide import QtGui, QtCore

"""
Jago Ngoding tutorial PySide bahasa Indonesia

author: Ibnu Jakaria
"""

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.resize(300, 200)
window.setWindowTitle('Tutorial PySide')

layout = QtGui.QFormLayout(window)

nasiGoreng = QtGui.QCheckBox('Nasi Goreng')
nasiPecel = QtGui.QCheckBox('Nasi Pecel')
nasiKuning = QtGui.QCheckBox('Nasi Kuning')

bungkus = QtGui.QRadioButton('Bungkus')

menuComboBox = QtGui.QComboBox()
menuComboBox.insertItem(1, 'Nasi Goreng')
menuComboBox.insertItem(2, 'Nasi Pecel')
menuComboBox.insertItem(3, 'Nasi Kuning')

fontComboBox = QtGui.QFontComboBox()

dateTimeEdit = QtGui.QDateTimeEdit(QtCore.QDateTime.currentDateTime())
dateEdit = QtGui.QDateEdit(QtCore.QDate.currentDate())
timeEdit = QtGui.QTimeEdit(QtCore.QTime.currentTime())

lineEdit = QtGui.QLineEdit()
spinBox = QtGui.QSpinBox()
textEdit = QtGui.QTextEdit()

button = QtGui.QPushButton('Pesan')

layout.addRow(QtGui.QLabel('Menu:'))
layout.addRow(nasiGoreng)
layout.addRow(nasiPecel)
layout.addRow(nasiKuning)

layout.addRow(QtGui.QLabel('Bungkus Makanan?'))
layout.addRow(bungkus)

layout.addRow(QtGui.QLabel('Menu Makanan'))
layout.addRow(menuComboBox)

layout.addRow(QtGui.QLabel('Pilih Font'))
layout.addRow(fontComboBox)

layout.addRow(QtGui.QLabel('Tanggal dan Waktu'))
layout.addRow(dateTimeEdit)

layout.addRow(QtGui.QLabel('Tanggal'))
layout.addRow(dateEdit)

layout.addRow(QtGui.QLabel('Waktu'))
layout.addRow(timeEdit)

layout.addRow(QtGui.QLabel('Nama'))
layout.addRow(lineEdit)

layout.addRow(QtGui.QLabel('Jumlah Porsi'))
layout.addRow(spinBox)

layout.addRow(QtGui.QLabel('Catatan'))
layout.addRow(textEdit)

layout.addRow(button)

window.show()

sys.exit(app.exec_())
