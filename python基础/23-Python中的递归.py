# -*- coding =utf-8 -*-
# @Time : 2022/7/25 16:46
# @Author : anpeng
# @File :23-Python中的递归.py
# @Software: PyCharm

"""
    递归的特点：
        1.函数内部调用自己
        2.必须要出口。
"""


# 1.累加程序--用递归实现
def add_num(num):
    if num == 1:
        return 1  # 函数出口，如果没有出口会报错：超出最大递归深度：996
    else:
        return num + add_num(num - 1)  # 调用自己


print(add_num(100))  # 5050


# 2.快速排序--用递归实现
def quick_sort(num_list):
    if len(num_list) < 2:
        return num_list
    else:
        high = len(num_list) - 1
        mid = high // 2  # //为整除，无小数，/为浮点除法，有小数
        left = []
        right = []
        mid_value = num_list.pop(mid)  # 选了基准元素后，一定要在遍历这数组前删除这个元素，否则
        # 当第一轮比较大小时，若right数组没有元素，left数组和原数组一样，陷入死循环
        for i in range(len(num_list)):
            if num_list[i] > mid_value:
                right.append(num_list[i])
            else:
                left.append(num_list[i])
        return quick_sort(left) + [mid_value] + quick_sort(right)


arg_list = [3, 5, 9, 23, 8, 6]
print(quick_sort(arg_list))  # [3, 5, 6, 8, 9, 23]
