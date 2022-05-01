"""
Created by hu-jinwen on 2022/4/23
"""

"""
1. 设计一个game 类
2. 定义一个类属性 记录游戏最高分
   定义一个实例属性 记录当前玩家姓名
3. 方法：
静态方法：show help 显示游戏帮助信息
类方法：show_top_score 记录历史最高分
实例方法：start_game 开始当前玩家的游戏
4. 主程序步骤：
 查看帮助信息
 查看历史最高分
 创建游戏对象，开始游戏

"""


class Game:
    show_top_score = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_help():
        print("进入游戏")

    @classmethod
    def top_score(cls):
        print("这是游戏的历史最高分 %d" % cls.show_top_score)

    def start_game(self):
        print(" %s 游戏开始啦。。。" % self.name)



game = Game("小胡")
game.show_help()
game.top_score()
game.start_game()


