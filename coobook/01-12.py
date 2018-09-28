#!/usr/bin/python3
#coding:utf-8
words = [
    'look','into','my','eyes','look','into','my','eyes','the','eyes',
    'the','eyes','the','not','around','the','eyes',"don't",'look','around',
    'the','eyes','look','into','my','eyes',"your're",'under'
]

from collections import Counter
#
word_counts = Counter(words)
#出现最频繁的 3 个单词
top_three = word_counts.most_common(3)
print(top_three)
print(word_counts['not'])
print(word_counts['eyes'])
#增加计数，可以简单的用加法
#订一个列
morewords = ['why','are','you','not','looking','in','my','eyes']
#根据列中的内容，增加一个单词
for word in morewords:
    word_counts[word] += 1
print(word_counts['eyes'])

#或者使用update()
word_counts.update(morewords)
print(word_counts)
#使用加减对字典操作
a = Counter(words)
b = Counter(morewords)
c = a+b
print(c)
d =a - b
print(d)