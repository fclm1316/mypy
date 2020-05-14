#encoding:utf-8
import sys
sys.path.append("..")
import pymysql
from lib.logger import Log
from base64 import decodestring
log = Log.make_logger()

class mydb():
    def __init__(self,password,config):
        self.pwd = decodestring(password)
        self.config = config

    def __enter__(self):
        try:
            self.connection  = pymysql.connect(password=self.pwd,**self.config)
            self.cursor = self.connection.cursor()
            log.info("connect to db")
        except Exception as e:
            log.error(e)
            log.error("connect error")
            sys.exit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.cursor.close()
            self.connection.close()
            log.info("disconnect to db")
        except Exception as e:
            log.error(e)
            log.error("disconnect error")
            sys.exit()

    def exec_sql(self,SQL):
        try:
            self.cursor.execute(SQL)
            self.connection.commit()
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            self.connection.rollback()
            log.error(e)
            log.error(SQL)
            log.error("rollback")


class getMysqlLog():
    def __init__(self,host,dbuser,dbpwd,port=3306):
        self.host = host
        self.dbuser = dbuser
        self.pwd = decodestring(dbpwd)
        self.port = port

    def __enter__(self):
        try:
            self.connection = pymysql.connect(host=self.host,user=self.dbuser,password=self.pwd,port=self.port)
            self.cursor = self.connection.cursor()
            log.info("connect to db")
        except Exception as e:
            log.error(e)
            log.error("connect error")
            sys.exit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.cursor.close()
            self.connection.close()
            log.info("disconnect to db")
        except Exception as e:
            log.error(e)
            log.error("disconnect error")
            sys.exit()

    def exec_sql(self,):
        try:
            SQL = "select variable_value from infomation_schema.global_variables where variable_name='slow_query_log_file';"
            self.cursor.execute(SQL)
            self.connection.commit()
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            self.connection.rollback()
            log.error(e)
            log.error(SQL)
            log.error("rollback")
