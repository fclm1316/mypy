#!/usr/bin/python3
#coding:utf-8
import requests
from bs4 import BeautifulSoup
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/70.0.3538.77 Safari/537.36'}
response = requests.get('https://www.toutiao.com/a6630723098503070215/',headers=header)
soup = BeautifulSoup(response.text,'lxml')
mysoup = soup.find_all('img',attrs={'src':'http://p9.pstatp.*?'})
print(mysoup)
print(soup)
