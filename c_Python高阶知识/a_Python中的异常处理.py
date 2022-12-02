# -*- coding = utf-8 -*-
# @Time : 2022/11/24 15:41
# @Author : anpeng
# @File : a_Python中的异常处理.py
# @Software : PyCharm
"""
    1、了解异常：程序执行过程中，解释器检测到语法错误，导致程序中止退出的情况。这就是所谓的异常。
        常见的异常：以r模式打开一个不存在的文件，会报[FileNotFoundError]异常。
                 未定义而先使用变量，会报[NameError]异常。
                 除数为零，会报[ZeroDivisionError]异常。

    2、捕获异常：
        try:
            可能发生错误的代码
        except Exception as e： # as e 作用是打印异常信息
            print(e)
            出现异常后的处理代码

        注意：1、不能只写except，会报[do not use bare 'except']警告。
             2、Exception是各种异常类的顶级类，起码应该写个Exception，但只写Exception会报[Too broad exception clause]弱警告。
             5、如果尝试执行代码的异常类型和指定捕获的异常类型不一致，则无法捕获异常。
             6、一般try下方只放一行尝试执行的代码。

        捕获未知异常：若不知道会出何种异常且不想报弱警告，可以写[except Exception as e:]，并且需要在异常处理代码中使用异常e。
        捕获指定异常：上述写法为捕获未知异常，将Exception换成NameError等其他具体子类异常，则可以捕获指定异常。
        捕获多个异常：当捕获多个异常时，把要捕获的异常类型名字放在except后，并使用元组方式进行书写。只会捕获遇到的第一个异常。

    3、异常的else
        try:
            可能发生错误的代码。
        except Exception as e： # as e 作用是打印异常信息
            print(e)
            出现异常后的处理代码。
        else：
            没有异常要执行的代码。

    4、异常finally
        try:
            可能发生错误的代码
        except Exception as e： # as e 作用是打印异常信息
            print(e)
            出现异常后的处理代码
        else：
            没有异常时要执行的代码
        finally：
            无论是否有异常都要执行的代码。

    5、异常传递[嵌套]
        try:
            执行代码
            try：
                执行代码
            except：
                异常处理
        except：
            异常处理

    6、自定义异常
        步骤：
            1、定义异常：自定义的异常类必须继承Exception, 同时需要改写__str__方法(设置抛出异常的描述信息)
            2、抛出异常：使用raise关键抛出异常对象--raise 异常类名(参数)
            3、捕获异常：使用except捕获异常。
"""

# 1.捕获未知异常--尝试以r模式打开文件，出现异常时，打印异常信息
from CustomException import ShortInputException

try:
    file = open('test.txt', 'r')
except Exception as e:
    print(e)

# 2.捕获指定异常
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)

# 3.捕获多个异常
try:
    file = open('test.txt', 'r')
    result = 5 / 0
except (ZeroDivisionError, FileNotFoundError) as exception:
    print(exception)

# 4.没有异常时执行else中的代码
try:
    result = 10 // 3  # 整除
except Exception as e:
    print(e)
else:
    print(result)

# 5.finally子句：无论有无异常都要执行的代码
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)
else:
    pass  # 有异常后，else中的代码不会被执行
finally:
    print('this is finally cause.')

# 6.自定义异常
try:
    content = input('请输入密码：')
    if len(content) < 3:
        raise ShortInputException(len(content), 3)
except Exception as result:
    print(result)
else:
    print("密码输入完成")
