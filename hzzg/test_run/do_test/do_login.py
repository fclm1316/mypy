#!/usr/bin/python3
#coding:utf-8
import unittest
from hzzg.test_run.test_driver import Web_Driver

class LogIn(Web_Driver):
    u'''登陆测试'''
    def test_login1(self):
        u'''登陆测试1'''
        pass
    def test_login2(self):
        u'''登陆测试2'''
        self.assertEqual(2,3,msg='失败')

