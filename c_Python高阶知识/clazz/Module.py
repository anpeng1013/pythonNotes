# -*- coding = utf-8 -*-
# @Time : 2022/11/26 16:19
# @Author : anpeng
# @File : Module.py
# @Software : PyCharm
"""
    将模块全部导入时，该模块中的可执行代码也会在被导入位置执行一次且该模块的__name__=模块名。
    要想被导入模块中的可执行代码不运行，可将该模块中的可执行代码放入条件判断中。
"""
__all__ = ['function']

def function():
    print(__name__)
    return 'this is a function in module "Module"'

def func():
    pass

print('---the module "Module has been load--"')  # 会在导入位置被执行。
