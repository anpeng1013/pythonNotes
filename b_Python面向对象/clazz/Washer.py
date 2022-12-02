# -*- coding = utf-8 -*-
# @Time : 2022/11/10 16:30
# @Author : anpeng
# @File : Washer.py
# @Software : PyCharm
# import datetime

class Washer:
    def __init__(self, brand):
        self.brand = brand

    def wash(self):
        print(str(self.brand + '牌洗衣机正在洗衣服中>>>'))
