#!/usr/bin/python3
#coding:utf-8

#单引号加载 json
import json
aa = 'd:/data/test/ttt0.txt'
with open(aa,'r') as f:
    aa = f.read()
    data = json.dumps(eval(aa))
    # print(data)
    bb = json.loads(data)
    print(bb)


# if __name__ == "__main__":
#     pass