"""
    字节串：用b''或b""表示。其实就是未经编码的二进制字节序列数据,即只能包含ASCII字符。
        字节串bytes和字符串str的对比：
            字符串由若干字符组成，以字符为单位进行操作；字节串由若干字节组成，以字节为单位进行操作。
            字节串和字符串除了操作单位不同外，他们支持的所有方法基本相同。
            字符串和字节串都是不可变序列，不能增加和修改数据。

        bytes只负责简单记录以字节序列的形式（二进制形式）来存储数据，至于这些数据到底表示什么
        内容（字符串、数字、图片、音视频等），完全由程序的解析方式决定。

        字符串以ASCII格式编码可以将字符串数据转换成字节串。

"""
# 字节串与字符串的区别
from sys import getsizeof

# getsizeof()获取变量内存占用的大小，而Python中的int，float等变量实际对应的是C语言中
# 的一个结构体，所以该字节获取的字节数能作为参考。

var_bytes = b'anpeng love huli'
var_str = '安鹏'
print(chr(var_bytes[0]))  # 'a' 一个字节， 字节串以字节为单位进行操作
print(var_str[0])  # '安'包含多个字节， 字符串以字符为单位进行操作
print(getsizeof(var_str[0])) # 字符串变量实际占用的内存大小
print(len(var_str)) # 字符串变量中的字符个数
print(getsizeof(var_bytes[0])) # 字节串变量实际占用的内存大小
print(len(var_bytes)) # 字节串变量的具体值占用的字节数。

# 字节串的操作与字符串基本相同
print(var_bytes[1::2])  # 字节串切片
print(var_bytes.find(b'en', 1))  # 字节串查找的子串也必须是字节串
print(var_bytes.replace(b'an', b'An'))  # 字符串的修改
bytes_list = var_bytes.split(b' ')  # 字节串用来分割的子串也必须是字节串
print(bytes_list)
var_bytes2 = b' '.join(bytes_list) # 字节串的拼接的子串也必须是字节串
print(var_bytes2)



