# bug就是程序中出现的错误

# 常见bug：NameError: name 'schoolname' is not defined
schoolName = '中山大学' + ' sun yat-sen university'
print(schoolName)

# 常见bug：IndentationError: unexpected indent
# print(123) 一般Python语句需要顶格写
print(123)

# Debug调试工具
# Debug工具是PyCharm IDE中集成的用来调试程序的工具，可以用来
# 查看程序的执行细节和流程或者调试解决bug。

# Debug使用步骤
# 1.打断点
# 断点位置：单击目标代码行号的左侧空白位置。
print("断点位置") # 单击行号右边区域，出现红点即可

    # 2.Debug调试
print("Debug调试-启动快捷键：shift+F9")
print("Debug调试-进入语句运行快捷键：F7")
print("Debug调试-逐条语句运行快捷键：F8")
print("Debug调试-运行到下个断点处：F9")