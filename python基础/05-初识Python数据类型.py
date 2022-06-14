"""
数据类型分类：
    数值型：int（整型）、float（浮点型）
    布尔型：True（真）、False（假）
    字符串：str--单引号和双引号都可以

    列表：list--类似于数组
    元组：tuple--类似于不可修改的数组
    集合：set--无重复元素的集合
    字典：dic--无重复键值对的集合（值可以重复，键不能重复）
"""
# 检测数据类型 type()
# int--整型
var1 = 1

# float-浮点型
var2 = 1.1
print(type(var1))
print(type(var2))

# str--字符串，特点：单引号和双引号都可以
var3 = "hello world"
print(type(var3))

# bool--布尔型，通常作判断使用，两个取值True和False
var4 = True  # True和False首字母必须大写。
print(type(var4))

# list--列表，类似于数组。
var5 = [1, 2, 3]
print(type(var5))

# tuple--元组，类似于不改变的数组
var6 = (10, 20, 30)
print(type(var6))

# set--集合，无重复元素的集合
var7 = {'a', 'b', 'c'}
print(type(var7))

# dict--字典，无重复键值对元素的集合
var8 = {'name': "anpeng", 'age': 25}
print(type(var8))

