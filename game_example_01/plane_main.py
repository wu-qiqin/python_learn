"""
Created by hu-jinwen on 2022/4/28
"""

from plane_spirits import *


class PlaneGame(object):
    """"定义飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        # 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有化方法，精灵和精灵组创建
        self.__creat_spirits()
        # 设置定时器事件-创建敌机
        pygame.time.set_timer(CREASTE_ENEMY_EVEVT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
        pygame.time.set_timer(ENEMY_FIRE_EVENT, random.randint(500, 1000))

    def __creat_spirits(self):
        # 创建背景精灵
        bg1 = Background("./雷霆战机/images/bg/bg2.jpg")
        bg2 = Background("./雷霆战机/images/bg/bg2.jpg")
        bg2.rect.y = -bg2.rect.height
        self.bg_group = pygame.sprite.Group(bg2, bg1)

        # 创建敌机的精灵组
        self.enemy = Enemy()
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄和英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):

        print("游戏开始。。。")

        while True:
            # 设置刷新帧率
            self.clock.tick(FREME_PER_SEC)
            # 事件监听
            self.__event_handle()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_spirits()
            # 更新显示
            pygame.display.update()

    def __event_handle(self):
        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.game_over()
                continue
            elif event.type == CREASTE_ENEMY_EVEVT:
                # print("敌机出现。。。")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机添加到精灵组
                self.enemy_group.add(enemy)
                continue
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            elif event.type == ENEMY_FIRE_EVENT:
                self.enemy.enemy_fire()
                # print("敌机发射。。。")

    def __check_collide(self):
        # 子弹摧毁敌机功能
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 敌机撞毁英雄
        enemy_list = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表是否有内容
        if len(enemy_list) > 0:
            # 英雄牺牲
            self.hero.kill()
            # 游戏结束
            PlaneGame.game_over()
        # 敌机的子弹摧毁英雄
        bullet_list = pygame.sprite.spritecollide(self.hero, self.enemy.enemy_bullets, True)
        # t1 = pygame.time.wait(3000)
        # print(t1)
        # 判断列表是否有内容
        if len(bullet_list) > 0:
            # 英雄牺牲
            self.hero.kill()
            self.enemy.enemy_bullets.kill()
            print("game over")
            # 游戏结束
            PlaneGame.game_over()

    def __update_spirits(self):

        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        self.enemy.enemy_bullets.update()
        self.enemy.enemy_bullets.draw(self.screen)

    @staticmethod
    def game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
