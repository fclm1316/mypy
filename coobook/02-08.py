#!/usr/bin/python3
#coding:utf-8
#跨行匹配，跨越多行匹配
import re
test1 = '/* this is a comment */'
test2 = '''/* this is  a 
multiline comment */'''
comment = re.compile(r'/\*(.*?)\*/')
print(comment.findall(test1))
print(comment.findall(test2))
#comment2 = re.compile(r'/\*((?:.|\n))*?\*/')
#(?:.|\n) 指定一个非捕获组
# 使用 re.DOTALL 可以让(.) 匹配包括换行符在内的任意字符
comment3 = re.compile(r'/\*(.*?)\*/',re.DOTALL)
print(comment3.findall(test2))
