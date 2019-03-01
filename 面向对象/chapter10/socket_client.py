#!/usr/bin/python3
#coding:utf-8
import socket
#定义协议
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接服务
client.connect(('127.0.0.1',8000))
#发送信息
client.send("aaa".encode("utf8"))
#接受信息
data = client.recv(1024)
print(data.decode("utf8"))
client.close()


