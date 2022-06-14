"""
    输入函数：input("提示信息")
    输入特点：
        1.当程序执行到input，等待用户输入，输入完成后才能继续向下执行。
        2.在Python中，input接收用户输入后，一般存储到变量中，方便使用。
        3.在Python中，input会把接收到的任意用户输入繁荣数据都当做字符串处理。

"""
password = input('请输入你的密码：')
print(f'您输入的密码是{password}')
print(type(password)) #<class 'str'