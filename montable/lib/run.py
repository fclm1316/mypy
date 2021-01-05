#!/usr/bin/python
#coding:utf-8
import time, re, os,sys, glob
sys.path.append("..")
from etc.setting_general import abs_path,xls_ods_path
from lib.logger import Log
from lib.TablesAnalysis import db2Tables,oracleTables,mysqlTables,ods2alldb
from lib.ToolBox import getDate
log = Log.make_logger()

def run(ipinfo):
    try:
        dbtype,host,user,encpwd,app_id,app_name,env,dbuser,encdbpwd,db_port,db_dbname,tab_owner,importance_table = ipinfo[:]
        log.info("{} {}".format("get",host))
    except Exception as e:
        log.error('{} {} {}'.format(e, "run get ipinfo error",ipinfo))
        return

    if dbtype == 1:
        db2Tables(abs_path,host,dbuser,encdbpwd,db_port,db_dbname,tab_owner,importance_table)

    elif dbtype == 2:
        #pass
        oracleTables(abs_path,host,dbuser,encdbpwd,db_port,db_dbname,tab_owner,importance_table)

    elif dbtype == 3:
        #pass
        mysqlTables(abs_path,host,dbuser,encdbpwd,db_port,db_dbname,tab_owner,importance_table)
                
    else:
        log.critical('{} {}'.format(ipinfo,"not pattern any dbtpye"))
        return

def run_ods(ipinfo_ods):
    try:
        target_dbs = ipinfo_ods[8]

    except Exception as e:
        log.error('{} {} {}'.format(e, "run_ods get  ipinfo error",ipinfo))
        return 

    if target_dbs == 1:
        ods2alldb(ipinfo_ods,xls_ods_path,1)

    elif target_dbs == 2:
        ods2alldb(ipinfo_ods,xls_ods_path,2)

    elif target_dbs == 3:
        ods2alldb(ipinfo_ods,xls_ods_path,3)

    else:
        log.critical('{} {}'.format(ipinfo,"not pattern any target_dbs"))
        return


def run_yzAyc(ipinfo_yz_yc):
    try:
        target_dbs = ipinfo_yz_yc[8]

    except Exception as e:
        log.error('{} {} {}'.format(e, "run_ods get  ipinfo error",ipinfo))
        return 

    if target_dbs == 1:
        ods2alldb(ipinfo_ods,xls_ods_path,1)

    elif target_dbs == 2:
        ods2alldb(ipinfo_ods,xls_ods_path,2)

    elif target_dbs == 3:
        ods2alldb(ipinfo_ods,xls_ods_path,3)

    else:
        log.critical('{} {}'.format(ipinfo,"not pattern any yzAyc"))
        return



if __name__ == '__main__':
    run()
