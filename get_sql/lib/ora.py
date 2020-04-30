#encoding:utf-8
import sys,os,re,getfile
sys.path.append("..")
from etc.setting_general import *

execOrcTopSh = """
sh /tmp/{} {} >/tmp/OrcTopSql.xtx
cat /tmp/OrcTopSql.xtx
"""

other_cmd = """
sqlplus / as sysdba @/tmp/{} >/tmp/{};
"""

def oraTopData(val,host,dbuser):
    pat_first = re.compile(r'------>')
    pat_clear= re.compile(r'=======>')
    sql_test = ""
    for line in val.split("\n"):
        if pat_first.search(line):
            hash_value = line.split(",")[1]
            Total_time = line.split(",")[2]
            Avg_time = line.split(",")[3]
            executions = line.split(",")[4]
            rows = line.split(",")[5]
        elif pat_clear.search(line):
            sql_test = ''
        else:
            sql_test = line.replace("\"","'")
            if len(sql_test) >0:
                getfile.saveSql_ora(hash_value,Total_time,Avg_time,executions,rows,sql_test)
