#encoding:utf-8
#!/usr/bin/python3
#coding:utf-8
import unittest
import HTMLTestReportCN
import HTMLTestRunner
# from hzzg.test_run.do_test.do_login import *

test_dir ='./do_test'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*.py')
# test_unit = unittest.TestSuite()
# test_name = [LogIn('test_login1'),LogIn('test_login2'),TestTest('test_test1'),TestTest('test_test2')]
# test_unit.addTests(test_name)

if __name__ == '__main__':
    with open('./test_demo.html','wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='自动化测试报告',
                                               description='测试用例')
        runner.run(discover)
        # runner.run(test_unit)
