import sys, time
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.resize(250, 200)
window.setWindowTitle('Tutorial PySide')

layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom, window)

btnMessageDialog = QtGui.QPushButton('Message Dialog')
btnErrorDialog = QtGui.QPushButton('Error Dialog')
btnInputDialog = QtGui.QPushButton('Input Dialog')
btnProgressDialog = QtGui.QPushButton('Progress Dialog')
btnFileDialog = QtGui.QPushButton('File Dialog')

layout.addWidget(btnMessageDialog)
layout.addWidget(btnErrorDialog)
layout.addWidget(btnInputDialog)
layout.addWidget(btnProgressDialog)
layout.addWidget(btnFileDialog)


def showMessageDialog():
    messageBox = QtGui.QMessageBox(window)
    messageBox.setWindowTitle('Message Box')
    messageBox.setText('The document has been modified')
    messageBox.setInformativeText('Do you want to save your changes?')
    messageBox.setStandardButtons(
        QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel
    )
    messageBox.setDefaultButton(QtGui.QMessageBox.Save)
    result = messageBox.exec_()

    if result == QtGui.QMessageBox.Save:
        print('tombol save dipilih')
    elif result == QtGui.QMessageBox.Discard:
        print('tombol discard dipilih')
    else:
        print('tombol cancel dipilih')

def showErrorMessageDialog():
    dialog = QtGui.QErrorMessage(window)
    dialog.showMessage('Maaf, telah terjadi error :(')

def showInputDialog():
    text = QtGui.QInputDialog.getText(
        window, 'Masukkan Nama', 'Nama'
    )
    integer = QtGui.QInputDialog.getInt(
        window, 'Masukkan Usia', 'Usia'
    )
    double = QtGui.QInputDialog.getDouble(
        window, 'Masukkan Berat Badan', 'Berat Badan'
    )
    print('Nama: ', text[0])
    print('Usia: ', integer[0])
    print('Berat Badan: ', double[0])

def showProgressDialog():
    dialog = QtGui.QProgressDialog(window)
    dialog.setMinimum(0)
    dialog.setMaximum(100)

    for i in range(100):
        dialog.setValue(i)
        time.sleep(.100)

    dialog.setValue(dialog.maximum())

def showFileDialog():
    fileNames = QtGui.QFileDialog.getOpenFileNames(
        window, 'Open File', '~/'
    )[0]

    for fileName in fileNames:
        print(fileName)
    # fileName = QtGui.QFileDialog.getOpenFileName(
    #     window, 'Select Image', '~/', 'Images Files(*.jpg *.png *.gif)'
    # )[0]
    #
    # print (fileName)

btnMessageDialog.clicked.connect(showMessageDialog)
btnErrorDialog.clicked.connect(showErrorMessageDialog)
btnInputDialog.clicked.connect(showInputDialog)
btnProgressDialog.clicked.connect(showProgressDialog)
btnFileDialog.clicked.connect(showFileDialog)

window.show()

sys.exit(app.exec_())
