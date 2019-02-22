#!/usr/bin/python3
#coding:utf-8
from class_method import Date
class User:
   def __init__(self,birthday):
       # self.birthday = birthday
       #私有属性
       self.__birthday = birthday

   def get_age(self):
       #继承year mouth day 属性
       print(self.__birthday.year)
       print(self.__birthday.mouth)
       print(self.__birthday.day)
       return 2019  - self.__birthday.year

if __name__ == "__main__":
    user = User(Date.from_str('2000-12-13'))
    #获得属性。使用私有属性。
    #无法打印
    # print(user.birthday)
    print(user.get_age())
    #使用其他方法打印私有属性
    print(user._User__birthday)