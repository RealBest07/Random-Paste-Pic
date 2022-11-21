from PyQt5 import QtCore, QtGui, QtWidgets
from randomui import Ui_MainWindow
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

class ranptaste(Ui_MainWindow):
    def __init__(self) -> None:
        super().setupUi(MainWindow)
        self.gcn()

    def gcn(self):
        pass
#xxxxxxxxxxxx

if __name__ == "__main__":
    mycode = ranptaste()
    MainWindow.show()
    sys.exit(app.exec_())