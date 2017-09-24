import sys
from PySide import QtGui

"""
Jago Ngoding tutorial PySide berbasa Indonesia

author: Ibnu Jakaria
"""

class Jendela(QtGui.QWidget):

  def __init__(self):
    super(Jendela, self).__init__()

    self.icon = QtGui.QIcon('smile.png')
    self.siapkanUI()

  def siapkanUI(self):
    self.resize(800, 600)
    self.setWindowTitle('Jago Ngoding')
    self.setWindowIcon(self.icon)
    self.setToolTip('Belajar <strong>PySide</strong> yuk!')
    self.siapkanTombol()

  def siapkanTombol(self):
    self.button = QtGui.QPushButton('Halo!', self)
    self.button.resize(self.button.sizeHint())
    self.button.move(10, 10)
    self.button.setIcon(self.icon)
    self.button.setToolTip('Ini tombol dengan icon :)')

app = QtGui.QApplication(sys.argv)
jendela = Jendela()
jendela.show()
sys.exit(app.exec_())
