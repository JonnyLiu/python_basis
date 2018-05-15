# coding:utf-8

import MySQLdb

# 打开数据库
db = MySQLdb.connect("localhost","root","Lj970528","bigdata")

cursor = db.cursor()

sql = "DELETE FORM EMPLOYEE WHERE AGE > 20"

try:
    print "影响行数:",cursor.execute(sql)

    db.commit()

except:
    db.rollback()

db.close()
