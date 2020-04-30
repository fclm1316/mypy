#encoding:utf-8
import time,glob,os,tarfile,hashlib,sys
sys.path.append("..")
from etc.setting_general import local_tmp,local_template,route_tmp

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

def saveSql_db2(host,dbname,executable_id,insert_timestamp,section_type,num_executions,\
                stmt_exec_time,avg_exec_time,stmt_text):
    file_name = ''.join(host.replace('.','_') + '_' + dbname + '_' + time_now + '_db2.sql')
    file_path = os.path.join(local_tmp,file_name)
    sql_md5 = md5(stmt_text)
    sql = 'replace into db2_slow_sql(host,dbname,executable_id,insert_timestamp,section_type,' \
          'num_executions,stmt_exec_time,avg_exec_time,stmt_text,sql_md5) values ("{}","{}","{}",' \
          '"{}","{}",{},{},{},"{}","{}");\n'.format(host,dbname,executable_id,insert_timestamp,
                                                 section_type,num_executions,stmt_exec_time,
                                                 avg_exec_time,stmt_text,sql_md5)
    with open(file_path,'a') as f:
        f.write(sql)

def insert_db():
    all_file = glob.glob(os.path.join(local_tmp,'*.sql'))
    for sql_file in all_file:
        cmd = 'mysql -uhandsome -p handsomedb <'
        os.system(''.join(cmd + sql_file))
        os.system(''.join('rm ' + sql_file))

def saveSql_mysql(host,count,avg_time,total_time,avg_rows,total_rows,sql_text):
    file_name = ''.join(host.replace('.','_') + '_' +  time_now + '_mysql.sql')
    file_path = os.path.join(local_tmp,file_name)
    sql_md5 = md5(sql_text)
    sql = 'replace into mysql_slow_sql(host,count,avg_time,total_time,avg_rows,total_rows,sql_text,sql_md5)' \
          ' values ("{}",{},{},{},{},{},"{}","{}"});\n'.format(host,count,avg_time,total_time,avg_rows,
                                                               total_rows,sql_text.sql_md5)
    with open(file_path,'a') as f:
        f.write(sql)

def saveSql_ora(host,dbusr,hash_value,Total_time,Avg_time,executions,rows,sql_text):
    file_name = ''.join(host.replace('.','_') + '_' +  time_now + '_ora.sql')
    file_path = os.path.join(local_tmp,file_name)
    sql = 'replace into oracle_slow_sql(host,dbusr,hash_value,Total_time,Avg_time,executions,' \
          'rows,sql_text) values ("{}","{}","{}",{},{},{},{},"{}","{}")'.format(host,dbusr,
                                                    hash_value,Total_time,Avg_time,executions,rows,sql_text)
    with open(file_path,'a') as f:
        f.write(sql)

def md5(sql_text):
    sql_md5 = hashlib.md5(sql_text).hexdigest()
    return sql_md5
