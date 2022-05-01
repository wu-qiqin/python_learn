"""
Created by hu-jinwen on 2022/4/24
"""


def num1():

    return int (input("请输入整数："))


def num2():
    return num1()

# 利用 异常的传递性，在主程序中捕获异常

try:
    print(num2())

except Exception as result:

    print("未知错误：%s" % result)

