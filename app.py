import sys, os, shutil, glob, time
from PyQt4 import QtCore, QtGui 

from PyQt4 import *

from mainGui import Ui_mainWindow
from stopCalBox import Ui_MainWindow
from __builtin__ import str, int
from subprocess import Popen
#from all_func.graph import  basicGraph
from all_func.graph import  ohlcGraph
from all_func.userstats import centralTendency

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


class AppGui(QtGui.QMainWindow,Ui_mainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.enter.clicked.connect(self.generate_report)
        self.ui.comboBox.currentIndexChanged.connect(self.setDatePattern)
        self.ui.treeView.doubleClicked.connect(self.treeView_select_item)
        self.ui.autoCalculation.clicked.connect(self.autoCalculation)
        self.ui.stopAutoCalculation.clicked.connect(self.stopAutoCalculation)
    def generate_report(self):
        data_line = self.ui.lineEdit.displayText()
        print data_line
    startAutoCal = False
    def autoCalculation(self):
        if not self.startAutoCal:
            self.startAutoCal = True
            ohlcGraph.forever()
            self.stopCalBoxObject = Ui_MainWindow()
            self.stopCalBoxObject.setupUi(self)

    def stopAutoCalculation(self):
        if self.startAutoCal:
            self.startAutoCal= False

    def treeView_select_item(self,index):
        item = self.ui.treeView.selectedIndexes()[0]
        strData=[]
        strData = item.data(0).toPyObject()
        #self.treeMedia.currentIndex()
        print('' + str(strData))
        #data = QtCore.QString(strData)
        #drawStockGraph(str(strData),str(self.ui.comboBox.currentText()))
        a = ohlcGraph.graphing()

        a.calculateCT(str(strData),str(self.ui.comboBox.currentText()))

        # centralTendency.artmeticMean(str(strData))

    def setDatePattern(self,i):
        for count in range(self.ui.comboBox.count()):
          return self.ui.comboBox.itemText(count)
        return self.ui.comboBox.currentText()


app = QtGui.QApplication(sys.argv)

window = AppGui()	
ui = Ui_mainWindow()
window.show()
sys.exit(app.exec_())