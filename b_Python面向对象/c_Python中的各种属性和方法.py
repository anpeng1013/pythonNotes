# -*- coding = utf-8 -*-
# @Time : 2022/11/10 15:58
# @Author : anpeng
# @File : c_Python中的各种属性和方法.py
# @Software : PyCharm
"""
    python中的两种属性和三种方法：
        属性：
            类属性：直接在类中定义的 或 在类定义后通过[类名.属性名=值]添加的属性。可以通过[类名.属性名] 和 [实例名.属性]获取。
                   但是类属性只能通过[类名.类属性名=value]进行修改，用[实例名.属性=value]添加是实例属性！！！
                   *** 相当于java中的静态变量，是该类的所有实例化对象的共享数据。

            实例属性：使用[实例名.属性名=值] 或 类初始化方法中使用[self.属性名=值]添加的属性。
                    同样地，实例属性只能通过实例对象来访问和修改，类对象无法访问和修改实例属性。
                   *** 相当于java中的成员变量，是该实例对象的特有数据。

            注意：
                1、不建议在实例方法中通过 [self.实例属性名] 的方式获取非self方式添加的实例属性，因为不能保证实例对象添加了该属性。
                2、在类__init__方法中，通过[self.属性名=值]添加是实例属性，不是为类属性赋初值！！！
                3、同名的实例属性会覆盖类属性。
                4、记录的某项数据所有实例始终保持一致时，则定义为类属性。
                5、实例属性要求每个对象为其单独开辟一份空间来记录数据。而类属性会为全类共有，仅占用一份内存，更加节省内存空间。

        方法：
            实例方法：在类中定义，以self为第一个参数的方法都是实例方法。实例方法在通过实例进行调用时，Python会将调用对象作为self传入。
                    实例方法也可以通过类名进行调用，此时不会自动传递self，必须手动传入self或实例对象。
                    注意：在实例方法中可以通过[self.属性]访问实例属性，也可以通过[类名.属性]访问类属性。

            类方法：在类内部使用@classmethod来修饰的方法。类方法的第一个参数是cls，也会被自动传递，cls就是当前类的加载实体。
                    类方法和实例方法的区别，实例方法的第一个参数是实例self，而类方法的第一个参数是类cls。
                    类方法可以通过类进行调用，也可以通过实例进行调用。
                    注意：类方法中可以通过[cls.属性]访问类属性，但，访问实例属性时，必须传入实例参数，通过实例参数访问实例属性。

            静态方法：在类的内部使用@staticmethod修饰的方法。既不需要传递实例对象，也不需要传递类对象，通常作为一个工具方法使用。
                    既可以通过实例对象，也可以通过类对象进行调用。取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗。

    特殊的属性：
        __dict__：类名调用，返回类的各种成员组成的字典，包括模块名、类属性、各种方法、类文档(__doc__)等。实例名调用，返回对象的各种实例属性组成的字典。
        __doc__：可以通过类名和实例名调用，都返回类的说明文档
        __class__：实例名调用，返回实例对象所属的类。类名调用时，返回<class 'type'>,
        __base__：类名调用，返回子类的第一个直接父类
        __bases__：类名调用，返回子类的所有直接父类，因为Python支持多继承。
        __mro__：采用C3算法，也叫祖先同名方法的继承顺序，返回一个元组。子类在调用多个祖先都有的同名方法时，
                会优先调用元组中第一个遇到的祖先中的同名方法。

    特殊的方法：以双下划线开头且双下划线结尾，形如__xx__()的函数，叫做魔方函数，指的是具有特殊功能的函数
        __init__(self)：初始化对象。创建一个对象时默认被调用，不需要手动调用。其中self参数不需要开发者传递，Python解释器会自动将当前对象引用传递进去。
                    *** 其中带参数的__init__方法是为了在创建对象时添加实例属性，其定义可见Person.py文件中。

        __str__()：当使用print打印对象时，会默认输出对象的内存地址。
               如果重写__str__方法，print打印该类的实例化对象时，会输出__str__方法中return的数据。
               且对象的self也将指向return的数据。

        __del__()：当使用[del 对象名]删除对象时，Python会默认调用__del__方法，可以在其中输入一些提示信息。

"""
# 采用最新方法导入模块中类
from Computer import MateBook
from Person import Person, OverwriteStr

# 1 创建对象
anpeng = Person("anpeng")

# 2.1 通过实例名添加实例属性
anpeng.age = 26
# 2.2 通过类名添加类属性
Person.base = 'animal'  # 在后面通过类名或实例名获取该类属性时，编辑器会提示找不到该属性，但是运行后能获取到，因为一运行，就把该类属性添加成功了。

# 3.1 获取实例属性
# 3.1.1 通过[实例名.实例属性名]获取,不能用类名获取实例属性。
print(f'My name is {anpeng.name} and {anpeng.age} years old')
# 3.1.2 在实例方法中通过[self.实例属性名]获取
anpeng.hello()  # 在Person类的实例方法hello()中,通过了[self.name]的方法获取了在init方法中定义的实例属性
# 3.2 分别通过实例名和类名获取类属性的
print(Person.index, anpeng.index)

# 4.1 只能通过实例名或self修改实例属性 self修改实例名见init方法。
# 4.2 只能类名修改类属性，而不能通过实例名修改类属性
# anpeng.index = 2 (这样只会添加一个实例属性index，而不是修改了anpeng实例中保留的类属性index)
Person.base = '<class, animal>'
print(Person.base)

# 5.1 实例方法通过实例对象进行调用, 见上面3.1.2的anpeng.hello()
# 5.2 实例方法通过类名调用时，必须手动传入self或实例对象。
Person.hello(anpeng)  # hello everyone, my name is anpeng and 1

# 6.1 类方法通过实例调用--在类方法访问实例属性时，必须传入实例对象参数。
anpeng.speak(anpeng)  # this is class method and the current instance is anpeng
# 6.2 类方法通过类名调用--在类方法访问实例属性时，必须传入实例对象参数。
Person.speak(anpeng)  # 同上。

# 7.静态方法
Person.test_static_method()  # 类对象调用
anpeng.test_static_method()  # 实例对象调用

# 8.特殊属性
# 8.1 类名.__dict__ 和 实例名.__dict__
print(Person.__dict__)  # 类对象的各种成员组成的字典：模块名、类属性、各种方法、文档等
print(anpeng.__dict__)  # 只由实例对象的实例实例属性组成的字典。{'name': 'anpeng', 'age': 26}

# 8.2 __doc__ 类的说明文档
print(Person.__doc__)

# 8.3 __class__ 实例调用返回所属的类型；类调用返回type，所有类对象所属的类型是type
print(anpeng.__class__, Person.__class__)

# 8.4 __base__ 返回子类第一个直接父类
print(f'the first direct father of {MateBook} is {MateBook.__base__}')

# 8.5 __bases__ 返回子类的所有直接父类
print(f'the all direct father of {MateBook} is {MateBook.__bases__}')

# 8.6 __mro__ 返回子类的继承体系
print(MateBook.__mro__)

# 9.特殊方法[魔法方法]
# 9.1 __init__ 初始化方法。相当于java中的构造方法。带参数的__init__(self, arg)方法是为了在创建对象时添加实例属性，其定义可见Person.py文件中
print(anpeng.name)  # 获取__init__方法中添加的实例属性

# 9.2 __str__ 若不重写__str__方法，直接打印实例对象，返回的实例对象的内存地址，self也指向该地址。
# 重写__str__方法后，print打印该类的实例化对象时，会输出__str__方法中return的数据。且对象的self也将指向return的数据
test_str = OverwriteStr()
print(test_str)  # 'the function __srt__ has been overwritten' __str__方法中返回的数据。其实直接打印实例，就是在输出self对应的值。
test_str.print_self()  # the self of instance is: the function __srt__ has been overwritten

# 9.3 __del__ 当实例对象被删除时，会默认调用该方法。重写该方法，可以返回一些提示信息
