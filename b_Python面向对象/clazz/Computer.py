# -*- coding = utf-8 -*-
# @Time : 2022/11/11 10:01
# @Author : anpeng
# @File : Computer.py
# @Software : PyCharm
import datetime

class Computer(object):
    info = 'this is a computer'  # 类属性，相当于java中的静态变量

    def show(self):
        print('this is instance function of Computer class')

class Machine(object):

    def __init__(self):
        self.product_time = datetime.datetime.now()  # 父类的实例属性。

    def show(self):
        self.__init__()
        print(f'this is instance function of {self.__class__.__base__}')  # base和bases只能类名调用

    def get_product_time(self):
        print(f'the product time of the machine is {self.product_time}')

class MateBook(Machine, Computer):
    def __init__(self):
        Machine.__init__(self)  # 若子类中重写了init方法，则必须先显示调用父类初始化方法。本质是将父类初始化添加的属性添加(继承)到子类中.
        self.brand = 'huawei'
        self.product_time = '1996-11-15'

    def get_product_time(self):
        self.__init__()  # 如果先调用了父类的同名属性，实质上是子类的同名属性被重新赋值，所以需要调用子类自己的初始化再次重新赋值。
        print(self.product_time)

    def get_machine_product_time(self):  # 为保证调用到的是父类的同名实例属性，必须在调用父类方法前调用父类的初始化方法并将当前对象self传入
        Machine.__init__(self)  # 本质上，就是将当前对象self的product_time实例属性进行重新赋值
        Machine.get_product_time(self)

    def get_father_show(self):
        super(MateBook, self).__init__()
        super(MateBook, self).show()

class MagicBook(Computer):
    def __init__(self):  # 由于父类的init方法中并没有添加实例属性，所以即使子类重写init方法，也不必显示调用父类的init方法。
        self.brand = 'honor'

    def get_brand(self):
        print(f'this is an {self.brand} computer')

    def show(self):  # 重写父类Computer中的show方法，防止父类同名方法调用后修改实例属性的值，所以需要先调用初始化方法。
        self.__init__()
        print(f'the father function of the {self.__class__} has been overwritten')

    def call_father_show(self):
        super().__init__()  # 此时self会被自动传入，不需要手动传入，这是与父类名.函数名(self)的区别。
        Computer.show(self)  # 类对象调用实例方法时，必须手动传入实例对象。

class MateBook16(MateBook):
    pass
