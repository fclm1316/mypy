#!/usr/bin/python3
#coding:utf-8
import json
from collections import Counter

dict_1 = "d:/data/2011/mouth.txt"
dict_2 = "d:/data/2010/mouth.txt"

with open(dict_1,'r') as f1:
    f1_dict = f1.read()
    with open(dict_2,'r') as f2:
        f2_dict  = f2.read()
        #字典的合并0
        # d = {**d1,**d2}
        dict_3 = {**json.loads(f1_dict),**json.loads(f2_dict)}
        #字典的合并1
        # d = dict(d1,**d2)
        dict_4 = dict(json.loads(f1_dict),**json.loads(f2_dict))
        #字典的合并2
        # d3.update(d1)
        # d3.update(d2)
        dict_5 = {}
        dict_5.update(json.loads(f1_dict))
        dict_5.update(json.loads(f2_dict))
        #字典的合并3
        #d3 = dict(d1.items() + d2.items())
        print(dict_3)
        print(dict_4)
        print(dict_5)
#以上value key 不加，纯粹是合计
        dict_9 = dict(Counter(json.loads(f1_dict)) + Counter(json.loads(f2_dict)))
        print(dict_9)






# if __name__ == "__main__":
#     pass