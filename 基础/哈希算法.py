#!/usr/bin/python3
#coding:utf-8
from hashlib import md5,sha1,sha224,sha256,sha384,sha512
from pprint import pprint

hash_func = [md5,sha1,sha224,sha256,sha384,sha512]

def hash_show(s):
    result =[]
    for func in hash_func:
        hash_ojb = func(s.encode('utf-8'))
        hash_hex = hash_ojb.hexdigest()
        result.append((hash_ojb.name,len(hash_hex),hash_hex))
    return result

if __name__ == "__main__":
    s = 'hello world'
    rs = hash_show(s)
    pprint(rs)
