#!/usr/bin/python3
#coding:utf-8
import time
import pandas as pd
import csv
# t0 = time.perf_counter()
import os
import glob

in_path = 'D:/2000W'
in_path_file = glob.glob(os.path.join(in_path,'*.csv'))
out_path = 'D:/2000Wnew'


def pick_data(input_filename,output_filename):
    #pd.read_csv 打开文件，chunksize 分块读取（一千条？），返回的是一个可迭代的对象TextFileReader
    #巨大文件,C error: out of memory
    data_frame = pd.read_csv(input_filename,encoding='UTF-8',low_memory=False,chunksize=1000)
    with open(output_filename,'w',encoding='gb18030',newline='') as csv_write_file:
        filewrite = csv.writer(csv_write_file)
        #通过循环读取数据
        for  aa in  data_frame:
        #摘取名字和ID
            ID_name_ID = aa[['Name','CtfId']]
        # print(ID_name_ID)
        #写入csv文件，去掉index
    # ID_name_ID.to_csv(output_filename,encoding='utf_8_sig',index=False)
        #通过itertuples方法获得元组,命名为pandas。获得每列内容，循环内容
    # for row in ID_name_ID.itertuples(index=True,name='Pandas'):
            for row in ID_name_ID.itertuples(index=False,name='New_ID_NAME'):
                Name = getattr(row,'Name')
            #通过getattr()在列中获得CtfID
                CtfId = getattr(row,'CtfId')
                if len(str(CtfId)) == 18:
                    # filewrite.writerow(row)
                    birth_area = CtfId[0:2]
                    birth_year = CtfId[6:10]
                    birth_moon= CtfId[10:12]
                    birth_day = CtfId[12:14]
                    sex = CtfId[14:17]
                    if int(sex) % 2 == 0:
                        F_M = '女'
                    else:
                        F_M = '男'
                    bb = (Name,CtfId,str(birth_area),str(birth_year),str(birth_moon),str(birth_day),F_M)
                    # print(bb)
                    filewrite.writerow(bb)

def main():
    for in_file in in_path_file:
    #定义程序开始时间
        t_start = time.process_time()
        filename = os.path.basename(in_file)
        out_path_file = ''.join(out_path + '/'+ filename)
        pick_data(in_file,out_path_file)
        # print(in_file,out_path_file)
        t_end = time.process_time()
        t1 = t_end - t_start
        print('{0:s}  耗时: {1:.2f} s'.format(out_path_file,t1))



if __name__ == '__main__':
#定义程序开始时间
    main()
