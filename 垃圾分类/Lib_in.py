'''图书馆内部垃圾种类说明选择函数'''
import pygame,pgzero,pgzrun
import sys,random,os

from Button_class import Button
pygame.init()
screen = pygame.display.set_mode((800,600))
#说明信息页面（）
def info_load(selection):
    #可循环垃圾
    if selection==1:
        img = pygame.image.load('images\\circle_waste.info.png')
        while True:
            screen.blit(img, (0, 0))
            pygame.display.update()
    #有害垃圾
    elif selection==2:
        img = pygame.image.load('images\\harmful_waste_info.png')
        while True:
            screen.blit(img, (0, 0))
            pygame.display.update()
    #干垃圾
    elif selection==3:
        img = pygame.image.load('images\\dry_waste_info.png')
        while True:
            screen.blit(img, (0, 0))
            pygame.display.update()
    #湿垃圾
    elif selection==4:
        img = pygame.image.load('images\\wet_waste_info.png')
        while True:
            screen.blit(img, (0, 0))
            pygame.display.update()