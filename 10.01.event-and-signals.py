import sys, time
from PySide import QtGui

"""
Jago Ngoding tutorial PySide berbahasa Indonesia

author: Ibnu Jakaria
"""

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.resize(400, 130)
window.setWindowTitle('Tutorial PySide')

namaLabel = QtGui.QLabel('Nama')
namaEdit = QtGui.QLineEdit()
hasilLabel = QtGui.QLabel('Hasil: ')

layout = QtGui.QGridLayout(window)
layout.addWidget(namaLabel, 0, 0)
layout.addWidget(namaEdit, 1, 0)
layout.addWidget(hasilLabel, 2, 0)

def onNamaEditTextChanged():
    hasilLabel.setText(
        'Hasil: <strong style="color: red">' + namaEdit.text() + '</strong>'
    )

# menghubungakan signal dan slot
namaEdit.textChanged.connect(onNamaEditTextChanged)

window.show()

sys.exit(app.exec_())
