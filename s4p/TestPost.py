#!/usr/bin/python3
# coding:utf-8
import json

import params as params
from requests_toolbelt import MultipartEncoder
import requests

file_path = "c:/1_申请书.pdf"
url = 'http://192.168.99.161:10051/c_api/cams/requestDataUpload?'
m = MultipartEncoder({
    'vsnId': '01',
    'msgId': '1023310090110020190907000999',
    'orgnId': '102331009011',
    'recvId': '123456789012',
    'rsdFlg': '0',
    'imageData': (
    '1_申请书.pdf', open(file_path, 'rb'), 'application/octet-stream;boundary="--------------------------"',)}
    # 'imageData':('1_申请书.pdf',open(file_path,'rb'),'multipart/form-data')
    # 'imageData':('imageData',open(file_path,'rb'),'application/octet-stream')
)

respons = requests.post(url, data=m, headers={'Content-Type': m.content_type}, allow_redirects=False)
# respons = requests.post(url,data=m)
# print(json.dumps(body))
print(respons.text)
print(respons.status_code)

if __name__ == "__main__":
    pass
