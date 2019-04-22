#!/usr/bin/python3
#coding:utf-8
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8000))
server.listen()
sock , addr = server.accept()
while True:
    data = sock.recv(1024)
    print(data.decode("utf8"))
    re_data = input()
    sock.send(re_data.encode("utf8"))


