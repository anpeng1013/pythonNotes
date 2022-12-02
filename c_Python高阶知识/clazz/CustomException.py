# -*- coding = utf-8 -*-
# @Time : 2022/11/24 20:28
# @Author : anpeng
# @File : CustomException.py
# @Software : PyCharm

class ShortInputException(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):  # 设置抛出异常的描述信息
        return f'你输入的长度是{self.length}, 不能少于{self.min_len}个字符'
