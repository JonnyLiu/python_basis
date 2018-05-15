# coding:utf-8

import MySQLdb

db = MySQLdb.connect("localhost","root","Lj970528","bigdata")

cursor = db.cursor()

# SQL查询数据
cursor.execute("SELECT * FROM EMPLOYEE")

for i in range(cursor.rowcount):
    print cursor.fetchone()

db.close()