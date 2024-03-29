"""
    函数：
        作用：封装一段具有独立功能的代码块集合，对外提供调用函数名。在需要的位置调用这个函数名即可完成对应的需求，
                函数在开发过程中，可以高效实现代码复用。
            总结：封装代码、代码复用。

        pass 关键字：
            1、pass是一个空的语句块，表示什么也不做。
            2、pass的作用是为了保证程序结构的完整性，否则报错。
            3、常见用处：如果定义了一个函数，或者一个类，暂时不知道该函数或类具体的业务逻辑，可以使用pass语句，以让程序正常运行，不影响其他代码。

        步骤：
            1.定义函数
                def 函数名(参数):
                    函数体代码
                    .......

            2.使用函数
                函数名(参数)-参数可有可无
                必须先定义后使用。
            注意：定义不同函数时，默认标准格式是--前后间隔两行，可以在
                setting->editor->Code Style->python->Around top-level classes and functions中设置为一行。

                *** 程序执行中，遇到函数定义，Python将编译好的函数定义体代码加载内存，编译后函数代码中的变量及参数的值不确定，当遇到
                    函数调用时才去取对应变量或参数的值。

        参数：参数可有可无。
                参数传递内容：传递的都是地址，即形参地址和实参地址相同。
                            对于不可变对象：数字，字符串和元组等，当在函数体对形参进行赋值、更新、删除等修改操作时，解释器会重新
                                开辟内存空间来保存修改结果，并将新的地址赋值给形参。 这相当于是“传值”
                            对于可变对象：列表，集合以及字典等，只要函数体不对形参进行重新赋新地址值的操作，函数内就可以
                                对形参地址(同实参地址）指向的内容进行修改这相当于是“传地址”
                            注意:其实Python参数传递的都是引用，即“地址”。

                参数传递方式： 位置传递--对应位置传递实参
                            形参名传递--根据形参名传递参，跟位置无关。
                            参数默认值--在定义函数时，使用argName=value的方式默认赋值，如果参数没有被传递值，则使用该默认值。
                            缺省传递--可传递多个参数，形参名前需要加 *，对多个实参用元组进行包裹，如果缺省参数是字典，则用两个星号**包裹。
                            解缺省传递--在实参名加*或者**,让实参序列的每一个元素对应一个位置参数

        返回值：返回值可有可无，使用return。
                return：退出函数，返回函数计算结果。
                函数返回值可以作为参数，传入另一个函数中。

        说明文档：help(函数名)--查看函数的说明文档
                位置：函数体内部第一行，使用三引号包裹。
                对三引号回车后，可以使用:info_name:形式提供更多函数信息，如
                :author: <anpeng>
                :version: 1.0

        函数嵌套：函数内部调用另一个函数。
            调用别人：普通嵌套
            调用自己：特殊嵌套--递归。

        变量作用域：(关于变量作用域更多详细细节，见文件27-Python中的变量作用域)
            局部变量：定义在函数内部的变量，即只在函数体内部生效。用于在函数内部临时保存数据，若没有被内部函数引用形成闭包(见25-高阶函数)，
                    则函数调用结束后会立即销毁局部变量。
            全局变量：定义在函数外部，并且在定义之后的所有函数内外都能生效的的变量。
            自由变量：未在本作用域绑定的变量。
"""

# 1.函数定义
def function():
    print('anpeng love huli')

function()

# 2.函数的参数
# 2.1.1 参数传递内容之”传值“：数字、字符串、元组等不可变对象。
print('-' * 60)
def add(arg1, arg2):
    print('赋值前地址是：' + str(id(arg1)))
    arg1 = arg1 + arg2
    print('函数内形参arg1的地址是：' + str(id(arg1)), '内容是：' + str(arg1))

num1, num2 = map(int, input("请输入两个数字：").split())
print('传参前地址是：' + str(id(num1)))
add(num1, num2)  # 实参为数字，不可变对象，为值传递
print('函数外实参num1的地址是：' + str(id(num1)), '内容是：' + str(num1))

str1, str2 = 'anpeng', ' love huli'
print('传参前地址是：' + str(id(str1)))
add(str1, str2)  # 实参为字符串，不可变对象，为值传递。
print('函数外实参str1的地址是：' + str(id(str1)), '内容是：' + str1)

tuple1, tuple2 = (1, 2, 3), (3, 2, 1)
print('传参前地址是：' + str(id(tuple1)))
add(tuple1, tuple2)  # 实参为元组，不可变对象，为值传递。
print('函数外实参tuple1的地址是：' + str(id(tuple1)), '内容是：' + str(tuple1))

# 2.1.2 参数传递内容之”传地址“：列表、集合、字典等可变对象。
print('-' * 60)
def update_list(arg1):
    arg1[0] = 'anpeng'
    print('传参后形参地址：' + str(id(arg1)))
    print('函数内形参arg1[0]的地址是：' + str(id(arg1[0])), '内容是：' + str(arg1[0]))

list1 = ['a', 'b']
list2 = ['huli']
print('传参前实参地址是：' + str(id(list1)))
update_list(list1)
print('函数外实参list1[0]的地址是：' + str(id(list1[0])), '内容是：' + str(list1[0]))

add(list1, list2)  # 公共运算
print(f'公共运算符+号作用容器，会生成一个新容器，新容器的地址赋值给形参arg1，实参list1的地址不会变：{id(list1)}')

# 2.2.1 参数传递方式之位置参数
print('-' * 60)
def func_site_and_keywords(aa, bb, cc):
    print(f'a={aa},b={bb},c={cc}')

func_site_and_keywords(1, 2, 3)

# 2.2.2 参数传递方式之关键字参数
# 注意：位置传参和关键字传参同时存在时，位置传参必须在关键字传参之前
func_site_and_keywords(1, cc=2, bb=9)  # a=1,b=9,c=2

# 2.2.3 参数传递方式之默认参数
# 注意：有默认值的形参在调用时可传可不传，若传入实参，则以实参为准。
def func_default(arg1, arg2, arg3='anpeng'):
    print(f'a={arg1},b={arg2},c={arg3}')

func_default(1, 2)  # a=1,b=2,c=anpeng

# 2.2.4 参数传递方式之可变传递(包裹传递)：可以将多个参数打包传入
# 使用 (*形参名) 时，不需要用关键字传参，参数传入后以元组的形式保存
def func_packing(*args):
    print(type(args), args)

func_packing(1, 2, 'anpeng')  # <clazz 'tuple'> (1, 2, 'anpeng')

# 使用 (**形参名) 时，需要使用关键字传参，参数传入后默认以字典的形式保存。
def func_packing_keyword(**args):
    print(type(args), args)

func_packing_keyword(a=(1, 2, 3), b={'a', 'huli'})  # <clazz 'dict'> {'a': (1, 2, 3), 'b': {'huli', 'a'}}
func_packing_keyword(name='anpeng', age=25)

# 2.2.5 参数传递方式之拆包传递(解包裹)
# 将元组形式的参数按位置匹配传入，元组前需要加*
def func_unpacking(arg4, arg5, arg6):
    print(arg4, type(arg4), '\t', arg5, type(arg5), '\t', arg6, type(arg6))

func_unpacking(*(23, 'anpeng', 12.5))  # 23 <clazz 'int'> 	 anpeng <clazz 'str'> 	 12.5 <clazz 'float'>

# 将字典形式的参数按关键字来匹配，字典前需要加**
func_unpacking(*(1, 2.5, 'anpeng'))  # 1 <clazz 'int'> 	 2.5 <clazz 'float'> 	 anpeng <clazz 'str'>
func_unpacking(**{'arg4': 'anpeng', 'arg6': 25, 'arg5': 'huli'})  # 传入字典时，其键必须为形参名，不然对不上，没有位置顺序要求。


# 2.2.6 元组拆包和字典拆包
def return_num():
    return 100, 200

num1, num2 = return_num()  # 对元组进行拆包
print(num1, num2)

dict1 = dict(name='anpeng', age=25)
a, b = dict1  # 对字典进行拆包，取出来的是字典的key，通过key进行操作
print(dict1[a], dict1[b])

# 2.2.7 交换变量的值
# 方法一：借助第三个变量
a, b = 10, 99
print(a, b)
c = a
a = b
b = c
print(a, b)

# 方法二：直接交叉赋值
a, b = 3, 8
print(a, b)
a, b = b, a
print(a, b)


# 3.1 函数返回值
def func_add(*args):
    """
    多元素求和函数
    :author: <anpeng>
    :version: 1.0
    :param args:可变参数
    :return: 求和结果
    """
    result = 0
    for i in args:
        result += i
    return result

print(func_add(1, 2, 89, 10, 8, 5.6))  # 115.6

# 3.2 函数多返回值
def fun_multiple_return():
    return 1, 2, 3  # 返回多个数据的时候，默认是元组类型。

# return后面可以连接列表、元组或字典，以返回多个值。

print(fun_multiple_return())
# 4.1 查看函数的说明文档--使用help(函数名)直接打印函数的说明文档。
# 注意：函数名后不能加括号
help(len)


# 4.2 函数说明文档的位置和方法：说明文档在函数体第一行，并用三个双引号包裹。
# 注意：若函数体内第一行没有说明文档，则会将函数定义的上一行的单行注释作为说明文档。
def func_document():
    """this is an example of func_document"""
    print('func_document')

help(func_add)  # 三引号回车后，可以使用:info_name:的形式提供更详细的函数信息。
help(func_document)

# 5.1 函数嵌套调用之调用别人--普通嵌套
# 前面定义函数中调用了print函数，就是普通嵌套

# 5.2 函数嵌套调用之调用自己--递归嵌套。

# 6. 修改全局变量
# 需要在函数体内修改全局变量时，需要使用关键字global先声明这个全局变量，再对这个全局变量赋新值。
var = 'anpeng'

def update_global_var():
    global var
    var = 'Tom'

print(var)
update_global_var()
print(var)
