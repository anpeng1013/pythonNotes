# -*- coding =utf-8 -*-
# @Time : 2022/8/9 21:45
# @Author : anpeng
# @File :25-Python中的高阶函数.py
# @Software: PyCharm

"""
    高阶函数：把函数作为参数传入，这样的函数称为高阶函数，高阶函数是函数式编程的体现。
    1.体验内置函数：
        abs()函数可以完成对数字求绝对值计算。
        round()函数可以完成对数字的四舍五入计算
    2.内置高阶函数：
        map(function, sequence)：将传入的函数变量function作用到sequence变量的每个元素中，并将结果组成的新列表(python2)/迭代器(python3)返回。
              若有多个sequence，则并行使用来自多个sequence的参数，迭代调用function，当最短的sequence耗尽时停止，并返回一个迭代器，
              迭代器的每个元素是每次调用function的返回结果.

        reduce(function,sequence)：其中function必须有两个参数。第一次，function取序列中前两个元素进行计算，计算结果继续和序列sequence中的下一个元素做运算。
              一共进行n-1(n为序列的长度)次计算，返回第n-1次计算结果。此函数可用做：累加、累积等操作。

        filter(function, sequence)：用于过滤序列，过滤符合function函数的元素，返回一个filter可迭代对象。可以使用list()转换为list对象。

    3.闭包函数:
        定义：当一个函数的返回值是另一个函数，而返回的那个函数如果调用了其父函数内部的其它变量，如果返回的的这个函数在外部被执行，就产生了闭包。
        作用：使函数外部能够调用函数内部定义的变量。
        注意：闭包中被内部函数引用的变量，不会因为外部函数结束而被释放掉，而是一直存在内存中，直到内部函数调用结束。

        判断是否为闭包函数：
        函数名.__closure__ 在函数是闭包函数时，返回一个cell元素；不是闭包时，返回一个None.

"""

# 1.体验内置函数
print(abs(-10))
print(round(1.2), round(1.9))

# 2.体验高阶函数（函数式编程）
# 需求：要求对数字进行任意操作后进行计算
# 方法1:只能对传入数字进行取绝对值后进行加法计算

def add_num1(a, b):
    return abs(a) + abs(b)

print(1, 2)

# 方法2：可以对传入数字进行任意操作后进行加法计算

def add_num2(a, b, function):  # 函数和类定义的前后都要空两行。
    return function(a) + function(b)

print(add_num2(1.2, 1.9, round))  # 函数作为参数传入时，只需要写函数名，不用写括号。
# 函数式编程大量使用函数，减少了代码的重复，因此代码比较短，开发速度较快。

# 3.内置高阶函数
# 3.1 map(function, sequence)，将传入的函数变量function作用到sequence变量的每个元素中，并将结果组成的新列表(python2)/迭代器(python3)返回。
# 若有多个sequence，则并行使用来自多个sequence的参数，迭代调用function，当最短的sequence耗尽时停止，并返回一个迭代器，迭代器的每个元素是每次调用function的返回结果
# 需求：计算list1序列中各个数字的平方。
list1 = [i for i in range(1, 6, 1)]  # 列表表达式

def square(x):
    return x ** 2

result = map(square, list1)
print(result)  # <map object at 0x000001FC0CF08190> 直接打印函数名，输入的函数的内存地址。
print(list(result))  # [1, 4, 9, 16, 25]

# 3.2 reduce(function,sequence)，其中function必须有两个参数。每次function计算的结果继续和序列sequence的下一个元素做累计算。
# 需求：计算list2序列中各个数字的累加和
import functools

list2 = [i for i in range(1, 6, 1)]

def cumulate(arg1, arg2):
    return arg1 + arg2

print(functools.reduce(cumulate, list2))

# 3.3 filter(function, sequence)，用于过滤序列，过滤符合function函数的元素，返回一个filter可迭代对象。可以使用list()转换为list对象。
list3 = [i for i in range(1, 11, 1)]

def select(arg):
    return arg % 2 == 0

result = filter(select, list3)
print(result)  # <filter object at 0x0000029AEF059700> 返回的可迭代对象filter的内存地址
# print(list(result)) # 将迭代器filter转换为列表，就是逐个访问迭代器中的元素，并加入到列表中。
for i in result:  # 迭代器不管是for循环遍历操作，还是list()数据类型转换为列表操作，都会访问一次数据，访问一次后，迭代器中的数据索引消失，无法再获取值。
    # 若要for循环遍历filter对象，则需注释上一行list转换为列表的代码。
    print(i, end='\t')
print()

# 4.1 闭包函数实例
def outer_function():
    var = 'anpeng'

    def inner_function():
        print(var)

    return inner_function

var_function = outer_function()  # inner_function
var_function()

# 4.2 判断是否为闭包函数---函数名.__closure__ 在函数是闭包函数时，返回一个cell元素；不是闭包时，返回一个None.
name = 'anpeng love huli'

def outer_function2():
    def inner_function2():
        print(name)

    return inner_function2

var_function2 = outer_function2()
print(var_function2())  # None
print(var_function.__closure__)  # (<cell at 0x000002227F1BFFA0: str object at 0x000002227F1D1370>,)
