"""
    集合：存储不可重复数据的无序容器。
        创建：创建集合使用{}或者set()，但是如果要创建空集合只能使用set()，因为{}用来创建字典了。

"""
# 1.创建有数据的集合
set1 = {10, 20, 30, 10, 40, 50}  # 去重且无序
print(set1)  # {50, 20, 40, 10, 30}
set2 = set('anpeng')
str_list = list('anpeng')
str_tuple = tuple('anpeng')
print(set2, str_list, str_tuple, sep='\n')  # set(),list(),tuple()函数中传入字符串时都会拆分成一个个字符。

# 2.创建空集合
set2 = set()
print(set2, type(set2))  # set() <class 'set'>
set3 = {}
print(set3, type(set3))  # {} <class 'dict'>

# 3.集合增加数据
del set3
# add()增加单个数据
set2.add('anpeng')
set2.add(110)
print(set2)
# update()追加一个可迭代的序列
set2.update((12, 11, 10, 12))
print(set2)
set2.update('anpeng')  # "anpeng"会被拆分成单个字符追加进集合中
print(set2)

# 4.集合删除数据
# remove(),删除集合中的指定数据，如果数据不存在则报错。
set2.remove('a')
print(set2)
# discard(),删除集合中的指定数据，如果不存在也不会报错。
set2.discard('an')
# pop(),随机删除集合中的数据，并返回这个数据。
print(set2.pop())
print(set2)  # 随机删除

# 5.集合查找数据
# in 或者 not in
print('anpeng' in set2)
print('p' not in set2)
