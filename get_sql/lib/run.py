#encoding:utf-8
import time,re,os,sys
from base64 import decodestring
from fabric import Connection
sys.path.append("..")
from etc.setting_general import *
from lib.logger import Log
from lib import db2,mysql,ora,aix,getfile

log = Log.make_logger()

def run(ipinfo):
    try:
        dbtype,host,user,encpwd,app_id,app_name,env,dbuser,encpwd = ipinfo[:]
        log.info("get {}".format(host))
        pwd = decodestring(encpwd)
    except Exception as e:
        log.error('{}{}{}'.format(e,ipinfo,"get ipinfo error"))
        return

    try:
        c = Connection(host=host,user=user,connect_kwargs={'password':pwd},connect_timeout=60)

        if dbtype == "2":
            log.info("dbtype is db2")
            filepath = os.path.join(local_template,db2TopSqlsh)
            c.put(filepath,route_tmp)
            cmd =  db2.execDb2TopSh.format(db2TopSqlSh)
            result = c.run(cmd,warn=True,hide=True)
            if result.stderr != "":
                log.error('{}{}'.format(ipinfo,result.stderr))
            elif result.stdout != "":
                log.info("analysis db2 start")
                db2.getTopData(result.stdout,host,app_id,app_name,env)
                log.info("analysis db2 done")

        elif dbtype == "3":
            log.info("dbtype is aix")
            filepath = os.path.join(local_template,oracleShFile)
            c.put(filepath,route_tmp)
            cmd = ora.execOrcTopSh.format(oracleShFile,dbuser)
            result = c.run(cmd,warn=True,hide=True)
            if result.stderr != "":
                log.error('{}{}'.format(ipinfo,result.stderr))
            elif result.stdout != "":
                log.info("analysis oracle start")
                db2.getTopData(result.stdout,host,app_id,app_name,env)
                log.info("analysis oracle done")

        elif dbtype== "4":
            log.info("dbtype is mysql")
            logpath = mysql.getLog(host,dbuser,encdbpwd)
            localfile_name = os.path.join(local_tmp,''.join(host.replace('.','_') + "_mysql.log"))
            log.info("get log file")
            c.get(logpath,localfile_name)
            try :
                log.info("analysis mysql start")
                mysql.cmdSlow(localfile_name,host,app_id,app_name,env)
                log.info("analysis mysql done")
            except Exception as e:
                log.info("analysis mysql error {}").format(e)

        else:
            log.critical('{} {}'.format((ipinfo,"not pattern any dbtype")))
            return
        c.close()

    except Exception as e:
        log.critical('{}{}{}'.format(e,ipinfo,"connect error"))
        return

if __name__ == "__mian__":
    run()