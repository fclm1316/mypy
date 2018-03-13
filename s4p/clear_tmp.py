#!/usr/bin/python3
#import shutil
import glob
import os
import time
from datetime import date,datetime
HOME = os.environ['HOME']
FILES_DIR = os.path.join(HOME,'file')
LOG_DIR = os.path.join(HOME,'log')
COMLOG = os.path.join(LOG_DIR,'comlog')
ERRLOG = os.path.join(LOG_DIR,'errlog')
DBBAK = os.path.join(HOME,'db.bak')
today = date.today()
#date_time = datetime.date
#获得时间戳
time_now = int(time.time())
CURDATE = today.strftime('%Y%m%d')
#print(today)
#print(t_local)
#print(CURDATE)
def delete_file(d_path, d_time, *d_file):
    if len(d_file) == 0:
        #如果没有第三个参数，指定文件类型。多级目录os.walk
        all_file = glob.glob(os.path.join(d_path,'*'))
        for f_time in all_file:
            #st_ctime 创建时间 st_mtime 最后一次修改时间 st_size 字节大小
            stateinfo =  os.stat(f_time).st_mtime
            #换算时间
            time_delta = (time_now - stateinfo) /60/60/24
            if time_delta > d_time:
                #print('{0:d}'.format(int(time_delta)))
                print('delete files is :')
                print('{0:s}     {1:d}d ago'.format(os.path.join(f_time),int(time_delta)))
                #os.remove(f_time)
        #print(all_file)
        #print(d_path)
        #print(d_time)
    elif len(d_file) == 1:
        #aa = d_file[0]
        #print(aa)
        #获得的d_file 是元组....所以切片获得第一个。
        all_file = glob.glob(os.path.join(d_path,d_file[0]))
        for f_time in all_file:
            stateinfo =  os.stat(f_time).st_mtime
            time_delta = (time_now - stateinfo) /60/60/24
            if time_delta > d_time:
                print('delete files is :')
                print('{0:s}     {1:d}d ago'.format(os.path.join(f_time),int(time_delta)))
                #os.remove(f_time)
        #print(all_file)
    else:
        print('delete_file + args(path,days[,files]) ')

def delete_file_2(d_path,d_time,*d_file):
    if len(d_file) == 0:
        #调用系统命令来查找。使用C风格替换命令行中的变量
        all_file = os.system('find %s -type f -mtime +%d' % (d_path,d_time))
        print(all_file)
        #os.remove(all_file)
    elif len(d_file) == 1:
        all_file = os.system('find %s -type f -name %s -mtime +%d' % (d_path,d_file[0],d_time))
        print(all_file)
        #os.remove(all_file)
    else:
        print('delete_file + args(path,days[,files]) ')

def delete_dir(d_path,d_time):
    for w_path,w_dirs,w_files in os.walk(d_path):
        for walk_dirs in w_dirs:
            f_f = os.path.join(w_path, walk_dirs)
            stateinfo = os.stat(f_f).st_mtime
            time_delta = (time_now - stateinfo) /60/60/24
            if time_delta > d_time:
                shutil.rmtree(f_f)

def rename_file(re_file):
    if os.path.exists(re_file):
        os.rename(re_file,re_file + '_' + '%s' % (CURDATE))


delete_file(FILES_DIR,2,'tmp*')
delete_file(FILES_DIR,10,'*_[0-9]???_*.dat')
delete_file(LOG_DIR,30)
delete_dir(DBBAK,10)
rename_file(COMLOG)
rename_file(ERRLOG)
