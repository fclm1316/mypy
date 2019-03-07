#!/usr/bin/python3
#coding:utf-8
from selenium_web.chapter.test.my_calculator import Count
from selenium_web.chapter.test.unittest_test2 import MyTest
import unittest

class TestMy(MyTest):
    def test_sub1(self):
        j = Count(6,4)
        self.assertEqual(j.sub(),2,msg='jjj')

    def test_sub2(self):
        j = Count(7,4)
        self.assertEqual(j.sub(),3)

if __name__ == "__main__":
    unittest.main()
