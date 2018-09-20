#!/usr/bin/python3
#coding:utf-8
#import sys
import time
from collections import deque
fancy_loading = deque('>---------------------')
while True:
    print('\r%s' % ''.join(fancy_loading))
    fancy_loading.rotate(1)
#for linux 刷新
#    sys.stdout.flush()
    time.sleep(1)

