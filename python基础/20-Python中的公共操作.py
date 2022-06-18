"""
    公共操作：
        * 运算符：
            +：合并，用于字符串、列表、元组
            *：乘法，用于字符串，列表，元组
            in：元素是否存在，字符串，列表，元组，字典
            not in：元素是否不存在，字符串，列表，元组，字典。

        * 公共方法：
        * 容器类型转换：
"""
# 1.运算符之+：合并
print('anpeng' + ' love huli.')  # 合并字符串
print((1, 2) + (3, 6))  # 合并元组
print(['anpeng', 'hello'] + ['Tom', 'alice'])  # 合并列表

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
