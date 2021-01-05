#!/usr/bin/p)ython
#coding:utf-8
import os,sqlite3,sys,glob
sys.path.append("..")
#reload(sys)
#sys.setdefaultencoding('utf-8')
from etc.setting_mysql import *
from etc.setting_general import note_warning1,note_warning2
from lib.DBTool import mysql
from lib.ToolBox import formatDate,renameFile,md5
from lib.logger import Log

log = Log.make_logger()

sql_drop ='drop table if exists bibi'
sql_create = 'create table if not exists bibi(id integer primary key autoincrement,ip char(20),appname char(50),dbname char(20),dbtype intger(1),tablename char(50), tablecolumn char(50),text char(100), operation char(50),flag integer(1),owner char(50))'
sqlcreate_index = 'create index index_bibi_id on bibi (id)'

sql_insert = """insert into bibi(ip,appname,dbname,dbtype,tablename,tablecolumn,text,operation,flag,owner) values ("{}","{}","{}",{},"{}","{}","{}","{}",0,"{}")"""

select_all = 'select * from bibi where flag=0'

sql_alter = "ALTER TABLE {} MODIFY ({} {})"
sql_alter_db2 = "ALTER TABLE {} ALTER COLUMN {} SET DATA TYPE {}"
sql_alter_db2_simple = "ALTER TABLE {} ALTER COLUMN {} SET {}"
sql_add = "ALTER TABLE {} ADD {} {}"
sql_del = "ALTER TABLE {} DROP COLUMN {}" 

sql_recreate = "create table {}({})"
sql_redrop = "drop table {}"

db_type={1:'db2',2:'oracle',3:'mysql'}



def insert_apmdb(ipaddr,appname,dbname,create_date,sql_str,operation=0):
    dbmd5 = md5(" ".join(ipaddr + appname + dbname + create_date + sql_str))  
    if operation == 0:
        sql ='insert into tablemodify(md5, ipaddr, appname, dbname, create_date, sql_text, note_warning) values ("{0}","{1}","{2}","{3}","{4}","{5}","{6}") on duplicate key update ipaddr="{1}" ,appname="{2}", dbname="{3}", create_date="{4}", sql_text="{5}", note_warning="{6}"'.format(dbmd5,ipaddr,appname, dbname, create_date, sql_str, note_warning2)
    else:
        sql ='insert into tablemodify(md5, ipaddr, appname, dbname, create_date, sql_text, note_warning) values ("{0}","{1}","{2}","{3}","{4}","{5}","{6}") on duplicate key update ipaddr="{1}" ,appname="{2}", dbname="{3}", create_date="{4}", sql_text="{5}", note_warning="{6}"'.format(dbmd5,ipaddr,appname, dbname, create_date, sql_str, note_warning1)

    apmdb = mysql(apm_host,apm_port,amp_database,apm_user,apm_passwd)
    with apmdb:
        apmdb.exec_sql(sql)

    

def goToPast(dbpath,file_path,old_date,new_date):

    if os.path.exists(dbpath):
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute(sql_drop)
        cur.execute(sql_create)
        cur.execute(sqlcreate_index)
        con.commit()
        cur.close()
        con.close()
        log.info("recreate bibi")
    else:
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute(sql_create)
        cur.execute(sqlcreate_index)
        con.commit()
        cur.close()
        con.close()
        log.info("create bibi")

    con = sqlite3.connect(dbpath)
    cur = con.cursor()



    sql_apm="select ipaddr,appname,dbuser,dbtype,tablename,tablecolumn,context,operation,tabowner from tablecheck where create_time='{}'"
    apmdb = mysql(apm_host,apm_port,amp_database,apm_user,apm_passwd)
    format_date = formatDate(new_date)
    #format_date = '2020-10-14'
    #print sql_apm.format(format_date)
    with apmdb:
        #print sql_apm.format(format_date)
        rows = apmdb.exec_sql(sql_apm.format(format_date))
    for ip,appname,dbname,dbtype,tablename,tablecolumn,context,operation,tabowner in rows:
        cur.execute(sql_insert.format(ip,appname,dbname,dbtype,tablename,tablecolumn,context,operation,tabowner))
        con.commit()
        log.info("get apmdb tablecheck {} {} {}".format(ip,dbname,format_date))

    sql_update = "update bibi set flag=1 where ip='{}' and tablename='{}' and tablecolumn='{}' and dbname='{}'"
    sql_update_all = "update bibi set flag=1 where ip='{}' and tablename='{}' and dbname='{}'"
    pattern_all = "select tablecolumn,text from bibi where ip='{}' and tablename='{}' and dbname='{}'"
    while True:
        cur.execute(select_all)
        sql_target = cur.fetchone()
        if sql_target is not None:
            id,ip,appname,dbname,dbtype,tablename,tablecolumn,context,operation,flag,owner = sql_target
            #print type(owner)
            if len(owner) == 0 :
                filename = dbname
            else:
                #print owner
                filename = '{}-{}'.format(dbname,owner) 
            #context= context.strip('\n')
                #print filename
            if operation == u"更改":
                log.info('modify.................')
                if dbtype == 1:
                    log.info('modify.................db2')
                    db2_str = context.split('-->')[1]
                    db2_str = db2_str.split()
                    if len(db2_str) == 1:
                        db2_set_all = sql_alter_db2.format(tablename,tablecolumn,db2_str[0])

                    elif len(db2_str) == 5:
                        db2_set_column = sql_alter_db2.format(tablename,tablecolumn,db2_str[0])

                        db2_set_default_1 = db2_str[1]
                        db2_set_default_2 = db2_str[2]
                        db2_set_default_all = '{} {}'.format(db2_set_default_1, db2_set_default_2)
                        db2_set_default = sql_alter_db2_simple.format(tablename,tablecolumn,db2_set_default_all)

                        db2_set_null_1 = db2_str[3]
                        db2_set_null_2 = db2_str[4]
                        db2_set_null_all = '{} {}'.format(db2_set_null_1, db2_set_null_2)
                        db2_set_null = sql_alter_db2_simple.format(tablename,tablecolumn,db2_set_null_all)

                        db2_set_all = '{};{};{}'.format(db2_set_column,db2_set_default,db2_set_null)
                        #print db2_set_all

                    else:
                        db2_set_column = sql_alter_db2.format(tablename,tablecolumn,db2_str[0])

                        db2_set_unknow_1 = db2_str[1]
                        db2_set_unknow_2 = db2_str[2]
                        db2_set_unknow_all = '{} {}'.format(db2_set_unknow_1, db2_set_unknow_2)
                        db2_set_unknow = sql_alter_db2_simple.format(tablename,tablecolumn,db2_set_unknow_all)

                        db2_set_all = '{};{}'.format(db2_set_column,db2_set_unknow)

                    #sql_str = sql_alter_db2.format(tablename,tablecolumn,db2_set_all)
                    insert_apmdb(ip,appname,dbname,format_date,db2_set_all)
                    cur.execute(sql_update.format(ip,tablename,tablecolumn,dbname))
                    con.commit()
                else:    
                    log.info('modify.................other')
                    sql_str = sql_alter.format(tablename,tablecolumn,context.split('-->')[1])
                    insert_apmdb(ip,appname,dbname,format_date,sql_str)
                    cur.execute(sql_update.format(ip,tablename,tablecolumn,dbname))
                    con.commit()

            elif operation == u"增加":
                log.info('add.................')
                file_name = renameFile(ip,filename)
                #print file_name
                path_type = db_type.get(dbtype)
                past_day_file = os.path.join(file_path,old_date,path_type)
                past_file = os.path.join(past_day_file,file_name)
                list_table_name=[]

                with open(past_file,'r') as f:
                    all_table = f.readlines()
                    for table_line in all_table:
                        table_name = table_line.split(',')[0]
                        list_table_name.append(table_name)

                list_table_name=set(list_table_name)
                #增加，主要判断是单独增加字段，还是增加了整张表
                if tablename in list_table_name:
                    log.info('add.................column')
                    sql_str = sql_add.format(tablename,tablecolumn,context)
                    insert_apmdb(ip,appname,dbname,format_date,sql_str)
                    cur.execute(sql_update.format(ip,tablename,tablecolumn,dbname))
                    con.commit()
                else:
                    log.info('create.................table')
                    cur.execute(pattern_all.format(ip,tablename,dbname))
                    all_target = cur.fetchall()
                    column_list = []
                    for line in all_target:
                        create_column,create_text = line
                        #create_text.strip('\n')
                        a = '{} {}'.format(create_column,create_text)
                        column_list.append(a)
                    column_str = ','.join(column_list)
                    sql_str = sql_recreate.format(tablename,column_str)
                    insert_apmdb(ip,appname,dbname,format_date,sql_str,1)
                    cur.execute(sql_update_all.format(ip,tablename,dbname))
                    con.commit()
            else:
                file_name = renameFile(ip,filename)
                path_type = db_type.get(dbtype)
                now_day_file = os.path.join(file_path,new_date,path_type)
                now_file = os.path.join(now_day_file,file_name)
                list_table_name=[]

                with open(now_file,'r') as f:
                    all_table = f.readlines()
                    for table_line in all_table:
                        table_name = table_line.split(',')[0]
                        list_table_name.append(table_name)

                list_table_name=set(list_table_name)
                #减少，主要判断是减少了字段，还是删除了整张表
                if tablename in list_table_name:
                    log.info('del.................column')
                    sql_str = sql_del.format(tablename,tablecolumn,context)
                    insert_apmdb(ip,appname,dbname,format_date,sql_str)
                    cur.execute(sql_update.format(ip,tablename,tablecolumn,dbname))
                    con.commit()
                else:
                    #cur.execute(pattern_all.format(ip,tablename,dbname))
                    #all_target = cur.fetchall()
                    #column_list = []
                    #for line in all_target:
                    #    create_column,create_text = line
                    #    #print create_column,create_text
                    #    a = '{} {}'.format(create_column,create_text)
                    #    column_list.append(a)
                    #column_str = ','.join(column_list)
                    log.info('drop.................table')
                    sql_str = sql_redrop.format(tablename)
                    insert_apmdb(ip,appname,dbname,format_date,sql_str)
                    cur.execute(sql_update_all.format(ip,tablename,dbname))
                    con.commit()
                
                cur.execute(sql_update.format(ip,tablename,tablecolumn,dbname))
                con.commit()

                
        else:
            break


    cur.close()
    con.close()
