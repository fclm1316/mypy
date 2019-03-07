#!/usr/bin/python3
#coding:utf-8

def add(a,b):
    #就地修改a[list]
    a += b
    return a

class Company:
    def __init__(self,name,staffs=[]):
        self.name = name
        self.staffs = staffs
    def add(self,staffs_name):
        self.staffs.append(staffs_name)
    def remove(self,staffs_name):
        self.staffs.remove(staffs_name)



if __name__ == "__main__":
    print("----------------------------")
    com1 = Company("com1",["aa1","aa2"])
    com1.add("aa3")
    com1.remove("aa1")
    print(com1.staffs)

    com2 = Company("com2")
    com2.add("bb1")
    print(com2.staffs)

    com3 = Company("com3")
    com3.add("bb2")
    print(com2.staffs)
    print(com3.staffs)
    print("----------------------------")

    a = 1
    b = 2
    c = add(a,b)
    print(c)
    print(a,b)

    print("----------------------------")
    a = [1,2]
    b = [3,4]
    c = add(a,b)
    print(c)
    print(a,b)
    print("----------------------------")
    a = (1,2)
    b = (3,4)
    c = add(a,b)
    print(c)
    print(a,b)
