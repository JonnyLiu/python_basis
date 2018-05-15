# coding:utf-8
import MySQLdb

# 连接数据库
db = MySQLdb.connect("localhost","root","Lj970528","bigdata")
# 获取数据库游标
cursor = db.cursor()

# 创建表
sql = """CREATE TABLE EMPLOYEE(
        FIRST_NAME  CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT)"""

cursor.execute(sql)

db.close()