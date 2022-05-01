"""
Created by hu-jinwen on 2022/4/19
"""


class A:

    def __init__(self):
        """"""
        self.num_01 = 100
        self.__num_02 = 200
        self.num_03 = 300


    def __test(self):
        print("这是私有方法 %d %d" % (self.num_01, self.__num_02))

    def test(self):
        print("这是公有方法 %d %d" % (self.num_01, self.num_03))


class B(A):

    def demo(self):

        print("访问父类的公有属性 %d %d" % (self.num_01, self.num_03))

        self.test()


a = A()

a.test()

b = B()
print(b)
b.demo()

