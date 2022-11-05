"""
    步骤：
        1.导入模块
            import random
        2.使用模块功能
            random.randint()

"""
import random
import sys

num = random.randint(0, 10)
sys.stdout.write(str(num))  # 相当于print(num)
