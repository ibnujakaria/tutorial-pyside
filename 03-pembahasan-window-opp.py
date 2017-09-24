import sys
from PySide import QtGui, QtCore

"""
Jago Ngoding tutorial PySide berbasa Indonesia

author: Ibnu Jakaria
"""

class Jendela(QtGui.QWidget):

  def __init__(self):
    super(Jendela, self).__init__()

    self.icon = QtGui.QIcon('smile.png')
    self.siapkanUI()
    self.tampilkanDitengah()

  def siapkanUI(self):
    self.resize(800, 600)
    self.setWindowTitle('Jago Ngoding')
    self.setWindowIcon(self.icon)
    self.siapkanTombol()

  def tampilkanDitengah (self):
    # frameSize = self.frameSize()
    # screenSize = QtGui.QDesktopWidget().screenGeometry()
    # xPoint = screenSize.width() / 2 - frameSize.width() / 2
    # yPoint = screenSize.height() / 2 - frameSize.height() / 2
    # self.move(xPoint, yPoint)

    frameWindow = self.frameGeometry()
    centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
    frameWindow.moveCenter(centerPoint)
    self.move(frameWindow.topLeft())

  def siapkanTombol(self):
    self.button = QtGui.QPushButton('Exit', self)
    self.button.resize(self.button.sizeHint())
    self.button.move(10, 10)
    self.button.clicked.connect(QtCore.QCoreApplication.instance().quit)

app = QtGui.QApplication(sys.argv)
jendela = Jendela()
jendela.show()
sys.exit(app.exec_())
