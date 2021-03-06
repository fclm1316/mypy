#!/usr/bin/python3
#coding:UTF-8
import requests
import re
from bs4 import BeautifulSoup
import sys
import urllib.request
from multiprocessing import Pool
import os
from requests.exceptions import RequestException
from url_3dm import *

#分割地址去掉后缀
input_url = os.path.splitext(input_url_all)[0]
# print(input_url)
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/70.0.3538.77 Safari/537.36'}
def get_page(url):
    try:
        #发送请求
        response = requests.get(url,headers=header)
        #状态码
        if response.status_code == 200:
            #return response.text
            #print(response.encoding)
            #指定编码
            response.encoding = 'UTF-8'
            #返回html
            return response.text
        return response.status_code
    except RequestException:
        return None
#
def pares_page(html_pattern):
    #html 中符合内容的正则表达式
    pattern = re.compile('<p align="center".*?img src="(htt.*?)" .*?alt=.*?<span>(.*?)</span>',re.S)
    items = re.findall(pattern,str(html_pattern))
    return items

def writ_to_file(save_path,name,type,files):
    #粘合名称.类型
    file_name = ''.join(save_path+name+type)
    print(file_name)
    #文件的地址
    file_content = requests.get(files)
    with open(file_name,'wb') as f:
        #写入二进制流
        f.write(file_content.content)
        f.close()

# def page48(html_pattern):
#     pattern = re.compile('<p align="center">.*?img src="(.*?)" alt=.*?</p>',re.S)
#     items = re.findall(pattern,str(html_pattern))
#     return items
def page48(html_pattern):
    #使用soup
    soup = BeautifulSoup(html_pattern,'lxml')
    pattern = re.compile('http.*?')
    #select 选择器
    for file_path in  soup.select("body div div div p img"):
        #获得src属性
        path = file_path.get('src')
        #剔除
        if re.search(pattern,path):
            yield path


def main48(page):
    url = input_url + '_' + '48' + '.html'
    html = get_page(url)
    print(page)
    for item in page48(html):
        name = os.path.splitext(item)[0].split('_')[1]
        type = os.path.splitext(item)[1]
        # print(name)
        writ_to_file(save_path,name,type,item)

def main(pageno):
    #翻页地址
    url = input_url + '_' + str(pageno) + '.html'
    # print(url)
    html = get_page(url)
#    print(html)
    print(pageno)
    for item in pares_page(html):
        # print(item)
        #分割
        type = os.path.splitext(item[0])[1]
        name = str(item[1]).replace('?','')
        # print(name)
        # print(name.strip(),type,item[0])
        writ_to_file(save_path,name,type,item[0])
        #for key,values in item:
        #   print(values)
def main1(pageno):
    #翻页地址
    url = input_url +  '.html'
    # print(url)
    html = get_page(url)
    #    print(html)
    print(pageno)
    for item in pares_page(html):
        print(item)
        #分割
        # type = os.path.splitext(item[0])[1]
        # name = str(item[1]).replace('?','')
        # print(name)
        # print(name.strip(),type,item[0])
        # writ_to_file(save_path,name,type,item[0])


if __name__ == '__main__' :
#     #指定进程数量 Pool(processes=5)
    #pool = Pool()
    #pool.map(main,[i for i in range(2,48)])
    main1(1)
    for i in range(2,48):
       main(i)
    main48(48)
