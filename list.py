import sys
from PyQt4.QtGui import *
import csv

reader = csv.reader(open('C:/Zerodha/Pi/Exported/BHEL-EQ.csv'))

fx_elements = {}
for row in reader:
    key = row[0]
    if key in fx_elements:
        # implement your duplicate row handling here
        pass
    fx_elements[key] = row[1:]
list = sorted(fx_elements.keys())
#print list

app = QApplication(sys.argv)
listWidget = QListWidget()
listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
#item = listWidget.QListWidgetItem('elements')
#listWidget.insertItem(list)
listWidget.show()
sys.exit(app.exec_()) 