# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphing.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
from pyqtgraph import PlotWidget
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(640, 480)
        self.graphicsView = PlotWidget(Form)
        self.graphicsView.setGeometry(QtCore.QRect(190, 80, 411, 341))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ## Define a top-level widget to hold everything
    w = QtGui.QWidget()
    ## Create some widgets to be placed inside
    btn = QtGui.QPushButton('press me')
    text = QtGui.QLineEdit('enter text')
    listw = QtGui.QListWidget()
    plot = pg.PlotWidget()
    ## Create a grid layout to manage the widgets size and position
    layout = QtGui.QGridLayout()
    w.setLayout(layout)
    ## Add widgets to the layout in their proper positions
    layout.addWidget(btn, 0, 0) # button goes in upper-left
    layout.addWidget(text, 1, 0) # text edit goes in middle-left
    layout.addWidget(listw, 2, 0) # list widget goes in bottom-left
    layout.addWidget(plot, 0, 1, 3, 1) # plot goes on right side, spanning 3 rows
    ## Display the widget as a new window
    w.show()
    ## Start the Qt event loop
    app.exec_()