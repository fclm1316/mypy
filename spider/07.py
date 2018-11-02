#!/usr/bin/python3
#coding:utf-8
import requests
#请求头.chrome 检查 network headers 获得
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                       'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                       'Chrome/70.0.3538.77 Safari/537.36"}
#响应体
respones = requests.get('http://www.baidu.com',headers=headers)
#获得响应体
print(respones.text)
#获得响应头
print('==================')
print(respones.headers)
print('==================')
print(respones.status_code)
