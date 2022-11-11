"""
    公共操作：
        * 运算符：
            +：合并，用于字符串、列表、元组
            *：乘法，用于字符串，列表，元组
            in：元素是否存在，字符串，列表，元组，字典
            not in：元素是否不存在，字符串，列表，元组，字典。

        * 公共方法：
            len()：计算容器中的元素个数
            del或del():删除容器或删除指定字典指定的键值对
            max()：返回容器中元素最大值
            min()：返回容器中元素最小值
            range(start,end,step)：生产从start到end的数字，步长为step，供for循环使用
            enumerate()：用于将一个可遍历的数据对象(如列表，元组或字符串)组合成一个索引序列，同时列出数据和数据下标，一般用在for循环中。

        * 容器类型转换：
            可以参见第09-数据类型转换。
"""
# 1.运算符之+：合并
print('anpeng' + ' love huli.')  # 合并字符串
print((1, 2) + (3, 6))  # 合并元组
print(['anpeng', 'hello'] + ['Tom', 'alice'])  # 合并列表
# print({1, 2, 3} + {'anpeng', 'hello'})  # +号不能合并集合

# 2.运算符之*：乘法
print('anpeng' * 3)
print('-' * 10)
print((1, 2) * 5)
print([1, 2, 3] * 2)

# 3.运算符之in和not in：判断是否存在。
print('an' in 'anpeng')
print('an' not in 'anpeng')
print(12 in (23, 12, 24))
print(12 not in (23, 12, 24))
print(12 in [23, 12, 24])
print(12 not in [23, 12, 24])
print('name' in {'name': 'anpeng', 'age': 25})
print('names' not in {'name': 'anpeng', 'age': 25})
print(type({'name': 'anpeng', 'age': 25}.keys()))  # <clazz 'dict_keys'> 是字典关键字类型，不是list或tuple

# 4.公共方法之len()
str1 = 'anpeng'
list1 = [1, 2, 3, 4, 5, 6]
tuple1 = (10, 20, 30, 40, 50, 60)
set1 = {'anpeng', 'set', 'tom', 'time', 'huli'}
dict1 = {'name': 'anpeng', 'age': 25, 'school': 'sun-yat san university'}
print(len(str1), len(list1), len(list1), len(set1), len(dict1))  # 字典中统计的是键值对个数

# 5.公共方法之del
# del 目标 或del(目标)
# 注意：只有列表和字典支持元素项删除。
del str1, list1[0], tuple1, set1, dict1['school']
print(list1, dict1, sep='\n')

# 6.公共方法之max和min
print(max(list1), min(list1))

# 7.公共方法之range(start, end, step) 三个参数与切片类似,不包含结束位。
# 左闭右开区间取数，步长为step，供for循环使用
for i in range(1, 10, 1):
    print(i, end=' ')
print()
for i in range(10):  # range(0,10,1)可以简化为range(10):默认从0开始，默认间隔为1
    print(i, end=' ')
print()

# 8.公共方法之enumerate，用于将一个可遍历的数据对象(如列表，元组或字符串)组合成一个索引序列，同时列出数据和数据下标，一般用在for循环中。
# 语法：enumerate(可遍历对象, start=0)
# 注意：start参数用来设置遍历数据的下标的起始值，默认为0
str1 = 'anpeng'
for i in enumerate(str1):
    print(i,
          end=' ')  # (0, 'a') (1, 'n') (2, 'p') (3, 'e') (4, 'n') (5, 'g')
print()
