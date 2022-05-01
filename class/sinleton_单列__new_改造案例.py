"""
Created by hu-jinwen on 2022/4/23
"""

class Game:

    ins = None
    int_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.ins is None:
            cls.ins = super().__new__(cls)
        return cls.ins


    def __init__(self):
        if Game.int_flag:
             return
        print("设定初始值")
        Game.int_flag = True


game1 = Game()
print(game1)

game2 = Game()
print(game2)