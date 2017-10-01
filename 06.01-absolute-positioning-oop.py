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

    self.btn1 = QtGui.QPushButton('Tombol 1', self)
    self.btn1.resize(280, 70)
    self.btn1.move(10, 10)

    self.btn2 = QtGui.QPushButton('Tombol 2', self)
    self.btn2.resize(135, 100)
    self.btn2.move(10, 90)

    self.btn3 = QtGui.QPushButton('Tombol 3', self)
    self.btn3.resize(135, 100)
    self.btn3.move(155, 90)

app = QtGui.QApplication(sys.argv)
jendela = Jendela()
jendela.show()
sys.exit(app.exec_())
