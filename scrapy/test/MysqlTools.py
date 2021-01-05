#!/usr/bin/env python3
#coding:utf-8
import sys
import pymysql


class mydb:
    def __init__(self,dbconfig):
            self.dbconf = dbconfig

    def __enter__(self):
        try:
            self.connection = pymysql.connect(**self.dbconf)
            self.cursor = self.connection.cursor()
            print('connect to db')
        except Exception as e:
            print(e,"connect to error")
            sys.exit()

    def __exit__(self,exc_type,exc_val,exc_tb):
        try:
            self.cursor.close()
            self.connection.close()
            print('disconnect db')
        except Exception as e:
            print(e,'disconnect error')
            sys.exit()

    def exec_sql(self,SQL):
        try:
            self.cursor.execute(SQL)
            self.connection.commit()
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            self.connection.rollback()
            print(e)
            print('rollback')

if __name__ == "__main__":
    pass