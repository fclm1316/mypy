#!/usr/bin/python3
#coding:utf-8
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
hearlist = ['a0','a1','a2','a3','a4','a5','a6','a7','a8','a9',\
            'b0','b1','b2','b3','b4','b5','b6','b7','b8','b9',\
            'c0','c1','c2','c3','c4','c5','c6','c7','c8','c9',\
            'd0','d1','d2','d3','d4','d5','d6','d7','d8','d9',\
            'e0','e1','e2','e3','e4','e6','e7']
data_frame = pd.read_csv(input_file,header=None,names=hearlist,encoding='gb18030')
data_frame.to_csv(output_file,index=False,encoding='gb18030')
