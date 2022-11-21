# -*- coding = utf-8 -*-
# @Time : 2022/11/11 11:32
# @Author : anpeng
# @File : d-Python中的继承体系.py
# @Software : PyCharm

"""
继承的概念：
    继承：一般是指子女继承父辈的财产。面向对象编程中的继承指的是多个类之间的所属关系，即子类会继承父类全部属性和方法。
    旧式类：不由任意内置类型派生出的类，叫经典类或旧式类。
            class 类名：
                代码
                ......
    新式类：默认继承内置object基类的类，也可以在括号指定继承其他父类。
            class 类名(object):
                代码：
                ......
    Python中所有类默认继承object类，object类是顶级类或基类；其他子类叫派生类。

单继承：指的是子类只继承一个父类的情况，会默认继承父类的所有属性和方法。先从子类中找属性和方法，没有再从父类中找。

多继承：子类同时继承多个父类，若多个父类中有相同的同名方法或属性时，会默认使用第一个父类的同名属性或方法。
       方法解析顺序：MRO(method resolution order)，祖先同名方法的继承顺序，采用C3算法，返回一个祖先类型的元组。
                  子类在调用多个祖先都有的同名方法时，会优先调用元组中第一个遇到的祖先同名方法。

子类重写父类的属性和方法：若父类的方法或属性被子类重写时，子类会优先调用子类中重写的方法和属性。如果先调用了父类的同名属性，
                    实质上是子类的同名属性被重新赋值，所以需要调用子类自己的初始化再次重新赋值

子类调用父类的同属性和同名方法：子类中调用父类的同名方法和类属性时，直接使用[父类名.方法名] 和 [父类名.类属性名]。
                        注意：1.为保证调用到的是父类的同名实例属性，必须在调用父类方法前调用父类的初始化方法并将当前对象self传入
                            本质上，就是将当前对象self的product_time实例属性进行重新赋值。
                             2.如果先调用了父类的同名属性，实质上是子类的同名属性被重新赋值，所以需要调用子类自己的初始化再次重新赋值.

多重继承：

super方法：

"""
from Computer import MateBook, MagicBook

# 1.单继承：子类同时只继承一个父类
magicBook = MagicBook()
magicBook.get_brand()  # this is an honor computer
# 1.1 子类默认继承父类全部属性和方法。先从子类中找属性，没有再从父类中找。
print(f'access the father class attribute of magicBook: {magicBook.info}')
# 1.2 先从子类中找方法，没有再从父类中找
magicBook.show()

# 2.多继承：子类同时继承多个父类。
mateBook = MateBook()
print(mateBook.__class__)  # 返回实例的类型：<class 'Computer.MateBook'>
print(mateBook.__class__.__base__)  # 返回子类的第一个直接父类：<class 'Computer.Machine'>
print(mateBook.__class__.__bases__)  # 返回子类的所有直接父类：(<class 'Computer.Machine'>, <class 'Computer.Computer'>)
# 2.1 MRO 返回子类的继承顺序，即在调用祖先中同名方法时，会优先调用第一遇到的祖先中的同名方法。
print(MateBook.__mro__)  # (<class 'Computer.MateBook'>, <class 'Computer.Machine'>, <class 'Computer.Computer'>, <class 'object'>)
mateBook.show()  # this is instance function of <class 'Computer.MateBook'>。

# 3.重写--子类和父类具有同名方法和属性时，优先调用子类的方法和属性
magicBook.show()  # the father function of the <class 'Computer.MagicBook'> has been overwritten。

# 5.子类调用父类中的同名方法和属性。
# 5.1 子类中需要调用父类的同名类属性和同名方法时，直接使用[父类名.方法名]和[父类名.类属性名]
magicBook.call_father_show()  # this is instance function of Computer class

# 5.2 为保证调用到的是父类的同名实例属性，必须在调用父类方法前调用父类的初始化方法并将当前对象self传入
# 本质上，就是将当前对象self的product_time实例属性进行重新赋值。
mateBook.get_father_product_time()  # the product time of the machine is 2022-11-15 20:31:02.770606

# 5.3 如果先调用了父类的同名属性，实质上是子类的同名属性被重新赋值，所以需要调用子类自己的初始化再次重新赋值。
mateBook.get_product_time()  # 1996-11-15
