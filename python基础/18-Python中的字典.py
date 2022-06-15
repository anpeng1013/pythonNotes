"""
    字典：字典数据是以键值对形式出现，字典数据和数据顺序没有关系即字典不支持下标。后期无论数据如何变化，只需要按照对应的键的名字查找数据即可。
        创建：使用dict()函数创建字典：name=value传入关键字，使用可迭代对象，使用映射来创建字典。
              还可以直接使用大括号映射方式创建字典。
        新增
        删除
        修改
        查询
        keys
        values
"""
# 1.dict(d)--创建一个字典。
# dict字典的值可以任何数据类型，但键必须不可变的，如字符串，数字或元组。

# 通过name=value的形式传入关键字，此时key的名称必须遵循命令规则，而值value可以是任意类型
print('使用name=value形式传入关键字-----------------------------------')
print(dict(a=1, b=1))  # 这里的a相当于key的名字，所以需要遵循命名规则，
print(dict(a1_2=3))  # 任何形式的name都会被转为字符串。
# print(dict(1 = a, 2 = b)) # name标识符由字母、数字、下划线组成，但不能由数字开头
print(dict(_1=2, a2=3))

# 使用可迭代对象创建字典
print('使用可迭代对象-------------------------------------------------')
print(dict(((1, 2),)))  # 元组中单个元素时，需要在元素后面添加逗号
print(dict(((1, 2), ((1, 2), 3))))  # 第二个键为元组(1,2)
print(dict([('a', 3)]))  # 列表中单个元素时，不需要在元素后面加逗号。
# print(dict([([1, 2, 3], 1), [4, 3]])) # TypeError: unhashable type: 'list' 第一个键是列表，不符合键不可变的特点。

# 使用映射来创建字典,关键字参数会被继续传递。
print('使用映射来创建字典----------------------------------------------')
print(dict({1: 2, 'a': 110}))
print(dict({'a': 12, 2: 33}, a=89, b=0b101))
# print(dict({'124': 12}, ((1, 2), (2, 3)))) #dict函数使用映射后，后面只能使用关键字参数，不能使用可迭代对象。

# 直接使用大括号方式直接创建字典
print('使用大括号映射来创建字典-----------------------------------------')
dictVar = {'a': 12, 12: 'age'}
print(dictVar)
print(type(dictVar), 'test commit keymap')
