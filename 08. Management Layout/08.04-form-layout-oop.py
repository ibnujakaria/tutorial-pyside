import sys
from PySide import QtGui

"""
Jago Ngoding tutorial PySide berbahasa Indonesia

author: Ibnu Jakaria
"""

class Jendela(QtGui.QWidget):

  def __init__(self):
    super(Jendela, self).__init__()

    self.siapkanUI()

  def siapkanUI(self):
    self.resize(300, 200)
    self.setWindowTitle('Tutorial PySide')

    self.namaLineEdit = QtGui.QLineEdit()
    self.emailLineEdit = QtGui.QLineEdit()
    self.asalLineEdit = QtGui.QLineEdit()
    self.submitBtn = QtGui.QPushButton('Submit')

    self.layout = QtGui.QFormLayout(self)
    self.layout.addRow('Nama', self.namaLineEdit)
    self.layout.addRow('Email', self.emailLineEdit)
    self.layout.addRow('Asal', self.asalLineEdit)
    self.layout.addRow(self.submitBtn)

app = QtGui.QApplication(sys.argv)
jendela = Jendela()
jendela.show()
sys.exit(app.exec_())
