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
expression = lambda: 100

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

# 5.lambda的经典面试题
result = [lambda x: x + i for i in range(10)]
print(result[0](10))
