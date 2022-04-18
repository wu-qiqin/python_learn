"""
Created by hu-jinwen on 2022/4/17
"""
"""
小明体重 50公斤
小明每次跑步会减肥1公斤
小明每次吃饭会增加2公斤

"""


class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s 体重是%.2f公斤" % (self.name,self.weight)

    def run(self):
        print("%s 爱运动" % self.name)
        self.weight -= 1

    def eat(self):
        print("%s 是吃货" % self.name)
        self.weight += 2


xiaoming = Person("xiaoming", 50)

xiaoming.run()
xiaoming.eat()

print(xiaoming)

xiaomei = Person("xiaomei",40)
xiaomei.run()
xiaomei.eat()
print(xiaomei)