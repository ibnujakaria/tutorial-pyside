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
    self.resize(800, 600)
    self.setWindowTitle('Jago Ngoding')

app = QtGui.QApplication(sys.argv)
jendela = Jendela()
jendela.show()
sys.exit(app.exec_())
