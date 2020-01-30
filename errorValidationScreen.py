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
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow,  QAction, qApp, QSplashScreen, QMessageBox, QGridLayout, QGroupBox, QVBoxLayout
from PyQt5.QtCore import Qt, QMetaType

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
		
		widget = QWidget(self)
		self.setCentralWidget(widget)
		self.reviewButton = QtWidgets.QPushButton("Review",self)
		self.layout = QGridLayout()
		self.layout.addWidget(self.reviewButton,1,1)
		widget.setLayout(self.layout)
		
		self.show()
	
	#Create Layout
	def createGridLayout(self):
		layout = QGridLayout()
		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("Click to validate errors")
		self.b1.clicked.connect(self.buttonClicked)
		self.b1.move(30,30)
		layout.addWidget(self.b1,0,0,2,2)
		return layout

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
	
	def showPopUp(self):
		#Show pop up window
		msg = QMessageBox()
		msg.setWindowTitle("Validation Error")
		msg.setStandardButtons(QMessageBox.Ignore|QMessageBox.Open)
		msg.setDefaultButton(QMessageBox.Ignore)
		x = msg.exec_()  # this will show our messagebox
	
	def buttonClicked(self):
		#Push button to show window
		self.showPopUp()
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())