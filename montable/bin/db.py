#!/usr/bin/python
import time,os,sys
sys.path.append("..")
reload(sys)
from concurrent.futures import ThreadPoolExecutor
from lib.ToolBox import getDate
from lib.GetIpInfo import ipInfo
from lib.logger import Log
from lib import run,difftable
from etc.setting_general import abs_path,sqlite3path
from lib.DaysOfFuturePast import goToPast


log = Log.make_logger()

def main():

    str_today = getDate(0)
    str_sevenday = getDate(7)
    log = Log.make_logger()

    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        all_task = [executor.submit(run.run,(ip),) for ip in ipInfo()]
#----------------------------------------------------------------------------
#    old_date='20201009'
#    new_date='20201010'
#    difftable.dodiff(abs_path,old_date,new_date)
#----------------------------------------------------------------------------
#    dbpath = os.path.join(abs_path,sqlite3path)
#    file_path = os.path.join(abs_path,"dbtables")
#    goToPast(dbpath,file_path,old_date,new_date)
#----------------------------------------------------------------------------


    cost_time =  time.time() - start_time
    log.info('>>>>> cost : {:.2f} s <<<<< '.format(cost_time))



if __name__ == '__main__':
    main()
