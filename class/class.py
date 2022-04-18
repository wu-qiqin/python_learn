"""
Created by hu-jinwen on 2022/4/17
"""


class Cat:
    def eat(self):
        print("小猫吃饭")

    def drink(self):
        print("小猫喝水")


tom = Cat()

tom.eat()
tom.drink()

print(tom)
addr = id(tom)
print(addr)
print("%x" % addr)
