# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(670, 482)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_cargar = QtGui.QPushButton(self.centralwidget)
        self.btn_cargar.setGeometry(QtCore.QRect(10, 10, 99, 27))
        self.btn_cargar.setObjectName(_fromUtf8("btn_cargar"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 211, 221))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.btn_visualizar = QtGui.QPushButton(self.centralwidget)
        self.btn_visualizar.setGeometry(QtCore.QRect(120, 10, 101, 27))
        self.btn_visualizar.setObjectName(_fromUtf8("btn_visualizar"))
        self.cb_filtros = QtGui.QComboBox(self.centralwidget)
        self.cb_filtros.setGeometry(QtCore.QRect(10, 280, 211, 31))
        self.cb_filtros.setObjectName(_fromUtf8("cb_filtros"))
        self.cb_filtros.addItem(_fromUtf8(""))
        self.cb_filtros.addItem(_fromUtf8(""))
        self.cb_filtros.addItem(_fromUtf8(""))
        self.label_algoritmo = QtGui.QLabel(self.centralwidget)
        self.label_algoritmo.setGeometry(QtCore.QRect(10, 330, 211, 21))
        self.label_algoritmo.setAcceptDrops(True)
        self.label_algoritmo.setText(_fromUtf8(""))
        self.label_algoritmo.setObjectName(_fromUtf8("label_algoritmo"))
        self.btn_aplicar = QtGui.QPushButton(self.centralwidget)
        self.btn_aplicar.setGeometry(QtCore.QRect(10, 370, 211, 27))
        self.btn_aplicar.setObjectName(_fromUtf8("btn_aplicar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Restaurador", None))
        self.btn_cargar.setText(_translate("MainWindow", "Cargar", None))
        self.btn_visualizar.setText(_translate("MainWindow", "Visualizar", None))
        self.cb_filtros.setItemText(0, _translate("MainWindow", "New Item", None))
        self.cb_filtros.setItemText(1, _translate("MainWindow", "filtro1", None))
        self.cb_filtros.setItemText(2, _translate("MainWindow", "filtro2", None))
        self.btn_aplicar.setText(_translate("MainWindow", "Aplicar", None))

