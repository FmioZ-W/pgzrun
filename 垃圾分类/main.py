import pygame,pgzero,pgzrun
import sys,random,os
from Button_class import Button
from pygame.locals import *

pygame.init()
pygame.display.set_caption('垃圾分类')
#屏幕大小
screen = pygame.display.set_mode((1000,600))
#主界面
def main_show():
    #加载图片
    background = pygame.image.load('images\\back_main.png').convert()
    screen.blit(background,(0,0))
    game_info = pygame.image.load('images\\game_info.png')
    game_begin = pygame.image.load('images\\game_begin_text.png')
    game_begin_button = screen.blit(game_begin,(250,450))
    game_begin_button = Button(game_begin_button)
    game_end = pygame.image.load('images\\game_end_text.png')
    game_end_button = screen.blit(game_end,(650,450))
    game_end_button = Button(game_end_button)
    game_book = pygame.image.load('images\\game_book_text.png')
    game_book_button = screen.blit(game_book,(415,350))
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
                    help_info_display()                  #游戏说明
                if game_begin_button.is_touch(pos):
                    playground_page_show()                #游戏开始
                if game_end_button.is_touch(pos):        #退出游戏
                    print('再见！')
                    sys.exit()
        pygame.display.flip()


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
            main_show()
        pygame.display.flip()


<<<<<<< HEAD
#精灵类--垃圾桶
class Trash(pygame.sprite.Sprite):
    def __init__(self,img_file_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file_path)
        self.rect = self.image.get_rect()
        #self._layer = -1

#精灵类--垃圾
class Waste(pygame.sprite.Sprite):
    def __init__(self,img_file_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file_path)
        self.rect = self.image.get_rect()
        #self._layer = -2

choices = ['11','21','31','32','33','41','42']

# 鼠标是否在物体上
def is_in_rect(pos,rect):
    x, y = pos
    rx,ry,rw,rh = rect
    if (rx<=x<=rx+rw) and (ry<=y<=ry+rh):
        return True
    return False

def playground_page_show():

    background_plg = pygame.image.load('images\\playground_out.png')
    screen.blit(background_plg,(0,0))
    #垃圾桶精灵类
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
    waste_group1 = pygame.sprite.Group()         #精灵组--垃圾
    waste_group2 = pygame.sprite.Group()
    waste_group3 = pygame.sprite.Group()
    waste_group4 = pygame.sprite.Group()
    waste_group = pygame.sprite.Group()
    for s in choices:
        print(s)
        waste = Waste('images\\'+str(s)+'.png')
        waste_group.add(waste)
        if s[0]=='1':
            waste_group1.add(waste)
            print(len(waste_group1.sprites()))
        elif s[0]=='2':
            waste_group2.add(waste)
            print(len(waste_group2.sprites()))
        elif s[0]=='3':
            waste_group3.add(waste)
            print(len(waste_group3.sprites()))
        elif s[0]=='4':
            waste_group4.add(waste)
            print(len(waste_group4.sprites()))


    n = 7
    while n:
        # s = random.choice(choices)
        # choice_ = pygame.image.load('images\\'+str(s)+'.png')
        if n==1:
            flag_1 = flag_2 = flag_3 = flag_4 = False
            s1 = pygame.sprite.spritecollide(to_1,waste_group1,False)
            print(len(s1),len(waste_group1.sprites()))
            print(len(pygame.sprite.spritecollide(to_3,waste_group3,False)))
            if len(s1)==len(waste_group1.sprites()):
                flag_1 = True
            if len(pygame.sprite.spritecollide(to_2,waste_group2,False))==len(waste_group2.sprites()):
                flag_2 = True
            if len(pygame.sprite.spritecollide(to_3,waste_group3,False))==len(waste_group3.sprites()):
                flag_3 = True
            if len(pygame.sprite.spritecollide(to_4,waste_group4,False))==len(waste_group4.sprites()):
                flag_4 = True
            if flag_1 and flag_2 and flag_3 and flag_4:
                game_win = pygame.image.load('images\\game_win.png')
                screen.blit(game_win,(0,0))
                break
            else:
                game_fail = pygame.image.load('images\\game_fail.png')
                screen.blit(game_fail,(0,0))
                break
        choice_ = random.choice(list(waste_group))           #随机出现垃圾   精灵类
        choice_x = random.randint(50,900)                    #垃圾位置随机
        choice_y = random.randint(300,500)
        screen.blit(choice_.image,(choice_x,choice_y))
        pygame.display.flip()
        run_flag = True
        is_move = False
        flag = True
        while run_flag:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                #鼠标按下
                if event.type == MOUSEBUTTONDOWN:
                    w,h = choice_.image.get_size()
                    pos = pygame.mouse.get_pos()
                    if is_in_rect(event.pos,(choice_x,choice_y,w,h)):       # 鼠标是否在物体上
                        is_move = True
                    if info_button.is_touch(pos):
                        page_show()
                    if back_button.is_touch(pos):
                        main_show()
                #鼠标弹起
                if event.type == MOUSEBUTTONUP:
                    if is_move:
                        is_move = False
                        # bol = pygame.sprite.collide_rect(choice_,to_1)
                        # print(bol)
                        if pygame.sprite.collide_rect(choice_,to_1) or pygame.sprite.collide_rect(choice_,to_2) or\
                            pygame.sprite.collide_rect(choice_,to_3) or pygame.sprite.collide_rect(choice_,to_4):
                            screen.blit(background_plg, (0, 0))
                            screen.blit(to_1.image, (50, 70))
                            screen.blit(to_2.image, (300, 70))
                            screen.blit(to_3.image, (550, 70))
                            screen.blit(to_4.image, (800, 70))
                            screen.blit(info_lib, (5, 550))
                            screen.blit(back_, (5, 5))
                            run_flag = False
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
                        screen.blit(back_,(5,5))
                        screen.blit(choice_.image,(choice_x,choice_y))
                        pygame.display.flip()
            pygame.display.flip()
        n-=1

#playground_page_show()


def page_show():
    background_libin = pygame.image.load('images\\waste_main.png')
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
        img = pygame.image.load('images\\circle_waste_info.png')
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


main_show()
pygame.quit()
=======
pygame.quit()
>>>>>>> df723081dc548c1cd4758d2cb416f17527be0d45
