__author__ = 'Devinderjeet'
import sys
from __builtin__ import str

from PyQt4 import QtCore, QtGui

from ui.graphing import Ui_Graphing

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class graphingGui(QtGui.QWidget,Ui_Graphing):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Graphing()
        self.ui.setupUi(self)
