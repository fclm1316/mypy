#!/usr/bin/python3
#coding:utf-8
import base64
str0 = '123456'
str1 = '7nUXB6OM4mI='
# str2 = base64.b64decode(str)
str3 = base64.b64encode(str0.encode('utf-8'))
str4 = base64.b64decode('MTIzNDU2').decode('utf-8')
print(str(str3,'utf-8'))
print(str4)

if __name__ == "__main__":
    pass