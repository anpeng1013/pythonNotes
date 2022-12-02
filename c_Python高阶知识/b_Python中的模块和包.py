# -*- coding = utf-8 -*-
# @Time : 2022/11/25 20:25
# @Author : anpeng
# @File : b_Python中的模块和包.py
# @Software : PyCharm
"""
Python的模块和包
    模块(module)：是一个python文件，以.py结尾，包含了函数定义，类和变量，也能包含可执行代码。
    包：包将有联系的模块文件组织在一起，即放在同一文件夹下，创建包时，会自动生成__init__.py文件，用于说明它是一个包，而不是文件夹，可以被别的包调用。

    在不同包、或者不同模块之间相互导入：
        原始方法：被导入的包名、模块名、类名、函数名、变量名等需要符合标识符命名规则(字母、数字、下划线组成，尤其是不能以数字开头),否则导入时识别不了。
            1、同包中的不同模块之间：
                from 模块名 import 类名/函数名/变量名
            2、不同包中的不同模块之间：
                1) 先导入模块 -- from 包名 import 模块名
                   再调用模块 -- 模块名.函数()/类名()/变量名
                2) 直接引入不同包的某一模块中的函数或类或变量
                   from 包名.模块名 import 类名/函数名/变量名
                   直接调用函数()等。
                3) 使用[from 包名 import *]时，必须在__init__.py文件添加__all__=['modulename']，控制允许导入的模块列表。

        最新方法：在(file–>setting–>project:server–>project structure)中包设置为source文件，包名变蓝。
                只要文件夹变蓝后，就可以在其它任意位置直接导入其中的source文件(模块)，使用方法如下：
                1) 直接引用需要使用的模块或函数或类或变量，报错后按alt+enter会自动补全。
                2) from 模块名 import 函数名/类名/变量 -- 直接调用函数名()/类名()/变量名
                3) import 模块名 -- 间接调用模块名.函数名()/类名()/变量名

    若模块名或函数名太长可以设置别名：设置别名后只能使用别名，而不能使用原来的名字。
        import 模块名 as 别名
        from 模块名 import 功能名 as 别名
        例如：import numpy as np

    导入模块[import 模块名]和导入功能[from 模块名 import 函数/类/变量]的区别：
        导入模块[import 模块名]：会将模块的所有内容导入，且会运行其中的可执行代码。
        导入功能[from 模块名 import 功能]：只导入指定功能，不会运行模块中的可执行代码。

    导入模块中的所有功能(函数、类、变量)：[from 模块名 import *] 之后直接使用功能名调用，从而不再用模块名.功能名

    模块定位顺序：
        1、当前模块所在的目录
        2、如果不在当前目录，Python则会搜索环境变量PYTHONPATH下的每个目录。
        3、如果以上都找不到，Python会查看默认路径。UNIX下，默认路径一般为/usr/local/lib/python

        注意：
            1、自己的文件名不要和已有模块名重复，否则导致模块功能无法使用。
            2、使用[from 模块 import 功能]的时候，如果功能名字重复，调用到的是最后定义的或导入的功能。
            3、变量名也覆盖模块名[功能名]等。

    模块属性：
        __name__：模块标识符。以本模块为启动模块时，本模块中的__name__等于__main__，以其他模块为启动模块时，当前模块中的__name__等于当前模块名。
        __all__：如果一个模块文件中有__all__变量，当使用[from xx import *]导入时，只能导入这个列表中的元素，也就是功能。
"""
import math
from Washer import Washer
import time as t
from Module import *

# 1.导入系统模块
print(math.sqrt(16))

# 2.导入自定义模块
haier = Washer('haier')
haier.wash()

# 3.设置并使用模块别名
t.sleep(1)  # 延迟一秒
print("hello anpeng")

# 4.模块属性__name__
# 4.1 当前模块为启动模块，本模块的__name__=__main__
print(__name__)

# 4.2 当前模块为启动，被导入模块的__name__=模块名
print(function())

# 5.模块属性__all__
# func()函数不在all属性中，不能调用。
