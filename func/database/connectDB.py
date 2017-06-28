__author__ = 'Devinderjeet'
import MySQLdb
def connectionDB():
    try:
        cnn=MySQLdb.connect(user="root",host="localhost",db="icicibank") # you can use the db library you like here
                                           # i have used pyodbc to connect to MS  Access db
        return cnn
    except Exception, e:
        print e

def getData():
    cnn = connectionDB()
    cursor = cnn.cursor()
    cursor.execute("select * from two_min") # DataTable is a table in Data.mdb
    rawData = cursor.fetchall()
    cnn.commit()
    cnn.close()
    return rawData

def _app_get_data():
    conn = connectionDB()
    cur = conn.cursor()
    cur.execute("SELECT * FROM two_min")
    allSQLRows= cur.fetchall()
    return allSQLRows