'''图书馆内部垃圾种类说明选择函数'''
import pygame,pgzero,pgzrun
import sys,random,os
from pygame.locals import *
from Button_class import Button

pygame.init()
screen = pygame.display.set_mode((1000, 600))

def page_show():
    background_libin = pygame.image.load('images\\libriry_in.png')
    screen.blit(background_libin,(0,0))
    # fontType = os.path.join('fonts\\myrb.ttf')
    # fontObject = pygame.font.Font(fontType,32)
    # text_info = fontObject.render('要学会分类哦',True,(255,255,255))
    # background_libin.blit(text_info,(20,200))
    circle_waste = pygame.image.load('images\\circle_waste.png')
    circle_waste_button = screen.blit(circle_waste,(50,100))
    circle_waste_button = Button(circle_waste_button)
    harmful_waste = pygame.image.load('images\\harmful_waste.png')
    harmful_waste_button = screen.blit(harmful_waste,(300,100))
    harmful_waste_button = Button(harmful_waste_button)
    wet_waste = pygame.image.load('images\\wet_waste.png')
    wet_waste_button = screen.blit(wet_waste,(550,100))
    wet_waste_button = Button(wet_waste_button)
    dry_waste = pygame.image.load('images\\dry_waste.png')
    dry_waste_button = screen.blit(dry_waste,(800,100))
    dry_waste_button = Button(dry_waste_button)
    back = pygame.image.load('images\\back_button.png')
    back_button = screen.blit(back, (5, 5))
    back_button = Button(back_button)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if circle_waste_button.is_touch(pos):
                    info_load(1)
                elif harmful_waste_button.is_touch(pos):
                    info_load(2)
                elif wet_waste_button.is_touch(pos):
                    info_load(3)
                elif dry_waste_button.is_touch(pos):
                    info_load(4)
        pygame.display.flip()
#说明信息页面（）
def info_load(selection):
    #可循环垃圾
    screen = pygame.display.set_mode((1000, 600))
    if selection==1:
        img = pygame.image.load('images\\circle_waste.info.png')
        back = pygame.image.load('images\\back_button.png')
        back_button = screen.blit(back, (5, 5))
        back_button = Button(back_button)
        pygame.display.flip()
        while True:
            screen.blit(img, (0, 0))
            screen.blit(back, (5, 5))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==QUIT:
                    sys.exit()
                if event.type==MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if back_button.is_touch(pos):
                        page_show()
    #有害垃圾
    elif selection==2:
        img = pygame.image.load('images\\harmful_waste_info.png')
        back = pygame.image.load('images\\back_button.png')
        back_button = screen.blit(back, (5, 5))
        back_button = Button(back_button)
        pygame.display.flip()
        while True:
            screen.blit(img, (0, 0))
            screen.blit(back, (5, 5))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==QUIT:
                    sys.exit()
                if event.type==MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if back_button.is_touch(pos):
                        page_show()
    #干垃圾
    elif selection==3:
        img = pygame.image.load('images\\dry_waste_info.png')
        back = pygame.image.load('images\\back_button.png')
        back_button = screen.blit(back, (5, 5))
        back_button = Button(back_button)
        pygame.display.flip()
        while True:
            screen.blit(img, (0, 0))
            screen.blit(back, (5, 5))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==QUIT:
                    sys.exit()
                if event.type==MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if back_button.is_touch(pos):
                        page_show()
    #湿垃圾
    elif selection==4:
        img = pygame.image.load('images\\wet_waste_info.png')
        back = pygame.image.load('images\\back_button.png')
        back_button = screen.blit(back, (5, 5))
        back_button = Button(back_button)
        pygame.display.flip()
        while True:
            screen.blit(img, (0, 0))
            screen.blit(back,(5,5))
            #pygame.display.update()
            for event in pygame.event.get():
                if event.type==QUIT:
                    sys.exit()
                if event.type==MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if back_button.is_touch(pos):
                        page_show()
            pygame.display.flip()

#page_show()
