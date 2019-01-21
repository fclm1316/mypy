#!/usr/bin/python3
#coding:utf-8
import pandas as pd
from pyecharts import Pie

input_filename = 'D:/2000Wnew/sheng/tongji/heji.csv'
output_path ='D:/2000Wnew/sheng/tongji/'

data_frame = pd.read_csv(input_filename,encoding='gb18030',low_memory=False,names=['省','总计','男','女',
                                                                                   'S90','S80','S70','S60','S50',
                                                                                   'S40','S30','S20','Sxx'])
S90 = sum(data_frame.S90)
S80 = sum(data_frame.S80)
S70 = sum(data_frame.S70)
S60 = sum(data_frame.S60)
S50 = sum(data_frame.S50)
S40 = sum(data_frame.S40)
Sxx = sum(data_frame.Sxx)
S50_S40 = S50+S40

list_human = [S90,S80,S70,S60,S50_S40,Sxx]
attr = ['90后','80后','70后','60后','50后','未知']

pie = Pie('各年龄段对比',width=700,height=700)
pie.add('',attr,
        list_human,
        center=[50,55],
        is_label_show=True)
pie.render(''.join(output_path + 'pie.html'))
