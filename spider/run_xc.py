#!/usr/bin/python3
#coding:utf-8
import re
from bs4 import BeautifulSoup
import requests
from requests import RequestException
from spider.xc_config import *

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/70.0.3538.77 Safari/537.36'}


new_url = xc_url + "/index.php"

def test_index_page(url):
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            response.encoding = 'GB18030'
            return response.text
        return None
    except RequestException:
        print('失败')
        return None

def pares_index_page(url):
    pattern = re.compile('<th><a href=.*? target=.*?<a href="(.*?)">(.*?)</a></h2>',re.S)
    part = re.findall(pattern,str(url))
    for url_junp,name in part:
        print(url_junp,name)

def item_20(num , page_no):
    in_page_20 = xc_url + '/'+ num + '&search=&page=' + page_no
    page_index_20 = test_index_page(in_page_20)
    print(page_index_20)

def main():
    html = test_index_page(new_url)
    soup = BeautifulSoup(html,'lxml')
    print(soup.title.get_text())
    # pares_index_page(html)
    item_20(num20,1)

if __name__ == '__main__':
    main()
