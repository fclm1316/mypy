#!/usr/bin/python3
#coding:utf-8
class Company():
    #初始化
    def __init__(self,employee_list):
        self.employee = employee_list
    #魔法函数，加强类的类型,返回可迭代的
    def __getitem__(self,item):
        return self.employee[item]
    #为对象定义len长度，方便外部直接调用。它是class类，使用len()函数会报 TypeError
    #首先外部使用len()时查找自定义的__len__(self),如果没有，退一步__getitem__，序列化也可以获得长度，切片
    #如果都没有 TpyeError
    def __len__(self):
        return len(self.employee)

    #定义字符串
    def __str__(self):
        return ','.join(self.employee)
    #终端界面显示内容
    def __repr__(self):
        return ','.join(self.employee)


company = Company(['tom','bob','jane'])
# employee = company.employee
# for em in employee:
#     print(em)
for em in company:
    print(em)

#切片化获得长度
company1 = company[0:3]
print(len(company1))
#内置长度函数，获得长度
print(len(company))
print(company)
