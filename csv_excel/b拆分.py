#!/usr/bin/python3
#coding:utf-8
from datetime import datetime
import csv
import os
import glob
import time
from concurrent.futures import ThreadPoolExecutor

test_path = ['d:/data/2019.csv','d:/data/2009.csv']
input_file = 'd:/data/'
in_path_file = glob.glob(os.path.join(input_file,'*.csv'))

def make_dir(path):
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)


def writeCSV(mouth, row,out_path):
    list_size =[]
    list_size.append(row)
    if len(list_size) == 20000:
        with open(os.path.join(out_path + '/' + str(mouth) + '.csv'), 'a+', encoding='gb18030', newline='') as csv_write:
            for rows in list_size:
                firewrite = csv.writer(csv_write)
                firewrite.writerow(rows)
        list_size = []
    else:
        with open(os.path.join(out_path + '/' + str(mouth) + '.csv'), 'a+', encoding='gb18030', newline='') as csv_write:
            for rows in list_size:
                firewrite = csv.writer(csv_write)
                firewrite.writerow(rows)
        list_size = []


def ByMonth(input_file):
    #json 必须是双引号
    mouth_dirt = {"1月":0,"2月":0,"3月":0,"4月":0,"5月":0,
                  "6月":0,"7月":0,"8月":0,"9月":0,"10月":0,
                  "11月":0,"12月":0}
    dir_name = os.path.join(input_file).split('.')[0]
    make_dir(dir_name)
    with open(input_file,'r',encoding='gb18030',newline='') as csv_file:
        filereader = csv.reader(csv_file)
        next(filereader)
        for row in filereader:
            work_date = datetime.strptime(row[0],'%Y%m%d')
            if work_date.month == 1:
                writeCSV(1,row,dir_name)
                mouth_dirt['1月'] += 1
            elif work_date.month == 2:
                writeCSV(2,row,dir_name)
                mouth_dirt['2月'] += 1
            elif work_date.month == 3:
                writeCSV(3,row,dir_name)
                mouth_dirt['3月'] += 1
            elif work_date.month == 4:
                writeCSV(4,row,dir_name)
                mouth_dirt['4月'] += 1
            elif work_date.month == 5:
                writeCSV(5,row,dir_name)
                mouth_dirt['5月'] += 1
            elif work_date.month == 6:
                writeCSV(6,row,dir_name)
                mouth_dirt['6月'] += 1
            elif work_date.month == 7:
                writeCSV(7,row,dir_name)
                mouth_dirt['7月'] += 1
            elif work_date.month == 8:
                writeCSV(8,row,dir_name)
                mouth_dirt['8月'] += 1
            elif work_date.month == 9:
                writeCSV(9,row,dir_name)
                mouth_dirt['9月'] += 1
            elif work_date.month == 10:
                writeCSV(10,row,dir_name)
                mouth_dirt['10月'] += 1
            elif work_date.month == 11:
                writeCSV(11,row,dir_name)
                mouth_dirt['11月'] += 1
            else:
                writeCSV(12,row,dir_name)
                mouth_dirt['12月'] += 1
    with open(os.path.join(dir_name + '/' + 'mouth' +'.txt'), 'w',encoding='gb18030', newline='') as write_dirt:
        write_dirt.write(str(mouth_dirt))


if __name__ == "__main__":
    #循环读取，循环结算
    # data_fram = pd.read_csv(input_file,encoding='gb18030',low_memory=False,chunksize=1000,header=0)
    # for aa in data_fram:
    #     print(aa['WORKDATE'].value_counts())
    time_start = time.time()
    executor = ThreadPoolExecutor(max_workers = 4)
    # all_task = [executor.submit(ByMonth,(file_list)) for file_list in test_path]
    # executor.map(ByMonth,test_path):
    for data in executor.map(ByMonth,in_path_file):
        time_end = time.time()
        print(time_end - time_start)
