import sys, time
from PySide import QtGui

"""
Jago Ngoding tutorial PySide berbahasa Indonesia

author: Ibnu Jakaria
"""

class Jendela(QtGui.QWidget):

    def __init__(self):
        super(Jendela, self).__init__()

        self.siapkanUI()
        self.siapkanListener()

    def siapkanUI(self):
        self.resize(250, 200)
        self.setWindowTitle('Tutorial PySide')

        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom, self)

        self.btnMessageDialog = QtGui.QPushButton('Message Dialog')
        self.btnErrorDialog = QtGui.QPushButton('Error Dialog')
        self.btnInputDialog = QtGui.QPushButton('Input Dialog')
        self.btnProgressDialog = QtGui.QPushButton('Progress Dialog')
        self.btnFileDialog = QtGui.QPushButton('File Dialog')

        self.layout.addWidget(self.btnMessageDialog)
        self.layout.addWidget(self.btnErrorDialog)
        self.layout.addWidget(self.btnInputDialog)
        self.layout.addWidget(self.btnProgressDialog)
        self.layout.addWidget(self.btnFileDialog)

    def siapkanListener(self):
        self.btnMessageDialog.clicked.connect(self.showMessageDialog)
        self.btnErrorDialog.clicked.connect(self.showErrorMessageDialog)
        self.btnInputDialog.clicked.connect(self.showInputDialog)
        self.btnProgressDialog.clicked.connect(self.showProgressDialog)
        self.btnFileDialog.clicked.connect(self.showFileDialog)

    def showMessageDialog(self):
        messageBox = QtGui.QMessageBox(self)
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

    def showErrorMessageDialog(self):
        dialog = QtGui.QErrorMessage(self)
        dialog.showMessage('Maaf, telah terjadi error :(')

    def showInputDialog(self):
        text = QtGui.QInputDialog.getText(
            self, 'Masukkan Nama', 'Nama'
        )
        integer = QtGui.QInputDialog.getInt(
            self, 'Masukkan Usia', 'Usia'
        )
        double = QtGui.QInputDialog.getDouble(
            self, 'Masukkan Berat Badan', 'Berat Badan'
        )
        print('Nama: ', text[0])
        print('Usia: ', integer[0])
        print('Berat Badan: ', double[0])

    def showProgressDialog(self):
        dialog = QtGui.QProgressDialog(self)
        dialog.setMinimum(0)
        dialog.setMaximum(100)

        for i in range(100):
            dialog.setValue(i)
            time.sleep(.100)

        dialog.setValue(dialog.maximum())

    def showFileDialog(self):
        fileNames = QtGui.QFileDialog.getOpenFileNames(
            self, 'Open File', '~/'
        )[0]

        for fileName in fileNames:
            print(fileName)

        # fileName = QtGui.QFileDialog.getOpenFileName(
        #     self, 'Select Image', '~/', 'Images Files(*.jpg *.png *.gif)'
        # )[0]
        #
        # print (fileName)

app = QtGui.QApplication(sys.argv)
jendela = Jendela()
jendela.show()
sys.exit(app.exec_())
