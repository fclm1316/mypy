#!/usr/bin/python3
#coding:utf-8
import re
#re 模块,正则表达式
# \w 匹配字母数字及下划线
# \W 匹配非字母数字及下划线
# \s 匹配任意空白字符，等价于[\t\n\r\f]
# \S 匹配任意非空字符
# \d 匹配任意数字，等价于[0-9]
# \D 匹配任意非数字
# \A 匹配字符串开始
# \Z 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串
# \z 匹配字符串结束
# \G 匹配最后匹配完成的位置
# \n 匹配一个换行符
# \t 匹配一个制表符
# ^ 匹配字符串的开头
# $ 匹配字符串的末尾
# . 匹配任意字符，除了换行符，当 re.DOTALL 标记被指定时，则可以匹配包括换行符的任意字符
# [...] 用来表示一组字符，单独列出；[amk]匹配 'a','m'或'k'
# [^...] 不在[]中的字符；[^abc] 匹配除了a,b,c之外的字符
# * 匹配0个或者多个的表达式
# + 匹配1个或者多个的表达式
# ? 匹配0个或者1个由前面的正则表达式定义的片段，非贪婪方式
# {n} 精确匹配N个前面表达式
# {n,m} 匹配n到m次由前面的正则表达式定义的片段，贪婪方式
# a|b 匹配a或者b
# () 匹配括号内的表达式
content = 'Hello 1234567 World_This is a Bruce Wayne'
#长度
print(len(content))
#Hello 开头 空格 数字+++ 空格 数字{有4个} \w字母下划线 {有10个} 任意匹配 Wayen结尾
result = re.match('^Hello\s\d\d\d\d{4}\s\w{10}.*Wayne$',content)
print(result)
#属组
print(result.group())
#span匹配位置
print(result.span())
print('============================')
#分组属性.括号匹配内容
result = re.match('^Hello\s(\d+)\d{4}\s\w{10}.*Wayne$',content)
print(result.group(1))
#贪婪匹配,只有7  .*尽可能多匹配直到()
print('============================')
result = re.match('^Hel.*(\d+).*Wayne$',content)
print(result.group(1))
#非贪婪匹配,1234567
print('============================')
result = re.match('^Hel.*?(\d+).*Wayne$',content)
print(result.group(1))

content = '''Hello 1234567 World_This is  
Bruce Wayne
'''
#匹配换行符
print('============================')
result = re.match('^Hel.*?(\d+).*Wayne$',content,re.S)
print(result.group(1))

#match从头匹配 search任意匹配查询一个  findall查询所有匹配结果
#re.sub 替换字符串中的每一个字串返回替换或的字符串
content = 'Hello 1234567 World_This is Bruce Wayne Dick Grayson Jason Todd Damian Wayne'
content = re.sub('\d+','',content)
print(content)
print('----------------------------')
#group 1 中 \1
content = 'Hello 1234567 World_This is Bruce Wayne Dick Grayson Jason Todd Damian Wayne'
content = re.sub('(\d+)',r'\1 8910',content)
print(content)
print('----------------------------')
pattern = re.compile('.*?wayne.*',re.I)
result = re.match(pattern,content)
print(result)
print('============================')

