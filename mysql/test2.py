# coding:utf-8
import MySQLdb

# 连接数据库
db = MySQLdb.connect("localhost","root","Lj970528","bigdata")
# 获取数据库游标
cursor = db.cursor()
# SQL插入数据

try:
     sql = """INSERT INTO EMPLOYEE(
          FIRST_NAME,
          LAST_NAME,
          AGE,
          SEX,
          INCOME
          )
          VALUES("Mac","Mohan","20","M","2000")"""
     cursor.execute(sql)
     db.commit()
except:
     db.rollback()

# 关闭数据库
db.close()

