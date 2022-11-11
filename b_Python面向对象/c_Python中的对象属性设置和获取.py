# -*- coding = utf-8 -*-
# @Time : 2022/11/10 15:58
# @Author : anpeng
# @File : c_Python中的对象属性设置和获取.py
# @Software : PyCharm
"""
属性即是特征，比如洗衣机的高度，宽度，重量。
    分为对象属性和类属性。
    语法：
        对象属性添加：对象名.属性名=值
        对象获取：对象名.属性名

        类属性添加：self.属性名=值
        类属性获取：self.属性名

    区别：
        类属性，是所有实例化对象都具有的属性(可能属性值不同)
        对象属性，是对象特有的，不同对象的含有的属性类别可能会不同。

    注意：不建议在类方法中通过 [self.对象属性名] 的方式获取对象属性，因为不能保证对象添加了该属性。
"""
from Washer import Washer  # 采用最新方法导入模块中类

# 1.创建对象
huawei = Washer('huawei')
huawei.wash()
haier = Washer('haier')
haier.wash()

# 2.外部添加属性
huawei.width = 100
huawei.height = 200
huawei.weight = 50

# 3.外部获取属性
print(f'洗衣机的品牌是{huawei.brand}, 宽度是{huawei.width}, 高度是{huawei.height}, 重量是{huawei.weight}')
# print(f'洗衣机的品牌是{haier.brand}, 宽度是{haier.width}') 'Washer' object has no attribute 'width' 因为并没有给haier洗衣机添加宽度属性。
