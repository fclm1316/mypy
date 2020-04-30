#encoding:utf-8
import sys,re,os,getfile
sys.path.append("..")
from etc.setting_general import *
reload(sys)
sys.setdefaultencoding('utf-8')

def db2TopSqlFile(host,dbname):
    filename = ''.join("db2TopSqlSh_" + host.replace(".","_") + "_" + dbname + ".sh")
    filepath = os.path.join(local_template,filename)
    exec_sh = """. $HOME/.profile;
    db2 connect to {0:s};
    db2 "select * from (select executable_id,insert_timestamp,section_type,num_executions,stmt_exec_time,
    case when num_executions =0 then stmt_exec_time/(num_executions+1) else stmt_exec_time/num_executions end as
    avg_exec_time,substr(stmt_text,1,3000) stmt_text from table(mon_get_pkg_cache_stmt(null,null,null,-2))
    as t where upper(stmt_text) not like '%MON_GET_PKG_CACHE_STMT%' order by avg_exec_time desc ) where 
    avg_exec_time >1000" >/tmp/{0:s}.xtx
    db2 disconnect {0:s};
    """.format(dbname)
    with open(filepath,'w') as f:
        f.writelines(exec_sh)
    return filepath,filename

execDb2TopSh="""
sh /tmp/{};
cat /tmp/{}.xtx
"""