#encoding:utf-8
import  time
from lib import run,getfile,TP,logger
from multiprocessing import Pool

log = logger.Log()

#def getIpInfo():
#    try:
#        with open('ip') as f:
#            return f.readlines()
#    except Exception as e:
#        print(e)
#        return []
def main():
    pool = TP.ThreadPool(5)
    for ip in getIpInfo():
        ip = ip.split()
        pool.run(func=run.run,args=(ip,))
    pool.colse()
    while True:
        if pool.active_count ==1:
            getfile.insert_db()
            break
        else:
            time.sleep(2)

if __name__ == "__mian__":
    main()


# def main(ip):
#     ip = ip.split()
#     print(ip)
#     run.run(ip)
#
# if __name__ == '__main__':
#     pool = Pool(processes=5)
#     pool.map(main,[ip for ip  in getIpInfo()])
#     getfile.insert_db()
#     getfile.tarFile()
