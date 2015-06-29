#!/usr/bin/env python
# -*- coding: utf-8 -*-

#V1.1.2015.06.22.2330

import sys
import time
from PyQt4 import QtGui, QtCore

class Main(QtGui.QMainWindow):

	MODIFIED = False

	def __init__(self, parent = None):
		QtGui.QMainWindow.__init__(self, parent)
		#Para identificar el nombre del archivo que se va a abrir
		self.fileName = ""

		self.initUI()

	def createActions(self):
		#Creacion de aquellos botones que nos serviran para desempeniar las acciones requeridas
		#Estableciendo la accion y su icono
		self.newAction = QtGui.QAction(QtGui.QIcon("icons/Nuevo.png"), "Nuevo", self)
		#Estableciendo el tooltip que sera mostrado
		self.newAction.setStatusTip("Crear un nuevo arhivo")	
		#Estableciendo el atajo del teclado para activar la accion	
		self.newAction.setShortcut("Ctrl+N")
		#Asociendo el disparador de la accion
		self.newAction.triggered.connect(self.new)
		#Estableciendo la accion y su icono
		self.openAction = QtGui.QAction(QtGui.QIcon("icons/Abrir.jpg"), "Abrir", self)
		#Estableciendo el tooltip que sera mostrado
		self.openAction.setStatusTip("Abrir un arhivo existente")	
		#Estableciendo el atajo del teclado para activar la accion	
		self.openAction.setShortcut("Ctrl+O")
		#Asociendo el disparador de la accion
		self.openAction.triggered.connect(self.open)
		#Estableciendo la accion y su icono
		self.saveAction = QtGui.QAction(QtGui.QIcon("icons/Guardar.png"), "Guardar", self)
		#Estableciendo el tooltip que sera mostrado
		self.saveAction.setStatusTip("Guardar archivo")	
		#Estableciendo el atajo del teclado para activar la accion	
		self.saveAction.setShortcut("Ctrl+S")
		#Asociendo el disparador de la accion
		self.saveAction.triggered.connect(self.save)
		#Establecer la accion y su icono
		self.saveAllAction = QtGui.QAction(QtGui.QIcon("icons/GuardarComo.png"), "Guardar como",self)
		#Establecer el tooltrip que sera mostrado
		self.saveAllAction.setStatusTip("Guardar como")
		#Establecer el atajo del teclado para activar la accion
		self.saveAllAction.setShortcut("Ctrl+M")
		#Asociar el disparador de la accion
		self.saveAllAction.triggered.connect(self.saveAll)
		#Establecer la accion y su icono
		self.exitAction = QtGui.QAction(QtGui.QIcon("icons/Salir.png"), "Salir",self)
		#Establecer el tooltrip que sera mostrado
		self.exitAction.setStatusTip("Salir")
		#Establecer el atajo del teclado para activar la accion
		self.exitAction.setShortcut("Ctrl+E")
		#Asociar el disparador de la accion
		self.exitAction.triggered.connect(self.exit)
		#Establecer la accion y su icono
		self.optionAction = QtGui.QAction(QtGui.QIcon("icons/Opcion1.png"), "",self)
		#Establecer el tooltrip que sera mostrado
		self.optionAction.setStatusTip("")
		#Establecer el atajo del teclado para activar la accion
		self.optionAction.setShortcut("")
		#Asociar el disparador de la accion
		"""self.optionAction.triggered.connect(self.exit)"""
		#Establecer la accion y su icono
		self.compileAction = QtGui.QAction(QtGui.QIcon("icons/Compilar.png"), "",self)
		#Establecer el tooltrip que sera mostrado
		self.compileAction.setStatusTip("Compilar")
		#Establecer el atajo del teclado para activar la accion
		self.compileAction.setShortcut("")
		#Asociar el disparador de la accion
		"""self.compileAction.triggered.connect(self.exit)"""
		#Establecer la accion y su icono
		self.licenseAction = QtGui.QAction(QtGui.QIcon("icons/Licencia.png"), "Licencia",self)
		#Establecer el tooltrip que sera mostrado
		self.licenseAction.setStatusTip("Licencia")
		#Establecer el atajo del teclado para activar la accion
		self.licenseAction.setShortcut("Ctrl+L")
		#Asociar el disparador de la accion
		self.licenseAction.triggered.connect(self.license) #esto hace falta
		#Establecer la accion y su icono
		self.creditsAction = QtGui.QAction(QtGui.QIcon("icons/Creditos.png"), "Creditos",self) #hace falta el icono
		#Establecer el tooltrip que sera mostrado
		self.creditsAction.setStatusTip("Creditos")
		#Establecer el atajo del teclado para activar la accion
		self.creditsAction.setShortcut("Ctrl+C")
		#Asociar el disparador de la accion
		self.creditsAction.triggered.connect(self.credits) #esto hace falta
		#Estableciendo la accion y su icono
		self.copyAction = QtGui.QAction(QtGui.QIcon("icons/Copiar.png"), "Copiar", self)
		#Estableciendo el tooltip que sera mostrado
		self.copyAction.setStatusTip("Copiar al portapapel")	
		#Estableciendo el atajo del teclado para activar la accion	
		self.copyAction.setShortcut("Ctrl+C")
		#Asociendo el disparador de la accion
		self.copyAction.triggered.connect(self.text.copy)
		#Estableciendo la accion y su icono
		self.cutAction = QtGui.QAction(QtGui.QIcon("icons/Cortar.png"), "Cortar", self)
		#Estableciendo el tooltip que sera mostrado
		self.cutAction.setStatusTip("Cortar al portapapel")	
		#Estableciendo el atajo del teclado para activar la accion	
		self.cutAction.setShortcut("Ctrl+X")
		#Asociendo el disparador de la accion
		self.cutAction.triggered.connect(self.text.cut)
		#Estableciendo la accion y su icono
		self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/Pegar.png"), "Pegar", self)
		#Estableciendo el tooltip que sera mostrado
		self.pasteAction.setStatusTip("Copiar del portapapel")	
		#Estableciendo el atajo del teclado para activar la accion	
		self.pasteAction.setShortcut("Ctrl+V")
		#Asociendo el disparador de la accion
		self.pasteAction.triggered.connect(self.text.paste)
		#Estableciendo la accion y su icono
		self.undoAction = QtGui.QAction(QtGui.QIcon("icons/Deshacer.png"), "Deshacer", self)
		#Estableciendo el tooltip que sera mostrado
		self.undoAction.setStatusTip("Deshacer")	
		#Estableciendo el atajo del teclado para activar la accion	
		self.undoAction.setShortcut("Ctrl+Z")
		#Asociendo el disparador de la accion
		self.undoAction.triggered.connect(self.text.undo)
		#Estableciendo la accion y su icono
		self.redoAction = QtGui.QAction(QtGui.QIcon("icons/Rehacer.png"), "Rehacer", self)
		#Estableciendo el tooltip que sera mostrado
		self.redoAction.setStatusTip("Rehacer")	
		#Estableciendo el atajo del teclado para activar la accion	
		self.redoAction.setShortcut("Ctrl+Y")
		#Asociendo el disparador de la accion
		self.redoAction.triggered.connect(self.text.redo)

	def initToolBar(self):
		
		self.toolBar = self.addToolBar("Opciones")

		#Agregando las acciones al toolbar
		self.toolBar.addAction(self.newAction)
		self.toolBar.addAction(self.openAction)
		self.toolBar.addAction(self.saveAction)
		self.toolBar.addSeparator()
		self.toolBar.addAction(self.copyAction)
		self.toolBar.addAction(self.cutAction)
		self.toolBar.addAction(self.pasteAction)
		self.toolBar.addAction(self.compileAction)
		self.toolBar.addSeparator()
		self.toolBar.addAction(self.undoAction)
		self.toolBar.addAction(self.redoAction)
		self.toolBar.addSeparator()

		#Indica si se realizo algun cambio en el PlainTextEdit
		self.text.modificationChanged[bool].connect(self.modified)

		self.addToolBarBreak()

	def initFormatBar(self):

		self.formatBar = self.addToolBar("Formato")

	def initMenuBar(self):
		#Creando un Objeto MenuBar
		menuBar = self.menuBar()		

		#Agregando las opcions al MenuBar
		fileMenuBar = menuBar.addMenu("Inicio")
		optionMenuBar = menuBar.addMenu("opciones")
		compileMenuBar = menuBar.addMenu("Compilar")
		editMenuBar = menuBar.addMenu("Editar")
		#viewMenuBar = menuBar.addMenu("Ver") 
		aboutMenuBar = menuBar.addMenu("Acerca de") 

		fileMenuBar.addAction(self.newAction)
		fileMenuBar.addAction(self.openAction)
		fileMenuBar.addAction(self.saveAction)
		fileMenuBar.addAction(self.saveAllAction)
		fileMenuBar.addSeparator()
		fileMenuBar.addAction(self.exitAction)

		optionMenuBar.addAction(self.optionAction)

		compileMenuBar.addAction(self.compileAction)

		editMenuBar.addAction(self.copyAction)
		editMenuBar.addAction(self.cutAction)
		editMenuBar.addAction(self.pasteAction)
		editMenuBar.addAction(self.undoAction)
		editMenuBar.addAction(self.redoAction)

		aboutMenuBar.addAction(self.licenseAction)
		aboutMenuBar.addAction(self.creditsAction)


	def new(self):
		#Creando subventana nueva
		window = Main(self)
		window.show()

	def open(self):
		#verifica si hay cambios que guardar
		if self.MODIFIED:
			flags = QtGui.QMessageBox.Yes
			flags |= QtGui.QMessageBox.No
			flags |= QtGui.QMessageBox.Cancel
			r = QtGui.QMessageBox.information(self, self.tr('Modificado'),
				self.tr('Desea guardar los cambios'),
				flags)
			if r == QtGui.QMessageBox.Yes:
				self.save()
				self.openFile()
			elif r == QtGui.QMessageBox.No:
				self.openFile()
		else:
			self.openFile()
		self.MODIFIED = False
			
	def openFile(self):
			#Obteniendo el nombre del archivo
			self.fileName = QtGui.QFileDialog.getOpenFileName(self, 'Abrir archivo')
			#Sino es nulo
			if self.fileName:
			#Abriendo el archivo y cargando su texto en el editor
				with open(self.fileName,"rt") as file:
					self.text.setPlainText(file.read())

	def save(self):
		#Si el archivo no existe
		if not self.fileName:
			self.fileName = QtGui.QFileDialog.getSaveFileName(self, 'Guardar archivo')

		if self.MODIFIED:
			with open(self.fileName,"wt") as file:
				file.write(self.text.toPlainText())
			self.MODIFIED = False

	#Establece la fila y columna actual del cursor
	def cursorActual(self):
		cursor = self.text.textCursor()
		row = cursor.blockNumber() + 1
		column = cursor.columnNumber() + 1
		self.statusBar.showMessage("Fila: {} , Columna: {}".format(row, column))

	#Agregando todos los elementos a la ventana principal
	def initUI(self):
		#Agregando la region de texto a la ventana
		#self.text = QtGui.QTextEdit(self)
		self.text = QtGui.QPlainTextEdit(self) #Hice este cambio para saber si el texto se modifica
		#Relacionando el metodo para saber en que fila y columna se esta
		self.text.cursorPositionChanged.connect(self.cursorActual)
		#Haciendo que el text abarque el espacio entero que se tiene
		self.setCentralWidget(self.text)
		#Cargando todas las barras necesarias
		self.createActions()
		self.initToolBar()
		self.initFormatBar()
		self.initMenuBar()
		
		self.setWindowIcon(QtGui.QIcon("icons/icon.png"))
		self.statusBar = self.statusBar()
		#self.setGeometry(100,100,1030,800)
		self.setWindowTitle("Raptor")
		self.setMinimumSize(750,500)

	def exit(self):
		if self.MODIFIED:
			flags = QtGui.QMessageBox.Yes
			flags |= QtGui.QMessageBox.No
			flags |= QtGui.QMessageBox.Cancel
			r = QtGui.QMessageBox.information(self, self.tr('Modificado'),
				self.tr('Desea guardar los cambios'),
				flags)
			if r == QtGui.QMessageBox.Yes:
				self.save()
			elif r == QtGui.QMessageBox.No:
				sys.exit(0)
		else:
			sys.exit(0)

	def saveAll(self):
		self.fileName = QtGui.QFileDialog.getSaveFileName(self, 'Guardar como')

		if self.fileName:
			with open(self.fileName,"wt") as file:
				file.write(self.text.toPlainText())

	def modified(self):
		self.MODIFIED = True

	def closeEvent(self, evento):
		r = None
		if self.MODIFIED:
			flags = QtGui.QMessageBox.Yes
			flags |= QtGui.QMessageBox.No
			flags |= QtGui.QMessageBox.Cancel
			r = QtGui.QMessageBox.information(self, self.tr('Modificado'),
				self.tr('Desea guardar los cambios'),
				flags)
		if r == QtGui.QMessageBox.Yes:
			self.guardarComo()
		elif r == QtGui.QMessageBox.No:
			evento.accept()
		elif r == QtGui.QMessageBox.Cancel:
			evento.ignore()

	def credits(self):
		inf = Information('Credits').exec_()

	def license(self):
		inf = Information('License').exec_()

#Muestra la licencia y los creditos.
class Information(QtGui.QDialog):
	def __init__(self, type):
		super(Information, self).__init__()

		self.type = type;

		if self.type == 'License':
			#self.setGeometry(420,180,650,275)
			self.setWindowTitle('Licencia')
		else:
			#self.setGeometry(420,180,200,175)
			self.setWindowTitle('Creditos')
		
		
		image = QtGui.QPixmap('images/raptor4.png')
		labelImg = QtGui.QLabel("",self)
		labelImg.setPixmap(image)

		text = self.read()
		label = QtGui.QLabel(text, self)

		gridL = QtGui.QGridLayout(self)
		gridL.addWidget(labelImg, 0, 0)
		gridL.addWidget(label, 1, 0)

	#Lee el archivo de texto que contiene ya sea la licencia o los creditos
	def read(self):
		text = ''

		if self.type == 'License':
			archive = 'Information/License.txt'
		else:
			archive = 'Information/Credits.txt'

		with open(archive, 'r') as f:
			for l in f:
				text = text + l
		return text

def splash():
	#Creando y desplegando el Splash Screen
	splashPixmap = QtGui.QPixmap('images/raptor4.png')
	splashScreen = QtGui.QSplashScreen(splashPixmap, QtCore.Qt.WindowStaysOnTopHint)
	#Agregando la barra de progreso
	progressBar = QtGui.QProgressBar(splashScreen)
	splashScreen.setMask(splashPixmap.mask())
	#progressBar.setGeometry(splashScreen.width()/10, 8*splashScreen.height()/9,8*splashScreen.width()/10, splashScreen.height()/32)
	return splashScreen
	#for i in range(0,100):
	#	progressBar.setValue(i)
	#	t = time.time()
	#	while time.time() < t + 0.1:
			#app.processEvents()
		

def main():
	app = QtGui.QApplication(sys.argv)

	splashScreen = splash()
	splashScreen.show()

	app.processEvents()

	time.sleep(3)

	main = Main()
	main.show()

	splashScreen.finish(main)

	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
