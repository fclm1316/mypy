#!/usr/bin/python3
#coding:utf-8
import pymysql

ip = '192.168.99.101'
port = '3306'
database = 'mbfedb'
user = 'mbfedb'
passwd = 'Mbfedb@123'

#打开数据库
db = pymysql.connect(ip,user,passwd,database)
#使用游标
cursor = db.cursor()
#使用execute() 方法执行SQL查询
cursor.execute("SELECT VERSION()")
#使用ftechome()方法获取单条数据
data = cursor.fetchone()
#获取前3条
# date =  cursor.fetchmany(3)
#获取所有结果
# data = cursor.fetchall()

print("Database version {0:s}".format(data[0]))

db.close()



if __name__ == "__main__":
    pass