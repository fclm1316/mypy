#!/usr/bin/python3
#coding:utf-8
import pandas as pd
from pyecharts import Map

input_filename = 'D:/2000Wnew/sheng/tongji/heji.csv'
output_path ='D:/2000Wnew/sheng/tongji/'

data_frame = pd.read_csv(input_filename,encoding='gb18030',low_memory=False,names=['省','总计','男','女',
                                                                                   'S90','S80','S70','S60','S50',
                                                                                   'S40','S30','S20','Sxx'])
sheng = data_frame.省
sum_human = data_frame.总计
data_list_sheng = [i for i in sheng.values]
data_list_human = [i for i in sum_human.values]

map = Map('地图分布图',width=1200,height=600)
map.add('',
        data_list_sheng,
        data_list_human,
        maptype='china',
        is_visualmap=True,
        visual_text_color='#000',
        visual_range=[1,2500000],
        is_label_show=True)
map.render(''.join(output_path + 'map.html'))
