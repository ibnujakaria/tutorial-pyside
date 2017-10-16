import sys
from PySide import QtGui, QtCore

app = QtGui.QApplication(sys.argv)

mainWindow = QtGui.QMainWindow()
mainWindow.resize(800, 600)
mainWindow.setWindowTitle('Tutorial PySide')

# menjadikan calendar widget sebagai central widget
calendar = QtGui.QCalendarWidget()
mainWindow.setCentralWidget(calendar)

def exit():
    print ('Tombol exit ditrigger')

topMenuHome = QtGui.QMenu('&Home')
exitAction = topMenuHome.addAction('Exit')
exitAction.setShortcut('Ctrl+q')
exitAction.triggered.connect(exit)

mainWindow.menuBar().addMenu(topMenuHome)

popupMenu = QtGui.QMenu('Popup')
popupMenu.addAction('Help')
popupMenu.addAction('About')
popupMenu.addAction('Exit')
popupMenu.setParent(mainWindow)
popupMenu.hide()

def onMouseRealease (event):
    if event.button() == QtCore.Qt.MouseButton.RightButton:
        popupMenu.popup(event.pos())
    else:
        popupMenu.hide()
mainWindow.mouseReleaseEvent = onMouseRealease


toolbar = QtGui.QToolBar('Tes')
toolbar.addAction('Aksi 1')
toolbar.addAction('Aksi 2')
toolbar.addAction('Aksi 3')
toolbar.setMovable(False)
mainWindow.addToolBar(toolbar)

mainWindow.statusBar().showMessage('Halo~ pesan ini akan tampil selama 2 detik', 2000)

mainWindow.show()

sys.exit(app.exec_())
