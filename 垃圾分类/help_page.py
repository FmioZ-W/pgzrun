import pygame,pgzero,pgzrun
import sys,random,os
from pygame.locals import *
from Button_class import Button

def help_info_display():
    screen = pygame.display.set_mode((1000,600))
    background_help = pygame.image.load('images\\game_info.png')
    screen.blit(background_help,(0,0))
    back = pygame.image.load('images\\back_button.png')
    back_button = screen.blit(back,(5,5))
    back_button = Button(back_button)
    pygame.display.flip()
    flag_bc = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if back_button.is_touch(pos):
                    flag_bc = 1
                    break
        if flag_bc == 1:
            break
       # pygame.display.flip()

help_info_display()