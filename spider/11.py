#!/usr/bin/python3
#coding:utf-8
#14-02.py
#解析器
# BeautifulSoup(markup,'html.parser')标准解析器
# BeautifulSoup(markup,'lxml')html解析器
# BeautifulSoup(markup,'xml')xml解析器
# BeautifulSoup(markup,'html5lib')解析器
from bs4 import BeautifulSoup
html_doc = """
<html><head>
<title>The Dormouse's story</title>
</head>
<body>
<c class="title" name='dromouse'><b>The Dormouse's story</b></c>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><span>Lacie</span></a> and
<a href="http://example.com/tillie" class="sister" id="link3"><span>Tillie</span></a>
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'lxml')
#修复html,格式化
print(soup.prettify())
#打印title标签的内容
print(soup.title.string)
print(soup.title.text)
print('===================')
#打印所有title
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.c)
print('===================')
#获取名称
print(soup.title.name)
#获取属性
print('===================')
print(soup.c.attrs['name'])
print(soup.c['name'])
#嵌套选择
print('===================')
print(soup.head.title.string)
print(soup.body.p.text)
#text 获取到，而string无法获取到
print(soup.body.p.string)
#获取子节点和孙子节点
print('-------------------')
print(soup.p.contents)
print('-------------------')
#迭代器方式返回
print(soup.p.children)
for i,child in enumerate(soup.p.children):
    print(i,child)
print('+++++++++++++++++++')
#返回子,孙节点
print(soup.p.descendants)
for i,child in enumerate(soup.p.descendants):
    print(i,child)
print('*******************')
#获取父节点
print(soup.a.parent)
print(list(enumerate(soup.a.parent)))
print('*******************')
print(soup.a.parents)
print(list(enumerate(soup.a.parents)))
#获取兄弟节点
print('############################')
print(list(enumerate(soup.a.next_siblings)))
print(list(enumerate(soup.a.previous_siblings)))

#查找所有
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print(soup.find_all('a'))
#循环打出span ,根据标签
for span in soup.find_all('a'):
    print(span.find_all('span'))
#attrs 查找.字典形式
print(soup.find_all(attrs={'class':'story'}))
print('@@@@@@@@@@@@@@@@@@@')
#class内置关键字，加下划线
print(soup.find_all(class_='story'))
print(soup.find_all(id='link1'))
