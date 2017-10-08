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

    self.btn1 = QtGui.QPushButton('Tombol 1')
    self.btn2 = QtGui.QPushButton('Tombol 2')
    self.btn3 = QtGui.QPushButton('Tombol 3')

    self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom, self)
    self.layout.addWidget(self.btn1)
    self.layout.addWidget(self.btn2)
    self.layout.addWidget(self.btn3)

app = QtGui.QApplication(sys.argv)
jendela = Jendela()
jendela.show()
sys.exit(app.exec_())
