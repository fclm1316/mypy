#!/usr/bin/python
#coding:utf-8
import os,glob,difflib,re,sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf-8')
from datetime import date,datetime
import sqlite3
sys.path.append("..")
from etc.setting_general import sqlite3path,abs_path
from lib.DBTool import mysql
from etc.setting_mysql import *
from lib.ToolBox import md5,saveXLS
from lib.logger import Log
from lib.DaysOfFuturePast import goToPast 
log = Log.make_logger()

today = date.today()
create_time = today.strftime('%Y-%m-%d')


sql_drop='drop table if exists paopao'
sql_create = 'create table if not exists paopao(id integer primary key autoincrement,ip char(20),dbuser char(20),sysmbol char(2),tablename char(100), tablecolumn char(50),text char(50), flag integer(1), md5 char(50),owner char(50))'
sqlcreate_index = 'create index index_paopao_id on paopao (id)'
sqlinsert = """
insert into paopao(ip,dbuser,sysmbol,tablename,tablecolumn,text,flag,md5,owner) values ("{}","{}","{}","{}","{}","{}",0,"{}","{}")
"""



sqlselect_0 = 'select * from paopao where flag = 0;'
sqlselect_1 = 'select * from paopao where flag = 1;'
update_sql_1 = """update paopao set flag=1 where id={};"""
update_sql_3 = """update paopao set flag=3 where id={};"""
update_sql_md5 = """update paopao set flag=2 where md5='{}';"""
select_target = """select text from paopao where id ={};"""
select_pattern = """select id from paopao where ip='{}' and dbuser='{}' and tablename='{}' and tablecolumn='{}';"""
select_pattern_all = """select id,md5 from paopao where ip='{}' and dbuser='{}' and tablename='{}' and tablecolumn='{}' and md5='{}';"""



apm_sql = """
SELECT a.env,a.dbs,b.app_name from hosts a JOIN app b on a.dbs !=0 and a.ipaddr='{}' AND a.app_id = b.app_id JOIN database_passwd c on  c.hostid = a.hostid and c.dbname='{}'
"""

apm_sql2 = """
SELECT a.env,a.dbs,b.app_name from hosts a JOIN app b on a.dbs !=0 and a.ipaddr='{}' AND a.app_id = b.app_id JOIN database_passwd c on  c.hostid = a.hostid and c.dbname='{}' and c.tabowner='{}'
"""

finally_list = []


def read_file(filename):
    with open(str(filename),'r') as fileread:
        return fileread.readlines()

def splitname(str):
    #print str
    ip = str.split('-')[:4]
    ip = '.'.join(ip)
    name_owner = str.split('-')[4:]
    #print name_owner
    try:
        name = name_owner[0] 
        owner = name_owner[1] 
    except:
        name = name_owner[0]
        owner = ''
    finally:
        return ip,name,owner

def insert_apmdb(info_list):
    apmdb = mysql(apm_host,apm_port,amp_database,apm_user,apm_passwd)
    with apmdb:
        for i in info_list:
            sysmbol,ip,dbuser,tablename,tablecolumn,text,tabowner = i.split('|')[:]
            #text_sysmbol = '{} {}'.format(sysmbol, text)
            if sysmbol == '+':
                sysmbol = '增加'
            elif sysmbol == '-':
                sysmbol = '减少'
            else:
                sysmbol = '更改'

            if len(tabowner) == 0 :
                rows = apmdb.exec_sql(apm_sql.format(ip,dbuser))
            else:
                rows = apmdb.exec_sql(apm_sql2.format(ip,dbuser,tabowner))
                
            #print apm_sql.format(ip,dbuser)
            env,dbs,app_name = rows[0]
            dbmd5 = md5(" ".join(ip + dbuser + tablename + tablecolumn + str(dbs) + str(env) + create_time + text))
            sql ='insert into tablecheck(ipaddr, appname, dbuser, dbtype, tablename, tablecolumn, create_time, context, env,dbmd5,sendstatus,operation,tabowner) values ("{0}","{1}","{2}",{3},"{4}","{5}","{6}","{7}",{8},"{9}",{10},"{11}","{12}") on duplicate key update ipaddr="{0}" ,appname="{1}", dbuser="{2}", dbtype={3}, tablename="{4}", tablecolumn="{5}", create_time="{6}", context="{7}", env={8} ,sendstatus={10}, operation="{11}",tabowner="{12}"'.format(ip,app_name, dbuser, dbs, tablename, tablecolumn, create_time, text, env,dbmd5, 0, sysmbol,tabowner)
            apmdb.exec_sql(sql)


def dodiff(abs_path,old_date,new_date):
    dbpath = os.path.join(abs_path,sqlite3path)
    if os.path.exists(dbpath):
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute(sql_drop)
        cur.execute(sql_create)
        cur.execute(sqlcreate_index)
        con.commit()
        cur.close()
        con.close()
        log.info("recreate paopao")
    else:
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute(sql_create)
        cur.execute(sqlcreate_index)
        con.commit()
        cur.close()
        con.close()
        log.info("create paopao")

    con = sqlite3.connect(dbpath)
    cur = con.cursor()

    dict_today = {}
    dict_yestoday = {}


    new_path = os.path.join(abs_path,"dbtables",new_date,"*","*.xtx")
    for new_files in glob.glob(new_path):
        basename = os.path.basename(new_files)
        dict_today[basename] = new_files
        log.info("get new_path {}".format(dict_today[basename]))

    old_path = os.path.join(abs_path,"dbtables",old_date,"*","*.xtx")
    for old_files in glob.glob(old_path):
        basename = os.path.basename(old_files)
        dict_yestoday[basename] = old_files
        log.info("get old_path {}".format(dict_yestoday[basename]))

    for key,value in dict_today.items():
        basename = key.split(".")[0]
        ip,name,owner = splitname(basename)
        #print ip,name,owner
        today_value = value
        yestoday_value = dict_yestoday.get(key)
        if yestoday_value:
            read_today = read_file(today_value)
            read_yestoday = read_file(yestoday_value)
            d = difflib.Differ()
            diff = d.compare(read_yestoday,read_today)
            log.info("compare yestoday today ")
            write_file = ''
            for line in diff:
                if len(line.strip()) > 0:
                    if re.match('\+|\-',line):
                        sysmbol = line.split()[0]
                        #new_line =line.lstrip('- ').split(',')[0]
                        new_line =line.lstrip('- |+ ')
                        tablename = new_line.split(',')[0]
                        tablecolumn = new_line.split(',')[1]
                        text = ' '.join(new_line.split(',')[2:])
                        text =  text.replace('ASDFGHJKL','').strip('\n')
                        sum_md5 = md5("".join(ip + name + tablename + tablecolumn + text + owner))
                        log.info("insert difftable.db {},{},{},{},{}".format(sysmbol,tablename,tablecolumn,text,sum_md5,owner))
                        log.info(sqlinsert.format(ip,name,sysmbol,tablename,tablecolumn,text,sum_md5,owner))
                        cur.execute(sqlinsert.format(ip,name,sysmbol,tablename,tablecolumn,text,sum_md5,owner))
                        con.commit()

    while True:

        cur.execute(sqlselect_0)
        sql_target = cur.fetchone()
        #print sql_target
        if sql_target is not None:
            id,ip,dbuser,sysmbol,tablename,tablecolumn,text,flag,sum_md5,owner = sql_target
                #print select_pattern.format(ip,dbuser,tablename,tablecolumn)
            #print id,sum_md5
            cur.execute(select_pattern_all.format(ip,dbuser,tablename,tablecolumn,sum_md5))
            #print select_pattern_all.format(ip,dbuser,tablename,tablecolumn,sum_md5)
            all_target = cur.fetchall()
            #print all_target
            #print all_target
            if len(all_target) == 1:
                update_id1 = all_target[0][0]
                cur.execute(update_sql_1.format(update_id1))
                #print update_sql_1.format(update_id1)
                con.commit()
            else:
                update_md5 = all_target[0][1] 
                cur.execute(update_sql_md5.format(update_md5))
                con.commit()
        else:
            #print "break"
            break
                

    while True:

        cur.execute(sqlselect_1)
        sql_target = cur.fetchone()
        if sql_target is not None:
            id,ip,dbuser,sysmbol,tablename,tablecolumn,text,flag,sum_md5,owner = sql_target
                #print select_pattern.format(ip,dbuser,tablename,tablecolumn)

            cur.execute(select_pattern.format(ip,dbuser,tablename,tablecolumn))
            all_target = cur.fetchall()
            if len(all_target) == 2:
                update_id1 = all_target[0][0] 
                update_id2 = all_target[1][0] 
                text_1 = cur.execute(select_target.format(update_id1))
                text_1 = cur.fetchone()[0]
                text_2 = cur.execute(select_target.format(update_id2))
                text_2 = cur.fetchone()[0]
                cur.execute(update_sql_3.format(update_id1))
                cur.execute(update_sql_3.format(update_id2))
                con.commit()
                #if md5(text_1) != md5(text_2):
                join_text = '{} --> {}'.format(text_1,text_2)
                #print join_text
                list_str = "{}|{}|{}|{}|{}|{}|{}".format("C", ip, dbuser,tablename,tablecolumn, join_text,owner)
                #print update_id1,update_id2
                finally_list.append(list_str)
            else:
                cur.execute(update_sql_3.format(id))
                con.commit()
                #print "sysmbol"
                list_str = "{}|{}|{}|{}|{}|{}|{}".format(sysmbol, ip, dbuser,tablename,tablecolumn, text,owner)
                finally_list.append(list_str)
        else:
            break

    cur.close()
    con.close()

    insert_apmdb(finally_list)
    past_day = os.path.join(abs_path,"dbtables",old_date)
    #goToPast(dbpath,past_day)


sql_drop_dudu='drop table if exists dudu'
sql_create_dudu='create table if not exists dudu(id integer primary key autoincrement,tablename char(20), tablecolumn char(20),text char(254),md5 char(32),own char(5),flag integer(1))'
sqlcreate_index_dudu='create index index_pappao_md5 on dudu (md5);'

sql_insert_dudu = """
insert into dudu(tablename,tablecolumn,text,md5,own,flag) values ("{}","{}","{}","{}","{}",0)
"""

sql_select_dudu = 'select * from dudu where flag=0 order by id'
sql_select_md5 = 'select * from dudu where md5="{}" order by id'
sql_update1_md5 = 'update dudu set flag = 1 where md5 ="{}"'
sql_update2_md5 = 'update dudu set flag = 2 where md5 ="{}"'

sql_select_2 ="""
select tablename,tablecolumn,text from dudu where own="{}" and flag=2
"""

def short_list(long_list):
    return_list = []
    for i in long_list:
        tablename = i.split(',')[0]
        tablecolumn = i.split(',')[1]
        tabletext = ' '.join(i.split(',')[2:])
        text = tabletext.replace('ASDFGHJKL','')
        return_list.append('{},{},{}'.format(tablename.upper(),tablecolumn.upper(),text.upper()))
    return return_list   
    
    
def ods_diff(ods_ip,ods_schema,target_ipaddr,target_tabowner,filename,target_list_all,ods_list_all,xls_path):
    short_target_list = short_list(target_list_all)
    short_ods_list = short_list(ods_list_all)
    own_target = sorted(list(set(short_target_list).difference(set(short_ods_list))))
    own_ods = sorted(list(set(short_ods_list).difference(set(short_target_list))))
    same = sorted(list(set(short_target_list).intersection(set(short_ods_list))))
    log.info("get own_target,own_ods,same {}-> {}".format(target_ipaddr,ods_ip))
    #diff = []
    #saveXLS(abs_path,ods_ip,target_ipaddr,filename,own_ods,own_target,same,diff)

    if len(own_target) != 0 and len(own_ods) != 0:
        finally_target_list = []
        finally_ods_list = []
        finally_diff = []

        log.info("own_target {}  =! own_ods {}".format(target_ipaddr,ods_ip))

        dbname = '{}_{}_{}_{}.db'.format(target_ipaddr.replace('.','-') ,target_tabowner ,ods_ip.replace('.','-'),ods_schema)
        dbpath = os.path.join(abs_path,xls_path,dbname)

        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute(sql_drop_dudu)
        cur.execute(sql_create_dudu)
        cur.execute(sqlcreate_index_dudu)
        con.commit()
        

        for i in own_target:
            tablename = i.split(',')[0]
            tablecolumn = i.split(',')[1]
            tabletext = i.split(',')[2]
            checkmd5 = md5(''.join(tablename + tablecolumn))
            cur.execute(sql_insert_dudu.format(tablename,tablecolumn,tabletext,checkmd5,'target'))
            con.commit()
        for j in own_ods:
            tablename = j.split(',')[0]
            tablecolumn = j.split(',')[1]
            tabletext = j.split(',')[2]
            checkmd5 = md5(''.join(tablename + tablecolumn))
            cur.execute(sql_insert_dudu.format(tablename,tablecolumn,tabletext,checkmd5,'ods'))
            con.commit()

        while True:
            cur.execute(sql_select_dudu)
            sql_target = cur.fetchone()
            if sql_target is not None:
                id,tablename,tablecolumn,tabletext,tabmd5,own,flag = sql_target[:]
                cur.execute(sql_select_md5.format(tabmd5))
                all_target = cur.fetchall()
                if len(all_target) == 2:
                    finally_tablename = all_target[0][1]
                    finally_tablecolumn = all_target[0][2]
                    finally_tabletext1 = all_target[0][3]
                    finally_tabletext2 = all_target[1][3]
                    finally_tabletext = '源 {} --> ods {}'.format(finally_tabletext1,finally_tabletext2)
                    finally_diff.append('{},{},{}'.format(finally_tablename,finally_tablecolumn,finally_tabletext))
                    cur.execute(sql_update1_md5.format(tabmd5))
                    con.commit()
                else:
                    cur.execute(sql_update2_md5.format(tabmd5))
                    con.commit()
            else:
                break

        cur.execute(sql_select_2.format('target'))
        all_target = cur.fetchall()
        finally_target  = []
        for i in all_target:
            finally_tablename = i[0]
            finally_tablecolumn = i[1]
            finally_tabletext = i[2]
            finally_target.append('{},{},{}'.format(finally_tablename,finally_tablecolumn,finally_tabletext))

        cur.execute(sql_select_2.format('ods'))
        all_ods= cur.fetchall()
        finally_ods  = []
        for i in all_ods:
            finally_tablename = i[0]
            finally_tablecolumn = i[1]
            finally_tabletext = i[2]
            finally_ods.append('{},{},{}'.format(finally_tablename,finally_tablecolumn,finally_tabletext))
            
        #print "---------------------------------------------------------------------"
        #print finally_diff
        #print "---------------------------------------------------------------------"
        #print finally_target 
        #print "---------------------------------------------------------------------"
        #print finally_ods
        cur.close()
        con.close()

        saveXLS(ods_ip,target_ipaddr,filename,finally_ods,finally_target,same,finally_diff,xls_path)
    else:    
        #len(own_target) == 0 and len(own_ods) == 0:
    
        #len(own_target) != 0 and len(own_ods) == 0:

        #len(own_target) == 0 and len(own_ods) != 0:   
        log.info(" save own_target {} own_ods {}".format(target_ipaddr,ods_ip))
        diff = []
        saveXLS(ods_ip,target_ipaddr,filename,own_ods,own_target,same,diff,xls_path)


        



