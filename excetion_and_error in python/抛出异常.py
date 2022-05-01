"""
Created by hu-jinwen on 2022/4/24
"""


def input_password():
    pwd = input("请输入密码:")

    if len(pwd) >= 8:
        return pwd
    print("密码长度不够")

    ex = Exception("密码长度不够")
    raise ex


try:
    print(input_password())
except Exception as result:
    print(result)

