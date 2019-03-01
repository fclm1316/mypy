#!/usr/bin/python3
#coding:utf-8
import socket

# 1 指明协议
#AF_INET->ipv4  ;AF_INET6->ipv6  AF_IPX-> linux 进程间通讯
#socket.SOCK_STREAM 指明TCP协议   ；socket.SOCK_DGRAM UDP
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2 绑定地址端口
server.bind(('0.0.0.0',8000))
# 3 监听端口
server.listen()
# 4 接受讯息,阻塞式
sock , addr = server.accept()
# 5 从客户端获取数据,数据:1kb
data = sock.recv(1024)
print(data.decode("utf8"))
sock.send("haha {}".format(data.decode("utf8")).encode("utf8"))
# 关闭服务端
server.close()
# 关闭sock连接,只要不主动关闭一直连接
sock.close()


