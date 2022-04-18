"""
Created by hu-jinwen on 2022/4/16
"""
# +=


def demo_num(num, num_list):
    """

    :type num_list: object
    """
    # num = num +num
    num += num

    # 列表中+= 等于调用extend 函数，不是赋值
    # num_list.extend(num_list)
    num_list += num_list

    print(num)
    print(num_list)


gl_num = 10
gl_list = [4, 5, 6]

demo_num(gl_num, gl_list)

print(gl_num)
print(gl_list)
