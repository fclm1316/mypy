#!/usr/bin/python3
#coding:utf-8
#shell 通配符匹配字符串
#glob
from fnmatch import fnmatch,fnmatchcase
#不区分大小写
fnmatch('foo.txt','*.txt')
fnmatch('foo.txt','?oo.txt')
fnmatch('Dat45.csv','Dat[0-9]*')
names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
Name = [name for name in names if fnmatch(name,'Dat*.csv')]
print(Name)
#区分大小写
fnmatchcase('foo.txt','*.TXT')