"""
Created by hu-jinwen on 2022/4/19
"""


class A:

    def num(self):
        self.num_01 = 100
        self.__num_02 = 200

    def __test(self):
        print("这是私有方法 %d %d" % (self.num_01, self.__num_02))


class B(A):
    def demo(self):
        # 访问父类的私有属性：NG
        print("调用A类的私有数字 %d %d" % (self.num_01, self.__num_02))
        # 访问父类的私有方法 ；NG
        self.__test()


b = B()
print(b)

print(b.__test)
b.demo()
