#!/usr/bin/python3
#coding:utf-8
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8000))
while True:
    re_data = input()
    if re_data == "exit":
        client.close()
        break
    else:
        client.send(re_data.encode("utf8"))
        data = client.recv(1024)
        print(data.decode("utf8"))

