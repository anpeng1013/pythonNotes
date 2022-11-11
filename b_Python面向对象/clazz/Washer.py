# -*- coding = utf-8 -*-
# @Time : 2022/11/10 16:30
# @Author : anpeng
# @File : Washer.py
# @Software : PyCharm
class Washer:
    def __init__(self, brand):  # self魔法方法，在创建对象时自动调用，self参数自动传递。
        self.brand = brand

    def wash(self):
        print(str(self) + " " + self.brand + '牌洗衣机正在洗衣服中>>>')
