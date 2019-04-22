#!/usr/bin/python3
#coding:utf-8
import csv
import os
from datetime import datetime
import time
# 思路: 打开文件  逐行读取  判断分类 存入列表 满20000写文件
file_path = 'd:/data/ttt'
out_path ='d:/data/'
#定义字典，判断累加
year_dict ={'2009':0,'2010':0,'2011':0,'2012':0,'2013':0,'2014':0,'2015':0,'2016':0,'2017':0,'2018':0,'2019':0}
year_list =['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
header_list =['WORKDATE','REFID','SEQNO','TRNCODE','CLASSID','PRESDATE','PRESTIME','ORIGINATOR', \
              'ACCEPTOR','DCFLAG','NOTETYPE','NOTENO','CURCODE','CURTYPE','ISSUEDATE', \
              'SETTLAMT','ISSUEAMT','REMNAMT','PAYINGACCT','PAYER','PAYINGBANK','PCBANK', \
              'BENEACCT','BENENAME','BENEBANK','BCBANK','AGREEMENT','PURPOSE','MEMO','TERMTYPE', \
              'TERMID','ACCTOPER','AUDITOR','AUTHDEVID','PAYKEY','TESTKEY','WORKROUND','CLEARDATE', \
              'CLEARROUND','EXCHGDATE','EXCHGROUND','CLEARTIME','CLEARSTATE','ERRCODE','FEEPAYER', \
              'FEECODE','FEE','TRUNCFLAG','CLEARAREA','EXCHAREA','ROUTEID','PRESAREA','ACPTAREA', \
              'EXTRADATAFLAG','ATTACHFILE','RESERVED']

def writeCSV1(year,row):
    with open(os.path.join(out_path +  str(year) +'.csv'), 'a+',encoding='gb18030', newline='') as csv_write:
        firewrite = csv.writer(csv_write)
        firewrite.writerow(row)

def writeCSV(year,row):
    #定义列大小
    list_size =[]
    list_size.append(row)
    #等于20000条时写文件
    if len(list_size) == 20000:
        with open(os.path.join(out_path + str(year) +'.csv'), 'a+',encoding='gb18030', newline='') as csv_write:
            for rows in list_size:
                firewrite = csv.writer(csv_write)
                firewrite.writerow(rows)
        #写完后清空列表
        list_size = []
    else:
        #最后不足20000的写入
        with open(os.path.join(out_path + str(year) +'.csv'), 'a+',encoding='gb18030', newline='') as csv_write:
            for rows in list_size:
                firewrite = csv.writer(csv_write)
                firewrite.writerow(rows)
        list_size = []


if __name__ == '__main__':
    time_start = time.time()

    with open(file_path,'r',encoding='gb18030',newline='') as csv_file:
        #获得列表名
        for years in year_list:
            #定义文件名
            output_by_year = os.path.join(out_path + years + '.csv')
            with open(output_by_year,'w',encoding='gb18030',newline='') as csv_write:
                firereader = csv.reader(csv_file)
                firewrite = csv.writer(csv_write)
                firewrite.writerow(header_list)

        for row in firereader:
            #格式化时间
            work_date = datetime.strptime(row[0],'%Y%m%d')
            # print(work_date.year,work_date.month,work_date.day)
            #判断 分类
            if work_date.year == 2009:
                writeCSV(2009,row)
                year_dict['2009'] +=1

            elif work_date.year == 2010:
                writeCSV(2010,row)
                year_dict['2010'] +=1

            elif work_date.year == 2011:
                writeCSV(2011,row)
                year_dict['2011'] +=1

            elif work_date.year == 2012:
                writeCSV(2012,row)
                year_dict['2012'] +=1

            elif work_date.year == 2013:
                writeCSV(2013,row)
                year_dict['2013'] +=1

            elif work_date.year == 2014:
                writeCSV(2014,row)
                year_dict['2014'] +=1

            elif work_date.year == 2015:
                writeCSV(2015,row)
                year_dict['2015'] +=1

            elif work_date.year == 2016:
                writeCSV(2016,row)
                year_dict['2016'] +=1

            elif work_date.year == 2017:
                writeCSV(2017,row)
                year_dict['2017'] +=1

            elif work_date.year == 2018:
                writeCSV(2018,row)
                year_dict['2018'] +=1

            else:
                writeCSV(2019,row)
                year_dict['2019'] +=1

    with open(os.path.join(out_path + 'year_dict' +'.txt'), 'a+',encoding='gb18030', newline='') as write_file:
        write_file.write(str(year_dict))
        # {'2009': 17199, '2010': 473669, '2011': 602910, '2012': 569211, '2013': 527294,
        # '2014': 462602, '2015': 423780, '2016': 400474, '2017': 371426, '2018': 373545, '2019': 68952}
    time_end = time.time()
    print(time_end - time_start)
