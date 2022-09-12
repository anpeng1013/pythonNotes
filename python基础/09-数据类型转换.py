"""
    Python中转换类型的函数
        int(x[,base])：将x转换为一个整数，base为进制数。
                        若x是纯数字，则不能有base参数，否则报错；其作用对x取整。
                        若x为str，则base可有可无。str中不能有小数点。
        float(x)：将x转换为一个浮点数。
        str(x)：将对象x转换为字符串
        complex(real[,imag])：创建一个复数，real为实部，image为虚部。
        chr(x)：将一个整数转换为一个Unicode字符。
        ord(x)：将一个字符转换为它的ASCII整数值。
        hex(x)：将一个整数转换为一个十六进制字符串。
        oct(x)：将一个整数转换为一个八进制字符串。
        bin(x)：将一个整数转换为一个二进制字符串。

        repr(x)：将对象x转换为表达式字符串,格式字符会原样输出，比如\n\t。
        eval(str)：用来计算在字符串中有效的Python表达式，并返回表达式运算的值。
        map(function,iterator):对可迭代对象进行迭代使用function函数，返回一个迭代器。直接打印map的结果则返回的是一个对象。

        tuple(s)：将序列s转换为一个元组。
        list(s)：将序列s转换为一个列表。
        set(s)：转换为可变集合。
        dict(d)：创建一个字典。d必须是一个（key，value）元组序列。

"""
# 1.int(x[,base])
# x有两种：str/int
# 若x为纯数字，则不能有base参数，否则报错。作用是对x取整。

print('int()函数------------------------------------')
print(int(3.14159))
# print(int(32, 8)) #TypeError: int() can't convert non-string with explicit base

# 若x为str，则base可有可无。str表示的须为整型，不能是如'3.14'的字符串。
# print(int('3.14')) # ValueError: invalid literal for int() with base 10: '3.14'

# 若有base时，则将x视为base进制数字，print函数直接打印其他进制数时，会将其转换成十进制数。
print(int('111', 2))  # 7
print(int('777', 8))  # 511
print(int('fff', 16))  # 4095

# 若x不符合base规范，则报错
# print(int('9', 2)) # 报错：因为二进制没有9这个数字
# print(int('abc', 8)) # 报错：因为16进制才允许有abc
print(int("1001"))  # 1001:默认为十进制。

# 2.float()--将数据转换成浮点型
print('float()函数-----------------------------------')
print(float(1))  # 1.0
print(float('10'))  # 10.0

# 3.str()--将数据转换成字符串型
print('str()函数-----------------------------------')
print(type(str(110)))  # str：将整型转换成字符串
print(str({'anpeng': 'huli', 'ap': 'hl'}))  # 将字典转换为字符串
print(str({'anpeng', 'huli', 'love', 'you'}))  # 将集合转换为字符串

# 4.tuple()--将一个序列转换为一个元组。
print('tuple()函数-----------------------------------')
print(tuple('anpeng'))  # 将字符串可迭代对象"anpeng"，拆分单个字符的元组
print(tuple([1, 2, 3]))  # 将列表有序序列转为成元组
print(tuple({1, 2, 3}))  # 将集合无序序列转换为元组,因为集合无序，所以每次转换的元组元素次序不一样
print(tuple({1: 2, 2: 3, 3: 4}))  # 将字典无序的关键字序列转换为元组

# 5.list()--将一个序列转化为一个列表
print('list()函数-----------------------------------')
print(list('love'))  # 将字符串可迭代对象'love'，拆分单个字符的列表
print(list(('a', 'b', 'c')))  # 将元组有序序列转为成列表
print(list({'a', 'b', 'c'}))  # 将集合无序序列转换为列表,因为集合无序，所以每次转换的列表元素次序不一样。
print(list({'a': 'b', 'b': 'c', 'c': 'd'}))  # 将字典无序的关键字序列转换为列表

# 6.set()--将一个序列转化为一个集合
print('set()函数-----------------------------------')
print(set('hulili'))  # 将字符串可迭代对象'hulili'，拆分成单个字符的无序组合，并且去重
print(set((3, 2, 3, 4)))  # 将元组有序序列转为成集合，重复的元素去掉
print(set([1, 2, 3, 2]))  # 将列表有序序列转换成集合，重复的元素去掉
print(set({1: 2, 2: 3, 3: 4}))  # 将字典无序的关键字序列转换为列表

# 7.dict(d)--创建一个字典。
# dict字典的值可以任何数据类型，但键必须不可变的，如字符串，数字或元组。
print('dict()函数-----------------------------------')

# 通过key=value键值对的形式，此时key的名称必须遵循命令规则，而值value可以是任意类型
print(dict(a=1, b=1))  # 这里的a相当于key的名字，所以需要遵循命名规则：字母、下划线、数字组成，但不能由数字开头，
print(dict(a1_2=3))  # 任何形式的key都会被转为字符串。
# print(dict(1 = a, 2 = b)) # key标识符由字母、数字、下划线组成，但不能由数字开头
print(dict(_1=2, a2=3))

# 注意：使用可迭代对象和映射创建字典时关键字可以是数字；而使用key=value创建字典时，key标识符会被转换成字符串。

# 使用可迭代对象创建字典
print(dict(((1, 2),)))  # 元组中单个元素时，需要在元素后面添加逗号
print(dict(((1, 2), ((1, 2), 3))))  # 第二个键为元组(1,2)
print(dict([('a', 3)]))  # 列表中单个元素时，不需要在元素后面加逗号。
# print(dict([([1, 2, 3], 1), [4, 3]])) # TypeError: unhashable type: 'list' 第一个键是列表，不符合键不可变的特点。

# 使用映射来创建字典,关键字参数会被继续传递。
print(dict({1: 2, 'a': 110}))
print(dict({'a': 12, 2: 33}, a=89, b=0b101))
# print(dict({'124': 12}, ((1, 2), (2, 3)))) #dict函数使用映射后，后面只能使用关键字参数，不能使用可迭代对象。

# 8.eval()--计算字符串中的有效Python表达式，并返回表达式的表达式指示的对象
str1 = '1'
str2 = '1.1'
str3 = '(1000,2000,3000)'
str4 = '[1, 2, 3]'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))

# 9.complex(real[,imag])：创建一个复数，real为实部，image为虚部。
print(complex(12))  # 12+0j
print(complex(13, 14))  # 13+14j
print(type(complex(1, 2)))  # <class 'complex'>

# 10.repr(x)：将对象x转换为字符串形式,格式字符会原样输出
print(repr(str3))  # 将‘(1000,2000,3000)'字符原样输出，不像eval函数那样将其转换为tuple
str5 = '物品\t单价\t数量\n包子\t1\t2'
print(str5)
print(repr(str5))

# 11.chr(x)：将一个整数转换为一个Unicode字符。
print(chr(65))  # 'A'
print(chr(32))  # ' '
print(chr(97))  # 'a'

# 12.ord(x)：将一个字符转换为它的ASCII整数值。
print(ord('a'))  # 97
print(ord(' '))  # 32
print(ord('A'))  # 65
print(ord('安'))  # 23433

# 13.hex(x)：将一个整数转换为一个十六进制字符串。
print(hex(12))  # 0xc
print(hex(65535))  # 0xffff

# 14.oct(x)：将一个整数转换为一个八进制字符串。
print(oct(12))
print(oct(65535))

# 15.bin(x)：将一个整数转换为一个二进制字符串。
print(bin(12))
print(bin(65535))


# 16.map(function,iterator,...)
# 并行使用来自iterator的参数，迭代调用function，当最短的iterator耗尽时停止，并返回一个迭代器，迭代器的每个元素是每次调用function的返回结果。
def function(x, y, z):
    return [x, y, z]


tuple1 = (1, 2, 3)
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4, 5]
result = map(function, tuple1, list1, list2)
print(result)
for i in result:  # result是一个可迭代对象，使用for循环迭代打印。
    print(i)
print(list(result))  # [] 迭代器中的数据在for循环遍历后，索引数据会消失。

# 迭代器不管是for循环遍历操作，还是list()数据类型转换为列表操作，都会访问一次数据，访问一次后，迭代器中的数据索引消失，无法再获取值。
