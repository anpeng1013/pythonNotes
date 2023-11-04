# -*- coding = utf-8 -*-
# @Time : 2022/10/23 22:06
# @Author : anpeng
# @File : 27-Python中的变量作用域.py
# @Software : PyCharm

"""
    1、Python中能够隔离变量作用域的代码段是def、clazz、lambda。

    2、if/elif/else、try/except/finally、for/while代码段不能隔离作用域，这些语句中的变量，在语句调用结束后可以继续访问。

    3、Python中的四大变量及其作用域
        Local(局部变量)：定义在def、clazz、lambda语句内部的变量，只在函数或类语句内部有效，外部无法访问。
                在函数语句中的变量，若没有被其内部函数引用形成闭包(见25-高阶函数)，则函数调用结束后会立即销毁局部变量。
        Enclosing(嵌套变量)：定义在内部函数外且在外部函数中的非全局的外部变量。若在内部函数中引用了这些变量，则形成闭包。
                            若内部函数中有同名变量，可用nonlocal关键字声明。
        global(全局变量)：定义在最外层函数和类外部的，并且在定义之后能全局访问得到的变量。若函数中有同名的全局变量，则可以global关键字声明。
        Built-in(内建变量)：Python函数库中的变量或函数。在Python中，函数也可以被认为是变量的一种。

    4.变量搜素：
        1.内部代码可以访问外部变量，但外部代码无法访问内部变量。
        2.Python查找变量的顺序：局部作用域-->嵌套作用域-->全局作用域-->内建作用域。
        3.创建的内外部变量同名时，内部的同名变量会被创建成新的局部变量。
        4.若需要同时访问内外部存在同名变量，则需要用global或nonlocal声明外部变量

    5.自由变量--global、nonlocal声明的变量
        global--在内部代码块中需要修改全局变量的值(地址值）时，必须使用global声明。
        nonlocal--在内部函数中需要外部函数中的非全局变量的值(地址值)时，必须使用nonlocal声明。

"""
# 1.Python中的只要函数体和类定义体才可以分隔作用域，而循环、分支、异常捕获代码块不分隔作用域，在其中定义的变量相当于全局变量。
# 1.1 循环结构中定义的变量，可以在循环结束后继续被访问。
i = 0
while i < 3:
    a = i
    print(a, end='\t')
    i += 1

print()
print(a)  # 2

for j in range(3):
    b = j
    print(b, end='\t')

print()
print(b)  # 2

# 1.2 分支结构中定义的变量，可以在分支结束继续被访问，前提是该分支被执行。
if a > 1:
    c = 'branch var'
else:
    d = 'branch var'

print(c)  # branch var 只能打印c，打印d会报错，因为else中的d定义语句没有被执行

# 1.3 异常捕获代码中定义的变量，可以在捕获结束后继续被访问。
try:
    try_var = 'this is a try var'
    print(b)
except:
    except_var = "this is a except var"
finally:
    finally_var = 'this is a finally var'

print(try_var)
# print(except_var) # 若没有捕获到异常，则异常处理except代码块中定义的变量不能被访问，因为没被执行。
print(finally_var)  # 不管有没有捕获到异常，finally代码块中的语句都会被执行，所以能够访问。

# 2.四大变量及其作用域
print("-" * 20 + '四大变量及其作用域' + '-' * 20)
built_in_var = 'this is a built-in var ' + str(int)  # built-in 内建变量
global_var = 'this is global var'  # global 全局变量

def var_enable_domain():
    enclosing_var = 'this is enclosing var'  # enclosing 嵌套变量

    def inner_function():
        local_var = 'this is a local var'  # local 局部变量
        print(local_var)
        print(enclosing_var)
        print(global_var)
        print(built_in_var)
        print(inner_function.__closure__)  # 内部函数引用外部非全局变量，形成闭包。

    inner_function()

var_enable_domain()

# 3.自由变量
print("-" * 20 + "自由变量" + "-" * 20)

def free_var():
    enclosing_int = 1013
    enclosing_list = ['anpeng', 'love', 'huli']

    def inner_function():
        nonlocal enclosing_int  # 数字、字符串、元组为不可变类型，想要对外部的这些变量进行修改必须进行声明，否则会创建新的局部变量
        enclosing_int = 1124
        enclosing_list.append('very much')  # 列表、集合、字典为可变类型，对这些变量内部的内容进行修改时，并没有修改变量本身的地址值，
        # 所以不需要进行声明。
        global try_var
        print(try_var)
        try_var = 18  # 函数内需要修改全局变量的值时，必须使用global进行声明，否则只会创建新的局部变量
        print(try_var)
        print(inner_function.__closure__)

    inner_function()
    print(enclosing_int)
    print(enclosing_list)

free_var()
