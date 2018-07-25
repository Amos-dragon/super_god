#!/usr/bin/env python3
#coding: utf-8


import sys

sys.path.append("/Users/xuguolong/PycharmProjects/whaleex")
from Api_automation.py.config import Test_case



class API():

    def url(self):
        url = "https://gw.qa.whaleex.net"
        return url


    def timeout(self):
        timeout = 2
        return timeout


    def Api_public_currency(self):
        public_currency = "{}/BUSINESS/api/public/currency".format(API().url())
        return  public_currency


    def Api_public_symbol(self):
        public_symbol =  "{}/BUSINESS/api/public/symbol".format(API().url())
        return public_symbol


    def Api_public_ticker(self):
        public_ticker =  "{}/BUSINESS/api/public/ticker".format(API().url())
        return public_ticker


    def Api_public_orderBook(self):
        public_orderBook = "{}/BUSINESS/api/public/orderBook/symbol/1".format(API().url())
        return public_orderBook

