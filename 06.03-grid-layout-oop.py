import sys
from PySide import QtGui

"""
Jago Ngoding tutorial PySide berbasa Indonesia

author: Ibnu Jakaria
"""

class Jendela(QtGui.QWidget):

  def __init__(self):
    super(Jendela, self).__init__()

    self.siapkanUI()

  def siapkanUI(self):
    self.resize(300, 200)
    self.setWindowTitle('Tutorial PySide')

    self.btn1 = QtGui.QPushButton('Tombol 1')
    self.btn2 = QtGui.QPushButton('Tombol 2')
    self.btn3 = QtGui.QPushButton('Tombol 3')
    self.btn4 = QtGui.QPushButton('Tombol 4')

    self.layout = QtGui.QGridLayout(self)
    self.layout.addWidget(self.btn1, 0, 0)
    self.layout.addWidget(self.btn2, 0, 1)
    self.layout.addWidget(self.btn3, 1, 0)
    self.layout.addWidget(self.btn4, 1, 1)

app = QtGui.QApplication(sys.argv)
jendela = Jendela()
jendela.show()
sys.exit(app.exec_())
