# noinspection LanguageDetectionInspection
"""
    元组()：存贮多个可重复的多类型数据的不可变容器。
        特点：定义元组使用小括号，且逗号隔开各个数据，数据可以是不同的数据类型。
              如果元组的数据只有一个，那么这个数据后面应该添加逗号，否则会忽略括号，数据数据类型是唯一的
              这个数据的数据类型。

"""
# 1.元组的定义
tuple1 = (1, 2, 2, 'anpeng')  # 元组数据可重复,可不同类型
tuple2 = (1,)  # 单个数据应该加逗号
tuple3 = ((1))  # 只有一个数据时，多重括号都会被忽略
tuple4 = ([1])  # 元组中的元素是任意类型。
print(type(tuple1), type(tuple2), type(tuple3), type(tuple4))  # <class 'tuple'> <class 'tuple'> <class 'int'> <class 'list'>

# 2.元组的查找(元组不支持修改，只查找)
# 2.1 元组查找之下标索引
print(tuple1[3])

# 2.2 元组查找之index() # 返回元素的下标，与字符串和列表的index函数功能用法相同，元素不存在时会报错。
print(tuple1.index('anpeng'))  # 3
print(tuple1.index(2, 2))  # 可以省略结束下标 2

# 2.3 元组查找之count() # 返回指定数据出现的次数
print(f'the number of 2 in this tuple is: {tuple1.count(2)}')  # 2

# 2.4 元组查找之len() # 返回元组的元素个数
print(len(tuple1))  # 4

# 3.元组的修改
# 元组内的直接数据如果修改，则立即报错！ 但是，如果元组里面有列表，修改列表中的数据则是可以的。慎用！
del tuple2, tuple3, tuple4
tuple2 = (1, 2, 3, ['anpeng'])
tuple2[3][0] = 'anpeng love huli'
print(tuple2) # 元组中的列表数据是可以修改的
