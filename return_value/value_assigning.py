"""
Created by hu-jinwen on 2022/4/16
"""


def demo_num(num, num_list):
    """

    :type num_list: object
    """
    # num = 100
    # num_list = [1, 2, 3]
    num_list.append(7)
    print(num)
    print(num_list)


gl_num = 10
gl_list = [4, 5, 6]

demo_num(gl_num, gl_list)

print(gl_num)
print(gl_list)
