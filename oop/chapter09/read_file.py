#!/usr/bin/python3
#coding:utf-8
#500G,一行
def myreadlines(f,newline):
    buf = ""
    while True:
        #查找buf 中是否含有分割字符串
        while newline in buf:
            #查找出字符串在buf中的位置
            pos = buf.index(newline)
            print(pos)
            #切片，迭代返回 0到17位
            yield buf[:pos]
            #跳过字符串17 + 3 位,更新切片读取位置
            buf = buf[pos + len(newline):]
            print(buf)
        #先读取一次读入1024字节
        chunk = f.read(1024)

        if not chunk:
            #读到文件结尾
            yield buf
            break
        buf += chunk

with open('input.txt') as f:
    for line in myreadlines(f,"{|}"):
        print(line)
