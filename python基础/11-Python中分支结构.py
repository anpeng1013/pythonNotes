"""
    单分支判断结构
        if 条件：(条件成立执行下方缩进代码，否则执行else后面的缩进代码)
            代码1
            ……
        else:
            代码2

    多分支判断结构
        if 条件1：
            条件1成立执行的代码1
        elif 条件2：（多分支机构）
            条件2成立执行的代码2
        …………
        else:
            以上条件都不成立执行的代码3
        ** Python中没有switch语句

    分支嵌套结构
        if 条件1：
            执行代码1
            if 条件2：
                执行代码2

    三目运算符
        条件成立的表达式 if 条件 else 条件不成立的表达式
        Python中没有 [条件 ？成立表达式 ：不成立表达式]这种三目运算符。


"""
# 1.单重判断
age = int(input('请输入您的年龄：'))  # input函数接收的都是str
if age >= 18:
    print(f'您输入的年龄是{age}，已经成年，可以上网……')
else:
    print(f'您输入的年龄是{age}，您未成年，不可以上网！')

print('这个代码是否执行？')

# 2.多重判断
if age < 18:
    print(f'您输入的年龄是{age}，童工')
elif (age >= 18) and (age <= 60):  # 这里可以简写成 18 <= age <= 60
    print(f'您输入的年龄是{age}，合法')
elif age > 60:
    print(f'您输入的年龄是{age},退休')
else:
    print(f'您输入的年龄不符合规范！')

# 3.分支嵌套
if age >= 18:
    print(f'您已经{age}岁了，是个大人了')
    if age < 60:
        print('趁年轻，好好赚钱吧!')
        if age < 25:
            print('刚毕业吧？')
        else:
            print('好好赚奶粉钱！')
    else:
        print('该颐养天年了！')
else:
    print('你还是个孩子哦……')

# 4.三目运算符
print('成年' if age > 18 else '未成年')

