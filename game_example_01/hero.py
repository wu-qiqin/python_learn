"""
Created by hu-jinwen on 2022/4/26
"""

import pygame

from plane_spirits import *

# 游戏初始化
pygame.init()

screen = pygame.display.set_mode((480,700))

# 绘制背景图像:
# 加载图像数据
bg = pygame.image.load("./雷霆战机/images/bg/bg1.jpg")

# blit 绘制图像
screen.blit(bg, (0, 0))

# update 更新屏幕显示
pygame.display.update()


# 绘制英雄的飞机
# 加载英雄图像数据
hero = pygame.image.load("./雷霆战机/images/hero/hero.png")
# blit 绘制图像
screen.blit(hero, (100,100))
# update 更新屏幕显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 01 定义rect 记录飞机的初始位置
hero_rect = pygame.Rect(150,300,80,100)

# 01 创建敌机精灵
enemy = GameSprite("./雷霆战机/images/enemy/enemy.png")
enemy_1 = GameSprite("./雷霆战机/images/enemy/enemy1.png", 2)
# 02 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy_1,enemy)


# #游戏循环
while True:

    clock.tick(60)

    for even in pygame.event.get() :
        # 判断事件类型，是否是退出事件
        if even.type == pygame.QUIT:
            print("退出游戏。。。")

            pygame.quit()
            exit()

# 02 修改飞机的位置
    hero_rect.y -= 5
    if hero_rect.y <= -100:
        hero_rect.y = 700


# 03 调用blit 方法绘制图像
    screen.blit(bg, (0,0))
    screen.blit(hero,hero_rect)


# 01 让敌机的精灵组调用两个方法
# update--让组内所用精灵更新位置
    enemy_group.update()
# draw
    enemy_group.draw(screen)
# 04 调用update 方法更新显示
    pygame.display.update()

    pass


pygame.quit()

