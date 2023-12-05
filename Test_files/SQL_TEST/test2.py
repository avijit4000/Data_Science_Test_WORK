import mysql.connector
# print('avijit')
avijit=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Biswas.123'
)

cur=avijit.cursor()

cur.execute('select * from fsds_db.fsds1')
for i in cur:
    print(i)