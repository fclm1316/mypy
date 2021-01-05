#!/usr/bin/python
import time,os,sys
sys.path.append("..")
reload(sys)
from concurrent.futures import ThreadPoolExecutor
from lib.GetIpInfo import ipInfo_compare
from lib.logger import Log
from lib.run import run_ods


log = Log.make_logger()

def main():

    log = Log.make_logger()
    start_time = time.time()
# ods   
    with ThreadPoolExecutor() as executor:
        all_task = [executor.submit(run_ods,(ip),) for ip in ipInfo_compare(0)]


    cost_time =  time.time() - start_time
    log.info('>>>>> cost : {:.2f} s <<<<< '.format(cost_time))



if __name__ == '__main__':
    main()
