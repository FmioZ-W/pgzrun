import pygame,pgzero,pgzrun
import sys,random,os
from pygame.locals import *
from Button_class import Button
from Lib_in import page_show
pygame.init()
screen = pygame.display.set_mode((1000, 600))

#精灵类--垃圾桶
class Trash(pygame.sprite.Sprite):
    def __init__(self,img_file_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file_path)
        self.rect = self.image.get_rect()
        self._layer = -1

#精灵类--垃圾
class Waste(pygame.sprite.Sprite):
    def __init__(self,img_file_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file_path)
        self.rect = self.image.get_rect()
        self._layer = -2

choices = ['11','21','31','32','33','41','42']

def is_in_rect(pos,rect):
    x, y = pos
    rx,ry,rw,rh = rect
    if (rx<=x<=rx+rw) and (ry<=y<=ry+rh):
        return True
    return False

def playground_page_show():

    background_plg = pygame.image.load('images\\playground_out.png')
    screen.blit(background_plg,(0,0))
    to_1 = Trash('images\\circle_waste.png')
    screen.blit(to_1.image,(50,70))
    to_2 = Trash('images\\harmful_waste.png')
    screen.blit(to_2.image,(300,70))
    to_3 = Trash('images\\wet_waste.png')
    screen.blit(to_3.image,(550,70))
    to_4 = Trash('images\\dry_waste.png')
    screen.blit(to_4.image,(800,70))
    #图书馆说明按钮
    info_lib = pygame.image.load('images\\info_lib.png')
    info_button = screen.blit(info_lib,(5,550))
    info_button = Button(info_button)
    #返回按钮
    back_ = pygame.image.load('images\\back_button.png')
    back_button = screen.blit(back_,(5,5))
    back_button = Button(back_button)
    #s = random.choice(choices)
    #垃圾的精灵组
    waste_group = pygame.sprite.Group()         #精灵组--垃圾
    for s in choices:
        waste = Waste('images\\'+str(s)+'.png')
        waste_group.add(waste)


    n = 7
    while n:
        n-=1
        # s = random.choice(choices)
        # choice_ = pygame.image.load('images\\'+str(s)+'.png')
        choice_ = random.choice(list(waste_group))           #随机出现垃圾
        choice_x = random.randint(50,900)                    #垃圾位置随机
        choice_y = random.randint(250,550)
        screen.blit(choice_.image,(choice_x,choice_y))
        pygame.display.flip()
        run_flag = True
        is_move = False
        while run_flag:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                #鼠标按下
                if event.type == MOUSEBUTTONDOWN:
                    w,h = choice_.image.get_size()
                    pos = pygame.mouse.get_pos()
                    if is_in_rect(event.pos,(choice_x,choice_y,w,h)):
                        is_move = True
                    if info_button.is_touch(pos):
                        page_show()
                    if back_button.is_touch(pos):
                        main_show()
                #鼠标弹起
                if event.type == MOUSEBUTTONUP:
                    is_move = False
                #鼠标移动
                if event.type == MOUSEMOTION:
                    if is_move:
                        screen.blit(background_plg,(0,0))
                        x,y = event.pos
                        choice_w,choice_h = choice_.image.get_size()       #物体随鼠标移动
                        choice_x = x - choice_w/2
                        choice_y = y - choice_h/2
                        screen.blit(background_plg,(0,0))
                        screen.blit(to_1.image, (50, 70))
                        screen.blit(to_2.image, (300, 70))
                        screen.blit(to_3.image, (550, 70))
                        screen.blit(to_4.image, (800, 70))
                        screen.blit(info_lib, (5, 550))
                        screen.blit(choice_.image,(choice_x,choice_y))
                        pygame.display.flip()


            pygame.display.flip()
#playground_page_show()


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
                if back_button.is_touch(pos):
                    playground_page_show()
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