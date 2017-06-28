__author__ = 'Devinderjeet'


from PyQt4 import QtCore, QtGui


import MySQLdb
conn = MySQLdb.connect(user="root", host="localhost", passwd="", db="icicibank")

cur = conn.cursor()

cur.execute("SELECT * FROM two_min")
row = cur.fetchone()
while row is not None:
    print row[1],row[2],row[3],row[4],row[5],row[6]
    row = cur.fetchone()

cur.close()
conn.close()

def fillQTable(self):
    #data = [('1','2','3','4'),('5','6','7','8')] #this is from database
    data = self.getData()
    rowCount = len(data)
    colCount = 4
    self.qttable.setRowCount(rowCount)
    self.qttable.setColumnCount(colCount)
    self.qttabke.verticalHeader().setVisible(False)
    self.qttabke.setHorizontalHeaderLabels(QString("num1;num2;num3;num4").split(";"))
    self.qttabke.horizontalHeader().setVisible(True)
    for s in range(colCount):
        self.qttable.horizontalHeaderItem(s).setTextAlignment(Qt.AlignLeft)
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            item = QTableWidgetItem(col)
            self.qttabke.setItem(i, j, item)

def connectionDB(self):
    try:
        cnn=MySQLdb.connect(user="root", host="localhost", passwd="", db="icicibank") # you can use the db library you like here
                                           # i have used pyodbc to connect to MS  Access db
        return cnn
    except Exception, e:
        print e

def getData(self):
    cnn = self.connectionDB()
    cursor = cnn.cursor()
    cursor.execute("select * from DataTable") # DataTable is a table in Data.mdb
    rawData = cursor.fetchall()
    cnn.commit()
    cnn.close()
    return rawData