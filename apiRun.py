#!/usr/bin/env python3
#coding: utf-8



import sys,json
import unittest,pymysql
sys.path.append("/Users/xuguolong/PycharmProjects/whaleex")
from Api_automation.py.config import Test_case,Database_Connection




class LianXi(unittest.TestCase):

        # @classmethod
        def setUp(self):
            pass

        def test_1(self):
            Test_case.Testcase.test_Mysql_public_currency(self)


        def test_2(self):
            Test_case.Testcase.test_Mysql_public_symbol(self)


        def test_3(self):
            Test_case.Testcase.test_Redis_public_ticker(self)


        def test_4(self):
            Test_case.Testcase.test_Mongo_public_orderBook(self)




if __name__ == '__main__':
    unittest.main()
