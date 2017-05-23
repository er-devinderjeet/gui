import sys, os, shutil, glob
from PyQt4 import QtCore, QtGui 

from PyQt4 import *

from mainGui import Ui_mainWindow
from __builtin__ import str, int
from subprocess import Popen


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
        self.ui.treeView.doubleClicked.connect(self.treeView_select_item)

    def generate_report(self):
        data_line = self.ui.lineEdit.displayText()
        print data_line

    def treeView_select_item(self,index):
        item = self.ui.treeView.selectedIndexes()[0]
        strData = item.data(0).toPyObject()
        #self.treeMedia.currentIndex()
        print('' + str(strData))

app = QtGui.QApplication(sys.argv)

window = AppGui()	
ui = Ui_mainWindow()
window.show()
sys.exit(app.exec_())