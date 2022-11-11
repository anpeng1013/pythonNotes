"""
    字典：字典数据是以键值对形式出现，字典数据的存储顺序和数据存入顺序没有关系即字典不支持下标。后期无论数据如何变化，只需要按照对应的键的名字查找数据即可。
        创建：使用dict()函数创建字典：name=value传入关键字，使用可迭代对象，使用映射来创建字典。
            还可以直接使用大括号映射方式创建字典。
        新增：字典序列名[key]=value
        删除：del() 或者 del ：删除字典或删除字典指定键值对，clear()：清空字典。
        修改：字典序列名[key]=value
        查询：key查找，get(),keys(),values(),items()
        遍历：遍历keys()，values(),items()
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
nullDict = {}  # 空字典
nullDict1 = dict()  # 空字典
print(dictVar, type(nullDict), nullDict1)

# 2.字典常见操作之新增或修改数据
# 写法：字典序列名[key]=value
# 如果key存在则修改这个值，如果key不存在则新增此键值对。
dictVar['id'] = 110  # add
dictVar['a'] = 13  # amend
print(dictVar)

# 3.字典常见操作之删除数据
# del() 或者 del ：删除字典或删除字典指定键值对,如果指定key没有则会报错。
# dict.clear()：清空字典
del nullDict, nullDict1
del dictVar['a']
del (dictVar['id'])
print(dictVar)
dictVar.clear()  # 清空字典
print(dictVar)

# 4.字典常见操作之查找
# 4.1 key值查找,key存在返回对应的value，否则报错。
dictVar['name'] = 'anpeng'
dictVar['age'] = 25
dictVar['gender'] = 'male'
print(dictVar['name'])  # anpeng

# 4.2 get()函数查找
# 写法：字典序列.get(key，默认值)。如果当前查找的key不存在则返回第二个参数(默认值),如果省略第二个参数，则返回None
print(dictVar.get('name'), dictVar.get('names', 'huli'), dictVar.get('id'))  # anpeng huli None

# 4.3 keys()函数-查找键集合，可迭代对象
print(dictVar.keys())  # dict_keys(['name', 'age', 'gender'])

# 4.4 values()函数-查找值的集合
print(dictVar.values())  # dict_values(['anpeng', 25, 'male'])

# 4.5 items()函数,查找字典中所有的键值对，返回可迭代对象，里面的数据是元组。
print(dictVar.items())  # dict_items([('name', 'anpeng'), ('age', 25), ('gender', 'male')])

# 5.字典常见操作之遍历
for key in dictVar.keys():
    print(key)  # 遍历key

for value in dictVar.values():
    print(value)  # 遍历value

for item in dictVar.items():
    print(item)  # 遍历item

for key, value in dictVar.items():
    print(f'{key}={value}')  # 拆包访问key,value
