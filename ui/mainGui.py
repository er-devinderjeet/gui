# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGui.ui'
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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.resize(681, 562)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(30, 90, 191, 411))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 461, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.enter = QtGui.QPushButton(self.layoutWidget)
        self.enter.setObjectName(_fromUtf8("enter"))
        self.horizontalLayout.addWidget(self.enter)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(32, 60, 191, 20))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(250, 90, 401, 411))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        self.backTestModeButton = QtGui.QPushButton(self.centralwidget)

        self.backTestModeButton.setGeometry(QtCore.QRect(560, 0, 121, 31))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.backTestModeButton.setFont(font)
        self.backTestModeButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 69, 94);"))
        self.backTestModeButton.setObjectName(_fromUtf8("backTestModeButton"))

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuPredict = QtGui.QMenu(self.menubar)
        self.menuPredict.setObjectName(_fromUtf8("menuPredict"))
        self.menuChart = QtGui.QMenu(self.menubar)
        self.menuChart.setObjectName(_fromUtf8("menuChart"))
        self.menuTechnical_Anaylsis = QtGui.QMenu(self.menubar)
        self.menuTechnical_Anaylsis.setObjectName(_fromUtf8("menuTechnical_Anaylsis"))
        mainWindow.setMenuBar(self.menubar)
        self.actionCalculate_OLS = QtGui.QAction(mainWindow)
        self.actionCalculate_OLS.setEnabled(False)
        self.actionCalculate_OLS.setObjectName(_fromUtf8("actionCalculate_OLS"))
        self.actionQuit = QtGui.QAction(mainWindow)
        self.actionQuit.setEnabled(True)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionHello = QtGui.QAction(mainWindow)
        self.actionHello.setObjectName(_fromUtf8("actionHello"))
        self.actionOLS_Tool = QtGui.QAction(mainWindow)
        self.actionOLS_Tool.setObjectName(_fromUtf8("actionOLS_Tool"))
        self.actionOLS_Tool_2 = QtGui.QAction(mainWindow)
        self.actionOLS_Tool_2.setObjectName(_fromUtf8("actionOLS_Tool_2"))
        self.actionCandleStick = QtGui.QAction(mainWindow)
        self.actionCandleStick.setObjectName(_fromUtf8("actionCandleStick"))
        self.actionLine = QtGui.QAction(mainWindow)
        self.actionLine.setObjectName(_fromUtf8("actionLine"))
        self.actionLine_2 = QtGui.QAction(mainWindow)
        self.actionLine_2.setObjectName(_fromUtf8("actionLine_2"))
        self.actionCandleStick_2 = QtGui.QAction(mainWindow)
        self.actionCandleStick_2.setObjectName(_fromUtf8("actionCandleStick_2"))
        self.actionRSI = QtGui.QAction(mainWindow)
        self.actionRSI.setObjectName(_fromUtf8("actionRSI"))
        self.actionLine_3 = QtGui.QAction(mainWindow)
        self.actionLine_3.setObjectName(_fromUtf8("actionLine_3"))
        self.actionOLS_Tool_3 = QtGui.QAction(mainWindow)
        self.actionOLS_Tool_3.setObjectName(_fromUtf8("actionOLS_Tool_3"))
        self.actionCandleStick_3 = QtGui.QAction(mainWindow)
        self.actionCandleStick_3.setObjectName(_fromUtf8("actionCandleStick_3"))
        self.menuFile.addAction(self.actionQuit)
        self.menuPredict.addAction(self.actionOLS_Tool_3)
        self.menuChart.addAction(self.actionLine_3)
        self.menuChart.addAction(self.actionCandleStick_3)
        self.menuTechnical_Anaylsis.addAction(self.actionRSI)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuChart.menuAction())
        self.menubar.addAction(self.menuTechnical_Anaylsis.menuAction())
        self.menubar.addAction(self.menuPredict.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Friend - Application of Financial  Market", None))
        self.label.setText(_translate("mainWindow", "Enter Stock Name", None))
        self.enter.setText(_translate("mainWindow", "Enter", None))
        self.comboBox.setItemText(0, _translate("mainWindow", "Select Date", None))
        self.comboBox.setItemText(1, _translate("mainWindow", "d-m-Y H:M:S", None))
        self.comboBox.setItemText(2, _translate("mainWindow", "d-m-Y H:M", None))

        self.backTestModeButton.setText(_translate("mainWindow", "BackTest Mode", None))

         #menu
        self.menuFile.setTitle(_translate("mainWindow", "File", None))
        self.menuPredict.setTitle(_translate("mainWindow", "Predict", None))
        self.menuChart.setTitle(_translate("mainWindow", "Chart", None))
        self.menuTechnical_Anaylsis.setTitle(_translate("mainWindow", "Technical Anaylsis", None))

        self.actionQuit.setText(_translate("mainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("mainWindow", "Ctrl+Q", None))

        self.actionLine.setText(_translate("mainWindow", "Line", None))
        self.actionCandleStick.setText(_translate("mainWindow", "CandleStick", None))

        self.actionOLS_Tool.setText(_translate("mainWindow", "OLS Tool", None))
        self.actionRSI.setText(_translate("mainWindow", "RSI", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

