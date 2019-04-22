#!/usr/bin/python3
#coding:utf-8

from collections import Counter
import os
import json
from pyecharts import Bar


file_path ='d:/data/'
out_path = 'd:/data/big_dict.xtx'

big_dict = {}
for root,dir,files in os.walk(file_path):
    for file in files:
        file_name = os.path.join(root,file)
        files = os.path.basename(file_name).split('.')
        if files[1] == 'txt' and files[0] != 'mouth':
            # print(file_name)
            with open(file_name,'r') as file:
                # print(file_name)
                json_data = json.loads(file.read())
                # json_dumps = json.dumps(eval(file.read()))
                # json_loads = json.loads(json_dumps)
                # print(json_loads)
                big_dict = Counter(big_dict) + Counter(json_data)
top_10 = sorted(big_dict.items(),key= lambda x:x[1] ,reverse=True)
print(type(big_dict))
with open(out_path,'w') as file_write:
    file_write.write(str(dict(top_10)))
i = 0
list_x = []
list_y = []
for key,values in top_10:
    if i < 10 :
        print(key,values)
        list_x.append(key[0:6])
        list_y.append(values)
        i += 1
    else:
        break


bar = Bar('统计','数量 TOP10')
bar.add('数量',list_x,list_y,xaxis_name='各行',
            is_label_show=True)
bar.render(''.join(file_path +'各行' +'.html'))




# if __name__ == "__main__":
#     pass