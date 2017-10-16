from PySide import QtGui, QtCore

"""
Jago Ngoding tutorial PySide berbahasa Indonesia

author: Ibnu Jakaria
"""

class Kakek (QtCore.QObject):

    telahDatang = QtCore.Signal()

    def __init__(self):
        super(Kakek, self).__init__()

    def datang (self):
        print("Kakek telah datang...")
        self.telahDatang.emit()


kakek = Kakek()

def katakanHalo():
    print("Halo kakek!")

kakek.telahDatang.connect(katakanHalo)

for i in range(10):
    kakek.datang()
