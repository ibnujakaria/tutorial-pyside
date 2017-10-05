import sys, time
from PySide import QtGui

"""
Jago Ngoding tutorial PySide berbahasa Indonesia

author: Ibnu Jakaria
"""

class Jendela(QtGui.QWidget):

    def __init__(self):
        super(Jendela, self).__init__()

        self.siapkanUI()
        self.siapkanListener()

    def siapkanUI(self):
        self.resize(400, 130)
        self.setWindowTitle('Tutorial PySide')

        self.namaLabel = QtGui.QLabel('Nama')
        self.namaEdit = QtGui.QLineEdit()
        self.hasilLabel = QtGui.QLabel('Hasil: ')

        self.layout = QtGui.QGridLayout(self)
        self.layout.addWidget(self.namaLabel, 0, 0)
        self.layout.addWidget(self.namaEdit, 1, 0)
        self.layout.addWidget(self.hasilLabel, 2, 0)

    def siapkanListener(self):
        self.namaEdit.textChanged.connect(self.onNamaEditTextChanged)

    def onNamaEditTextChanged(self):
        self.hasilLabel.setText(
            'Hasil: <strong style="color: red">' + self.namaEdit.text() + '</strong>'
        )

app = QtGui.QApplication(sys.argv)
jendela = Jendela()
jendela.show()
sys.exit(app.exec_())
