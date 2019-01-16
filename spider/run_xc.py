#!/usr/bin/python3
#coding:utf-8
import re
from bs4 import BeautifulSoup
import requests
from requests import RequestException
from spider.config import *

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

def prase_page(num , page_no):
    in_page = xc_url + '/'+ thread + str(num)+ '&search=&page=' + str(page_no)
    # print(in_page_20)
    item_page = test_index_page(in_page)
    if item_page:
        soup = BeautifulSoup(item_page,'lxml')
        # print(item_page)
        for url_name in soup.select("div  table  tbody  tr  td  h3  a"):
            url = url_name.get("href")
            name = url_name.get_text()
            pattern1 = re.compile('htm_data.*?',re.I)
            if  re.search(pattern1,url) and not re.search(pattern_not,url):
                print(url,name)





def main():
    # html = test_index_page(new_url)
    # soup = BeautifulSoup(html,'lxml')
    # print(soup.title.get_text())
    # pares_index_page(html)
    prase_page(22,1)

if __name__ == '__main__':
    main()
