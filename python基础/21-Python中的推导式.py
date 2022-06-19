"""
    # 列表推导式：用一个表达式创建一个有规律的列表或控制一个有规律的列表。列表推导式又叫列表生成式

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
