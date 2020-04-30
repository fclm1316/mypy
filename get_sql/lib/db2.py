#encoding:utf-8
import sys,re,os,getfile
reload(sys)
sys.setdefaultencoding("utf-8")
from logger import Log

db2TopSql ="""
db2 connect to {};
    db2 "select * from (select executable_id,insert_timestamp,section_type,num_executions,stmt_exec_time,
    case when num_executions =0 then stmt_exec_time/(num_executions+1) else stmt_exec_time/num_executions end as
    avg_exec_time,substr(stmt_text,1,3000) stmt_text from table(mon_get_pkg_cache_stmt(null,null,null,-2))
    as t where upper(stmt_text) not like '%MON_GET_PKG_CACHE_STMT%' order by avg_exec_time desc ) where 
    avg_exec_time >1000;"
db2 disconnect {0:s};
"""

def getTopData(val,host,dbname):
    log = Log.make_logger()
    pattern = re.compile("x'.*'")
    newline = ''
    stmt_text = ''
    for line in val.split("\n"):
        if pattern.search(line):
            executtable_id = line.split()[0]
            insert_timestamp = line.split()[1]
            section_type = line.split()[2]
            num_execution = line.split()[3]
            stmt_exec_time = line.split()[4]
            avg_exec_time = line.split()[5]
            stmt_text = re.sub(r'[\x00-\x1f]','',stmt_text)
            if len(stmt_text) >0:
                stmt_text = re.sub(r'  |\'|\"','',stmt_text)
                newline = ''.join(executtable_id + '|'+ insert_timestamp + '|' + section_type + '|' + num_execution
                                  + '|' + stmt_text + '|' + stmt_exec_time + '|' +avg_exec_time + '|' + stmt_text)
                getfile.saveFile(newline,host,dbname)
                getfile.saveSql_db2(host,dbname,executtable_id,insert_timestamp,section_type,num_execution,
                                    stmt_exec_time,avg_exec_time,stmt_text)
                stmt_text = ""
                newline = ""