"""
Created by hu-jinwen on 2022/4/17
"""

class Cat:
# init 属性 01-名词
# 方法 02-动词
    def __init__(self,new_name):
        self.name = new_name

    def drink(self):
        print("%s喝水" % self.name)

    def __del__(self):
        print("%s gone" % self.name)

    def __str__(self):
        return "我是小猫[ %s ]" % self.name


tom = Cat("Tom")
# tom.drink()

print(tom)
#
# lazy_cat = Cat("Lazy_cat")
# lazy_cat.drink()
#
# # del 关键字可以删除一个对象
# del tom
#
# print("*"*50)
#
