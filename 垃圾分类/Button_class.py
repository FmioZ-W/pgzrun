import pygame
import os

class Button(pygame.rect.Rect):        #构造矩形对象
    def __init__(self,object):
        #继承Rect类的构造方法
        super().__init__(object)
    def is_touch(self,pos):
        #检测有没有按到按钮
        if self.right >= pos[0] >= self.left and self.bottom >= pos[1] >= self.top:
            return True
        else:
            return False