#from lib.ToolBox import getDate
#from lib.DBTool import mysql,oracle
#from lib.GetIpInfo import ipInfo
#print getDate(-1)

import sqlite3,os,sys
sys.path.append("..")
reload(sys)
from lib.difftable import dodiff
from etc.setting_general import sqlite3path
from lib.DaysOfFuturePast import goToPast

#abs_path = '/home/montable/tmp'
abs_path = '/home/montable/'
old_date='20201127'
new_date='20201204'

dodiff(abs_path,old_date,new_date)


dbpath = os.path.join(abs_path,sqlite3path)
file_path = os.path.join(abs_path,"dbtables")

goToPast(dbpath,file_path,old_date,new_date)

#sqlselect = 'select * from paopao where flag = 0 '
##sqlselect = 'select * from paopao where id = 31 '
#update_sql = """update paopao set flag={} where id={} """
#select_target = """select text from paopao where id ={}"""
#select_pattern = """select id from paopao where ip='{}' and dbuser='{}' and tablename='{}' and tablecolumn='{}'"""
##sqlselect = 'select * from paopao where flag = 1 limit 1'
#dbpath = os.path.join(abs_path,sqlite3path)
#con = sqlite3.connect(dbpath)
#cur = con.cursor()
#
#finally_list = []
#
#while True:
#    cur.execute(sqlselect)
#    sql_target = cur.fetchone()
#    if sql_target is not None:
#        id,ip,dbuser,sysmbol,tablename,tablecolumn,text,flag = sql_target
#            #print select_pattern.format(ip,dbuser,tablename,tablecolumn)
#        cur.execute(select_pattern.format(ip,dbuser,tablename,tablecolumn))
#        all_target = cur.fetchall()
#        if len(all_target) == 2:
#            update_id1 = all_target[0][0] 
#            update_id2 = all_target[1][0] 
#            text_1 = cur.execute(select_target.format(update_id1))
#            text_1 = cur.fetchone()[0]
#            text_2 = cur.execute(select_target.format(update_id2))
#            text_2 = cur.fetchone()[0]
#            cur.execute(update_sql.format(1,update_id1))
#            cur.execute(update_sql.format(1,update_id2))
#            con.commit()
#            join_text = '{} --> {}'.format(text_1,text_2)
#            list_str = "{}|{}|{}|{}|{}|{}".format("C", ip, dbuser,tablename,tablecolumn, join_text)
#            #print update_id1,update_id2
#            finally_list.append(list_str)
#        else:
#            cur.execute(update_sql.format(2,id))
#            con.commit()
#            list_str = "{}|{}|{}|{}|{}|{}".format(sysmbol, ip, dbuser,tablename,tablecolumn, text)
#            finally_list.append(list_str)
#    else:
#        break
#
#insert_apmdb(finally_list)
