__author__ = 'Devinderjeet'
from all_func.stats import linearRegr

from ui.OLSWindow import Ui_MainWindow
import sys, os, shutil, glob, time
from PyQt4 import QtCore, QtGui

class widgetOLSWindow(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculateOLSButton.clicked.connect(self.widget_Calculate_OLS)

    def open_VariableX_CSV(self):
        pass

    def browse_VariableX_CSV(self):
        pass
    def open_VariableY_CSV(self):
        pass
    def browse_VariableY_CSV(self):
        pass
    def widget_Calculate_OLS(self):
        app_Obj_A = linearRegr.user_Defined_Linear_Regression()
        app_Obj_A.user_Defined_OLS()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = widgetOLSWindow()
    window.show()
    sys.exit(app.exec_())