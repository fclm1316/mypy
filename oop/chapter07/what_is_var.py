#!/usr/bin/python3
#coding:utf-8
#python 变量实质是一个指针,便利贴
# a = 1
# a 贴在 1 上
# b = "abc"
#先生成对象，然后在贴便利贴

#便利贴，产生一个盒子
a = [1,2,3]
b = a
#操作b
b.append(4)
print(a)

print(id(a),id(b))
print(a is b)

c = [1,2,3,4]
d = [1,2,3,4]
print(c is d)

#小整数,字符串。
a = 1
b = 1
print(id(a),id(b))
print(a is b)



if __name__ == "__main__":
    pass