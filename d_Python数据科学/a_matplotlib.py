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

        总结：
            * Canvas(画板)位于系统层，用户一般接触不到。
            * Figure(画布)建立在Canvas之上
            * Axes(绘图区)建立在Figure之上
            * 坐标轴axis、图例legend等辅助显示以及图像层都建立在Axes之上

"""

import random
import matplotlib.pyplot as plt

# 1.matplotlib.pyplot模块--折线图
# 1.1 折线图绘制与显示--展现上海一周的天气温度。
plt.figure()  # 创建画布
plt.plot(range(1, 8), [17, 17, 18, 15, 11, 11, 13])  # 绘制折线图
plt.show()  # 显示图像

# 1.2 设置画布属性与图片保存
plt.figure(figsize=(20, 8), dpi=80)  # figsize：指定图像的长宽  dpi：dot per inch 图像的像素，每英寸多少个像素点。
plt.plot(range(1, 11), [random.randint(0, 11) for i in range(10)])
"""

    plt.savefig(path) path中包含图像文件名
"""
