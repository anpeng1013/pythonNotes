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

    2.函数式编程：
        定义：可以将函数作为一个参数，传入另一函数中，传入时只要需要写函数名，不用加括号。
        作用：对处理的数据可以采取不同的函数进行，可以减少函数定义，解决代码臃肿问题。

    3.内置高阶函数：
        map(function, sequence)：将传入的函数变量function作用到sequence变量的每个元素中，并将结果组成的新列表(python2)/迭代器(python3)返回。
              若有多个sequence，则并行使用来自多个sequence的参数，迭代调用function，当最短的sequence耗尽时停止，并返回一个迭代器，
              迭代器的每个元素是每次调用function的返回结果.

        reduce(function,sequence)：其中function必须有两个参数。第一次，function取序列中前两个元素进行计算，计算结果继续和序列sequence中的下一个元素做运算。
              一共进行n-1(n为序列的长度)次计算，返回第n-1次计算结果。此函数可用做：累加、累积等操作。

        filter(function, sequence)：用于过滤序列，过滤符合function函数的元素，返回一个filter可迭代对象。可以使用list()转换为list对象。

    4.闭包函数:
        定义：函数A的内部定义了另一个函数B，如果函数B引用了函数A范围内的变量，那么内部函数B就被认为是闭包(Closure)。
        判断：函数名.__closure__ 在函数是闭包函数时，返回一个cell元素；不是闭包时，返回一个None.
        作用：使函数外部能够引用函数内部定义的变量。
        注意：
            1).闭包中被内部函数引用的变量，不会因为外部函数调用结束而被释放掉，而是保存在编译后的内部函数定义体中，直到程序结束。
            2).外部函数A的返回值，可以返回内部函数B，也可以返回其他值。
            3).内部函数B只能引用外部函数A中的变量，而不能对其赋新的地址值。
                对于不可变的类型：数字、字符串、元组等同于不能修改变量的值。
                对于可变类型：列表、字典、集合，则可以修改容器内部的值，因为容器变量地址并没有被修改。


"""

# 1.体验内置函数
print(abs(-10))  # abs()返回参数的绝对值
print(round(1.2), round(1.9))  # round()对参数进行四舍五入，并返回

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

# 4.1 闭包函数作为返回值。 闭包的特点就是内部函数引用了外部函数中的变量。
def outer_function(x):  # 返回闭包函数

    def inner_function(y):
        return x + y

    print(inner_function.__closure__)  # cell对象，是闭包。
    return inner_function

var_function = outer_function(10)  # inner_function
print(var_function(13))  # 23

def outer_function1():  # 不返回闭包函数
    var1 = 'anpeng love huli'

    def inner_function1():
        print(var1)

    inner_function1()
    print(inner_function1.__closure__)  # cell对象，只要内部函数引用了外部(非全局)变量就是是闭包。
    return 'anpeng really love huli'

print(outer_function1())

# 4.2 闭包函数只能引用，而不能修改外部(非全局)变量的值。
def outer_function2():
    var2 = 0

    def inner_function2():
        var2 = 1
        print(var2)

    print(var2)
    inner_function2()
    print(var2)

outer_function2()  # 0 1 0 虽然在外部函数中定义一个变量var2，但是其不会改变外部函数中的局部变量的地址

# 4.2 闭包函数的作用
# 4.2.1 保留上次运行结果--计算均值
# 通过定义average类实现
class Average:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)

average = Average()
print(average(1), average(2), average(9))  # 1.0  1.5  4.0

# 通过闭包函数实现
def compute_average():
    series = []

    def averager(new_value):
        series.append(new_value)  # 此处并没对外部列表series变量赋新的地址值，只是对列表添加元素。
        total = sum(series)
        return total / len(series)

    return averager

average = compute_average()
print(average(4), average(8), average(3))  # 4.0  6.0  5.0

# 闭包函数实现的优化：nonlocal(自由变量)的使用
# 上面例子中，把所有值存储在历史列表中，在每次调用average时都要调用sum求和，更好的方式是
# 只存储目前的总值和元素的个数，然后使用这两个数计算均值。
def compute_average1():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1  # 因为数字是不可变类型，若不使用nonlocal声明为自由变量，则会隐式创建新的count局部变量，就没有引用外部的count形成闭包。
        total += new_value
        return total / count

    return averager

average = compute_average1()
print(average(8), average(7), average(3))  # 8.0  7.5  6.0

# 4.2.2 通过外部函数传入不同的参数，得到不同的结果。类似于4.1中的outer_function
def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [i for i in lines if keep in i]
        return filter_doc

    return the_filter

# 取出文件"25-result.txt"中含有"huli"关键字的行
filter_huli = make_filter('huli')
filter_result = filter_huli("25-result.txt")
print(filter_result)

# 取出文件"25-result.txt"中含有"anpeng"关键字的行
filter_anpeng = make_filter('anpeng')
filter_result = filter_anpeng("25-result.txt")
print(filter_result)
