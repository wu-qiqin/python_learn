"""
Created by hu-jinwen on 2022/4/16
"""
num = 10000


def num_1():
    # global 会备注全局变量
    global num
    num = 10

    print("%d" % num)


def num_2():

    print("%d " % num)


num_1()
num_2()

