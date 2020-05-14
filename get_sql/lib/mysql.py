#encoding:utf-8
import re,os,sys
sys.path.append("..")
from lib import getfile
from lib.MysqlTool import getMysqlLog

mysqlTopSql = """
/usr/bin/mysqldumpslow -s -c -t 30 {} >/tmp/mysql123.txt;
"""

mysqlChkProcess = '''
ps -ef|grep mysqldumpslow|grep -v grep| wc -l
'''

mysqlCatFile = """
cat /tmp/mysql123.txt
"""

def getTopData(val,host):
    pattern = re.compile(r'Count:.*?Time=.*?Lock=.*?Rows=.*?')
    sql_text =""
    for line in val.split("\n"):
        sql_text = ""
        for line in val.split("\n"):
            if pattern.search(line):
                count = line.split()[1]
                avg_time = line.split()[2].split('=')[1].replace('s','')
                total_time = line.split()[3]
                total_time = re.sub(r'\(|\)|s','',total_time)
                avg_rows = line.split()[6].split('=')[1]
                total_rows = line.split()[7]
                total_rows = re.sub(r'\(|\)|s','',total_rows)
            elif len(line) > 0:
                sql_text = ''.join(sql_text + line)
            else:
                sql_text = re.sub(r'[\x00=\x1f]','',sql_text)
                sql_text = sql_text.replace('"','\'')
                if len(sql_text) > 0:
                    getfile.saveSql_mysql(host,count,avg_time,total_time,avg_time,avg_rows,total_time,sql_text)
                sql_text = ''


def cmdSlow(val,host,app_id,app_name,env):
    tmp_log = ''.join(val + '.txt')
    cmd1 = '/usr/bin/mysqldumpslow -s -c -t 30 {0:s} >{0:s}.txt'.format(val)
    os.system(cmd1)
    with open(tmp_log) as f:
        pattern = re.compile(r'Count:.*?Time=.*?Lock=.*?Rows=.*?')
        sql_text = ''
        for line in f:
            if pattern.search(line):
                count = line.split()[1]
                avg_time = line.split()[2].split('=')[1].replace('s','')
                total_time = line.split()[3]
                total_time = re.sub(r'\(|\)|s','',total_time)
                # avg_rows = line.split()[6].split('=')[1]
                # total_rows = line.split()[7]
                # total_rows = re.sub(r'\(|\)|s','',total_rows)
            elif len(line) > 1:
                sql_text = ''.join(sql_text + line)
            else:
                sql_text = re.sub(r'[\x00=\x1f]','',sql_text)
                sql_text = sql_text.replace('"','\'')
                if len(sql_text) > 0:
                    getfile.saveSql_mysql(host,app_id,app_name,env,sql_text,count,avg_time,total_time)
                sql_text = ''
    cmd2 = 'rm {} {}'.format(val,tmp_log)
    os.system(cmd2)


def getLog(host,dbuser,encdbpwd):
    db = getMysqlLog(host,dbuser,encdbpwd)
    with db:
        result = db.exec_sql()
        return result[0][0]
