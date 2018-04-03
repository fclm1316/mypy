#!/usr/bin/python3
#coding:utf-8
import sys
import pandas as pd
input_file = sys.argv[1]
data_frame = pd.read_csv(input_file,encoding='gb18030')
print(data_frame)