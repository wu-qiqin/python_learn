"""
Created by hu-jinwen on 2022/4/14
"""


def test(num):
    result = "hello"
    print("%s  :函数要返回数据的内存地址是 %d" % (result, id(result)))

    # return result


test("hello")

print(id(12))

d = {}
