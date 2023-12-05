import mysql.connector
# print('avijit')
avijit=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Biswas.123'
)
# print(avijit.is_connected())

cur=avijit.cursor()
# cur.execute('show databases')
# for x in cur:
#     print(x)
    
# cur.execute('create database fsds_db')
cur.execute("use fsds_db")
# cur.execute('create table fsds1 (name varchar(40) , roll_no int , male_id varchar(50))')

cur.execute("insert into fsds1 values ('avijit',3545,'avijit4000@gmail.com')")