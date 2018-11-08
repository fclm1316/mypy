#!/usr/bin/python3
#coding:utf-8
import requests
response = requests.get('http://www.bing.com')
print('================================')
print(type(response))
print('================================')
print(response.status_code)
print('================================')
print(type(response.text))
print('================================')
print(response.cookies)
print('++++++++++++++++++++++++++++++++')
print(requests.post('http://httpbin.org/post'))
print('++++++++++++++++++++++++++++++++')
print(requests.put('http://httpbin.org/put'))
print('++++++++++++++++++++++++++++++++')
print(requests.delete('http://httpbin.org/delete'))
print('++++++++++++++++++++++++++++++++')
print(requests.head('http://httpbin.org/get'))
print('++++++++++++++++++++++++++++++++')
print(requests.options('http://httpbin.org/get'))
print('--------------------------------')
response = requests.get('http://httpbin.org/get')
print(response.text)
print('--------------------------------')
#传入参数
response = requests.get('http://httpbin.org/get?name=Wayne&age=30')
print(response.text)
print('--------------------------------')
data = {
    'name':'Wayne',
    'age':'30'
}
response = requests.get("http://httpbin.org/get",params=data)
print(response.text)
print('--------------------------------')
response = requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.json())
print(type(response.json()))
#获取二进制文件
response = requests.get('http://github.com/favicon.ico')
print(type(response.text),type(response.content))
# with open('favicon.ico','wb') as w_f:
#     w_f.write(response.content)
#     w_f.close()

#添加请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/70.0.3538.77 Safari/537.36'}
response = requests.get('http://www.zhihu.com/explore',headers=headers)
print(response.text)

data = {
    'name':'Wayen',
    'age':'30'
}
url = 'http://httpbin.org/post'
response = requests.post(url,data=data,headers=headers)

url = 'http://www.jianshu.com'
response = requests.get(url)

