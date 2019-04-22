#!/usr/bin/python3
#coding:utf-8
#requests -> urllib -> socket
import socket
from urllib.parse import urlparse

def get_url(url):
    # 通过socket请求html
    # 通过urlparse 解析域名，子路径
    url = urlparse(url)
    # 域名 host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,8000))

    client.send("GET {}HTTP/1.1\r\nHost:{}\r\nConnection:close".format(path,host).encode("utf8"))
    #指定类型
    data = b""
    #循环获取数据
    while True:
        d = client.recv()
        #如果获取完了
        if d :
            data += d
        else:
            break
        data = data.decode("utf8")
        data_html = data.split("\r\n\r\n")[0]
    print(data_html)
    client.close()




if __name__ == "__main__":
    get_url("http://www.bing.com")
