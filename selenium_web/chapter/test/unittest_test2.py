#!/usr/bin/python3
#coding:utf-8

from selenium_web.chapter.test.my_calculator import Count
import unittest

class MyTest(unittest.TestCase):
    #初始化
    def setUp(self):
        print("test start;web_dirver;connect to db")
    #清扫
    def tearDown(self):
        print("test end;dirver.quit();disconnect db")

class DoTest(MyTest):
    #执行过程
    #装饰器
    @unittest.skip('跳过')
    # @unittest.skipIf(3 > 2 ,'跳过')
    # @unittest.skipUnless(3 > 2 ,'跳过')
    def test_add1(self):
        j = Count(2,3)
        #预判断
        self.assertEqual(j.add(),6,msg='hah')

    def test_add2(self):
        j = Count(5,9)
        #预判断
        self.assertEqual(j.add(),14,msg='waw')

if __name__ == '__main__':
    unittest.main(verbosity=2)
