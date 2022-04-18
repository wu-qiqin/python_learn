"""
Created by hu-jinwen on 2022/4/16
"""
# * args: 多值参数--元组
# * kwargs : 多值参数--字典

# 拆包语法（元祖+字典）

def sum (*args):

    print(args)

    num = 0
    for n in args:
        num += n

    return num


result = sum(1, 2, 3, 4, 5, 6, 8, 10)

print(result)


def num (*args, **kwargs):

    print(args)
    print(kwargs)


gl_list = (1, 2, 3, 4, 5)
gl_dic = {"name": "xiaohu", "age": 10}

num(*gl_list, **gl_dic)

