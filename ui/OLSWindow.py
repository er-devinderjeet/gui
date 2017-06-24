# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OLSWindow.ui'
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
        MainWindow.resize(455, 271)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.variableYButton = QtGui.QPushButton(self.centralwidget)
        self.variableYButton.setGeometry(QtCore.QRect(240, 50, 101, 31))
        self.variableYButton.setObjectName(_fromUtf8("variableYButton"))
        self.variableYLabel = QtGui.QLineEdit(self.centralwidget)
        self.variableYLabel.setGeometry(QtCore.QRect(40, 50, 191, 31))
        self.variableYLabel.setObjectName(_fromUtf8("variableYLabel"))
        self.openVariableYButton = QtGui.QPushButton(self.centralwidget)
        self.openVariableYButton.setGeometry(QtCore.QRect(350, 50, 75, 31))
        self.openVariableYButton.setObjectName(_fromUtf8("openVariableYButton"))
        self.label_Y = QtGui.QLabel(self.centralwidget)
        self.label_Y.setGeometry(QtCore.QRect(40, 9, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Y.setFont(font)
        self.label_Y.setObjectName(_fromUtf8("label_Y"))
        self.label_X = QtGui.QLabel(self.centralwidget)
        self.label_X.setGeometry(QtCore.QRect(40, 80, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_X.setFont(font)
        self.label_X.setObjectName(_fromUtf8("label_X"))
        self.variableXLabel = QtGui.QLineEdit(self.centralwidget)
        self.variableXLabel.setGeometry(QtCore.QRect(40, 140, 191, 31))
        self.variableXLabel.setObjectName(_fromUtf8("variableXLabel"))
        self.variableXButton = QtGui.QPushButton(self.centralwidget)
        self.variableXButton.setGeometry(QtCore.QRect(240, 140, 101, 31))
        self.variableXButton.setObjectName(_fromUtf8("variableXButton"))
        self.openVariableXButton = QtGui.QPushButton(self.centralwidget)
        self.openVariableXButton.setGeometry(QtCore.QRect(350, 140, 75, 31))
        self.openVariableXButton.setObjectName(_fromUtf8("openVariableXButton"))
        self.calculateOLSButton = QtGui.QPushButton(self.centralwidget)
        self.calculateOLSButton.setGeometry(QtCore.QRect(250, 190, 161, 31))
        self.calculateOLSButton.setObjectName(_fromUtf8("calculateOLSButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.variableYButton.setText(_translate("MainWindow", "Variable Y Browse", None))
        self.openVariableYButton.setText(_translate("MainWindow", "Open", None))
        self.label_Y.setText(_translate("MainWindow", "Depedent Variable Y (Stock)", None))
        self.label_X.setText(_translate("MainWindow", "Independent Variable X (Stock/Indice)", None))
        self.variableXButton.setText(_translate("MainWindow", "Variable X Browse", None))
        self.openVariableXButton.setText(_translate("MainWindow", "Open", None))
        self.calculateOLSButton.setText(_translate("MainWindow", "Calculate OLS", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

