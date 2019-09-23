#!/usr/bin/python3
#coding:utf-8
#保留最后N个元素
#保留最后有限的历史记录
from collections import deque
#list 线性储存，deque高效插入删除，双向列表，适用于队列栈
#定义函数，定义默认值5
def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    with open(r'01-03.txt') as f:
        for line,prevlines in search(f,'python',10):
            for pline in prevlines:
                print(pline,end='')
                print(line,end='')
                print('-' * 20)


#定义队列长度
    q = deque(maxlen=5)
    #结尾加
    q.append(1)
    print(q)
    q.append(2)
    print(q)
    q.append(3)
    print(q)
    q.append(4)
    print(q)
    q.append(5)
    print(q)
    q.append(6)
    print(q)
    q.append(7)
    print(q)
    #左侧加入
    q.appendleft(8)
    print(q)
    #右侧弹出
    print("---------")
    q.pop()
    print(q)
    #左侧弹出
    q.popleft()
    print(q)
