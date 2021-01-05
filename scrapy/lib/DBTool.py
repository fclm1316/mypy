#!/usr/bin/python
#coding:utf-8
import sys
sys.path.append("..")
import pymysql
from base64 import decodestring

class mysql():
    def __init__(self,host,port,database,user,password):
            self.host = host
            self.port = port
            self.database = database
            self.user = user
            self.pwd = decodestring(password)
        
    def __enter__(self):
        try:
            self.connection = pymysql.connect(host=self.host,user=self.user,db=self.database,password=self.pwd,port=self.port)
            self.cursor = self.connection.cursor()
            #print 'connect to mysql {}:{}'.format(self.host,self.port)
        except Exception as e:
            print e
            #print 'connect error mysql {}:{}'.format(self.host,self.port)
            sys.exit()

    def __exit__(self,exc_type,exc_val,exc_tb):
        try:
            self.cursor.close()
            self.connection.close()
            #print 'disconnect db mysql {}:{}'.format(self.host,self.port)
        except Exception as e:
            print e
            #print 'disconnect error mysql {}:{}'.format(self.host,self.port)
            sys.exit()


    def exec_sql(self,SQL):
        try:
            self.cursor.execute(SQL)
            self.connection.commit()
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            self.connection.rollback()
            print "{} {}".format(self.host,e)
