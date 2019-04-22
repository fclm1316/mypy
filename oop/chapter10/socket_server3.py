#!/usr/bin/python3
#coding:utf-8
import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8000))
server.listen()

def handle_sock(sock,addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        re_data = input()
        sock.send(re_data.encode("utf8"))

while True:
    sock , addr = server.accept()
    #放入线程中
    clent_thread = threading.Thread(target=handle_sock,args=(sock,addr))
    clent_thread.start()

