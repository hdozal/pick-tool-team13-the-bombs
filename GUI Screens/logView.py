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
		layout = self.createLayouts()
		widget.setLayout(layout)

		self.show()

	#Sets layout and fills elements of window
	def createLayouts(self):
		logEntry1 = QtWidgets.QTextEdit("Log 1")
		logEntry2 = QtWidgets.QTextEdit("Log 2")
		verticalLay = QtWidgets.QVBoxLayout()
		verticalLay.addWidget(logEntry1)
		verticalLay.addWidget(logEntry2)
		label = QtWidgets.QLabel("Vectors")

		horizLay = QtWidgets.QHBoxLayout()

		horizLay.addWidget(label)
		label.setAlignment(Qt.AlignTop)
		horizLay.addLayout(verticalLay)

		generalLayout = QGridLayout()
		search = QtWidgets.QTextEdit("Search")
		search.setMaximumHeight(30)
		search.setMaximumWidth(150)
		generalLayout.addWidget(search)
		generalLayout.addLayout(horizLay,1,0)
		generalLayout.setRowStretch(0,1)

		return generalLayout


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
	
	
	def buttonClicked(self):
		#Push button to show window
		self.showPopUp()
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())