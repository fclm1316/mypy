#!/usr/bin/python3
#coding:utf-8
#类的序列化
import json
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score



#转换函数

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

s = Student('Bob',23,32)

print(json.dumps(s,default=student2dict))

if __name__ == "__main__":
    pass