#!/usr/bin/python3
#coding:utf-8
from itertools import chain
my_list = [1,2,3]
my_dict = {
    "aaa" : "AAA",
    "bbb" : "BBB"
}


for value in chain(my_list,my_dict,range(5,10)):
    print(value)




if __name__ == "__main__":
    pass