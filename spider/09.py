#!/usr/bin/python3
#coding:utf-8
import urllib3
import requests
from requests.exceptions import ReadTimeout ,ConnectTimeout
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
#print(response.json())
#print(type(response.json()))
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

#post请求
data = {
    'name':'Wayen',
    'age':'30'
}
url_bin = 'http://httpbin.org/post'
response = requests.post(url_bin,data=data,headers=headers)
print(response)
url = 'http://www.jianshu.com'
response = requests.get(url)
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.history),response.history)
print(type(response.url),response.url)
print('****************************')
#上传文件
# files = {'filename':open('favicon.ico','rb')}
# response = requests.post(url_bin,files=files)
# print(response.text)
#获取cookie
url_bin ='http://www.baidu.com'
response = requests.get(url_bin)
print(response.cookies)
for key,values in response.cookies.items():
    print(key + '=' + values)

#会话维持,模拟登陆
print('****************************')
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)

#证书验证
#忽略警告信息
urllib3.disable_warnings()
#设置证书关闭
response = requests.get('https://www.12306.cn',verify=False)
#response = requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key'))
print(response.status_code)

#设置代理
#pip install 'requests[socks]'
# proxies = {
#     'http':'http://127.0.0.1:8888',
#     'https':'https://127.0.0.1:8888',
#     'http':'http://user:password@127.0.0.1:8888',
#     'https':'socks5://127.0.0.1:8888'
# }
# response = requests.get('https://www.google.com',proxies=proxies)
# print(response.status_code)

#超时设置
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
try:
    response = requests.get('http://httpbin.org/get',timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print('ReadTimeout')
except ConnectTimeout:
    print('ConnectTimeout')

#认证设置
from requests.auth import HTTPBasicAuth
# r = requests.get('http://123.123.123.123:9001',auth=('user','123'))
# print(r.status_code)
