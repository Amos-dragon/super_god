#!/usr/bin/env python3
#coding: utf-8


import requests,sys,re,operator,json
sys.path.append("/Users/xuguolong/PycharmProjects/whaleex")
from Api_automation.py.config import gather_api,Database_Connection





Total = 0
Success = 0
Fail = 0
Failpath = []



class Testcase():



    def test_Mysql_public_currency(self):
        case1 = '用例：1'
        print(' （{} 开始执行）'.format(case1))
        headers = {}
        try:
            self.response = requests.request("GET", url=gather_api.API().Api_public_currency(), headers=headers,timeout=gather_api.API().timeout())  # 设置超时时间
        except Exception as error_message:
            print(error_message)
        else:

            if self.response.status_code!=200:
                global Fail
                Fail += 1
                Failpath.append(case1)
                print(" 【测试结果：未通过】获取当前支持的所有数字货币:{}    - Response Status code: {}    - Response time: {}s    - Setting timeout:{}s".format(gather_api.API().Api_public_currency(), self.response.status_code,self.response.elapsed.total_seconds(), gather_api.API().timeout()))
                print('- 错误信息:')
                print('- 期望返回值: Response Status code:{}'.format(200))
                print('- 实际返回值: Response Status code:{}'.format(self.response.status_code))

            else:





                # 判断currency是否获取与数据库的一致
                Currencys = Database_Connection.Mysql.Mysql_Currencys_curr(currencys=True)
                currencys = []
                for x in Currencys:
                    if re.search(pattern='{}'.format(x), string=self.response.text, flags= re.I|re.M|re.S)!=None:
                        print("- 获取{}数字货币： Success".format(x))
                        currencys.append(x)
                    else:
                        currencys.append('None')

                if operator.eq(Currencys,currencys)==True:
                    pass
                else:
                    for x,y in zip(Currencys,currencys):
                        if operator.eq(x,y)==True:
                            pass
                        else:
                            print('- 错误信息：获取数据库MySQL_Currency表中Currency与Response匹配未一致：')
                            print('- 期望返回值:{}'.format(x))
                            print('- 实际返回值:{}'.format(y))
                print()






                # 判断icon是否获取且是否与数据库一致
                iCons = Database_Connection.Mysql.Mysql_Currencys_icon(icons=True)
                # iCons = ['https://s3.ap-northeast-1.amazonaws.com/whaleex-identify-testing/1529553605180-BTC.png', 'https://s3.ap-northeast-1.amazonaws.com/whaleex-identify-testing/1529553410915-ETH.png', 'https://s3.ap-northeast-1.amazonaws.com/whaleex-identify-testing/1529553484604-USDT.png', 'https://s3.ap-northeast-1.amazonaws.com/whaleex-identify-testing/1529553520344-默认币.png', 'https://s3.ap-northe-1.amazonaws.com/whaleex-identify-testing/1529553548276-EOS.png', 'https://s3.ap-northeast-1.amazonaws.com/whaleex-identify-testing/1529553566299-KEY.png', 'https://s3.ap-northeast-1.amazonaws.com/whaleex-identify-testing/1529553584817-POE.png', 'https://s3.ap-northeast-1.amazonaws.com/whaleex-identify-testing/1528959763980-屏幕快照_2018-05-28_下午1.44.57.png', 'https://s3.ap-northeamazonaws.com/whaleex-identify-testing/1528960117169-屏幕快照_2018-06-07_下午2.27.43.png']
                icons = re.findall(r'https.+?\.png', self.response.text, re.M|re.S)
                if icons == []:
                    print("- 错误信息：获取 [icon]: Fail")
                else:
                    ICONS = []
                    if operator.eq(iCons,icons)==True:
                        for x in icons:
                            print("- [icon]匹配： Success -{}".format(x))
                            ICONS.append(x)
                    else:
                        for x,y in zip(iCons,icons):
                            if operator.eq(x,y)==True:
                                pass
                            else:
                                print('- 错误信息：获取数据库MySQL_Currency表中icon与Response匹配icon未一致：')
                                print('- 期望返回值:{}'.format(x))
                                print('- 实际返回值:{}'.format(y))





                if operator.eq(Currencys,currencys)==True and len(iCons)==len(ICONS):
                    print(" 【测试结果：  通过】获取当前支持的所有数字货币:{}    - Response Status code: {}    - Response time: {}s".format(gather_api.API().Api_public_currency(), self.response.status_code, self.response.elapsed.total_seconds()))
                    global Success
                    Success +=1
                else:
                    print(" 【测试结果：未通过】获取当前支持的所有数字货币:{}    - Response Status code: {}    - Response time: {}s    - Setting timeout:{}s".format(gather_api.API().Api_public_currency(), self.response.status_code,self.response.elapsed.total_seconds(), gather_api.API().timeout()))
                    Fail += 1
                    Failpath.append(case1)

        finally:
            print(' （{} 执行完毕）'.format(case1))
            print()
            global Total
            Total+=1





    def test_Mysql_public_symbol(self):
        case2 = '用例：2'
        print(' （{} 开始执行）'.format(case2))
        headers = {}
        try:
            self.response = requests.request("GET", url=gather_api.API().Api_public_symbol(), headers=headers,timeout=gather_api.API().timeout())  # 设置超时时间
        except Exception as error_message:
            print(error_message)
        else:

            if self.response.status_code != 200:
                global Fail
                Fail += 1
                Failpath.append(case2)
                print(" 【测试结果：未通过】获取所有交易对:{}    - Response Status code: {}    - Response time: {}s    - Setting timeout:{}s".format(gather_api.API().Api_public_symbol(), self.response.status_code,self.response.elapsed.total_seconds(), gather_api.API().timeout()))
                print('- 错误信息1:')
                print('- 期望返回值: Response Status code:{}'.format(200))
                print('- 实际返回值: Response Status code:{}'.format(self.response.status_code))
            else:





                SQL_Symbolinfo = Database_Connection.Mysql.Mysql_symbol(KV=True)
                Re_symbolinfo = json.loads(self.response.text)




                Num3 = 0
                Num2 = 0
                if len(SQL_Symbolinfo) == len(Re_symbolinfo):
                    for x in SQL_Symbolinfo:
                        Num1 = len(x.keys())
                        Num2 += 1
                        for z in Re_symbolinfo:
                            if x['name'] == z['name']:
                                for y in range(len(x.keys())):
                                    SS = list(x.keys())[y]
                                    try:
                                        z[SS] == x[SS]
                                    except Exception as error_message:
                                        print("- 错误信息2：数据库MySQL_symbol中字段{}未在resopnse中匹配到:".format(SS))
                                    else:
                                        Num3 += 1
                                        print("- 匹配： Success [{} : {}] ".format(SS, z[SS]))
                                    finally:
                                        pass


                else:
                    Fail += 1
                    Failpath.append(case2)
                    print(" 【测试结果：未通过】获取所有交易对:{}    - Response Status code: {}    - Response time: {}s    - Setting timeout:{}s".format(gather_api.API().Api_public_symbol(), self.response.status_code,self.response.elapsed.total_seconds(), gather_api.API().timeout()))
                    print('- 错误信息4')
                    print('- 期望返回值: symbol数量:{}个'.format(len(SQL_Symbolinfo)))
                    print('- 实际返回值: symbol数量:{}个'.format(len(Re_symbolinfo)))


                if int(Num3/Num2) == Num1:
                    print(" 【测试结果：  通过】获取所有交易对:{}    - Response Status code: {}    - Response time: {}s".format(gather_api.API().Api_public_symbol(), self.response.status_code,self.response.elapsed.total_seconds()))
                    global Success
                    Success +=1
                else:
                    print(" 【测试结果：未通过】获取所有交易对:{}    - Response Status code: {}    - Response time: {}s    - Setting timeout:{}s".format(gather_api.API().Api_public_symbol(), self.response.status_code,self.response.elapsed.total_seconds(), gather_api.API().timeout()))
                    Fail += 1
                    Failpath.append(case2)




        finally:
            print(' （{} 执行完毕）'.format(case2))
            print()
            global Total
            Total+=1





    def test_Redis_public_ticker(self):
        case3 = '用例：3'
        print(' （{} 开始执行）'.format(case3))

        headers={}
        try:
            self.response = requests.request("GET",url=gather_api.API().Api_public_ticker(),headers=headers,timeout=gather_api.API().timeout())
        except Exception as error_message:
            print(error_message)
        else:

            if self.response.status_code != 200:
                global Fail
                Fail += 1
                Failpath.append(case3)
                print(" 【测试结果：未通过】获取所有交行情:{}    - Response Status code: {}    - Response time: {}s    - Setting timeout:{}s".format(gather_api.API().Api_public_ticker(), self.response.status_code,self.response.elapsed.total_seconds(), gather_api.API().timeout()))
                print('- 错误信息1:')
                print('- 期望返回值: Response Status code:{}'.format(200))
                print('- 实际返回值: Response Status code:{}'.format(self.response.status_code))
            else:


                RediStickerInfo = Database_Connection.Redis.Redis_public_ticker(self)
                Re_StickerInfo  = json.loads(self.response.text)




                symbols2 = []
                for x in Re_StickerInfo:
                    symbols2.append(str(x['symbolId']))
                symbols = symbols2[::-1]



                if operator.eq(RediStickerInfo,symbols) == True:
                    global Success,symbolsId
                    symbolsId = []
                    for x in RediStickerInfo:
                        print("- [symbolId : {}] 匹配：Success".format(x))
                        symbolsId.append(x)
                    print(" 【测试结果：  通过】获取所有行情:{}    - Response Status code: {}    - Response time: {}s".format(gather_api.API().Api_public_ticker(), self.response.status_code,self.response.elapsed.total_seconds()))
                    Success +=1

                else:
                    print(" 【测试结果：未通过】获取所有行情:{}    - Response Status code: {}    - Response time: {}s    - Setting timeout:{}s".format(gather_api.API().Api_public_ticker(), self.response.status_code,self.response.elapsed.total_seconds(), gather_api.API().timeout()))
                    print('- 错误信息2:')
                    print('- 期望返回值: symbolId:{}'.format(RediStickerInfo))
                    print('- 实际返回值: symbolId:{}'.format(symbols))
                    Fail += 1
                    Failpath.append(case3)





        finally:
            print(' （{} 执行完毕）'.format(case3))
            print()
            global Total
            Total+=1





    def test_Mongo_public_orderBook(self):
        pass
        case4 = '用例：4'
        print(' （{} 开始执行）'.format(case4))

        headers = {}
        try:
            self.response = requests.request("GET", url=gather_api.API().Api_public_orderBook(), headers=headers,timeout=gather_api.API().timeout())
        except Exception as error_message:
            print(error_message)
        else:

            if self.response.status_code != 200:
                global Fail
                Fail += 1
                Failpath.append(case4)
                print(" 【测试结果：未通过】根据交易对获取盘口行情:{}    - Response Status code: {}    - Response time: {}s    - Setting timeout:{}s".format(gather_api.API().Api_public_orderBook(), self.response.status_code,self.response.elapsed.total_seconds(), gather_api.API().timeout()))
                print('- 错误信息1:')
                print('- 期望返回值: Response Status code:{}'.format(200))
                print('- 实际返回值: Response Status code:{}'.format(self.response.status_code))
            else:

                pass
                Mg_orderBook = Database_Connection.Mongo.Mongo_public_orderBook(self)
                Re_orderBook = json.loads(self.response.text)


                num = 0
                for x, y in zip(Mg_orderBook, Re_orderBook):
                    if operator.eq(x, y) == True:
                        if str(Mg_orderBook[x])==str(Re_orderBook[y]):
                            num += 1
                            if num == len(Re_orderBook.keys()):
                                global Success
                                print(" 【测试结果：  通过】根据交易对获取盘口行情:{}    - Response Status code: {}    - Response time: {}s".format(gather_api.API().Api_public_orderBook(), self.response.status_code,self.response.elapsed.total_seconds()))
                                print("-  [orderBook] 匹配： Success")
                                print(Re_orderBook)
                                Success +=1
                    else:
                        print(
                            " 【测试结果：未通过】根据交易对获取盘口行情:{}    - Response Status code: {}    - Response time: {}s    - Setting timeout:{}s".format(gather_api.API().Api_public_orderBook(), self.response.status_code,self.response.elapsed.total_seconds(), gather_api.API().timeout()))
                        print('- 错误信息2:')
                        print('- 期望返回值: {}'.format(x))
                        print('________________________________________________________________________________________________________________________________________________________________________________________________')
                        print('- 实际返回值: {}'.format(y))
                        Fail += 1
                        Failpath.append(case4)



        finally:
            print(' （{} 执行完毕）'.format(case4))
            print()
            global Total
            Total += 1



        print('  -【 Total：{} 】'.format(Total))
        print('  -【 Sucess_Total：{} 】'.format(Success))
        print('  -【 Fail_Total：{} 】'.format(Fail))
        if Fail > 0:
            print('  - 失败用例如下：')
            for x in Failpath:
                print('  -【 Fail_case：{} 】'.format(x))
        else:
            pass






