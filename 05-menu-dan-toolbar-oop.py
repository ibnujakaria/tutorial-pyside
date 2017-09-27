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
        self.siapkanMenu()
        self.siapkanToolbar()
        self.siapkanPopupMenu()
        self.siapkanBagianTengah()
        self.statusBar().showMessage('Halo~ pesan ini akan tampil selama 2 detik', 2000)

    def siapkanBagianTengah(self):
        # menjadikan calendar widget sebagai central widget
        self.calendar = QtGui.QCalendarWidget()
        self.setCentralWidget(self.calendar)

    def siapkanMenu(self):
        topMenuHome = QtGui.QMenu('&Home')
        exitAction = topMenuHome.addAction('Exit')
        exitAction.setShortcut('Ctrl+q')
        exitAction.triggered.connect(QtCore.QCoreApplication.instance().quit)
        self.menuBar().addMenu(topMenuHome)

    def siapkanPopupMenu(self):
        self.popupMenu = QtGui.QMenu('Popup')
        self.popupMenu.addAction('Help')
        self.popupMenu.addAction('About')
        self.popupMenu.addAction('Exit')
        self.popupMenu.setParent(self)
        self.popupMenu.hide()

    def siapkanToolbar(self):
        toolbar = self.addToolBar('tes')
        toolbar.addAction('Aksi 1')
        toolbar.addAction('Aksi 2')
        toolbar.addAction('Aksi 3')
        toolbar.setMovable(False)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            self.popupMenu.popup(event.pos())
        else:
            self.popupMenu.hide()


app = QtGui.QApplication(sys.argv)
JendelaUtama = JendelaUtama()
JendelaUtama.show()
sys.exit(app.exec_())
