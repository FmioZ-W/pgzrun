import pygame,pgzero,pgzrun
import sys,random,os

from help_page import help_info_display
from Button_class import Button
from pygame.locals import *

pygame.init()
pygame.display.set_caption('垃圾分类')
#屏幕大小
screen = pygame.display.set_mode((1000,600))
#主界面
#加载图片
background = pygame.image.load('images\\background_main.png').convert()
screen.blit(background,(0,0))
game_info = pygame.image.load('images\\game_info.png')
game_begin = pygame.image.load('images\\game_begin_text.png')
game_begin_button = screen.blit(game_begin,(150,450))
game_begin_button = Button(game_begin_button)
game_end = pygame.image.load('images\\game_end_text.png')
game_end_button = screen.blit(game_end,(550,450))
game_end_button = Button(game_end_button)
game_book = pygame.image.load('images\\game_book_text.png')
game_book_button = screen.blit(game_book,(315,350))
game_book_button = Button(game_book_button)
pygame.display.flip()    #完整显示Surface更新到屏幕
while True:
    for event in pygame.event.get():  # 循环获取事件
        if event.type == QUIT:  # 若检测到事件类型为退出，则退出系统
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos,game_book_button.top,game_book_button.bottom)
            if game_book_button.is_touch(pos):
                help_info_display()
    pygame.display.flip()


pygame.quit()