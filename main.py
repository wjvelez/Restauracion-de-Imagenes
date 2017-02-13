from PyQt4 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication

import interfaz  # This file holds our MainWindow and all vent1 related things

# it also keeps events etc that we defined in Qt designer
import os  # For listing directory methods


class Interfaz(QtGui.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the vent1.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in vent1.py file automatically
        # It sets up layout and widgets that are defined
        self.btn_cargar.clicked.connect(self.leer_im)  # When the button is pressed Execute browse_folder function
        #self.ListWidget.__init__(self) # In case there are any existing elements in the list
        self.listWidget.itemClicked.connect(self.item_click)
        self.btn_visualizar.clicked.connect(self.ver_im)
        self.selec = ''
        self.algoritmo = ''
        self.btn_aplicar.clicked.connect(self.selec_algortimo)


    #muestra un listado de las imagenes
    def leer_im(self):
        self.listWidget.clear() # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Seleccione Carpeta")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory
        if directory: # if user didn't pick a directory don't continue
            for file_name in os.listdir(directory): # for all files, if any, in the directory
                self.listWidget.addItem(file_name)  # add file to the listWidget

    #selecciona una imagen de la lista
    def item_click(self, item):
        imagen = str(item.text())
    	print ('seleccionado:', imagen)
        self.selec = imagen

    #presenta la imagen seleccionada
    def ver_im(self):
        print ('archivo:, ', self.selec)

    #selecciona el algoritmo de restauracion a utilizar
    def selec_algortimo(self):
    	algoritmo = self.cb_filtros.currentText()
    	self.algoritmo = algoritmo
    	self.label_algoritmo.setText(' '+ algoritmo)
    	print (algoritmo)
    	
       	


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = Interfaz()  # We set the form to be our ExampleApp (vent1)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
	main() # run the main function
