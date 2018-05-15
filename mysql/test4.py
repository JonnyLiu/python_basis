# coding:utf-8
import MySQLdb

db = MySQLdb.connect("localhost","root","Lj970528","bigdata")

cursor = db.cursor()

# 更新数据库里面M的AGE加1
cursor.execute("UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'M'")

db.commit()

db.close()