# 变量就是一个存储数据的内存地址单元的名字而已。
# 定义变量
# 变量名=值（变量名是自定义，需要满足标识符的命令规则）

# 标识符
# 命令规则：
# 由数字、字母、下划线组成
# 不能数字开头
# 不能使用内嵌关键字
# 严格区分大小写

# 关键字
# False none True and as assert break class
# continue def del  elif else except finally for
# from global if import in is lambda nonlocal
# not or pass raise return try while with yield

print("关键字就是上面这些了")
# 命令习惯
# 见名知义
# 大驼峰：即每个单词首字母都大写，例如：MyName.
# 小驼峰：第二个（含）以后的单词首字母大写，例如：myName.
# 下划线：例如：my_name.

"""
1.定义变量
    语法：变量名=值
2.使用变量
    变量必须先定义后使用
3.看变量的特点
"""

# 定义变量：存储数据anpeng
my_name = 'anpeng'  # 下划线方式
print(my_name)

# 定义变量：存储数据中山大学
schoolName = '中山大学'  # 小驼峰方式
print(schoolName)

# 定义变量：存储数据1013
MyBirthday = 1013  # 大駝峰方式
print(MyBirthday)

# 同时定义多个变量
a, b = 12, 56  # 定义多个变量
print(a, b)
