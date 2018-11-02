#!/usr/bin/python3
#coding:utf-8
import requests
import re
import json
from multiprocessing import Pool
from requests.exceptions import RequestException
#定义一个页面得请求
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/70.0.3538.77 Safari/537.36'}
def get_one_page(url):
    try :
        response = requests.get(url,headers=header)
        #判断页面状态 200 响应成功，301跳转 404 找不到页面 502服务器错误
        if response.status_code == 200:
            return response.text
        return response.status_code
    except RequestException:
        return None

def pares_one_page(html):
    #创建匹配内容,() 内需要得内容
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    #print(items)
    #创建生成器
    for items  in items:
        yield {
            'index':items[0],
            'image':items[1],
            'title':items[2],
            #内容切片
            'acctor':items[3].strip()[3:],
            'time':items[4].strip()[5:],
            'score':items[5]+items[6]
        }
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()

#设置offset 传入参数
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    #print(html)
    #打印生成器内容
    for item in pares_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    #1-9 的数 ，放大10倍 10，20，30 ..... 传入
    #for i in range(10):
    #   main(i*10)
    #创建进程池，池不满就创建，满了就等待
    pool =Pool()
    pool.map(main,[i*10 for i in range(10)])
