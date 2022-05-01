"""
Created by hu-jinwen on 2022/4/27
"""
import random

import pygame

# 定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义每秒变化的帧数
FREME_PER_SEC = 60
# 创建敌机的定时器
CREASTE_ENEMY_EVEVT = pygame.USEREVENT

# 定义英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

# 定义敌机子弹发射事件
ENEMY_FIRE_EVENT = pygame.USEREVENT +2


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, self_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(self_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """ 背景精灵"""

    # 调用父类屏幕上下移动属性
    def update(self):
        # 判断背景图像是否移除屏幕, 如果移除屏幕，将背景移到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    def __init__(self):
        # 调用父类方法创建敌机精灵 同时指定敌机图片
        super().__init__("./雷霆战机/images/enemy/enemy1.png")

        # 指定敌机的初始随机速度 3-7
        self.speed = random.randint(3, 7)

        # 指定敌机的初始随机位置
        self.rect.y = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        # 创建子弹精灵组
        self.enemy_bullets = pygame.sprite.Group()

    def update(self):
        # 调用父类方法，保持垂直飞行
        super().update()

        # 判断飞机是否飞出屏幕，如果是，需要从精灵组 移除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组移出敌机")
            # kill 方法可以将精灵从精灵组中移除
            self.kill()

    def __del__(self):
        # print("敌机爆炸。。%s" % self.rect)
        pass

    def enemy_fire(self):

        # 创建子弹
        enemy_bullet = Enemy_Bullet()
        # 设置精灵的位置
        enemy_bullet.rect.bottom = - self.rect.bottom
        enemy_bullet.rect.centerx = random.randint(0, 480)
        # 将精灵添加到精灵组
        self.enemy_bullets.add(enemy_bullet)


class Hero(GameSprite):
    """ 英雄精灵"""

    def __init__(self):
        # 调用父类方法，设置image 和speed
        super().__init__("./雷霆战机/images/hero/hero01.png", 0)
        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

        self.speed = 5




    def update(self):
        self.move()
        # self.fire()
        # 英雄在水平方向的移动
        # super().update()
        # print("update....")
        # self.rect.x += self.speed
        # print(f"rect.x => {self.rect.x}")
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 700:
            self.rect.bottom = 700

    def move(self):
        """"""
        # 使用键盘提供的方法获取键盘按键  按键元组
        key_pressed = pygame.key.get_pressed()
        # print(key_pressed)

        # 判断元祖中获取的索引值 1
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif key_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        elif key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed
        # else:
        #     self.hero.speed = 0

            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > SCREEN_RECT.x:
                self.rect.x = SCREEN_RECT.x-self.rect.x
            elif self.rect.y < 0:
                self.rect.y = 0
            else:
                self.rect.y = 700

    def fire(self):

        # 创建子弹
        bullet = Bullet()

        # 设置精灵的位置
        bullet.rect.bottom = self.rect.bottom
        bullet.rect.centerx = self.rect.centerx
        # 将精灵添加到精灵组
        self.bullets.add(bullet)


class Bullet(GameSprite):
    # 子弹精灵
    def __init__(self):
        # 调用父类方法，设置子弹图片，同时设置初始速度
        super().__init__("./雷霆战机/images/bullet/bullet.png", -2)

    def update(self):
        # 调用父类方法，让子弹垂直发射
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁。。")


class Enemy_Bullet(GameSprite):

    def __init__(self):
        super().__init__("./雷霆战机/images/bullet/enemy_bullet.png", speed=random.randint(1,4))

    def update(self):
        # 调用父类方法，让敌机子弹垂直发射
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.top > 700:
            self.kill()

    def __del__(self):
        print("敌机子弹被销毁。。。")


