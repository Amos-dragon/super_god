#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pymysql,redis,pymongo,operator






class Mysql():


    def mysql_connection(self):
        try:
            db = pymysql.connect(
                host='*****',     # 主机名
                port=*,                    # 端口
                database='****',           # 数据库名称
                user='****',                  # 用户名
                password='****'           # 密码
            )
        except Exception as e:
            print('Error:{}'.format(e))
            # 查询前，必须先获取游标,游标就相当于一个缓冲区，存放暂时的结果
        else:
            database = db.cursor()
            return database








    def Mysql_Currencys_curr(currencys=False):
        database=Mysql().mysql_connection()
        """
                执行的都是原生SQL语句
                
                该方法获取一个查询结果集。结果集是一个对象
                print(Database.fetchone())

                获取全部的返回结果行
                print(Database.fetchall())
                """
        data=database.execute('SELECT short_name FROM currency')

        currencys = []
        for x in range(data):
            currencys.append(database.fetchone()[0])
        return currencys




    def Mysql_Currencys_icon(icons=False):
        database=Mysql().mysql_connection()
        data = database.execute('SELECT icon FROM currency')

        icons = []
        for x in range(data):
            icons.append(database.fetchone()[0])
        return icons




    def Mysql_symbol(KV=False):
        database=Mysql().mysql_connection()
        keys = 'name,tick_size,lot_size,min_qty,max_qty,min_notional'


        dataNum = database.execute('SELECT {} FROM symbol'.format(keys))


        symbolsinfo = []
        for x in range(dataNum):
            symbolsinfo.append(database.fetchone())



        dict_values = keys.replace('tick_size','tickSize').replace('lot_size','lotSize').replace('min_qty','minQty').replace('max_qty','maxQty').replace('min_notional','minNotional').lstrip('\'').rstrip('\'').split(',')
        KV = []
        for x in range(len(symbolsinfo)):
            SymbolInfo = {}
            for y in range((len(symbolsinfo[x]))):
                SymbolInfo[dict_values[y]] = symbolsinfo[x][y]
                if y==len(symbolsinfo[x])-1:
                    KV.append(SymbolInfo)
        return KV





class Redis():

    def redis_connection(self):
        try:
            """
            一个redis实例默认有16个数据库，从0-15
            指定数据库 - db=0
            redis 取出的结果默认是字节，设定decode_responses=True 改成字符串
            """
            res = redis.StrictRedis(
                host="****",
                port=*,
                db=0
            )
        except Exception as u:
            print(u)
        else:
            return res


    def Redis_public_ticker(list_keys=False):
        database = Redis().redis_connection()
        data_dict=database.hgetall('ticker')
        # database.hget('ticker',1) 取指定表中'key'对应的'value'


        list_keys = []
        for y in data_dict:
            # print(chardet.detect(y)) 识别字节是何种编码
            list_keys.append(y.decode('ASCII'))
        return list_keys





class Mongo():

    def Mongo_connection(self):
        try:
            mg = pymongo.MongoClient('****',*)
            """
            TradeMarket ：       数据库名
            simpleOrderBook      表名
            qw.qa.whaleex.net    数据库地址
            27017                端口号

            db.find_one()   读取一条-默认最新
            db.find()       读取所有
            find().count()  记录数量
            find().sort("id",pymongo.ASCENDING)   #升序
            find().sort("id",pymongo.DESCENDING)  #降序

            find({'age': {'$gt': 20}})
            $lt | 小于
            $gt | 大于
            $lte | 小于等于
            $gte | 大于等于
            $ne | 不等于
            $in | 在范围内
            $nin | 不在范围内
            """
        except Exception as x:
            print(x)
        else:
            return mg


    def Mongo_public_orderBook(self):
        Mg = Mongo().Mongo_connection()
        connect_orderBook = Mg.TradeMarket.simpleOrderBook
        symbolPK = connect_orderBook.find_one({"symbolId" : 1})


        key = ['lastUpdateId','timestamp','asks','bids']
        dict_pk = {}

        for x in range(len(key)):
            for y in list(symbolPK.keys()):
                if operator.eq(key[x],y)==True:
                    dict_pk[key[x]] = symbolPK[key[x]]


        for x in range(len(dict_pk['asks'])):
            for y in dict_pk['asks'][x].keys():
                if operator.eq('price',y)==True:
                    # 小数点后补0
                    dict_pk['asks'][x][y] = '%.8f' % (float(dict_pk['asks'][x][y]) / 100000000)
                    dict_pk['bids'][x][y] = '%.8f' % (float(dict_pk['bids'][x][y]) / 100000000)

                if operator.eq('quantity',y)==True:
                    dict_pk['asks'][x][y] = '%.10f' % (float(dict_pk['asks'][x][y]) / 10000000000)
                    dict_pk['bids'][x][y] = '%.10f' % (float(dict_pk['bids'][x][y]) / 10000000000)


        if len(dict_pk['asks'])>10:
            dict_pk['asks'] = dict_pk['asks'][0:10]
            dict_pk['bids'] = dict_pk['bids'][0:10]
        else:
            dict_pk['asks'] = dict_pk['asks'][0:len(dict_pk['asks'])]
            dict_pk['bids'] = dict_pk['bids'][0:len(dict_pk['asks'])]
        return dict_pk

