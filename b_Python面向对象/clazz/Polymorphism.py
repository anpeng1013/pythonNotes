# -*- coding = utf-8 -*-
# @Time : 2022/11/23 20:14
# @Author : anpeng
# @File : Polymorphism.py
# @Software : PyCharm

class Dog(object):
    def work(self):  # 父类提供统一的方法，可以是空方法，因为子类会改写。
        pass

class ArmyDog(Dog):
    def work(self):
        print('追击敌人！')

class DrugDog(Dog):
    def work(self):
        print('搜查毒品!')

class Person(object):
    def work_with_dog(self, dog):
        dog.work()
