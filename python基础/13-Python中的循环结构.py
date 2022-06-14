"""
    while循环：
        while 条件：
            条件成立重复执行的代码
            计数器控制语句
            …………

    循环控制：
        break：终止整个循环
        continue：退出本次循环，继而执行下一个循环代码。

    for循环：
        for 临时变量 in 序列：
            重复执行代码
            …………

    while……else：
        else后面跟的是循环条件不成立且循环正常结束时，执行的代码，相当于java中的do……while
        无论如何，else中的代码都会被执行一次，除非是遇到break。

    for……else：
        else后面跟的是循环条件不成立且循环正常结束时，执行的代码，相当于java中的do……while
        无论如何，else中的代码都会被执行一次，除非是遇到break。
"""
print('while循环..........................................')
# 1.while循环
i = 0
result = 0
while i <= 100:  # 1-100累加之和
    result = result + i
    i += 1

print(result)

# 2.while中嵌套if结构
print('while中嵌套if结构..................................')
i = 0
result = 0
while i <= 100:  # 1-100之间偶数累加之和
    if i % 2 == 0:
        result = result + i
    i += 1

print(result)

# 3.while中的计数器控制累加
print('while中的计数器控制累加.............................')
i = 2
result = 0
while i <= 100:  # 1-100
    result += i
    i += 2

print(result)

# 4.循环控制之break
print('循环控制之break....................................')
i = 1
while i <= 5:
    if i == 4:
        print('吃饱了，不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1

# 5.循环控制之continue
print('循环控制之continue.................................')
i = 1
while i <= 5:
    if i == 3:
        print('吃出了虫子，这个苹果不吃了')
        i += 1  # 在continue之前一定要修改计数器，否则进入死循环。
        continue
    print(f'吃了第{i}个苹果')
    i += 1

# 6.while循环嵌套
print('while循环嵌套......................................')
i = 0
while i <= 2:
    print('I love you')
    j = 0
    while j <= 2:
        print('I want to marry with you')
        j += 1
    i += 1

# 7.while循环嵌套之九九乘法表
print('while循环嵌套之九九乘法表...........................')
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}*{i}={j * i}', end='\t')
        j += 1
    print()
    i += 1

# 8.for循环
print('for循环............................................')
var = 'anpeng'
for i in var:
    print(i, end='\t')
print()

# 9.for循环控制之break
print('for循环控制之break.................................')
for i in var:
    if i == 'p':
        break  # 终止整个循环
    print(i, end='\t')
print()

# 10.for循环控制之continue
print('for循环控制之continue..............................')
for i in var:
    if i == 'p':
        continue  # 退出本次循环，继续执行下一次循环
    print(i, end='\t')
print()

# 11.while……else循环 # else后面的代码在循环条件不成立时且循环正常结束时执行，相当于java中的do……while。
print('while……else循环....................................')
i = 0
while i < 2:
    print('anpeng')
    i += 1
else:
    print('hello world!')

# 12.while……else循环之break
print('while……else循环控制之break.........................')
i = 0
while i < 4:
    if i == 2:
        break
    print('anpeng')
    i += 1
else:  # break时else中的代码不执行。
    print('hello world!')

# 13.while……else循环控制之continue
print('while……else循环控制之continue......................')
i = 0
while i < 4:
    if i == 2:
        i += 1
        continue
    print('anpeng')
    i += 1
else:  # continue时,else中的代码要执行。
    print('hello world!')

# 14.for……else循环控制之break
print('for……else循环控制之break...........................')
for i in var:
    if i == 'p':
        break # break时else中的代码不执行。
    print(i, end='\t')
print()

# 15.for……else循环控制之continue
print('for……else循环控制之continue........................')
for i in var:
    if i == 'p':
        continue # continue时,else中的代码要执行。
    print(i, end='\t')
print()
