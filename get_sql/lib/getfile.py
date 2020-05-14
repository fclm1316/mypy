#encoding:utf-8
import time,glob,os,tarfile,hashlib,sys
sys.path.append("..")
from etc.setting_general import *
from etc.setting_general import *
from lib.MySqlTool import mydb

time_now = time.strftime('%Y%m%d')

def saveFile(file_text,host,dbname):
    file_name = ''.join(host.replace('.','_') + '_' + dbname + '_' + time_now + '.xtx')
    file_path = os.path.join(local_tmp,file_name)
    with open(file_path,'a') as f:
        f.write(file_text)

def tarFile():
    tar_file = tarfile.open(''.join(os.path.join(local_tmp,time_now) + '.gz'), 'w:gz')
    all_file = glob.glob(os.path.join(local_tmp,'*.xtx'))
    for files in all_file:
        tar_file.add(files)
    tar_file.close()
    os.system('rm *.xtx')

def saveSql_db2(host,app_id,app_name,env,executable_id,stmt_text,num_execution,avg_exec_time,stmt_exec_time):
    file_name = ''.join(host.replace('.','_') + '_' + time_now + '_db2.sql')
    file_path = os.path.join(local_tmp,file_name)
    sql_md5 = md5(stmt_text)
    x_stmt_text = ''
    for v in stmt_text:
        try:
            x_stmt_text += v.encode('utf-8')
        except:
            x_stmt_text += '?'
            pass
    sql = 'insert into db2_slow_sql(app_id,app_name,env,sql_id,stmt_text,sql_md5,num_executions,avg_exec_time,stmt_exec_time)' \
          'values ({0},"{1}",{2},"{3}","{4}","{5}",{6},{7},{8} )on duplicate key update app_id={0},app_name={1},' \
          'env={2},sql_id="{3}",stmt_text="{4}",num_execution={6},avg_exec_time={7},stmt_exec_time={8};\n'\
        .format(app_id,app_name,env,executable_id,x_stmt_text,sql_md5,num_execution,avg_exec_time,stmt_exec_time)
    with open(file_path,'a') as f:
        f.write(sql)

# def saveSql_db2(host,dbname,executable_id,insert_timestamp,section_type,num_executions,\
#                 stmt_exec_time,avg_exec_time,stmt_text):
#     file_name = ''.join(host.replace('.','_') + '_' + dbname + '_' + time_now + '_db2.sql')
#     file_path = os.path.join(local_tmp,file_name)
#     sql_md5 = md5(stmt_text)
#     sql = 'replace into db2_slow_sql(host,dbname,executable_id,insert_timestamp,section_type,' \
#           'num_executions,stmt_exec_time,avg_exec_time,stmt_text,sql_md5) values ("{}","{}","{}",' \
#           '"{}","{}",{},{},{},"{}","{}");\n'.format(host,dbname,executable_id,insert_timestamp,
#                                                  section_type,num_executions,stmt_exec_time,
#                                                  avg_exec_time,stmt_text,sql_md5)
#     with open(file_path,'a') as f:
#         f.write(sql)

def insert_db():
    all_file = glob.glob(os.path.join(local_tmp,'*.sql'))
    with db:
        for sql_file in all_file:
            with open(sql_file) as f:
                for row in f:
                    db.exec_sql(row)
            os.system(''.join('rm' + sql_file))
    # for sql_file in all_file:
    #     cmd = 'mysql -uhandsome -p handsomedb <'
    #     os.system(''.join(cmd + sql_file))
    #     os.system(''.join('rm ' + sql_file))

def saveSql_mysql(host,app_id,app_name,env,executable_id,stmt_text,num_execution,avg_exec_time,stmt_exec_time):
    file_name = ''.join(host.replace('.', '_') + '_' + time_now + '_mysql.sql')
    file_path = os.path.join(local_tmp, file_name)
    sql_md5 = md5(stmt_text)
    sql = 'insert into mysql_slow_sql (app_id,app_name,env,stmt_text,sql_md5,num_executions,avg_exec_time,stmt_exec_time)' \
          'values ({0},"{1}",{2},"{3}","{4}","{5}",{6},{7} )on duplicate key update app_id={0},app_name={1},' \
          'env={2},stmt_text="{3}",num_execution={5},avg_exec_time={6},stmt_exec_time={7};\n' \
        .format(app_id,app_name,env,stmt_text,sql_md5,num_execution,avg_exec_time,stmt_exec_time)
    with open(file_path,'a') as f:
        f.write(sql)


# def saveSql_mysql(host,count,avg_time,total_time,avg_rows,total_rows,sql_text):
#     file_name = ''.join(host.replace('.','_') + '_' +  time_now + '_mysql.sql')
#     file_path = os.path.join(local_tmp,file_name)
#     sql_md5 = md5(sql_text)
#     sql = 'replace into mysql_slow_sql(host,count,avg_time,total_time,avg_rows,total_rows,sql_text,sql_md5)' \
#           ' values ("{}",{},{},{},{},{},"{}","{}"});\n'.format(host,count,avg_time,total_time,avg_rows,
#                                                                total_rows,sql_text.sql_md5)
#     with open(file_path,'a') as f:
#         f.write(sql)

def saveSql_ora(host,app_id,app_name,env,hash_value,sql_text,num_executions,avg_exec_time,Total_time,cost):
    file_name = ''.join(host.replace('.', '_') + '_' + time_now + '_ora.sql')
    file_path = os.path.join(local_tmp, file_name)
    sql_md5 = md5(sql_text)
    sql = 'insert into mysql_slow_sql (app_id,app_name,env,sql_id,stmt_text,sql_md5,num_executions,avg_exec_time,stmt_exec_time,max_cost)' \
          'values ({0},"{1}",{2},"{3}","{4}","{5}",{6},{7},{8},{9} )on duplicate key update app_id={0},app_name={1},' \
          'env={2},sql_id="{3}",stmt_text="{4}",num_execution={6},avg_exec_time={7},stmt_exec_time={8},max_cost={9}};\n' \
        .format(app_id,app_name,env,hash_value,sql_text,sql_md5,num_executions,avg_exec_time,Total_time,cost)
    with open(file_path,'a') as f:
        f.write(sql)
# def saveSql_ora(host,dbusr,hash_value,Total_time,Avg_time,executions,rows,sql_text):
#     file_name = ''.join(host.replace('.','_') + '_' +  time_now + '_ora.sql')
#     file_path = os.path.join(local_tmp,file_name)
#     sql = 'replace into oracle_slow_sql(host,dbusr,hash_value,Total_time,Avg_time,executions,' \
#           'rows,sql_text) values ("{}","{}","{}",{},{},{},{},"{}","{}")'.format(host,dbusr,
#                                                     hash_value,Total_time,Avg_time,executions,rows,sql_text)
#     with open(file_path,'a') as f:
#         f.write(sql)

def md5(sql_text):
    sql_md5 = hashlib.md5(sql_text).hexdigest()
    return sql_md5
