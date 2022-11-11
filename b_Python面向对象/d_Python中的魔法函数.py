# -*- coding = utf-8 -*-
# @Time : 2022/11/10 17:40
# @Author : anpeng
# @File : d_Python中的魔法函数.py
# @Software : PyCharm
"""
在Python中，以双下划线开头且双下划线结尾，形如__xx__()的函数，叫做魔方函数，指的是具有特殊功能的函数。
常见魔法方法：
    __init__(self)：初始化对象。创建一个对象时默认被调用，不需要手动调用。其中self参数不需要开发者传递，Python解释器会自动吧当前对象引用传递过去。
                    *** 其中带参数的__init__方法是为了在创建对象时初始化类属性，其定义可见Washer.py文件中。

    __str__()：当使用print打印对象时，会默认输出对象的内存地址。
               如果定义了__str__方法，print打印该类的实例化对象时，会输出__str__方法中return的数据。
               如果重载了__str__方法。那么对象的self也将指向return的数据。

    __del__()：当使用[del 对象名]删除对象时，Python会默认调用__del__方法，可以在其中输入一些提示信息。
"""
from clazz.Computer import Computers  # 采用原始方法(这里假定没有将clazz设为source文件)，导入模块中类

computer = Computers()
print(computer)  # this is a computer(打印的__str__方法中返回的数据，而不是对象内存地址了)
del computer
