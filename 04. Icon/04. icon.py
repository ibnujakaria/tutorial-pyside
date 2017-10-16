import sys
from PySide import QtGui

# mendeklrasikan QtGui applikasi
app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
icon = QtGui.QIcon('../smile.png')

button = QtGui.QPushButton('Halo!', window)
button.resize(button.sizeHint())
button.move(10, 10)
button.setIcon(icon)
button.setToolTip('Ini tombol dengan icon :)')

window.resize(800, 600)
window.setWindowTitle('Jago Ngoding')
window.setWindowIcon(icon)
window.setToolTip('Belajar <strong>PySide</strong> yuk!')
window.show()

sys.exit(app.exec_())
