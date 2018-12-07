#!/usr/bin/python3
#coding:utf-8
#主要处理json数据，offset 设置开关
import json
import re
import os
from _md5 import md5
from json.decoder import JSONDecodeError
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
# 定义首页，参数化offset 页数，keyword 关键字
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/70.0.3538.77 Safari/537.36'}
def get_page_index(offset,keyword):
    #Query String Parameters
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3,
        'from': 'gallery',
        'pd': ''
    }
    #urlencode 把字典转化成url请求参数
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('失败')
        return None

#解析josn
def parse_page_index(html):
    try:
        #将json格式转换成字典
        data_big = json.loads(html)
        #打印key值
        # for key in data.keys():
        #     print(key)
        #判断大字典中是否包含data 键 ,还有万一josn.loads后是个空
        if  data_big and 'data' in data_big.keys():
            #获得data_big中'data'的字典
            for item in data_big.get('data'):
               #item字典
               # print(item)
               #get()方法，从字典中获得值
               if item.get('article_url') != None:
                  # print(item.get('article_url'))
                  #生成器 整合 循环返回的值
                   yield item.get('article_url')
    except JSONDecodeError:
        pass

def get_para_detail(url):
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('失败')
        return None
#反爬虫。。。。。无法获取。。。。。。
def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    #soup 的 select 选择器
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('var gallery = (.*?);',re.S)
    result = re.search(images_pattern,html)
    if result:
        data = json.load(result.group(1))
        if data and 'sub_images' in data.key():
            sub_images = data.get('sub_imges')
            images = [item.get('url') for item in sub_images]
            for image in images:download_image(image)
            return {
                'title':title,
                'url':url,
                'images':images
            }

def download_image(url):
    print('正在下载',url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # return response.text
            save_image(response.content)
        return None
    except RequestException:
        print('请求图片出错',url)
        return None

def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()



def main():
    html = get_page_index(0,'街拍 美女')
    for url in parse_page_index(html):
        # print(url)
        html = get_para_detail(url)
        if html:
            result = parse_page_detail(html,url)
            print(result)

if __name__ == '__main__':
    main()