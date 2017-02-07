
import sys
import numpy as np
import cv2
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Restaurador de Imagenes")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.show()

app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
