"""
Created by hu-jinwen on 2022/4/26
"""
import pygame
pygame.init()

screen = pygame.display.set_mode((480,700))

# 绘制背景图像:
# 加载图像数据
bg = pygame.image.load("./雷霆战机/images/bg/bg1.jpg")

# blit 绘制图像
screen.blit(bg, (0, 0))

# update 更新屏幕显示
pygame.display.update()


#游戏循环
# while True:
#     pass


pygame.quit()

