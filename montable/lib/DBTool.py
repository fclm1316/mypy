#!/usr/bin/python
#coding:utf-8
import sys
#sys.path.append("..")
#from etc.setting_mysql import *
sys.path.append("..")
import pymysql,cx_Oracle,ibm_db
from lib.logger import Log
from base64 import decodestring
#pwd = decodestring(passwd)
log = Log.make_logger()

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
            log.info('connect to mysql {}:{}'.format(self.host,self.port))
        except Exception as e:
            log.error(e)
            log.error('connect error mysql {}:{}'.format(self.host,self.port))
            #sys.exit()

    def __exit__(self,exc_type,exc_val,exc_tb):
        try:
            self.cursor.close()
            self.connection.close()
            log.info('disconnect db mysql {}:{}'.format(self.host,self.port))
        except Exception as e:
            log.error(e)
            log.error('disconnect error mysql {}:{}'.format(self.host,self.port))
            #sys.exit()


    def exec_sql(self,SQL):
        try:
            #log.info(SQL)
            #log.info('insert into values')
            self.cursor.execute(SQL)
            self.connection.commit()
            log.info("execute sql {}".format(self.host,self.database))
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            self.connection.rollback()
            log.error("{} {}".format(self.host,e))

class oracle():
    def __init__(self,host,port,database,user,password):
            self.host = host
            self.port = port
            self.database = database
            self.user = user
            self.pwd = decodestring(password)
        
    def __enter__(self):
        try:
            self.connection = cx_Oracle.connect('{}/{}@{}:{}/{}'.format(self.user, self.pwd, self.host, self.port, self.database))
            self.cursor = self.connection.cursor()
            log.info('connect to oracle {}:{}'.format(self.host,self.port))
        except Exception as e:
            log.error(e)
            log.error('connect error oracle {}:{}'.format(self.host,self.port))
            #sys.exit()

    def __exit__(self,exc_type,exc_val,exc_tb):
        try:
            self.cursor.close()
            self.connection.close()
            log.info('disconnect db oracle {}:{}'.format(self.host,self.port))
        except Exception as e:
            log.error(e)
            log.error('disconnect error oracle {}:{}'.format(self.host,self.port))
            #sys.exit()


    def exec_sql(self,SQL):
        try:
            self.cursor.execute(SQL)
            self.connection.commit()
            log.info("execute sql {}".format(self.host))
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            self.connection.rollback()
            log.error("{} {}".format(self.host,e))

class db2():
    def __init__(self,host,port,database,user,password):
            self.host = host
            self.port = port
            self.database = database
            self.user = user
            self.pwd = decodestring(password)
        
    def __enter__(self):
        try:
            connStr = "HOSTNAME={};UID={};DATABASE={};PWD={};PORT={};PROTOCOL=TCPIP;".format(self.host,self.user,self.database,self.pwd,self.port)
            self.connection = ibm_db.connect(connStr,'','')
            log.info('connect to db2 {}:{} {}'.format(self.host,self.port,self.database))
        except :
            log.error('connect error db2 {}:{} {}'.format(self.host,self.port,ibm_db.conn_errormsg()))
            #sys.exit()

    def __exit__(self,exc_type,exc_val,exc_tb):
        ibm_db.close(self.connection)
        log.info('disconnect db db2 {}:{} {}'.format(self.host,self.port,self.database))
        #sys.exit()


    def select_sql(self,SQL):
        stmt = ibm_db.exec_immediate(self.connection,SQL)
        row = ibm_db.fetch_tuple(stmt)
        log.info("execute sql {} {}".format(self.host,self.database))
        while ( row ):
            yield row
            row = ibm_db.fetch_tuple(stmt)

class sqlite():
    pass
