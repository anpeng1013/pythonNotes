# -*- coding = utf-8 -*-
# @Time : 2022/12/2 17:30
# @Author : anpeng
# @File : a_matplotlib.py
# @Software : PyCharm
"""
    matplotlib--用于画图的Python库，是数据可视化的工具。[给自己看的数据可视化]
        mat  -- 矩阵[matrix]
        plot -- 图表
        lib  -- 库[library]

    更多数据可视化工具：JS库--国外D3和国内echarts。[给别人看的数据可视化]
        奥卡姆剃刀原理：如无必要勿增实体。

    matplotlib的三层结构：
        容器层：主要有Canvas、Figure、Axes组成。
            Canvas是位于底层的系统层，在绘图的过程中充当画板的角色，即放置画布(Figure)的工具。
            Figure是Canvas上方的第一层，也是需要用户来操作的应用层的第一层，在绘图过程中充当画布的角色。
            Axes是应用层的第二层，在绘图过程中相当于画布上的绘图区的角色。
                * Figure：是指整个图形(可以通过plt.figure()设置画布的大小的分辨率等)
                * Axes(坐标系)：数据的绘图区域
                * Axis(坐标轴)：坐标系中的一条轴，包含大小限制、刻度和刻度标签。
            特点：
                * 一个figure(画布)可以包含多个axes(坐标系/绘图区)，但是一个axes只能属于一个figure。
                * 一个axes(坐标系/绘图区)可以包含多个axis(坐标轴)，包含两个即为2维坐标系，三个即为3维坐标系

        辅助层：
            辅助层是Axes(绘图区)内的除了根据数据绘制出的图像以外的内容，主要包括Axes外观(facecolor)、边框线(spines)、坐标轴(axis)、
            坐标轴名称(axis label)、坐标轴刻度(tick)、坐标轴刻度标签(tick label)、网格线(grid)、图例(legend)、标题(title)等内容。

        图像层：
            图像层是指Axes(绘图区)内，通过plot(折线图)、scatter(散点图)、bar(柱状图)、histogram(直方图)、pie(饼图)等函数根据数据绘制出的图像。
                折线图plot：变化情况
                散点图scatter：关系规律
                柱状图bar：统计对比--x轴为不连续的分类数据
                直方图histogram：分布状况--x轴为连续的定量数据
                    直方图，形状类似于柱状图，却有着与柱状图有着完全不同的含义。直方图涉及统计学概念，首先要对数据进行分组，然后统计每个分组内数据元的数量。
                    在坐标系中，横轴标出每个组的端点，纵轴表示频数，每个矩形的高代表对应的频数，称这样的统计图为频数分布直方图。
                饼图pie：分类占比
                    plt.pie(x, labels=, autopct=, colors)
                        x：数量，自动算百分比
                        labels：每部分名称
                        autopct：占比显示指定%1.2f%% 两个小数
                        colors：每部分颜色
            颜色字符：
                r--红色  g--绿色  b--蓝色  w--白色  c--青色  m--洋红  y--黄色  k--黑色
            折线样式：
                -实线  --虚线  -.点划线  :点虚线  ''空格

        总结：
            * Canvas(画板)位于系统层，用户一般接触不到。
            * Figure(画布)建立在Canvas之上
            * Axes(绘图区)建立在Figure之上
            * 坐标轴axis、图例legend等辅助显示以及图像层都建立在Axes之上

"""

import random
import matplotlib.pyplot as plt
import numpy as np

# 1.matplotlib.pyplot模块--折线图plt.plot
# 设置画布属性
plt.figure(figsize=(20, 8), dpi=100)  # figsize：指定画布的长宽  dpi：dot per inch 图像的像素，每英寸多少个像素点。
# 设置绘图数据
x = range(60)
y_shanghai = [random.randint(20, 30) for i in x]  # randint是闭区间，range是左闭右开区间。
y_beijing = [random.randint(10, 15) for j in x]
# 两个城市温度对比
plt.plot(x, y_shanghai, color='r', linestyle='--', label='上海')  # color设置折线的颜色，linestyle设置折线样式，默认为实线
plt.plot(x, y_beijing, color='b', label='北京')  # label显示图例，还需调用plt.legend()
# 显示图例
plt.legend()
# 修改刻度
x_label = ["11点{}分".format(i) for i in x]  # 中文问题解决方案--见浏览器Python收藏夹中。
plt.xticks(x[::5], x_label[::5])
plt.yticks(range(10, 40, 5))
# 添加网格
plt.grid(True, linestyle='--', alpha=0.5)  # alpha为清晰度
# 添加描述信息
plt.xlabel("时间变化", fontsize=18)  # 设置标签字体大小
plt.ylabel("温度变化", fontsize=18)
plt.title("上海、北京11点到12点每分钟的温度变化情况", fontsize=18)
# 保存图片
plt.savefig('a_pyplot.png')  # 保存图片到指定路径，path中包含图像文件名。这里保存一次后注释掉。
plt.show()  # plt.show()会释放资源，如果在显示图像之后保存图片，只能保存空图片。

# 一张画布多个子图  可以通过matplotlib.pyplot.subplots()创建一个带有多个axes(坐标系/绘图区)的图，该函数返回两个对象，画布和坐标系列表。
figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 8), dpi=100)  # nrows设置坐标系的行数，ncols设置坐标系的列数。一行里有两个axes
axes[0].plot(x, y_shanghai, color='r', linestyle='-.', label='上海')  # 绘图
axes[1].plot(x, y_beijing, color='b', label='北京')
axes[0].legend()  # 显示标签
axes[1].legend()
axes[0].set_xticks(x[::5], x_label[::5])  # 修改刻度
axes[0].set_yticks(range(10, 40, 5))
axes[1].set_xticks(x[::5], x_label[::5])
axes[1].set_yticks(range(10, 40, 5))
axes[0].grid(linestyle='--', alpha=0.5)  # 修改网格
axes[1].grid(linestyle='--', alpha=0.5)
axes[0].set_xlabel("时间变化", fontsize=18)  # 添加描述信息
axes[0].set_ylabel("温度变化", fontsize=18)
axes[0].set_title("上海11点到12点每分钟的温度变化情况", fontsize=18)
axes[1].set_xlabel("时间变化", fontsize=18)  # plt.函数名()相当于面向过程的画图方法，axes.set_方法名()相当于面向对象的画图方法。
axes[1].set_ylabel("温度变化", fontsize=18)
axes[1].set_title("北京11点到12点每分钟的温度变化情况", fontsize=18)
plt.show()

# 绘制数学函数图像
x = np.linspace(-10, 10, 1000)
y = np.sin(x)
plt.figure(figsize=(20, 8), dpi=100)
plt.plot(x, y)
plt.grid(linestyle='--', alpha=0.5)
plt.show()

# 2.matplotlib.pyplot模块--散点图plt.scatter
x = [1, 1.2, 2, 3.1, 5, 6.3, 7, 7.2, 8]
y = [i + 1 for i in x]
plt.figure(figsize=(10, 4), dpi=100)
plt.scatter(x, y)
plt.show()

# 3.matplotlib.pyplot模块--柱状图plt.bar
# 不同电影的票房
movie_name = ['战狼2', '大话西游', '捉妖记', '长津湖', '澳门风云']
tickets = [54, 30, 36, 58, 10]
# 创建画布
plt.figure(figsize=(20, 8), dpi=100)
plt.bar(range(len(movie_name)), tickets, color=['r', 'g', 'y', 'r', 'b'])
# 修改x刻度
plt.xticks(range(len(movie_name)), movie_name)
# 添加标题
plt.title('国产电影票房收入对比')
# 添加网格显示
plt.grid(linestyle='--', alpha=0.5)
# 显示图像
plt.show()

# 不同天数的电影票房
movie_name = ['长津湖', '流浪地球', '战狼2']
first_day = [3, 1.5, 2]
first_week = [12, 13, 10]
plt.figure(figsize=(20, 8), dpi=100)
plt.bar(range(3), first_day, width=0.2, label='首日票房')
plt.bar([0.2, 1.2, 2.2], first_week, width=0.2, label='首周票房')
plt.legend(fontsize=18)  # 修改标签字体大小
plt.xticks([0.1, 1.1, 2.1], movie_name, fontsize=18)  # 这里用fontsize也可以，和设置标签字体一样
plt.show()

# 4.matplotlib.pyplot模块--直方图plt.hist
# 准备数据
height = [random.randint(150, 180) for i in range(60)]  # 60个同学的身高数据
# 绘制画布
plt.figure(figsize=(20, 8), dpi=100)
# 绘制直方图
distance = 5
group_number = int((max(height) - min(height)) / distance)
plt.hist(height, bins=group_number)
# 修改刻度
plt.xticks(range(min(height), max(height) + distance, distance))
# 添加网格
plt.grid(linestyle='--', alpha=0.5)
plt.show()

# 5.matplotlib.pyplot模块--饼图plt.pie
movie_name = ['战狼2', '大话西游', '捉妖记', '长津湖', '澳门风云']
tickets = [54, 30, 36, 58, 10]
plt.figure(figsize=(15, 8), dpi=100)
plt.pie(tickets, labels=movie_name, colors=['r', 'g', 'b', 'r', 'k'], autopct='%1.2f%%')
plt.legend(fontsize=18)
plt.axis('equal')
plt.show()
