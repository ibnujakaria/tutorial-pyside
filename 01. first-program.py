import sys
from PySide import QtGui

# mendeklrasikan QtGui applikasi
app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.resize(800, 600)
window.setWindowTitle('Jago Ngoding')
window.show()

sys.exit(app.exec_())