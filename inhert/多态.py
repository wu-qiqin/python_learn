"""
Created by hu-jinwen on 2022/4/21
"""


class Dog(object):
    def __init__(self,name):
        self.name = name

    def game(self):
        print("%s 欢乐的玩耍" % self.name)


class Xiaotianqian(Dog):
    def game(self):
        print("%s 飞到天上玩" % self.name)

class Person(object):
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s and %s 快乐的玩耍" % (self.name, dog.name))


#wangcai = Dog("wangcai")
# wangcai.game()

wangcai = Xiaotianqian("wangcai dog")
wangcai.game()

xiaohu = Person("xiaohu")
xiaohu.game_with_dog(wangcai)

