# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphing_1.ui'
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

class Ui_Graphing(object):
    def setupUi(self, Graphing):
        Graphing.setObjectName(_fromUtf8("Graphing"))
        Graphing.resize(640, 480)
        self.centralwidget = QtGui.QWidget(Graphing)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 591, 411))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        Graphing.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Graphing)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Graphing.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Graphing)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Graphing.setStatusBar(self.statusbar)

        self.retranslateUi(Graphing)
        QtCore.QMetaObject.connectSlotsByName(Graphing)

    def retranslateUi(self, Graphing):
        Graphing.setWindowTitle(_translate("Graphing", "Graphing", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Graphing = QtGui.QMainWindow()
    ui = Ui_Graphing()
    ui.setupUi(Graphing)
    Graphing.show()
    sys.exit(app.exec_())

