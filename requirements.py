import os

os.system('cmd /c "pip install fpdf2 & pip install mysql.connector"')
import mysql.connector as ms

# connecting sql database and creating cursor

db = ms.connect(
    host='localhost',
    user='root',
    password='',
)

if db.is_connected():
    print('database connected.')
else:
    print("error while connecting database.")
    
cur = db.cursor()

cur.execute('create database if not exists libman;')
cur.execute('use libman;')
cur.execute('''
            create table libdata(bookname varchar(100),
            author varchar(30),
            issued_date varchar(20),
            exp_return varchar(20),
            issued_by varchar(30),
            issuer_class varchar(10),
            return_act varchar(20),
            mobile bigint(10),
            PRN_No int(11) UNIQUE);                                     
            ''')
