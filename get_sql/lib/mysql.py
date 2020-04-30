#encoding:utf-8
import re,getfile

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


