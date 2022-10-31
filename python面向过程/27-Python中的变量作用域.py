# -*- coding = utf-8 -*-
# @Time : 2022/10/23 22:06
# @Author : anpeng
# @File : 27-Python中的变量作用域.py
# @Software : PyCharm

"""
1、内部代码可以访问外部变量。
2、Python不要求声明变量，但是假定在函数定义体中赋值的变量时局部变量。
"""
global_var = 'this is global var'

def var_enable_domain():
    inner_var = 'this is inner var'
    print(global_var)
    print(inner_var)

var_enable_domain()
