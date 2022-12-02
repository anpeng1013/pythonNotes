# -*- coding = utf-8 -*-
# @Time : 2022/11/23 20:03
# @Author : anpeng
# @File : f_Python中的多态实现.py
# @Software : PyCharm

"""
    多态的概念依赖于继承。
        定义：多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的结果。
        步骤：
            1、定义父类，并提供公共方法。
            2、派生子类，并重写父类方法。
            3、传递子类对象给调用者，可以看到不同子类的执行结果不同。
"""
from Polymorphism import DrugDog, ArmyDog, Person

ad = ArmyDog()
dd = DrugDog()
anpeng = Person()
anpeng.work_with_dog(ad)  # 传入不同的dog对象，执行不同的工作。
anpeng.work_with_dog(dd)
