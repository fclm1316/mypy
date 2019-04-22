#!/usr/bin/python3
#coding:utf-8
import unittest
import HTMLTestRunner

test_dir = './test_suite'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*.py')


if __name__ == "__main__":
    with open('./mian.html','wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='自动化测试报告',
                                               description='测试用例')
        runner.run(discover)
