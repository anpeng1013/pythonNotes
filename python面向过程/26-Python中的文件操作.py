# -*- coding = utf-8 -*-
# @Time : 2022/10/23 11:57
# @Author : anpeng
# @File : 26-Python中的文件操作.py
# @Software : PyCharm

"""
1.文件编码
    为什么要编码：
        1.文件数据必须首先存储到计算机中，然后才能被计算机处理。计算机存储数据的部件主要是存储器；存储数据的具体单位是存储单元。
        1.比特位(bit)：是计算机中最小的信息单元。一个比特只能通过高低电平表示0和1的一个二进制数据。
        2.字节(byte)：由8个相邻的比特位组成的信息存储单元，字节是计算机最小的编址单位，因而是计算机最基本的存储单元。以字节为单位赋予的地址称为字节编址。
        3.人类各个国家的语言太多，计算机需要表示的符号远远超过8个比特位所能表达的256个符号，无法用一个字节来完全表示。
        4.因此必须进行从人类语言字符char到计算机byte的编码。

    常见的编码方式：
        ASCII码：ASCII是American Standard Code for Information Interchange(美国信息交换标准码)的缩写。ASCII码用一个字节编码西文字符、特殊字符
                、阿拉伯数字等。字节的最高位为0，用低七位表示，总共有128个。0-31是控制字符如换行、回车等，32-126位打印字符，可以通过键盘输入并显示出来。127为删除。

        扩展的ASCII码：ISO-8859-1码是ISO组织在ASCII码基础上利用最高位扩展得到的，其仍然是单字节编码，总共能表示有256个西文字符。前128个字符和ASCII码一致。

        GB2312/GBK/GB18030：GBK和GB2312：GBK和GB2312都是对简体字的编码，但GB2312只支持六千多汉字的编码，而GBK支持1万多汉字编码。并且GBK兼容GB2312,
                            即可用GBK对GB2312编码的汉字进行解码，不会出现乱码。GB18030用于繁体字的编码。三者都是用两个字节进行编码。

        utf-16：unicode是国际标准化组织ISO创建的超语言字典，能够翻译世界上所有的语言。utf是unicode transform format, unicode转换格式的简写。
                16，代表16个比特，即两个字节进行编码。

        utf-8：是Unicode的另一种具体编码实现方式，是互联网使用最广的一种。因为utf-16对西文字符采用两个字节编码，存在存储浪费。
                而utf-8的最大特点，就是它采用一种变长的编码方式。它可以采用1-4个字节表示一个字符，根据不同的符号变化字节长度。
                utf-8的规则很简单，只有两条：
                1）对于单字节的符号，字节的第一位设为0，后面7位时这个符合的Unicode码。因此对于英文字符，utf-8编码和ASCII码是相同的
                2）对于n个字节的字符(n>1)，第一个字节的前n位都设为1，第n+1设为0，后面字节的前两位一律设为10。剩下的没有提及的二进制位，
                    全部为这个符号的Unicode码。

2.文件的基本操作
    打开模式：使用open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)打开file文件，
                file()和open()函数功能和用法完全相同。

            file：要打开的目标文件的字符串（可以包含文件所在的具体路径）
            mode：一个字符串，用于设置打开文件的访问模式-只读、写入、追加等，默认为只读r，详情见下方英文描述。
            buffering：设置缓冲区策略，默认为-1，不需要修改。
            encoding：文件编码方式。若不指定，则会通过locale.getpreferredencoding(False)获取，返回值根据windows系统所设置的地区变化。
                      例如，地区为中国大陆(简体中文)时，返回值为cp936。cp936其实就是GBK，因为IBM在code page文档中将GBK放在了第936页
            其余参数：使用默认值即可，不用修改。

            mode      Meaning
            --------- ---------------------------------------------------------------
            'r'       open for reading (default)
            'w'       open for writing, truncating the file first
            'x'       create a new file and open it for writing
            'a'       open for writing, appending to the end of the file if it exists
            'b'       binary mode
            't'       text mode (default)
            '+'       open a disk file for updating (reading and writing)
            'U'       universal newline mode (deprecated and removed)
            **** 注意：1、四个文件编辑主模式：r, w, x, a
                         * 以r主访问模式打开文件时，若文件不存在都会报错。w、a、x模式文件不存在会新建。
                         * 以r、w、x主访问模式打开文件时，文件指针都在开头，只有以a主访问模式打开文件时，文件指针才在末尾。
                         * 以w主访问模式打开文件时，原本内容会被清空。
                      2、两个文件内容模式：t(text mode) 和 b(binary mode)
                         * text mode 以文本模式打开文件，读取文件时返回的是字符串。字符串的编码方式默认是本地编码方式，
                                     通过locale.getpreferredencoding()可以获得，Windows10中是cp936,其实就是GBK。
                         * binary mode 以二进制模式打开文件，读取文件时返回的字节串。
                      3、四个文件编辑主模式都可以和两个文件内容模式搭配，比如'wb'(二进制写入)、'rt'(文本只读，这里的t可以省略，可只写'r')
                      4、'+'mode表示可读可写，需要与四大文件编辑模式组合使用，但文件指针的位置依旧按照四大主模式。
                      5、'x' mode，创建一个新文件用于写入。

            encoding：Python区分文件内容的打开方式，要么以文本模式，要么以二进制字节串模式。encoding只针对text mode文本模式。
            *** 在Python中可以使用charset-normalizer(字符集规范器)检测来自网络的文件的编码方式。
                而对于本地创建的文件，Python会使用locale.getpreferredencoding()获取底层操作系统的编码方式进行解码文件。

    文件指针：
        1、以r、w主访问模式打开文件时，文件指针都在开头，只有以a主访问模式打开文件时，文件指针才在末尾。
        2、不管是文件读取，还是写入，文件指针都会跟着向后移动相应的距离。
        3、file.tell()：返回文件指针当前位置，该位置只能是以字节为单位，起始为0
        4、file.seek(offset[, whence])：用来移动文件指针。
            file：文件对象
            whence：作为可选参数，用于指定文件指针要放置的位置，该参数的参数值有3个选择：0 代表文件头（默认值）、1 代表当前位置、2 代表文件尾
            offset：表示相对于whence位置文件指针的偏移量，偏移量也是以字节为单位的！！ 正数表示向后偏移，负数表示向前偏移。
                    例如，当whence==0 && offset==3（即seek(3,0)），表示文件指针移动至距离文件开头处3个字节的位置。
                    注意：当offset值非0时，Python要求文件必须以二进制格式打开，否则会抛出io.UnsupportedOperation异常。


    读取数据：
        read()：文件对象.read(num)，num表示要从文件中读取的数据长度，单位默认是字节（若要以字符为单位，需要在打开文件函数的参数中，
                设置编码格式encoding=’utf-8‘）如果没有传入num，则读取文件所有数据。
        readlines()：可以按照行的方式把整个文件的内容进行一次性读取，并返回一个列表，文件中的一行为列表中的一个元素。
        readline()：一次读取文件的一行内容。

            *** 注意：若以r主访问模式打开的必须是已存在的文件！否则会报错
                    ！！！以r只读模式打开的文件存在中文时，一定要使用charset-normalizer中detect方法检查文件的编码方式。
                    charset-normalizer是chardet的升级版，是conda环境的集成模块，不需要安装。而chardet需要安装。usage：见2.1

    写入数据：
        write(string)：文件对象.write(string/bytes)，string表示要写入文件的字符串。bytes表示字节串，仅适用于二进制打开的文件。
        writelines(list)：list表示要写入文件的字符串列表，需要注意的是，writelines函数向文件中写入多行数据时，不会自动添加换行符。

            *** 注意：不管是读取文件还是写入文件，都依赖于文件指针的当前位置。不同的打开方式将会决定文件读取和写入的结果。
                 例如，以a+(可读可追加)模式打开文件，文件指针在末尾，此时读取文件会从末尾开始读取，从而读不到任何内容。

    关闭文件：close()
        注意：可以只打开和关闭文件，不进行任何读写操作，但是比较占内存。

3.文件备份
    需求：用户输入当前目录下任意文件名，程序完成对该文件的备份功能。(备份文件名为xx[备份]后缀，例如：26-Python中的文件读取.txt)。
    步骤：
        1、接收用户输入的文件名
        2、规划备份文件名
        3、备份文件写入数据。
    作用：避免文件被误删除和误修改。

4.文件和文件夹的操作

"""

from charset_normalizer import detect
import locale


# 1 读取文件数据
# 1.1 检测文件的编码方式
def check_charset(file_name):
    with open(file_name, 'rb') as f:  # 使用with语句，可以不用手动关闭文件
        data = f.read()
        charset = detect(data)['encoding']
    return charset

# 1.1 read(num)
print('-' * 20 + 'read(num)' + '-' * 20)
r_file = open("26-Python中的文件读取.txt", encoding='utf-8')  # 默认以'r'只读方式打开文件
result = r_file.read(2)  # 默认单位为字节，若要以字符为单位进行读取，设置文件的编码方式，如encoding=‘utf-8’
print(result, r_file.tell())  # 安鹏 6 说明utf-8中’安鹏‘这两个汉字占三个字节，utf-8中大多数汉字占三个字节。

result = r_file.read()  # 若省略num参数，则默认文件指针之后的所有数据
print(result, r_file.tell())  # is studying the operation of file in python 50 读取数据后文件指针会继续后移。

r_file.seek(0)  # offset非0时，文件必须以二进制打开，这里的r_file以utf-8格式打开，offset只能是0，可选参数whence默认为0
# whence=0文件开头，whence=1当前位置，whence文件末尾。
result = r_file.read()
print(result, r_file.tell())
r_file.close()  # 关闭文件

# 1.2 readlines()
print('-' * 20 + 'readlines()' + '-' * 20)
r_file = open('26-Python中的文件读取.txt', encoding='utf-8')  # 不指定打开文件的编码方式为utf-8时，中文显示会出现乱码，甚至报错
result = r_file.readlines()
print(result)
r_file.close()

# 1.3 readline()
print('-' * 20 + 'readline()' + '-' * 20)
r_file = open('26-Python中的文件读取.txt', encoding='utf-8')
first_line = r_file.readline()
print(f'第一行内容：{first_line}')  # 打印文件一样内容时，文件一行的末尾有换行符，会换行一次，而print函数默认以换行结束，所以会换行两次。
second_line = r_file.readline()
print(f'第二行内容：{second_line}')
r_file.close()

# 2.文件写入
# 2.1 write写入字符串
print('-' * 20 + 'write写入字符串' + '-' * 20)
w_file = open('26-Python中的文件写入.txt', 'w+')  # 以w主访问模式打开文件，文件内容被清空，文件指针在开头
w_file.write('安鹏 love huli very much')  # 写入字符串后文件指针移动到文件末尾
w_file.seek(0, 0)  # 移动文件指针到开头进行读取
context = w_file.readline()
print(locale.getpreferredencoding())
w_file.close()
print(context)

# 2.2 write写入字节串
print('-' * 20 + 'write写入字节串' + '-' * 20)
w_file = open('26-Python中的文件写入.txt', 'wb+')  # 需要写入字节串时，必须以二进制方式打开文件
w_file.write(b'anpeng love huli')
w_file.seek(0, 0)  # 移动文件指针到开头进行读取
context = w_file.read()
w_file.close()
print(context)

# 2.3 新建文件并写入内容：'x' mode 若新建文件已存在时，会报错。
print('-' * 20 + 'x mode create a new file and open it for writing' + '-' * 20)
x_file = open('26-Python中的文件新建并写入.txt', 'xb+')
x_file.write(b'anpeng is huli boyfriend')
x_file.seek(0, 0)  # offset=0 whence=0，移动文件指针到开头进行读取
context = x_file.read()
x_file.close()
print(context)  # b" anpeng is huli boyfriend "

# 3.文件备份：避免文件被误删除和误修改
# 3.1 接收用户输入待备份文件名
old_name = input('请输入您要备份的文件名：')
# 3.2 规划备份文件的名字 xx[备份]后缀
suffix_dot_index = old_name.rfind('.')  # 提取文件后缀点的下标 使用rfind，如anpeng.txt.mp3,该文件的后缀是.mp3
new_name = old_name[:suffix_dot_index] + '[备份]' + old_name[suffix_dot_index:]
# 3.3 备份文件写入数据
old_file = open(old_name, 'rb')
new_file = open(new_name, 'wb')  # 二进制打开和写入，不会出现读取和写入乱码
# 不确定文件大小，循环读取再写入，当读取出来的数据没有时终止循环。
while True:
    context = old_file.read(1014)  # 每次读取1KB数据
    if len(context) == 0:
        break
    else:
        new_file.write(context)

old_file.close()
new_file.close()
