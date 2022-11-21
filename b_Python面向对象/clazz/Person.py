# -*- coding = utf-8 -*-
# @Time : 2022/11/14 18:47
# @Author : anpeng
# @File : Person.py
# @Software : PyCharm

class Person(object):
    """
    this is the doc of the Person object.
    """
    index = 0  # 直接在类中定义的属性，是类属性。

    def __init__(self, name):  # __init__的第一参数是self，所以它是实例方法。
        self.name = name  # self其实就调用该初始化方法的对象。所以通过[self.属性=属性值]定义的是实例属性。
        Person.index += 1  # 类属性只能通过类对象来修改，无法通过实例对象修改。每次创建person实例，都会使index加1。

    def hello(self):  # 在类中定义，且默认第一默认参数为self的方法，叫做实例方法。
        print(f'hello everyone, my name is {self.name} and {self.index}')  # 类属性可以通过实例对象进行访问，反之不行。

    @classmethod  # 用@classmethod修饰，且第一参数为类cls的方法叫做类方法
    def speak(cls, instance):
        print(f'this is class method and the current instance is {instance.name}')  # name为实例属性，只能通过实例对象进行访问。

    @staticmethod
    def test_static_method():
        print('this is a static method!')

class OverwriteStr(object):
    def __str__(self):
        return 'the function __srt__ has been overwritten'

    def print_self(self):
        print(f'the self of instance is: {self}')

    def __del__(self):
        print('the instance object of OverwriteStr class has been deleted...')
