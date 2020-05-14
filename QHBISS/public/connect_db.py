#!/usr/bin/python3
#coding:utf-8
import pymysql
import sys
#mysql 连接封装

config = {
'host' : '192.168.99.101',
'port' : 3306,
'database' : 'mbfedb',
'user' : 'mbfedb',
'passwd' : 'Mbfedb@123'
}
class DataBase:
    def __init__(self,):
        self.new_column = []

    def __enter__(self):
        try:
            #连接数据库
            self.connection = pymysql.connect(**config)
            #获得游标
            # self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
            #默认元组形式
            self.cursor = self.connection.cursor()
            print('connect to db')
        #捕获异常
        except Exception as e:
            print('connect db error')
            print(e)
            sys.exit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type如果抛出异常, 这里获取异常的类型
        #
        # exc_val如果抛出异常, 这里显示异常内容
        #
        # exc_tb如果抛出异常, 这里显示所在位置
        try:
            #断开游标
            self.cursor.close()
            #断开连接
            self.connection.close()
            print('disconnect db')
        except Exception as e:
            print('disconnect db error')
            print(e)
            sys.exit()

    def exec_sql(self, SQL):
        #执行sql
        try:
            print(SQL)
            #执行SQL
            self.cursor.execute(SQL)
            #提交
            self.connection.commit()
            # fetchall() 获取全部值
            # fetchmany(size) 取出一定数量值
            # ferchone() 获取单个值
            results = self.cursor.fetchall()
            #返回值
            return results
            # list_value = []
            # for i in results:
            #     for key,values in i.items():
            #         list_value.append(values)
            # return list_value
        except Exception as e:
            #提交异常回滚
            self.connection.rollback()
            print(e)

    def select(self, table_name, column=[], between=None, order_by=None, group_by=None, **kwargs):
        #查询
        if len(column) == 0:
            #判断需要查询的列长度,不同长度配不同语句
            self.new_column = '*'
        elif len(column) ==1:
            self.new_column = ''.join(column)
        else:
            self.new_column = ', '.join(column)
        # print(table_name,column,kwargs)
        if len(kwargs) == 0:
            #不同长度配不同where
            sql = 'select ' + self.new_column + ' from ' + table_name
            # print(sql)
            return self.exec_sql(sql)
        elif len(kwargs) == 1:
            for key,value in kwargs.items():
                where = "{0:s} = '{1:s}'".format(key,value)
                sql = 'select ' + self.new_column + ' from ' + table_name + ' where ' + where
                # print(sql)
                return self.exec_sql(sql)
        elif len(kwargs) >= 2:
            where_list =[]
            for key,value in kwargs.items():
                where = "{0:s} = '{1:s}'".format(key,value)
                where_list.append(where)
            # print(where_list)
            and_where = ' and '.join(where_list)
            sql = 'select ' + self.new_column + ' from ' + table_name + ' where ' + and_where
            # print(sql)
            return self.exec_sql(sql)




if __name__ == "__main__":
    #表名不能传参
    sql1 = "select codeid from base_generalcode where codetype= %s and codetypename = %s"
    sql2 = "select codeid from base_generalcode where codetypename = %s"
    sql3 = "select codeid from {0:s} where codetype= "
    data = [
        # ('pbccode','人行机构信息'),
        ('人行机构信息'),
        # ('errcode')
        ]
    exe_db = DataBase()
    # with exe_db :
    #    results = exe_db.exec_select(sql2,data)
    #    print(results)
    with exe_db :
        # results = exe_db.exec_select2('base_generalcode',column='codedesc',codetype='pbccode',codeid='001852034595')
        # print(results)
        # sql ='select codeid from base_generalcode'
        # results = exe_db.exec_select(sql)
        # print(results)

        # results = exe_db.exec_select2('base_generalcode',codetype='pbccode',codeid='001852034595')
        # print(results)
        results = exe_db.select('base_generalcode', column=['codedesc', 'codeid', 'codetypename'], codetype='pbccode', codeid='001852034595')
        print(results)
        results1 = exe_db.select('base_generalcode', codetype='pbccode', codeid='001852034595')
        print(results1)
