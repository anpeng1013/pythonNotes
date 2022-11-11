# -*- coding =utf-8 -*-
# @Time : 2022/8/9 19:41
# @Author : anpeng
# @File :24-Python中的lambda表达式.py
# @Software: PyCharm

"""
场景：如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化
语法：lambda 参数列表：表达式
注意：lambda表达式的参数可有可无，函数的参数在lambda表达式中完全适用
    lambda表达式能接收任何数量的参数但只能返回一个表达式的值

lambda经典面试题：
    result=[lambda x: x+i for i in range(10)]
    print(result[0](10)) # 结果为 19
"""


# 1.快速体验
# 函数
def function():
    return 200


print(function)
print(function())

# lambda表达式 匿名函数
expression = lambda: 100  # 正常情况下，不推荐将lambda表示式赋值给一个变量

print(expression)  # 匿名函数的内存地址
print(expression())  # 匿名函数返回值100

# 2.例子：计算a + b
# 函数实现
def add(a, b):
    return a + b

result = add(1, 2)
print(result)

# lambda实现
expression = lambda a, b: a + b
print(expression(2, 5))

# 3.lambda参数形式 与函数参数形式相同
# 无参数
expression = lambda: 100
print(expression())
# 一个参数
expression = lambda a: a
print(expression(14))
# 默认参数
expression = lambda a, b, c=18: a + b + c
print(expression(1, 1))
# 可变参数
expression = lambda *args: args
print(expression(1, 2, 3))
expression = lambda **kwargs: kwargs
print(expression(name='anpeng', age=20))

# 4.lambda应用
# 带判断的lambda
expression = lambda a, b: a if a > b else b
print(expression(3, 7))
# 列表数据按字典key的值排序
students = [
    {'name': 'jack', 'age': 22},
    {'name': 'anpeng', 'age': 25},
    {'name': 'huli', 'age': 20},
    {'name': 'Tom', 'age': 18}
]
# 按name值升序排序
students.sort(key=lambda x: x['name'])  # sort函数参照16-Python中的列表中sort函数。
print(students)

# 按age的值降序排序
students.sort(key=lambda x: x['age'], reverse=True)
print(students)

# 5.lambda的经典面试题。
result = [lambda x: x + i for i in range(10)]  # 结合了变量作用域、列表推导式、lambda匿名函数和函数运行机制的题目
"""
    1.首先，这是一个列表推导式，生成的是lambda匿名函数列表，即列表中的元素都是匿名函数。
    2.当result = [lambda x: x + i for i in range(10)]语句执行时，相当于在result列表中定义了十个匿名函数。
    3.Python中函数运行机制：遇到函数定义，直接将函数加载到内存而不会执行函数代码，只有当函数调用才会执行函数代码。
    4.所以，这里只是生成了匿名函数的列表而不会实际执行函数代码，也就是说暂时没有生成结果。函数内部的i依然变量，并没有具体的值，因为函数没有执行。
        只有当函数调用时才会实际执行函数代码，result[0]提取列表中的第一个匿名函数，在后面加上括号并传入参数result[0](10)才会实际调用函数，
        此时开始执行函数代码，才会去找对应的变量的值。
    5.Python中变量的作用域：本地作用域（local）-> 嵌套作用域（enclosing）-> 全局作用域（global）-> 内建作用域（built-in）
    6.Python中循环、分支、异常捕获代码块中定义的变量，在被调用之后的全局依旧能被访问，相当于全局变量。所以在列表推导式中的for循环结束后，
        i的变量为9,列表中定义的十个lambda匿名函数中的i此时还没被赋值，只要当函数被调用时，才会去找变量i的值。
"""
for i in range(len(result)):
    print(result[i](10), end='\t')  # 全是19

# 若要实现每个函数中的i呈现递增效果，可以在lambda表达式的参数中，使用默认参数，在构建函数的过程中，将i值赋值进去。
print()
result = [lambda x, i=i: x + i for i in range(10)]
for i in range(len(result)):
    print(result[i](10), end='\t')
