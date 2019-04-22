#!/usr/bin/python3
#coding:utf-8
class Date:
    #构造函数
    def __init__(self,year,mouth,day):
        self.year = year
        self.mouth = mouth
        self.day = day

#实例方法
    def tomorrow(self):
        self.day += 1

#使用静态方法格式化时间
    #装饰器
    @staticmethod
    def parse_from_str(date_str):
        year,mouth,day = tuple(date_str.split('-'))
        #静态方法不需要使用self，调用时必须Date()
        #缺点：更换类名称时，必须更换硬编码名称
        return  Date(int(year),int(mouth),int(day))
#使用类方法
    #装饰器
    @classmethod
    def from_str(cls,date_str):
        year,mouth,day = tuple(date_str.split('-'))
        #类方法传递进来的是类
        return  cls(int(year),int(mouth),int(day))

    def __str__(self):
        return "{year}/{mouth}/{day}".format(year=self.year,mouth=self.mouth,day=self.day)

if __name__ == "__main__":
    new_day = Date(2019,2,21)
    new_day.tomorrow() # tomorrow(new_day)
    print(new_day)
#当日期为字符串时，分割字符串，传入Date中
    date_str = '2019-02-21'
    year,mouth,day = tuple(date_str.split('-'))
    new_day = Date(int(year),int(mouth),int(day))
    print(new_day)

    #用staticmethod完成初始化
    print(Date.parse_from_str(date_str))
    #用classmethod完成初始化
    print(Date.from_str(date_str))
