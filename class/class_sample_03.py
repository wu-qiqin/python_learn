"""
Created by hu-jinwen on 2022/4/18
"""
"""
士兵突击
需求：
士兵小胡有一把手枪ak47
士兵可以开火
手枪可以发射子弹
枪可以装子弹---增加子弹数量

假设每个新兵都无枪

开发过程中 如果不知道定义什么初始值，可以设置为None

"""

class Gun:
    def __init__(self, model):
        self.model = model

        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("%s 没有子弹了。。" % self.model)

            return

        self.bullet_count -= 1
        print("%s 突突突。。。[%d]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name

        self.gun = None

    def fire(self):
        # 判断是否有枪
        #if self.gun == None:
        if self.gun is None:

            print("%s 还没有枪，无法射击" % self.name)
            return

        # 高喊口号
        print("加油，冲！！！ %s" % self.name)

        # 让枪装填子弹
        self.gun.add_bullet(10)

        # 发射子弹
        self.gun.shoot()


ak47 = Gun("ak47")

xiaohu = Soldier("小胡")

xiaohu.gun = ak47
xiaohu.fire()

print(xiaohu.gun)