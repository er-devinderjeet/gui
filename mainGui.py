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


         #leftside-view
        #model
        #tree view
        self.model = QtGui.QFileSystemModel(self.centralwidget)
        self.model.setRootPath('C:\Zerodha\Pi\Exported')

        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(30, 90, 191, 411))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index("C:\Zerodha\Pi\Exported"))
        #end tree view

        self.layoutWidget = QtGui.QWidget(self.centralwidget)

        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 611, 71))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
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
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox = QtGui.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.candleStick = QtGui.QRadioButton(self.layoutWidget)
        self.candleStick.setObjectName(_fromUtf8("candleStick"))
        self.horizontalLayout_2.addWidget(self.candleStick)
        self.lineChart = QtGui.QRadioButton(self.layoutWidget)
        self.lineChart.setObjectName(_fromUtf8("lineChart"))
        self.horizontalLayout_2.addWidget(self.lineChart)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(230, 100, 411, 51))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.autoCalculation = QtGui.QPushButton(self.layoutWidget1)
        self.autoCalculation.setObjectName(_fromUtf8("autoCalculation"))
        self.horizontalLayout_4.addWidget(self.autoCalculation)
        self.stopAutoCalculation = QtGui.QPushButton(self.layoutWidget1)
        self.stopAutoCalculation.setObjectName(_fromUtf8("stopAutoCalculation"))
        self.horizontalLayout_4.addWidget(self.stopAutoCalculation)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainWindow.setMenuBar(self.menubar)

        self.retranslateUi(mainWindow)
        QtCore.QObject.connect(self.candleStick, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit.selectAll)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Friend - Application of Financial  Market", None))
        self.label.setText(_translate("mainWindow", "Enter Stock Name", None))
        self.enter.setText(_translate("mainWindow", "Enter", None))
        self.comboBox.setItemText(0, _translate("mainWindow", "Select Date", None))
        self.comboBox.setItemText(1, _translate("mainWindow", "%d-%m-%Y %H:%M:%S", None))
        self.comboBox.setItemText(2, _translate("mainWindow", "%d-%m-%Y %H:%M", None))
        self.candleStick.setText(_translate("mainWindow", "Candle Stick", None))
        self.lineChart.setText(_translate("mainWindow", "Line Chart", None))
        self.autoCalculation.setText(_translate("mainWindow", "Auto-Calculation", None))
        self.stopAutoCalculation.setText(_translate("mainWindow", "Stop Auto-Calculation", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

