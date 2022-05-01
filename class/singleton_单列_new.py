"""
Created by hu-jinwen on 2022/4/23
"""


class Game:
    def __new__(cls, *args, **kwargs):
        print("开始游戏")

        a = super().__new__(cls)
        return a

    def __init__(self):
        print("设定初始值")


game = Game()
# print(game)
