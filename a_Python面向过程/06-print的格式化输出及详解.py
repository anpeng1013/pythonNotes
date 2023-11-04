"""
print格式化输出:
    * 格式化符号
        %s--字符串         %d--有符号十进制整数
        %f--浮点数         %u--无符号十进制整数
        %c--单字符         %o--八进制整数
        %x--十六进制整数（小写ox)
        %X--十六进制整数（大写OX)
        %e--科学计数法（小写'e'）
        %E--科学计数法（大写'E'）

    * f表达式-输出字符类串：f'输出的内容是{var}'

print()函数详解
    print(value[,..., sep='分隔符', end='结束符', file=sys.stdout])
        value：print()函数可打印多个对象，打印时默认以空格将多个对象隔开。
                打印多个对象时，输入时用逗号隔开。但是多个对象是字符串常量时，
                可以不用逗号隔开，但打印结果中多个字符串常量中间没有空格隔开。
        sep="自定义分隔符"：可以使用自己的分隔符，隔开多个打印的对象。
        end="自定义结束符"：默认为换行符，可以自己修改。
        file：默认将输出打印到控制台(sys.stdout)，输出可以打印到其它文件，
                但该文件必须用open()函数先打开，之后进行打印输出到文件。
                open()函数用法：varFile=open('fileName','a')，a表示文件可追加内容。

"""
# 定义变量：存储二进制、八进制、十六进制数
binary = 0b0111
octonary = 0o0777
hexadecimal = 0x0fff

# 直接用print函数打印非十进制数，
# 打印结果会自动转为十进制
print(binary)  # 打印结果：7
print(octonary)  # 打印结果：511
print(hexadecimal)  # 打印结果：4095

# python中使用bin()、oct()、hex()函数
# 输出二进制、八进制、十六进制数
print(bin(binary))  # 打印结果：0b111
print(bin(12))  # 打印结果：0b1100
print(oct(octonary))  # 打印结果：0o777
print(hex(hexadecimal))  # 打印结果：0xfff

# 如果不想输出0b、0o、0x的前缀，可以使用format()函数
print(format(binary, 'b'))
print(format(octonary, 'o'))
print(format(hexadecimal, 'x'))

age = 25
name = 'anpeng'
weight = 75.5
stu_id = 1
stu_id2 = 10001

# 1.今年我年龄是x岁 --整数 %d
print('今年我年龄是%d岁' % age)

# 2.我的名字是x --字符串 %s
print('我的名字是%s' % name)

# 3.我的体重是x公斤 --浮点数 %f
print('我的体重是%.2f公斤' % weight)  # %.2f：表示小数点后的小数位数

# 4.我的学号是x  -- %d
print('我的学号是%03d' % stu_id)  # %03d：表示输出的整数显示位数，不足的以00补全，超出当前位数则原样输出
print('我的学号是%03d' % stu_id2)

# 5.我的名字是x，年龄x岁了
print('我的名字是%s，年龄%d岁了' % (name, age))  # 多个格式化输出时，用圆括号
# 5.1 我的名字是x，明年x岁了
print('我的名字是%s，明年%d岁了' % (name, age + 1))

# 6.我的名字是x，年龄x岁了，体重x公斤，学号是x
print('我的名字是%s，年龄%d岁了，体重%.2f公斤，学号是%06d' % (name, age, weight, stu_id))

# %s 不仅可以格式化输出字符串，还可以输出整型和浮点型数
print('我的名字是%s，年龄%s岁了，体重%s公斤，学号是%s' % (name, age, weight, stu_id))

# f表达式格式化输出字符串
print(f'我的名字是{name}')

# print()函数详解
a = 15
b = 'love'
print(a, b)  # 直接打印多个对象
print('an''peng')  # 直接打印多个字符串，中间可以不要逗号，但打印结果没有空格
print(13, 14, sep='+')  # 修改分隔符
print('an''peng', end=' love huli forever\n')  # 修改结束符
f = open("06-print输出文件.txt", 'a')  # 向指定文件中打印内容。
print("ap love huli forever", "you known?", sep="--", end="...\n", file=f)
f.close()

print()
