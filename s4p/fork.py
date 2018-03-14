#!/usr/bin/python3
#coding:utf-8
import os
res = os.fork()
#print(res)
#print()
if res == 0:
    print(os.getpid(),os.getppid())
else:
    print(os.getpid())
