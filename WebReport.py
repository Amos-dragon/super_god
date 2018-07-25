#!/usr/bin/env python3
# coding:utf-8
import web,time

urls = (
    '/', 'index' #“/” 是一个正则表达式。
)



# 告诉web.py 在哪里可以搜索得到模板目录     提示：可在render 调用里添加cache = False 使得每次访问页面时都重载模板
render = web.template.render('/Users/xuguolong/PycharmProjects/whaleex/Api_automation/py/templates')


class index:
    def GET(self):

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        iterations = "1"

        return render.index(timestamp,iterations)  # 使用index.html模板，传递参数（这里会查找templates下第一个匹配上index.*的文件，所以我们的模板文件其实可以使用任何扩展名结尾）


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
