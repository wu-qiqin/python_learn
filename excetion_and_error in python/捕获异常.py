"""
Created by hu-jinwen on 2022/4/24
"""

try:
    num = int (input("请输入整数："))

    result = 5 / num

    print(result)

except ValueError:
    print("值错误：")

except Exception as result:
    print("未知错误； %s" % result)

else:
    print("输入正确")
finally:
    print("必须输出信息")

print("*" * 30)