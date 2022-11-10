# -*- coding = utf-8 -*-
# @Time : 2022/11/10 15:26
# @Author : anpeng
# @File : 01-Python中类的self.py
# @Software : PyCharm
"""
类中的self
    self指的是调用该函数的类的实例化对象。
"""

# 1.单个对象的self
class Washer:
    def __init__(self, brand):
        self.brand = brand

    def wash(self):
        print(str(self) + self.brand + '牌洗衣机正在洗衣服中>>>')

haier = Washer('haier')
haier.wash()  # <__main__.Washer object at 0x00000214E92D4FD0> haier牌洗衣机正在洗衣服中>>>
print(haier)  # <__main__.Washer object at 0x00000214E92D4FD0> 对象地址一致，说明是同一个。

# 2.多个对象的self
xiaomi = Washer('xiaomi')
