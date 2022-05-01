"""
Created by hu-jinwen on 2022/4/19
"""


class Animal:
    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")


class Dog(Animal):
    def bark(self):
        print("wangwang")


class XTQ(Dog):
    def fly(self):
        print(" i  can fly")


class Cat(Animal):
    def catch(self):
        print("catch a rat")


xtq = XTQ()
xtq.fly()
xtq.bark()
xtq.eat()

