import sys
from __builtin__ import str

from PyQt4 import QtCore, QtGui

#from all_func.graph import  basicGraph
from all_func.graph import ohlcGraph
from ui.mainGui import Ui_mainWindow
from widgetOLSWindow import widgetOLSWindow
from all_func.OLSStartegy import *
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

        #self.ui.enter.clicked.connect(self.app_Child_Window)

        #self.ui.comboBox.currentIndexChanged.connect(self.setDatePattern)
        self.ui.treeView.doubleClicked.connect(self.app_Tree_View_Select_Item)

        self.ui.actionQuit.triggered.connect(self.app_Quit)
        self.ui.actionOLS_Tool.triggered.connect(self.app_OLS_Tool)
        self.ui.backtestButton.clicked.connect(self.app_Backtest)
        #self.ui.actionOLS_Tool.triggered.connect(self.app_Calculate_OLS)
    def app_Enter_Button(self):
        data_line = self.ui.lineEdit.displayText()
        print data_line

    def app_Quit(self):
        sys.exit()

    def app_Tree_View_Select_Item(self):
        item = self.ui.treeView.selectedIndexes()[0]
        strData=[]
        strData = item.data(0).toPyObject()
        a = ohlcGraph.graphing()
        a.calculateCT(str(strData),str(self.ui.comboBox.currentText()))

    def app_OLS_Tool(self):
        self.widgetOLSTool_Obj = widgetOLSWindow()
        self.ui = Ui_mainWindow()
        self.widgetOLSTool_Obj.show()
    '''
    def app_Child_Window(self):
        self.child_win = ChildWindow(self)
        self.child_win.show()
    '''
    def app_Backtest(self):
        csv_dir = 'C:/Zerodha/Pi/Exported/'  # CHANGE THIS!
        symbol_list = ['ICICIBANK-EQ','Nifty 50']
        initial_capital = 10000.0
        heartbeat = 0.0
        a = HistoricalCSVDataHandler("ORDER",csv_dir,symbol_list)
        start_date =a._open_convert_csv_files()

        backtest = Backtest.Backtest(
            csv_dir, symbol_list, initial_capital, heartbeat,
            start_date, HistoricalCSVDataHandler, SimulatedExecutionHandler,
            Portfolio, OLSStrategy
        )
        backtest.simulate_trading()

app = QtGui.QApplication(sys.argv)

window = AppGui()	
ui = Ui_mainWindow()
window.show()
sys.exit(app.exec_())