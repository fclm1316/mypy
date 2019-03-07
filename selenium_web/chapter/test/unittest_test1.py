#!/usr/bin/python3
#coding:utf-8
import unittest
from selenium_web.chapter.test.my_calculator import Count

#继承类
class TestCount(unittest.TestCase):
    #初始化
    def setUp(self):
        print("test start;web_dirver;connect to db")

    #执行过程
    def test_add1(self):
        j = Count(2,3)
        #预判断
        self.assertEqual(j.add(),4,msg='hah')

    def test_add2(self):
        j = Count(5,9)
        #预判断
        self.assertEqual(j.add(),14,msg='wowo')

    #清扫
    def tearDown(self):
        print("test end;dirver.quit();disconnect db")


if __name__ == '__main__':
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add1"))
    suite.addTest(TestCount("test_add2"))
    #运行测试集合
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

