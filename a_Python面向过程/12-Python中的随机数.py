"""
    步骤：
        1.导入模块
            import random
        2.使用模块功能
            random.randint()

"""
import random
import sys

# 1.使用random.random()生成单个--介于0和1之间的随机浮点数
num = random.random()
sys.stdout.write(str(num) + '\n')  # 相当于print(num) 不会自动换行

# 2.使用random.randint()生成单个指定范围内的随机整数
num = random.randint(0, 10)  # randint是一个闭区间，左右都能取到。
print(num)

# 3.使用for循环生成随机数列表
randomList = []
for i in range(10):
    randomList.append(random.randint(1, 10))
print(randomList)

# 4.使用列表推导式生成随机数列表
randomList = [random.randint(1, 10) for i in range(10)]
print(randomList)

# 5.使用random.sample()直接生成随机数列表。
randomList = random.sample(range(1, 11), 10)  # range是左闭右开区间，左边能取到，右边取不到。
print(randomList)
