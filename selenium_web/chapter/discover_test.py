#!/usr/bin/python3
#coding:utf-8
import unittest

test_dir = './'

discover = unittest.defaultTestLoader.discover(test_dir,pattern='unittest_*.py')

if __name__ == "__main__":
    with open('./repo/repo.txt','w',encoding='gb18030') as f:
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(discover)
