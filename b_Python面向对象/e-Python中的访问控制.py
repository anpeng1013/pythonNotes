# -*- coding = utf-8 -*-
# @Time : 2022/11/21 17:46
# @Author : anpeng
# @File : e-Python中的访问控制.py
# @Software : PyCharm
"""
访问控制：
    * 与C++,C#,Java等语言类似，Python支持将类的属性和方法设置成特定的访问权限，但不是通过关键字区分，而是使用一套约定规则。
    * 在Python中可以通过属性以及方法是否有下划线“_”进行区分public、protected、private权限类型。

    在类的内部，所有访问权限的属性和方法都可正常使用。以下是针对类的外部访问：
        公有权限(public)：无下划线，可以直接打点进行调用。
        保护权限(protected)：单下划线，打点时不提示，但是可以正常使用。
        私有权限(private)：双划线，打点不提示，且不能强制使用。

    Python中没有严格意义的私有类型。私有类型的属性和方法在[外部调用或继承到子类中]时，实际上是被转换了，即私有属性和方法也可以被子类继承的。
        私有转换规则：__属性 --> _类名__属性  或  __方法 --> _类名__方法。
        私有强制调用：[类名.属性名] 或 [实例名.属性名] 或 [子类实例.属性名]
"""
from AccessControl import BaseClass, SubClass

# 1.外部调用保护权限
baseClass = BaseClass()
print(baseClass._protected)  # 不提示但会报弱警告

# 2.外部调用私有权限
print(baseClass._BaseClass__private, BaseClass._BaseClass__private)  # 只能强制调用，会报强警告，不推荐使用。

# 3.子类调用父类的保护权限
subClass = SubClass()
print(subClass._protected)  # 不提示但会报弱警告

# 4.子类调用父类的私有权限
print(subClass._BaseClass__private)  # 只能强制调用，会报强警告，不推荐使用。

# 5.在类的内部可以正常调用任意权限
baseClass.call_arbitrarily_permission()
