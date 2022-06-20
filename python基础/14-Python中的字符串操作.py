"""
    字符串：
        常识：
            单引号 ' '
            双引号 " "
            三引号 ''' ''' 或 """ """
            以上三种都可以表示字符串,单双引号不可以屏蔽换行，三引号可以。
            
        下标:
            字符串类似于字符数组，可以按照下标访问各个字符数据。
            
        切片:
            切片是指对操作对象截取其中一部分的操作。字符串、元组、列表都支持切片。
            语法：序列名[开始下标：结束下标：步长]
                注意：不包含结束下标对应的数据，即左闭右开区间，下标正负整数均可。
                    步长是选取间隔，正负整数均可，默认开始下标是0，默认步长是1。
                    步长间隔为整数时，从左向右(正向）开始选取；为负数时则相反。
                    开始下标和结束下标也对应着选取方向，开始下标在左边则从左边开始选取，反之则反。
                    下标区间和步长的方向必须相同，否则出现歧义，什么都查不到。           
        
        操作：
            查找：find()-检测某个子串是否包含在这个字符串中，如果存在则返回子串.严格区分大小写。
                    第一次出现的开始下标，否则返回-1。语法：字符串序列名.find(子串，开始查找位置，结束查找位置）
                    默认开始下标是0，默认结束下标是最后。
                    1.开始和结束下标可以同时省略，表示在整个字符串中查找
                    2.结束下标可以省略，只给出开始下标，默认到最后结束
                    3.不能省略开始下标，而只给出结束下标。
                    4.开始下标位置的字符会被查找，结束下标位置的字符不会被查找
                    
                index():该函数的功能用法和find完全相关，区别是find查找不到返回-1，而index会报异常。
                    语法：字符串序列名.index(子串，开始查找位置，结束查找位置）
                
                count():返回某个子串在字符串中出现的次数
                rfind():和find功能相同，返回子串最后一次出现的位置。
                rindex():和rindex功能相同，返回子串最后一次出现的位置。
            
            修改：replace()，替换子串。字符串序列.replace(旧子串，新子串，替换次数)
                    注意：1.如果替换次数超出子串次数，则实际替换次数为子串出现次数。
                        2.替换次数默认为子串出现次数
                        3.字符串是不可修改类型，替换后的字符串必须用新的变量接收，
                            原来的字符串没有改变。
                
                capitalize():将字符串的第一个字母转换大写，其他字母全部小写。
                title()：将字符串每个单词首字母转换成大写。
                upper()：将所有字母全部大写
                lower()：将所有字母全部小写
                
                lstrip()：删除字符串左侧空白字符串
                rstrip()：删除字符串右侧空白字符串
                strip()：删除字符串两侧空白字符串
                
                ljust()：返回一个原字符串左对齐，并使用指定字符(默认空格)填充至对应长度的新字符串。
                rljust()：返回一个原字符串右对齐，并使用指定字符(默认空格)填充至对应长度的新字符串。
                center()：返回一个原字符串居中对齐，并使用指定字符(默认空格)填充至对应长度的新字符串。
                
                
            分割：split()，按照指定子串分割字符串。字符串序列.split(分割子串,num）
                    注意：num表示的是分割子串出现的次数，即将返回num+1个数据。
                        返回数据必须用一个列表list接收,且会丢失分割子串。
                        
            合并：join()，将列表list中的字符串数据合并为一个大字符串.
                    拼接子串.join(字符串列表) 
                    
            编码：encode()可以将字符串编码成指定的格式
                注意：纯英文的str可以用编码为bytes，内容是一样的，含有中文的str可以
                用utf-8编码为bytes。含有中文的str不可以用ASCII编码，因为中文字符超出
                了ASCII编码的范围，Python会报错。
            
            解码：decode()可以将字符串解码成指定的格式
            
            判断：
                startswith()：检查字符串是否以指定的子串开头，如果设置开始和结束下标，在在指定范围为检查。
                endswith()：检查字符串是否以指定的子串结尾，如果设置开始和结束下标，在在指定范围为检查。

"""
# 1.字符串常识
print('an'
      'peng')  # 单引号 '' 不可以屏蔽换行
print("an"
      "peng")  # 双引号 "" 不可以屏蔽换行
print('''an
            peng''')  # 三引号 ''' '''  可以换行输出
print("""an
            peng""")  # 三引号 """ """ 可以换行输出

# 字符串的输出
name = 'anpeng'
print('我的名字是anpeng')
print(f'我的名字是{name}')
print('我的名字是%s' % name)
print('我的名字是' + name)

# 字符串的输入 使用input接收输入，input接收的都是str。
password = input('请输入您的密码：')  # 为了演示下面代码，注释一下三行代码
print(f'您输入的密码是{password}')
print(type(password))

# 2.字符串的下标
for i in range(len(name)):  # range(len(name))相当于0到len(name)-1
    print(name[i], end='\t')
print()

# 3.字符串的切片
num = '0123456789'
print(num[:6])  # 默认步长是1 默认开始下标是0
print(num[6:])  # 结束下标默认是最后
print(num[:])  # 都不写，默认全部。
print(num[::2])  # 取所有偶数
print(num[2:5:2])  # 开始下标从0开始，结束下标数据没有选取

# 负数测试
print(num[::-1])  # 步长为-1，输出为倒序，步长为负数时，反向(从右向左)选取
print(num[-4:-1])  # 下标-1表示最后一个数据，依次向前类推。
print(num[9::-1])  # 逆序，下标为负数时反向选取。

# 反向测试：如果选取方向(下标开始到结束的方向) 和 步长的方向冲突，则无法选取数据。
print(num[-4:-1:-1])  # 没有数据
print(num[-1:-4:-1])  # 方向一致

# 4.字符串的常用操作
# 字符串查找之find
subString = 'anpeng love huli forever and he is very sincere'
print(subString.find('an'))  # 第一个出现的下标0，开始和结束下标可以省略，表示在整个字符串序列总查找。
print(subString.find('an', 2))  # 第二次出现的下标25,默认结束位置是最后
print(subString.find('she'))  # -1 子串不存在

# 字符串查找之index
print(subString.index('an'))  # index功能与用法和find是相同的，唯一区别就是查找不到时会抛出异常
# print(subString.index('she')) # ValueError: substring not found

# 字符串查找之count
print(f"子串\'an\'的出现次数：{subString.count('an')}")  # 2
print(f"子串\'an\'的出现次数：{subString.count('ans')}")  # 0

# 字符串查找之rindex和rfind
print(f"子串'an'最后一次出现的位置：{subString.rindex('an')}")
print(f"子串'an'最后一次出现的位置：{subString.rfind('an')}")

# 字符串修改之replace
new_substring = subString.replace('a', 'A')  # 默认全部替换
print(new_substring)
print(subString)  # 原来的字符串没有改变。

# 字符串修改之capitalize
print(new_substring.capitalize())  # 第一个字母大写，其余全部小写

# 字符串修改之title
print(subString.title())  # 每个单词首字母大写

# 字符串修改之upper
print(subString.upper())  # 将所有字母全部大写

# 字符串修改之lower
print(new_substring.lower())  # 将所有字母全部小写

# 字符串修改之lstrip
print('  hello world'.lstrip())  # 删除字符串左边的空白字符

# 字符串修改之rstrip
print('hello everyone '.lstrip())  # 删除字符串右边的空白字符

# 字符串修改之strip
print(' hello anpeng '.strip())  # 删除字符串两侧的空白字符

# 字符串修改之ljust
print('hello world'.ljust(20, '-'))  # 指定的只能是字符，不能是字符串。
print('hello world'.rjust(20, '+'))
print('hello world'.center(20, '*'))

# 字符串分割之split
str_list = subString.split(' ')  # 默认分割次数为子串出现次数
str_list1 = subString.split(' ', 2)  # 分割数据为2+1个
print(str_list)
print(str_list1)

# 字符串合并之join
str_join = ' '.join(str_list)  # 将字符串数组用空格连接
print(str_join)

# 字符串编码encode
str_encode = 'anpeng'.encode('ascii')  # 纯英文的字符串采用ASCII编码变成字节串。
print(str_encode)  # b'anpeng'
str_encode2 = '中文'.encode('utf-8')  # 含有中文的str采用utf-8编码转换成字节串
print(str_encode2)  # b'\xe4\xb8\xad\xe6\x96\x87', 无法显示为ascii字符的字节会显示成十六进制数\x##。

# 字符串解码decode
print(str_encode.decode('ascii'))  # 将纯英文的字节串用ASCII解码得到字符串
print(str_encode2.decode('utf-8'))  # 将含中文的字节串用utf-8解码得到字符串

# 字符串判断开头startswith
print('anpeng love huli'.startswith('anpeng'))

# 字符串判断结尾endswith
print('anpeng love huli'.endswith('huli'))

# 字符串判断是否全部为英文字母
print('hello huli'.isalpha()) # False 有空格
print('anpeng'.isalpha()) # True

# 字符串判断是否全部为数字
print('0123456789'.isdigit()) # True
print('abc124'.isdigit()) # False

# 字符串判断是否全部为空格
print('  '.isspace()) # True
print('hello world'.isspace()) # False

# 字符串判断是否数字或字母或组合
print('abc124'.isalnum()) # True
print('anpeng 123'.isalnum()) # False