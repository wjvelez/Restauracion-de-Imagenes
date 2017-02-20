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
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(960, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(960, 400))
        MainWindow.setMaximumSize(QtCore.QSize(960, 400))
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_cargar = QtGui.QPushButton(self.centralwidget)
        self.btn_cargar.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.btn_cargar.setObjectName(_fromUtf8("btn_cargar"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 211, 341))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setWhatsThis(_fromUtf8(""))
        self.listWidget.setAccessibleName(_fromUtf8(""))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.btn_visualizar = QtGui.QPushButton(self.centralwidget)
        self.btn_visualizar.setGeometry(QtCore.QRect(120, 10, 101, 31))
        self.btn_visualizar.setObjectName(_fromUtf8("btn_visualizar"))
        self.cb_filtros = QtGui.QComboBox(self.centralwidget)
        self.cb_filtros.setGeometry(QtCore.QRect(450, 10, 261, 31))
        self.cb_filtros.setObjectName(_fromUtf8("cb_filtros"))
        self.cb_filtros.addItem(_fromUtf8(""))
        self.cb_filtros.addItem(_fromUtf8(""))
        self.cb_filtros.addItem(_fromUtf8(""))
        self.cb_filtros.addItem(_fromUtf8(""))
        self.cb_filtros.addItem(_fromUtf8(""))
        self.cb_filtros.addItem(_fromUtf8(""))
        self.cb_filtros.addItem(_fromUtf8(""))
        self.btn_aplicar = QtGui.QPushButton(self.centralwidget)
        self.btn_aplicar.setGeometry(QtCore.QRect(730, 10, 101, 31))
        self.btn_aplicar.setObjectName(_fromUtf8("btn_aplicar"))
        self.lbl_imDeg = QtGui.QLabel(self.centralwidget)
        self.lbl_imDeg.setGeometry(QtCore.QRect(250, 50, 340, 340))
        self.lbl_imDeg.setFrameShape(QtGui.QFrame.WinPanel)
        self.lbl_imDeg.setLineWidth(1)
        self.lbl_imDeg.setScaledContents(True)
        self.lbl_imDeg.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_imDeg.setIndent(0)
        self.lbl_imDeg.setObjectName(_fromUtf8("lbl_imDeg"))
        self.lbl_imRes = QtGui.QLabel(self.centralwidget)
        self.lbl_imRes.setGeometry(QtCore.QRect(610, 50, 340, 340))
        self.lbl_imRes.setFrameShape(QtGui.QFrame.WinPanel)
        self.lbl_imRes.setLineWidth(1)
        self.lbl_imRes.setMidLineWidth(0)
        self.lbl_imRes.setScaledContents(True)
        self.lbl_imRes.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_imRes.setIndent(0)
        self.lbl_imRes.setObjectName(_fromUtf8("lbl_imRes"))
        self.btn_guardar = QtGui.QPushButton(self.centralwidget)
        self.btn_guardar.setGeometry(QtCore.QRect(850, 10, 101, 31))
        self.btn_guardar.setObjectName(_fromUtf8("btn_guardar"))
        self.lbl_filtro = QtGui.QLabel(self.centralwidget)
        self.lbl_filtro.setGeometry(QtCore.QRect(270, 10, 68, 31))
        self.lbl_filtro.setObjectName(_fromUtf8("lbl_filtro"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(220, 10, 31, 381))
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setObjectName(_fromUtf8("line"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Restaurador", None))
        self.btn_cargar.setText(_translate("MainWindow", "Cargar", None))
        self.btn_visualizar.setText(_translate("MainWindow", "Visualizar", None))
        self.cb_filtros.setItemText(0, _translate("MainWindow", "seleccione", None))
        self.cb_filtros.setItemText(1, _translate("MainWindow", "mediano", None))
        self.cb_filtros.setItemText(2, _translate("MainWindow", "maximo", None))
        self.cb_filtros.setItemText(3, _translate("MainWindow", "minimo", None))
        self.cb_filtros.setItemText(4, _translate("MainWindow", "medioAritmetico", None))
        self.cb_filtros.setItemText(5, _translate("MainWindow", "puntoMedio", None))
        self.cb_filtros.setItemText(6, _translate("MainWindow", "medioContraHarmonico", None))
        self.btn_aplicar.setText(_translate("MainWindow", "Aplicar", None))
        self.lbl_imDeg.setText(_translate("MainWindow", "Imagen de Entrada", None))
        self.lbl_imRes.setText(_translate("MainWindow", "Imagen Restaurada", None))
        self.btn_guardar.setText(_translate("MainWindow", "Guardar", None))
        self.lbl_filtro.setText(_translate("MainWindow", "Filtro:", None))

