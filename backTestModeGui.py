__author__ = 'Devinderjeet'
import sys
from __builtin__ import str
import MySQLdb
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from func.database import connectDB
from ui.loadStockData import Ui_StockDataFromDatabase
import pyqtgraph as pg
import numpy as np
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

class backTestModeGui(QtGui.QMainWindow,Ui_StockDataFromDatabase):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_StockDataFromDatabase()
        self.ui.setupUi(self)
        #if(self.ui.actionDraw_Graph.triggered):
        self.ui.actionDraw_Graph.triggered.connect(self.app_DrawGraph)
        self.ui.loadStockDataButton.clicked.connect(self.app_FetchStockDataFromDatabase)

    def app_DrawGraph(self,stock_Data):
        stock_Data = np.random.normal(size=1000)
        y = np.random.normal(size=1000)
        pg.plot(stock_Data, y, pen=None, symbol='o')

    def app_FetchStockDataFromDatabase(self):
        data = connectDB._app_get_data()
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.horizontalHeader().setVisible(True)
        row = 0
        for col in range(7):
            for value in data:
                if value == None:
                    break
                row_value = value[1:]
                #print row_value[1]
                self.ui.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem(row_value[0]))
                self.ui.tableWidget.setItem(row, 1, QtGui.QTableWidgetItem(str(row_value[1])))
                self.ui.tableWidget.setItem(row, 2, QtGui.QTableWidgetItem(str(row_value[2])))
                self.ui.tableWidget.setItem(row, 3, QtGui.QTableWidgetItem(str(row_value[3])))
                self.ui.tableWidget.setItem(row, 4, QtGui.QTableWidgetItem(str(row_value[4])))
                self.ui.tableWidget.setItem(row, 5, QtGui.QTableWidgetItem(str(row_value[5])))
                self.ui.tableWidget.setItem(row, 6, QtGui.QTableWidgetItem(str(row_value[6])))
                row+=1

    def app_get_data(self):
        data,cur =connectDB._app_get_data()
        self.ui.tableWidget.setRowCount(len(data)) ##set number of rows
        self.ui.tableWidget.setColumnCount(7) ##this is fixed for myTableWidget, ensure that both of your tables, sql and qtablewidged have the same number of columns

        self.ui.tableWidget.setRowCount(len(data)) ##set number of rows

        row = 1
        while True:
            sqlRow = cur.fetchone()

            if sqlRow == None:
                break ##stops while loop if there is no more lines in sql table
            for col in range(1, 6): ##otherwise add row into tableWidget
                self.ui.tableWidget.setItem(row, col, QtGui.QTableWidgetItem(sqlRow[col]))
            row += 1
