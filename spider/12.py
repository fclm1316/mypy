#!/usr/bin/python3
#coding:utf-8
from pyquery import PyQuery as pq
html_doc = """
<html><head>
<title>The Dormouse's story</title>
</head>
<body>
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html"> second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
<c class="title" name='dromouse'><b>The Dormouse's story</b></c>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><span>Lacie</span></a> and
<a href="http://example.com/tillie" class="sister" id="link3"><span>Tillie</span></a>
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#初始化方式1
doc = pq(html_doc)
print(doc('head'))
print('=======================================')
#初始化方式1
doc = pq(filename='demo.html')
print(doc('a'))
print('=======================================')
doc = pq(url='http://www.bing.com')
print(doc('title'))
print('=======================================')
#css选择器
doc = pq(html_doc)
#没有严格的子集关系，层级关系即可
#id  class  li
#查找子元素
print(doc('#container .list li'))
print('=======================================')
items = doc('.list')
print(items)
print('---------------------------------------')
lls = items.find('li')
print(lls)
print('---------------------------------------')
lls = items.children()
print(lls)
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
lls = items.children('.active')
print(lls)
