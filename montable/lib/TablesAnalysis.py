#!/usr/bin/python
#coding:utf-8
import sys,time,os,re
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf-8')
from lib.logger import Log
from lib.ToolBox import fromatTuple,saveMysqlStr,makeDir,renameFile,saveOracleStr,saveDb2Str
from lib.DBTool import mysql,oracle,db2
from lib.difftable import ods_diff

log = Log.make_logger()
    

def db2Tables(path,host,dbuser,dbpwd,dbport,dbname,tabowner,importance_table):
    tuple_table = fromatTuple(importance_table,'upper')
    dir_path = makeDir(path,'db2')
    if tabowner == 'None':
        sql = 'select tabname,colname,typename,length,DEFAULT,NULLS from syscat.columns where tabname in{} '.format(tuple_table)
        save_file = renameFile(host,dbname)
    else:
        sql = "select tabname,colname,typename,length,DEFAULT,NULLS from syscat.columns where TABSCHEMA='{}' and tabname in{} ".format(tabowner,tuple_table)
        dbname_tabowner = '{}-{}'.format(dbname,tabowner)
        save_file = renameFile(host,dbname_tabowner) 

    save_path_file = os.path.join(dir_path,save_file)
    list_all = []
    targetdb = db2(host,dbport,dbname,dbuser,dbpwd)
    with targetdb:
        rows = targetdb.select_sql(sql)
        for i in rows:
            _a,_b,_c,_d,_e,_f = i[:]
            if _f == 'Y':
                _f = 'NOT NULL'
            else:
                _f = 'ASDFGHJKL'
            if str(_e) != 'None':
                _e = 'DEFAULT {}'.format(_e.strip())
            else:
                _e ='ASDFGHJKL'
            str_list = '{},{},{}({}),{},{}'.format(_a,_b,_c,_d,_e,_f)
            list_all.append(str_list)
            #print str_list
    #dir_path = makeDir(path,'db2')
    save_path_file = os.path.join(dir_path,save_file)
    log.info("saving file {}".format(save_file))
    saveDb2Str(list_all,save_path_file)




def oracleTables(path,host,dbuser,dbpwd,dbport,dbname,tabowner,importance_table):
    #print path,host,dbuser,dbpwd,db_port,db_dbname,importance_table
    tuple_table =  fromatTuple(importance_table,'upper')
    dir_path = makeDir(path,'oracle')

    if tabowner == 'None':
        sql = """select table_name,column_name,data_type,data_length,DATA_DEFAULT,nullable from all_tab_columns where table_name in{} """.format(tuple_table)
        save_file = renameFile(host,dbname)
    else:
        sql = """select table_name,column_name,data_type,data_length,DATA_DEFAULT,nullable from all_tab_columns where owner ='{}' and  table_name in{} """.format(tabowner,tuple_table)
        dbname_tabowner = '{}-{}'.format(dbname,tabowner)
        save_file = renameFile(host,dbname_tabowner) 

    save_path_file = os.path.join(dir_path,save_file)
    #sql = 'select table_name,column_name,data_type,data_length from all_tab_columns where table_name in{}'.format(tuple_table)
    targetdb = oracle(host,dbport,dbname,dbuser,dbpwd)
    with targetdb:
        rows = targetdb.exec_sql(sql)
    log.info("saving file {}".format(save_file))
    saveOracleStr(set(rows),save_path_file)





def mysqlTables(path,host,dbuser,dbpwd,dbport,dbname,tab_owner,importance_table):
    #print path,host,dbuser,dbpwd,db_port,db_dbname,importance_table
    tuple_table =  fromatTuple(importance_table,'lower')
    dir_path = makeDir(path,'mysql')
    save_file = renameFile(host,dbname)
    save_path_file = os.path.join(dir_path,save_file)
    sql = 'select table_name,column_name,column_type,COLUMN_DEFAULT,IS_NULLABLE from information_schema.columns where table_name in{} ;'.format(tuple_table)
    #sql = 'select table_name,column_name,column_type,IS_NULLABLE,COLUMN_KEY from information_schema.columns where table_name in{};'.format(tuple_table)
    #sql = 'select table_name,column_name,column_type from information_schema.columns where table_name in{};'.format(tuple_table)
    targetdb = mysql(host,dbport,dbname,dbuser,dbpwd)
    with targetdb:
        rows = targetdb.exec_sql(sql)
    log.info("saving file {}".format(save_file))
    saveMysqlStr(rows,save_path_file)






def odsTables(host,dbuser,dbpwd,dbport,dbname,schema):
    sql_all = "select tabname,colname,typename,length,DEFAULT,NULLS from syscat.columns where TABSCHEMA='{}' order by tabname".format(schema)
    sql_tabname = "select distinct(tabname) from syscat.columns where TABSCHEMA='{}' order by tabname".format(schema)
    list_all = []
    list_tabname = []
    targetdb = db2(host,dbport,dbname,dbuser,dbpwd)
    with targetdb:
        rows = targetdb.select_sql(sql_all)
        for i in rows:
            _a,_b,_c,_d,_e,_f = i[:]
            if _f == 'Y':
                _f = 'NOT NULL'
            else:
                _f = 'ASDFGHJKL'
            if str(_e) != 'None':
                _e = 'DEFAULT {}'.format(_e.strip())
            else:
                _e ='ASDFGHJKL'
            str_list = '{},{},{}({}),{},{}'.format(_a,_b,_c,_d,_e,_f)
            list_all.append(str_list)

        tabname = targetdb.select_sql(sql_tabname)
        for i in tabname:
            list_tabname.append(str(i[0]))

    return list_tabname,list_all

   
    
def db2Tables_return(host,dbuser,dbpwd,dbport,dbname,tabowner,importance_table):
    if len(importance_table) == 1:
       importance_table.append('ASDFGHJKL')
    if tabowner == 'None':
        sql = 'select tabname,colname,typename,length,DEFAULT,NULLS from syscat.columns where tabname in{} order by tabname'.format(tuple(importance_table))
    else:
        sql = "select tabname,colname,typename,length,DEFAULT,NULLS from syscat.columns where TABSCHEMA='{}' and tabname in{} order by tabname".format(tabowner,tuple(importance_table))
    #print sql
    list_all = []
    targetdb = db2(host,dbport,dbname,dbuser,dbpwd)
    with targetdb:
        rows = targetdb.select_sql(sql)
        for i in rows:
            _a,_b,_c,_d,_e,_f = i[:]
            if _f == 'Y':
                _f = 'NOT NULL'
            else:
                _f = 'ASDFGHJKL'
            if str(_e) != 'None':
                _e = 'DEFAULT {}'.format(_e.strip())
            else:
                _e ='ASDFGHJKL'
            str_list = '{},{},{}({}),{},{}'.format(_a,_b,_c,_d,_e,_f)
            list_all.append(str_list)
    return sorted(set(list_all))




#def ods2db2(ipinfo_ods,xls_path):
#    ods_ip,ods_dbuser,ods_pwd,ods_port,ods_dbname,ods_schema,app_name,target_ipaddr,target_dbs,target_dbuser,target_dbpassword,target_port,target_dbname,target_tabowner = ipinfo_ods[:]
#
#    ods_list_tabname,ods_list_all = odsTables(ods_ip,ods_dbuser,ods_pwd,ods_port,ods_dbname,ods_schema)
#
#    target_list_all = db2Tables_return(target_ipaddr,target_dbuser,target_dbpassword,target_port,target_dbname,target_tabowner,ods_list_tabname)
#
#    filename = '{}-{}'.format(ods_schema,app_name)
#
#    log.info("filename {}".format(filename))
#
#    ods_diff(ods_ip,ods_schema,target_ipaddr,filename,target_list_all,ods_list_all,xls_path)
#
#def ods2oracle(ipinfo_ods,xls_path):
#    ods_ip,ods_dbuser,ods_pwd,ods_port,ods_dbname,ods_schema,app_name,target_ipaddr,target_dbs,target_dbuser,target_dbpassword,target_port,target_dbname,target_tabowner = ipinfo_ods[:]
#
#    ods_list_tabname,ods_list_all = odsTables(ods_ip,ods_dbuser,ods_pwd,ods_port,ods_dbname,ods_schema)
#    
#    target_list_all = oracleTables_return(target_ipaddr,target_dbuser,target_dbpassword,target_port,target_dbname,target_tabowner,ods_list_tabname)
#
#    filename = '{}-{}'.format(ods_schema,app_name)
#    #print filename
#
#    log.info("filename {}".format(filename))
#
#    ods_diff(ods_ip,ods_schema,target_ipaddr,filename,target_list_all,ods_list_all,xls_path)


def ods2alldb(ipinfo_ods,xls_path,dbtype):
    ods_ip,ods_dbuser,ods_pwd,ods_port,ods_dbname,ods_schema,app_name,target_ipaddr,target_dbs,target_dbuser,target_dbpassword,target_port,target_dbname,target_tabowner = ipinfo_ods[:]

    if len(target_tabowner) == 0:
        target_tabowner = "none"

    ods_list_tabname,ods_list_all = odsTables(ods_ip,ods_dbuser,ods_pwd,ods_port,ods_dbname,ods_schema)
    
    if dbtype == 1 :
        target_list_all = db2Tables_return(target_ipaddr,target_dbuser,target_dbpassword,target_port,target_dbname,target_tabowner,ods_list_tabname)

    elif dbtype == 2:
        target_list_all = oracleTables_return(target_ipaddr,target_dbuser,target_dbpassword,target_port,target_dbname,target_tabowner,ods_list_tabname)

    elif dbtype == 3:
        target_list_all = mysqlTables_return(target_ipaddr,target_dbuser,target_dbpassword,target_port,target_dbname,target_tabowner,ods_list_tabname)

    filename = '{}-{}'.format(ods_schema,app_name)
    #print filename

    log.info("filename {}".format(filename))

    ods_diff(ods_ip,ods_schema,target_ipaddr,target_tabowner,filename,target_list_all,ods_list_all,xls_path)




def mysqlTables_return(host,dbuser,dbpwd,dbport,dbname,tab_owner,importance_table):
    if len(importance_table) == 1:
        importance_table.append('ASDFGHJKL')
    sql = 'select table_name,column_name,column_type,COLUMN_DEFAULT,IS_NULLABLE from information_schema.columns where table_name in{};'.format(tuple(importance_table))
    #print sql

    list_all = []
    #print type(host),type(dbport),type(dbname),type(dbuser)
    targetdb = mysql(host,dbport,dbname,dbuser,dbpwd)
    with targetdb:
        rows = targetdb.exec_sql(sql)
    for i in rows:
        a,b,c,d,e = i
        if e == 'YES':
            e = 'NOT NULL'
        else:
            e = 'ASDFGHJKL'
        if str(d).strip() != 'None':
            d = 'DEFAULT {}'.format(d.strip())
        else:
            d ='ASDFGHJKL'
        mysql_line = '{},{},{},{},{}'.format(a,b,c,d,e)
        list_all.append(mysql_line)
    return sorted(set(list_all))

    
def oracleTables_return(host,dbuser,dbpwd,dbport,dbname,tabowner,importance_table):
    if len(importance_table) == 1:
       importance_table.append('ASDFGHJKL')
    if tabowner == 'None':
        sql = """select table_name,column_name,data_type,data_length,DATA_DEFAULT,nullable from all_tab_columns where table_name in{} """.format(tuple(importance_table))
    else:
        sql = """select table_name,column_name,data_type,data_length,DATA_DEFAULT,nullable from all_tab_columns where owner ='{}' and  table_name in{} """.format(tabowner,tuple(importance_table))
    
    list_all = []
    targetdb = oracle(host,dbport,dbname,dbuser,dbpwd)
    with targetdb:
        rows = targetdb.exec_sql(sql)
    rows = set(rows)
    for i in rows:
        a,b,c,d,e,_f = i
        if _f == 'Y':
            _f = 'NOT NULL'
        else:
            _f = 'ASDFGHJKL'
        if str(e).strip() != 'None':
            e = 'DEFAULT {}'.format(e.strip())
        else:
            e ='ASDFGHJKL'
        oracle_line = '{},{},{}({}),{},{}'.format(a,b,c,d,e,_f)
        list_all.append(oracle_line)
    return sorted(set(list_all))
