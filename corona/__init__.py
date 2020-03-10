import pymysql



db = pymysql.connect(host='localhost', user='root', password='280011', db='corona')

cursor = db.cursor()

cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('DATABASE VERSION IS: %s' % data)

db.close()
