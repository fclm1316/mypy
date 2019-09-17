#!/usr/bin/python3
#coding:utf-8
import json
import requests

file_path = "c:/1_申请书.pdf"
url='http://192.168.99.161:10051/c_api/cams/requestDataUpload?'
Data = {'vsnId':'01',
        'msgId':'1023310090110020190907000999',
        'orgnId':'102331009011',
        'recvId':'123456789012',
        'rsdFlg':'0'}
f ={'imageData':open(file_path,'rb')},

respons = requests.post(url,data=Data,file=f)
# print(json.dumps(body))
print(respons.text)
print(respons.status_code)

if __name__ == "__main__":
    pass