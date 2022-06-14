"""
    列表[]：存贮多个可重复的多类型数据的可变容器。
        常用操作：增删改查
            增加：append(如果追加的是序列，则将整个序列加到列表中）、
                  extend(如果追加的是序列，则将这个序列的元素逐一添加到列表中。
            删除：del指定下标或者删除整个列表、pop删除指定下标或者最后一个数据
                  remove(数据)删除指定数据，clear清空列表。
            修改：下标修改，reverse：逆置，sort(key=None,reverse=True),reverse=True降序，reverse=False升序(默认)
            查找：下标查找[]、位置查找index、个数查找len、判断存在 in、判断不存在 not in、次数查找count、列表切片。

        复制：copy()，原始数据的拷贝副本，返回的是新的内存地址。

        遍历：
            while遍历 :
                i=0
                while i<len(list):
                    print(list[i])
                    i+=1

            for  遍历：
                for i in list:
                    print(i)

        嵌套：列表中元素包含列表。

"""
# 列表常用操作之查找
# 下标查找
names = ['anpeng', 'huli', 'tom', 'huli']
print(names)
print(names[0])  # 下标查找

# 函数查找之index：返回指定数据所在位置的下标。与str中的index类似,查找数据不存在时会报错。
# 列表序列.index(数据，开始下标，结束下标).
print(names.index('huli'))
print(names.index('huli', 2))

# 函数查找之count：统计数据在当前列表中出现的次数
print('the number of huli in this name_list: ' + str(names.count('huli')))  # 2

# 函数查找之len：列表中的数据个数
print('the number of elements in this name_list: ' + str(len(names)))

# 判断存在 in 判断指定数据是否在列表序列中
print('anpeng' in names)  # True
print('hello' in names)  # False

# 判断不存在 not in 判断指定数据是否不在列表序列中
print('hello' not in names)  # True
print('anpeng' not in names)  # False

# 列表切片
temp_list = names[:4:1]
print(temp_list)

# 列表常用操作之增加
# 列表序列.append(数据)
names.append('alice')  # 追加的数据是字符串时，应该使用append
print(names)
names.append(['jack', 'bob'])
print(names)  # 如果增加的数据是一个序列，则将整个序列添加到列表中

# 列表序列.extend(数据)
names.extend('Tom')  # 字符串是一种不可变的序列，将序列的元素逐个添加到列表中
print(names)
names.extend([12, 6, 520, 10])
print(names)

# 列表序列.insert(位置下标，数据)：指定位置添加数据，其余数据顺序后移
names.insert(1, 'love')  # insert指定位置添加数据，其余数据后移。
print(names)

# 列表常用操作之删除
# del list[index]:删除指定下标的数据，默认删除整个列表
names_list = names[:6:]  # 列表的切片
print(names_list)
temp_names = names_list[:5:]
print(temp_names)
del temp_names[0]  # 删除指定下标的数据
print(temp_names)
del temp_names  # 删除整个列表
# print(temp_names) temp_names is not defined 删除后变量未定义

# pop(下标):删除指定下标的数据(默认最后一个),并返回该数据
print(names_list.pop())  # 'alice' 默认最后一个
print(names_list)
print(names_list.pop(3))  # 'tom'
print(names_list)

# remove(数据)：删除列表中的指定数据，不返回任何数据。
names.remove('alice')  # 不返回数据
print(names)

# clear()：清空列表中的数据，不返回数据
names_list.clear()
print(names_list)  # []

# 列表常用操作之修改
num_list = [1, 5, 2, 7, 9, 3]
# 1.下标修改
num_list[2] = 6
print(num_list)  # [1, 5, 6, 7, 9, 3]

# 2.逆序reverse 返回值为空
num_list.reverse()
print(num_list)  # [3, 9, 7,6,5,1]

# 3.sort 默认升序
num_list.sort()  # 默认升序
print(num_list)  # [1, 3, 5, 6, 7, 9]
num_list.sort(reverse=True)  # 降序
print(num_list)  # [9, 7, 6, 5, 3, 1]

# 列表常用操作之复制
num_list.sort()  # 默认升序
num_list1 = num_list  # 直接赋值给新变量，相当于java中的引用，只是多了一个指向原数据的指针。
print(hex(id(num_list)), hex(id(num_list1)))  # 地址相同，说明指向同一个内存区域， id函数获取对象的内存地址,该内存地址为十进制表示。
num_list[1] = 4
print(num_list, num_list1)  # 修改原变量的值，新变量的值也会被修改。

# 使用copy函数拷贝数据副本
num_list2 = num_list.copy()
print(hex(id(num_list)), hex(id(num_list2)))  # 地址不同，说明拷贝成功
num_list[1] = 3
print(num_list, num_list2)  # 修改原变量的值，新变量的值不会被改变。

# 列表常用操作之while遍历
i = 0
while i < len(num_list):
    print(num_list[i], end=' ')
    i += 1
print()

# 列表常用操作之for遍历 优先使用for遍历
for i in num_list:
    print(i, end=' ')
print()

# 列表嵌套
num_list.append(num_list2)  # 使用append函数直接将列表添加到列表中
print(num_list)
print(num_list[len(num_list) - 1][1])  # num_list[len(num_list)-1] 这相当于一个列表名，直接加[]访问子列表中数据，与多维数组类似。
