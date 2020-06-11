#!/usr/bin/python3
# coding:utf-8
import pandas as pd
from pyecharts import Bar

input_filename = 'D:/2000Wnew/sheng/tongji/heji.csv'
output_path = 'D:/2000Wnew/sheng/tongji/'

data_frame = pd.read_csv(input_filename, encoding='gb18030', low_memory=False, names=['省', '总计', '男', '女',
                                                                                      'S90', 'S80', 'S70', 'S60', 'S50',
                                                                                      'S40', 'S30', 'S20', 'Sxx'])
sheng = data_frame.省
sum_human = data_frame.总计
sum_man = data_frame.男
sun_woman = data_frame.女

data_list_sheng = [i for i in sheng.values]
data_list_human = [i for i in sum_human.values]
data_list_man = [i for i in data_frame.男.values]
data_list_woman = [i for i in data_frame.女.values]

bar1 = Bar('各省人数', '分布', width=2000, height=800)
bar1.add('人数', data_list_sheng, data_list_human, xaxis_name='省份', is_label_show=True, xaxis_name_gap=30,
         xaxis_name_size=30
         )
bar1.render(''.join(output_path + 'bar1.html'))
bar2 = Bar('各省人数', '分布', width=2000, height=800)
bar2.add('男', data_list_sheng, data_list_man, is_label_show=True, label_color=['#ff0000'])
bar2.add('女', data_list_sheng, data_list_woman, is_label_show=True, label_color=['#0000ff'], xaxis_name='男女比例',
         xaxis_name_size=30, xaxis_name_gap=30)
bar2.render(''.join(output_path + 'bar2.html'))
