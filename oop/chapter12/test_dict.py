#!/usr/bin/python3
#coding:utf-8

b_t = {
    'a':[200,231,123,200],
    'b':{200,333,333,222}
     }

b_t2 = [1,2,3,'g',9]


for value in b_t.values():
    print(value)
    print(type(value))

#列转字典
#枚举
for key,value in enumerate(b_t2,start=1):
    print(key,value)

if __name__ == "__main__":
    pass