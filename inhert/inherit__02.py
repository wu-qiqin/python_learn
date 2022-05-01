"""
Created by hu-jinwen on 2022/4/19
"""


class Animal:
    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run (self):
        print("run")


class Dog(Animal):
    def bark(self):
        print("wangwang")


class XTQ(Dog):
    def fly(self):
        print(" i  can fly")

    def bark(self):
        # 针对子类的特殊方法
        print("wang fly")
        # super.
        # super().bark()
        Dog.bark(self)
        #如果使用子类调用，会出现死循环（递归调用）
        #XTQ.bark(self)

        # 增加其他的子类代码
        print("$#$%$^$&")


xtq = XTQ()
xtq.fly()
xtq.bark()


