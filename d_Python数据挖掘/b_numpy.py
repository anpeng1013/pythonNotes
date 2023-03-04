# -*- coding = utf-8 -*-
# @Time : 2022/12/5 22:02
# @Author : anpeng
# @File : b_numpy.py
# @Software : PyCharm

"""
    Numpy 高效的数学运算工具
        numpy优势
            numpy介绍：
                Numpy(Numerical Python)是一个开源的Python科学数值计算库。用于快速处理任意维度的数组。
                Numpy支持常见的数组和矩阵操作。对于同样的数值计算任务，使用Numpy比直接使用Python要简洁得多。
                Numpy使用ndarray对象处理多维数组，该对象是一个快速而灵活的大数据容器。
            ndarray介绍：
                n--n个  d--dimension维度  array--数组
                ndarray的用法--numpy.array()
            ndarray与Python原生list运算效率对比：
                ndarray的计算速度比原生list快了近十倍。
            ndarray的优势：
                存储风格：
                    ndarray--元素类型相同
                    list--元素类型不同
                并行化运算：
                    ndarray--支持并行化运算(向量化运算)
                    list--不支持并行化
                底层语言：
                    ndarray--Numpy底层使用C语言编写。

        ndarray属性
            形状(shape)--dimension
            大小(size)--元素总个数
            类型(dtype)--data type
            元素大小--itemsize

        基本操作
            ndarray.方法()
                生成数组的方法
                    生成0和1的数组:
                        np.zeros()和np.ones()
                    从现有数组生成:
                        np.array()、 np.copy()、 np.asarray()
                        深拷贝：完全复制一份源数据到新的内存位置，叫深拷贝，新数据不会因为源数据的变化而变化。
                        浅拷贝：只是增加了一个源数据的索引，新数据会跟随源数据的变化。
                        1、若现有数组为原生list,则np.array()、np.copy()、np.asarray()都是深拷贝
                        2、若现有数组为ndarray,则np.array()、np.copy()为深拷贝，np.asarray()为浅拷贝。
                    生成固定范围的数组：
                        np.linspace(a, b, n)--[a, b] 等距离化为n份
                        np.arange(a, b, c)-- [a, b) c为步长
                    生成随机数组：
                        np.random模块---分布状况(直方图)
                        均匀分布：uniform distribution，是概率统计中的重要分布之一，表示可能性相等的分布。但均匀分布在自然情况下极为罕见。
                            * np.random.rand(a, b)  返回a行b列的内一组均匀分布在[0,1)之间的float数
                            * np.random.uniform(low, high, size) 返回[low, high)内形状为size的均匀分布的float数。
                            * np.random.randint(low, high, size) 返回[low, high)内形状为size的均匀分布的int数。
                        正态分布：也叫高斯分布，是具有两个参数的连续型随机变量的分布。
                                其中，参数标准差越大，数据分布也平坦，标准差越小，数据分布越集中，集中在均值附近。
                            * np.random.randn(a, b)  返回a行b列的一组标准分布的float数
                            * np.random.normal(loc=0.0, scale=1.0, size) loc为期望，scale为标准差，size是形状
                            * np.random.standard_normal(size) 返回指定形状的标准正态分布的数组。
                数组的索引、切片
                形状修改
                类型修改
                数组去重
            numpy.函数名()
        ndarray运算
            逻辑运算
            统计运算
            数组运算
        合并、分割、IO操作、数据处理
"""
import numpy as np
import matplotlib.pyplot as plt

# 1.numpy中的ndarray的用法--numpy.array()
scores = np.array([[80, 89, 86, 67, 79],
                   [78, 97, 89, 67, 81],
                   [90, 94, 78, 67, 74],
                   [91, 91, 90, 67, 69],
                   [76, 87, 75, 67, 86],
                   [70, 79, 84, 67, 84],
                   [94, 92, 93, 67, 64],
                   [86, 85, 83, 67, 80]])
print(type(scores))  # <class 'numpy.ndarray'>
print(scores)

# 2.ndarray的属性
# 形状shape
print(scores.shape)  # (8, 5) 8行5列
# 大小size
print(scores.size)  # 8*5=40个元素
# 类型dtype
print(scores.dtype)  # int32
# 元素字节数
print(scores.itemsize)  # 4 -- 32位整数占4字节
# 创建数组时指定类型
var_array = np.array([i + 0.6 for i in range(10)], dtype=np.int32)
print(var_array)  # 将浮点数指定为整数时，会直接去掉小数点后面的数 [0 1 2 3 4 5 6 7 8 9]

# 3.基本操作
# 3.1 生成数组的方法
# 3.1.1 生成0和1数组--np.zeros()和np.ones()
print(np.zeros(shape=(3, 4), dtype=np.int32))
print(np.ones(shape=(3, 5), dtype=np.int32))
# 3.1.2 从现有数组生成--np.array()、 np.copy()、 np.asarray()
print('---------现有数组为原生list------------')
var_list = [[1, 2, 3] for i in range(3)]
array1 = np.array(var_list)
array2 = np.copy(var_list)
array3 = np.asarray(var_list)
var_list[2][2] = 0
print(var_list, array1, array2, array3, sep='\n')  # 原生list时，三者都是深拷贝
print('---------现有数组为ndarray------------')
var_ndarray = np.array([[1, 2, 3] for i in range(3)])
array1 = np.array(var_ndarray)
array2 = np.copy(var_ndarray)
array3 = np.asarray(var_ndarray)
var_ndarray[2][2] = 0
print(var_ndarray, array1, array2, array3, sep='\n')  # ndarray时，array和copy是深拷贝，asarray是浅拷贝。
# 3.1.3 生成固定范围的数组
print(np.linspace(0, 20, 5, dtype=np.int32))  # 闭区间，若不指定为int，即使给出参数能划分出int数组，也会默认是float
print(np.arange(0, 21, 5))  # 和range类似，左闭右开区间
# 3.1.4 生成随机数组
# 均匀分布
print(np.random.rand(4, 6))  # 4行6列 范围[0,1)
print(np.random.uniform(1, 3, (3, 4)))  # 3行4列 范围[1, 3) 默认为float  常用
print(np.random.randint(1, 3, (3, 4)))  # 3行4列 范围[1, 3) 默认为int
# 展示均匀分布
data = np.random.uniform(-1, 1, 1000000)
plt.figure(figsize=(20, 8), dpi=100)
plt.hist(data, 100)
plt.show()
# 正态分布
print(np.random.randn(4, 5))  # 返回在0附近的 4行5列个 符合标准正态分布的float数。
print(np.random.standard_normal((4, 5)))  # 与np.random.randn效果一样。
print(np.random.normal(2, 1, (4, 4)))  # 返回在2附近的 4行4列个 标准为1的正态分布float数 常用
# 展示正态分布
data = np.random.normal(1.75, 1, 10000000)
plt.figure(figsize=(20, 8), dpi=100)
plt.hist(data, 1000)
plt.show()
