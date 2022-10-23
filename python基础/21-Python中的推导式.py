"""
    # 列表推导式：list_var=[i for i in range(10)] 用一个表达式创建一个有规律的列表或控制一个有规律的列表。列表推导式又叫列表生成式
    # 字典推导式：dict_var={i : i**2 for i in range(10)} 快速合并列表为字典或提取字典中目标数据。
    # 集合推导式：set_var={i**2 for in [1, 2, 5, 3] } 注意集合有数据去重功能
    # 元组 ?  :   注意！使用tuple_var=(i for i in range(10))这种形式得到的是生成器，不是元组推导式
"""
# 1.列表推导式
# 需求：创建一个0-10的列表
# 1.1 while循环实现

list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

# 1.2 for循环实现
list2 = []
for j in range(10):
    list2.append(j)
print(list2)

# 1.3 列表推导式实现
list3 = [i for i in range(10)]
print(list3)

# 2.带if的列表推导式
# 创建0-10的偶数列表
# 2.1 range()步长实现
print([i for i in range(0, 10, 2)])

# 2.2 if实现
print([i for i in range(10) if i % 2 == 0])

# 3.多个for循环的列表推导式
# for 嵌套
list1 = []
for i in range(1, 3):
    for j in range(3):
        list1.append((i, j))
print(list1)
# 前面的for是外层循环，后面的for是内层循环。
print([(i, j) for i in range(1, 3) for j in range(3)])

# 4.字典推导式
# 4.1 创建一个字典：字典key是1-5的数字，value是这个数字的2次方
dict1 = {i: i ** 2 for i in range(1, 6)}
print(dict1)
dict2 = {i: 'anpeng' for i in range(3)}
print(dict2)

# 4.2 将两个列表合并为一个字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict3 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict3)

# 4.3 提取字典中的目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'LENOVO': 199, 'ACER': 99}
# 需求：提取上述电脑数量大于等于200的字典数据
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)

# 5.集合推导式
# 需求：创建一个集合，数据为下方列表的2次方
list1 = [1, 5, 9, 5]
set1 = {i ** 2 for i in list1}
print(set1)  # {81, 1, 25} 集合去重且无序。

# 6.元组生成器
# 需求：创建一个元组，数据为1-100中的素数
from math import sqrt

def is_prime(x):
    if 0 < x < 4:
        return True
    else:
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

print(is_prime(73))
tuple_var = tuple(i for i in range(1, 101) if is_prime(i))
print(tuple_var)
