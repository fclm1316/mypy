#!/usr/bin/python3
#coding:utf-8
from bs4 import BeautifulSoup
# with open('FH0001.xml',encoding='gb18030') as xml_file:
#     soup = BeautifulSoup(xml_file,'xml')
#     print(soup)
soup = BeautifulSoup(open('FH0001.xml'),'xml')
print(len(soup.nbrcs))
