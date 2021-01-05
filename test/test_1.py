#encoding:utf-8
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def test_1(num,str1,str2):
    time.sleep(1)
    print('{}====={}-------{}'.format(num,str1,str2))


with ThreadPoolExecutor(8)  as executor:
   all_task = [executor.submit(test_1,(num),'a','b') for num in range(20)]

