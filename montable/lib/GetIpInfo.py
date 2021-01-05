#!/usr/bin/python
#coding:utf-8
import sys
sys.path.append("..")
from etc.setting_mysql import *
from lib.logger import Log
log = Log.make_logger()

from lib.DBTool import mysql

def ipInfo():
    sql= 'select a.dbs,a.ipaddr,b.sysuser,b.syspassword,a.app_id,c.app_name,a.env,d.dbuser,d.dbpassword,d.port,d.dbname,d.tabowner,c.importance_table from hosts a join hosts_passwd b on a.dbs !=0 and a.host_status=1 and a.hostid=b.hostid and b.isinstance=1 join app c on a.app_id = c.app_id join database_passwd d on a.hostid=d.hostid ;'
    #sql= 'select a.dbs,a.ipaddr,b.sysuser,b.syspassword,a.app_id,c.app_name,a.env,d.dbuser,d.dbpassword,d.port,d.dbname,c.importance_table from hosts a join hosts_passwd b on a.dbs !=0 and a.host_status=1 and a.hostid=b.hostid and b.isinstance=1 join app c on a.app_id = c.app_id join database_passwd d on a.hostid=d.hostid and a.ipaddr="203.3.238.3" and d.dbname="hrmsdb";'
    apmdb = mysql(apm_host,apm_port,amp_database,apm_user,apm_passwd)
    with apmdb:
        rows = apmdb.exec_sql(sql)
        #print rows
        for dbs,ipaddr,sysuser,syspassword,app_id,app_name,env,dbuser,dbpassword,db_port,db_dbname,tab_owner,importance_table in rows:
            yield dbs,ipaddr.strip(),sysuser.strip(),syspassword.strip(),app_id,app_name.strip(),env,dbuser.strip(),dbpassword.strip(),int(db_port),db_dbname.strip(),str(tab_owner),importance_table

def ipInfo_compare(compare_type):
    #sql = 'select a.ip,a.dbuser,a.dbpwd,a.port,a.dbname,b.schema,b.compare_file,c.app_name from ods_ip a join ods_compare b on a.compare_id = b.compare_id join app c on b.app_id = c.app_id'
    sql = 'select a.ip,a.dbuser,a.dbpwd,a.port,a.dbname,b.schema,c.app_name,d.ipaddr,d.dbs,f.dbuser,f.dbpassword,f.port,f.dbname,f.tabowner from compare_ip a join compare_config b on a.compare_id = b.compare_id join app c on b.app_id = c.app_id join hosts d on d.hostid = b.hostid join database_passwd f on b.hostid = f.hostid and  b.compare_type = {}'.format(int(compare_type))
    apmdb = mysql(apm_host,apm_port,amp_database,apm_user,apm_passwd)
    with apmdb:
        rows = apmdb.exec_sql(sql)
        #print rows
        for ods_ip,ods_dbuser,ods_pwd,ods_port,ods_dbname,ods_schema,app_name,target_ipaddr, target_dbs,target_dbuser,target_dbpassword,target_port,target_dbname,target_tabowner in rows:
            yield ods_ip.strip(), ods_dbuser.strip(), ods_pwd.strip(), ods_port, ods_dbname.strip(), ods_schema.strip(), app_name, target_ipaddr,target_dbs, target_dbuser.strip(), target_dbpassword.strip(), target_port,target_dbname.strip(), str(target_tabowner)




if __name__ == "__main__":
    for i in ipInfo_ods():
        print i
