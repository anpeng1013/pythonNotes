"""
    输入函数：input("提示信息")
    输入特点：
        1.当程序执行到input，等待用户输入，输入完成后才能继续向下执行。
        2.在Python中，input接收用户输入后，一般存储到变量中，方便使用。
        3.在Python中，input会把接收到的用户输入数据都当做字符串处理。

"""
# 1.input函数一次输入单个值
password = input('请输入你的密码：')
print()
print(f'您输入的密码是{password}')
print(type(password))  # <class 'str'

# 2.使用input函数加map和split一次输入多个值
a, b, c = map(int, input('请输入三个数字,使用空格隔开：').split())  # 将输入的数字按空格进行分割，对分割得到的列表中每个数字字符依次使用int函数。
print(f'your input is {a}, {b}, {c}')

# 3.以逗号分隔多个数据
list1 = input('please enter three numbers,separate with comma ",":').split(',')
print()
print(list1)

# 4.使用input函数和eval函数一次输入多个值
a, b, c = eval(input('please enter three numbers again,separate with comma ",":'))
print()
print(f'your input is {a},{b},{c}, {type(a)}')
