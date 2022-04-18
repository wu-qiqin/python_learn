"""
Created by hu-jinwen on 2022/4/17
"""

"""

递归函数，自己调用自己
递归函数，必须要有一个出口

"""
def sum_num(num):
    print(num)

    if num == 0:
        return

    sum_num(num - 1)


sum_num(3)
