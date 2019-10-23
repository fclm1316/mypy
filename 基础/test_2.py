#!/usr/bin/python3
#coding:utf-8
import sqlalchemy
from 基础.test_1 import mytest_1

class mytest_2(mytest_1):
    def test_001(self):
        self.number = self.number + 1


if __name__ == "__main__":
    pass