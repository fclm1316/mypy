#!/usr/bin/python3
#coding:utf-8
import time
import pandas as pd
import linecache
import csv
from multiprocessing import Pool
# t0 = time.perf_counter()

t_start = time.process_time()
input_file = 'D:/2000W/last5000.csv'
output_file = 'D:/2000W/new5000.csv'


def pick_data(input_filename,output_filename):
    data_frame = pd.read_csv(input_filename,encoding='UTF-8',low_memory=False)
    ID_name_ID = data_frame[['Name','CtfId']]
    ID_name_ID.to_csv(output_filename,encoding='utf_8_sig',index=False)


def check_data(filename):
    data_frame = pd.read_csv(filename,encoding='UTF-8',low_memory=False)
    bb = data_frame.loc[[2]]


if __name__ == '__main__':
    # pick_data(input_file,output_file)
    check_data(output_file)
    t_end = time.process_time()
    t1 = t_end - t_start
    print('耗时: {0:.2f} s'.format(t1))
