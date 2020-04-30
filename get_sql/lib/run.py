#encoding:utf-8
from base64 import decodestring
from fabric import Connection
import db2,mysql,ora,aix,getfile,time,re,os,sys
from logger import Log
sys.path.append("..")
from etc.setting_general import *
log = Log.make_logger()

def run(ipinfo):
    try:
        log.info("get ipinfo")
        dbtype,host,user,encpwd = ipinfo[:4]
        pwd = decodestring(encpwd)
    except Exception as e:
        log.error('{}{}{}'.format(e,ipinfo,"get ipinfo error"))
        return

    try:
        c = Connection(host=host,user=user,connect_kwargs={'password':pwd},connect_timeout=60)

        if dbtype == "db2":
            log.info("dbtype is db2")
            dbname = ipinfo[4]
            cmd =  db2.db2TopSql.format(dbname,dbname)
            result = c.run(cmd,warn=True,hide=True)
            if result.stderr != "":
                log.error('{}{}'.format(ipinfo,result.stderr))
            elif result.stdout != "":
                log.info("analysis db2")
                db2.getTopData(result.stdout,host,dbname)
        elif dbtype == "aix":
            log.info("dbtype is aix")
            dbname = ipinfo[4]
            filepath,filename = aix.db2TopSqlFile(host,name)
            c.put(filepath,route_tmp)
            cmd = aix.execDb2TopSh.format(filename,dbname)
            result = c.run(cmd,warn=True,hide=True)
            if result.stderr != "":
                log.error('{}{}'.format(ipinfo,result.stderr))
            elif result.stdout != "":
                log.info("analysis aix")
                db2.getTopData(result.stdout,host,dbname)

        elif dbtype == "oracle":
            log.info("dbtype is oracle")
            dbuser = ipinfo[4]
            filepath = os.path.join(local_template,oracleShFile)
            c.put(filepath,route_tmp)
            cmd = ora.execOrcTopSh.format(oracleShFile,dbuser)
            result = c.put(cmd,warn=True,hide=True)
            if result.stderr != "":
                log.error('{} {}'.format(ipinfo,result.stderr))
            elif result.stdout !="":
                log.info("analysis oracle")
                ora.getTopData(result.stdout,host,dbuser)
        elif dbtype== "mysql":
            log.info("dbtype is mysql")
            pattern = re.compile(r'Reading mysql slow query log from')
            logpath = ipinfo[4]
            result = c.run(cmd,warn=True,hide=True)
            if re.search(pattern,result.stderr):
                time.sleep(2)
                cat_file = mysql.mysqlCatFile
                result = c.run(cat_file,warn=True,hide=True)
                if result.stderr !="":
                    log.error('{}{}'.format(ipinfo,result.stderr))
                elif result.stdout !="":
                    log.info("{}{}").format("analysis mysql",ipinfo)
                    # print(result.stdout)
                    mysql.getTopData(result.stdout,host)
        else:
            log.critical('{}{}'.format((ipinfo,"not pattern any dbtype")))
            return
        c.close()
    except Exception as e:
        log.critical('{}{}{}'.format(e,ipinfo,"connect error"))
        return

if __name__ == "__mian__":
    run()