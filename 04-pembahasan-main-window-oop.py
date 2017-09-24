import sys
from PySide import QtGui, QtCore

"""
Jago Ngoding tutorial PySide berbasa Indonesia

author: Ibnu Jakaria
"""

class JendelaUtama(QtGui.QMainWindow):
    def __init__(self):
        super(JendelaUtama, self).__init__()
        self.siapkanUI()
        self.show()

    def siapkanUI(self):
        self.resize(800, 600)
        self.setWindowTitle('Tutorial PySide')
        self.siapkanBagianTengah()

    def siapkanBagianTengah(self):
        # menjadikan text edit sebagai central widget
        # self.textEdit = QtGui.QTextEdit("Tulis sesuatu di sini")
        # self.setCentralWidget(self.textEdit)

        # menjadikan calendar widget sebagai central widget
        self.calendar = QtGui.QCalendarWidget()
        self.setCentralWidget(self.calendar)


app = QtGui.QApplication(sys.argv)
JendelaUtama = JendelaUtama()
JendelaUtama.show()
sys.exit(app.exec_())
