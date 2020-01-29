# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:39:54 2020
Menu reference: https://www.youtube.com/watch?v=aiCr9pkE5AI
@author: Eduardo
@modifications: Victor Vargas
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow,  QAction, qApp, QSplashScreen
from PyQt5.QtCore import Qt

import time

class App(QMainWindow):
	
	def __init__(self):
		super().__init__()
		self.title = 'PICK menu'
		self.left = 10              #starting position from the left of the screen to the app
		self.top = 50               #start position from the top of the screen to the app
		self.width = 640            #size
		self.height = 480           #size
		self.initUI()
	
	def initUI(self):
		
		#create Menu bar
		bar = self.menuBar()
		
		file = bar.addMenu("File")  
		edit = bar.addMenu("Edit")
		view = bar.addMenu("View")
		
		self.viewMenuBar(view)
		self.editMenuBar(edit)
		self.fileMenuBar(file)
		
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("Click to cleanse")
		self.b1.clicked.connect(self.buttonClicked)
		self.b1.move(30,30)
		self.show()
	
	#BUTONS IN MENU BAR
	def viewMenuBar(self, view):
		viewVecAct = QAction("View Vector", self)
		viewTabAct = QAction("View Table", self)
		
		view.addAction(viewVecAct)
		view.addAction(viewTabAct)
	
	def editMenuBar(self, edit):
		undoAct = QAction("Undo", self)
		undoAct.setShortcut('Ctrl+Z')
		
		redoAct = QAction("Redo", self)
		redoAct.setShortcut('Ctrl+Y')
		
		
		edit.addAction(undoAct)
		edit.addAction(redoAct)
		
	def fileMenuBar(self, file):
		#create actions
		saveAct = QAction("Save", self)
		saveAct.setShortcut('Ctrl+S')
		
		newAct = QAction("New Event", self)
		newAct.setShortcut("Ctr+N")
		
		quitAct = QAction("Exit", self)
		quitAct.setShortcut("Ctrl+Q")
		
		getJPEG = QAction("JPEG",self)
		getPNG = QAction("PNG",self)
		
		#exportAct = QAction("Export",self)
		file.addAction(newAct)
		file.addAction(saveAct)
		
		#put export, that will also contain options Like a menu whithin a menu
		exportTypes = file.addMenu("Export")
		exportTypes.addAction(getJPEG)
		exportTypes.addAction(getPNG)
		
		file.addAction(quitAct)
		
		#call Event
		quitAct.triggered.connect(self.quitEvent)
		
	#Events from some Buttons from Menu Bar
	def quitEvent(self):
		qApp.quit()
	
	def showSplash(self):
		# Create and display the splash screen
		splash_pix = QPixmap('loading.png')
		splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
		splash.setMask(splash_pix.mask())
		# Show a message at the center of the dialog
		splash.showMessage("Cleansing",0x0084)
		splash.show()
		app.processEvents()

		# Simulate something that takes time
		time.sleep(2)
		splash.finish(self)

	def buttonClicked(self):
		self.showSplash()
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())