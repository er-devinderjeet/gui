# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadStockData.ui'
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

class Ui_StockDataFromDatabase(object):
    def setupUi(self, StockDataFromDatabase):
        StockDataFromDatabase.setObjectName(_fromUtf8("StockDataFromDatabase"))
        StockDataFromDatabase.resize(1150, 650)
        StockDataFromDatabase.setMaximumSize(QtCore.QSize(1150, 650))
        self.centralwidget = QtGui.QWidget(StockDataFromDatabase)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 256, 581))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Albany AMT"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(290, 50, 831, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(660, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Albany AMT"))
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(640, 0, 20, 61))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 0, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 30, 341, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Albany AMT"))
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(750, 0, 20, 61))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.loadStockDataButton = QtGui.QPushButton(self.centralwidget)
        self.loadStockDataButton.setGeometry(QtCore.QRect(900, 30, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.loadStockDataButton.setFont(font)
        self.loadStockDataButton.setStyleSheet(_fromUtf8("background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";"))
        self.loadStockDataButton.setObjectName(_fromUtf8("loadStockDataButton"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(890, 0, 3, 61))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(780, 0, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(770, 30, 101, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.tabStockWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabStockWidget.setGeometry(QtCore.QRect(290, 70, 831, 521))
        self.tabStockWidget.setObjectName(_fromUtf8("tabStockWidget"))

        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))

        self.scrollArea = QtGui.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(770, 10, 41, 481))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 39, 479))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalSlider = QtGui.QSlider(self.scrollAreaWidgetContents)
        self.verticalSlider.setGeometry(QtCore.QRect(0, 20, 41, 451))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.tableWidget = QtGui.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 801, 481))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(1)
        #self.tableWidget.verticalHeader().setVisible(True)

        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        '''
        #
        typetab = QtGui.QTabWidget(self)
        types = producttypes() ##returns a tuple with type names e.g. [('Drinks',), ('Food',)]

        for name in types:
            tab = QtGui.QWidget()
            typetab.addTab(tab, name[0])
            typetablayout = QtGui.QGridLayout(tab)

        for name in types:
            tab = QtGui.QWidget()
            typetab.addTab(tab, name[0])
            products = typeitems(name[0]) ## returns items of that product type [('Coke',), ('Pepsi',)]
            typetablayout = QtGui.QGridLayout()
            for length in range(math.floor(len(products)/5) + 1):
                for width in range(5):
                    try:
                        button = QtGui.QPushButton(products[width][0])
                        button.setObjectName(products[width][0])
                        typetablayout.addWidget(button,length, width)
                    except IndexError:
                        break
                    print([length,width])
            typetab.setLayout(typetablayout)

        '''




        #
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.tableWidget.raise_()
        self.scrollArea.raise_()
        self.tabStockWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tabStockWidget.addTab(self.tab_4, _fromUtf8(""))
        StockDataFromDatabase.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(StockDataFromDatabase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuGraph = QtGui.QMenu(self.menubar)
        self.menuGraph.setObjectName(_fromUtf8("menuGraph"))
        StockDataFromDatabase.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(StockDataFromDatabase)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        StockDataFromDatabase.setStatusBar(self.statusbar)
        self.actionDraw_Graph = QtGui.QAction(StockDataFromDatabase)
        self.actionDraw_Graph.setObjectName(_fromUtf8("actionDraw_Graph"))
        self.menuGraph.addAction(self.actionDraw_Graph)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGraph.menuAction())

        self.retranslateUi(StockDataFromDatabase)
        self.tabStockWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StockDataFromDatabase)

    def retranslateUi(self, StockDataFromDatabase):
        StockDataFromDatabase.setWindowTitle(_translate("StockDataFromDatabase", "Friend - Load Stock Data ", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("StockDataFromDatabase", "Database", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.comboBox.setItemText(0, _translate("StockDataFromDatabase", "tick", None))
        self.comboBox.setItemText(1, _translate("StockDataFromDatabase", "1 min", None))
        self.comboBox.setItemText(2, _translate("StockDataFromDatabase", "2 min", None))
        self.comboBox.setItemText(3, _translate("StockDataFromDatabase", "5 min", None))
        self.comboBox.setItemText(4, _translate("StockDataFromDatabase", "10 min", None))
        self.comboBox.setItemText(5, _translate("StockDataFromDatabase", "day", None))
        self.label.setText(_translate("StockDataFromDatabase", "Database Stock Search", None))
        self.lineEdit.setPlaceholderText(_translate("StockDataFromDatabase", "e.g. ICICIBANK-EQ", None))
        self.loadStockDataButton.setText(_translate("StockDataFromDatabase", "Load Data", None))
        self.label_2.setText(_translate("StockDataFromDatabase", "Time Interval", None))
        self.label_3.setText(_translate("StockDataFromDatabase", "Window size", None))

        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("StockDataFromDatabase", "1", None))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("StockDataFromDatabase", "Date", None))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("StockDataFromDatabase", "Open", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("StockDataFromDatabase", "Low", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("StockDataFromDatabase", "High", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("StockDataFromDatabase", "Close", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("StockDataFromDatabase", "Volume", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("StockDataFromDatabase", "% change", None))
        self.tabStockWidget.setTabText(self.tabStockWidget.indexOf(self.tab_3), _translate("StockDataFromDatabase", "Default", None))
        self.tabStockWidget.setTabText(self.tabStockWidget.indexOf(self.tab_4), _translate("StockDataFromDatabase", "+", None))

        self.menuFile.setTitle(_translate("StockDataFromDatabase", "File", None))
        self.menuGraph.setTitle(_translate("StockDataFromDatabase", "Graph", None))
        self.actionDraw_Graph.setText(_translate("StockDataFromDatabase", "Draw Graph", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    StockDataFromDatabase = QtGui.QMainWindow()
    ui = Ui_StockDataFromDatabase()
    ui.setupUi(StockDataFromDatabase)
    StockDataFromDatabase.show()
    sys.exit(app.exec_())

