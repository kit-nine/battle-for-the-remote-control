from turtle import Screen
import pygame, sys
from pygame.locals import *
pygame.init()

SCREEN = pygame.display.set_mode((640, 480))
CLOCK = pygame.time.Clock()
FPS = 30
MOVEMENT_SPEED = 5
m1ilist,m1blist,m1flist,m1llist,m1rlist = [],[],[],[],[]

for i in range(4):
    m1ilist.append(pygame.image.load("m1\m1b" + str(0) + ".png").convert_alpha())
    m1blist.append(pygame.image.load("m1\m1b" + str(i) + ".png").convert_alpha())
    m1flist.append(pygame.image.load("m1\m1f" + str(i) + ".png").convert_alpha())
    m1llist.append(pygame.image.load("m1\m1l" + str(i) + ".png").convert_alpha())
    m1rlist.append(pygame.image.load("m1\m1r" + str(i) + ".png").convert_alpha())

class ColorMonster:
    def __init__(self,x,y,framerate):
        self.x = x
        self.y = y
        self.face = "back"
        self.frame = 0
        self.cycle = 0
        self.current_sprite_list = m1blist
        self.current_sprite = self.current_sprite_list[self.frame]
        self.interval = int(1000/framerate)

    def update(self):
        self.cycle += dt # this error doesnt matter because this code doesnt need to run, it only works in the main file
        if self.cycle >= self.interval:
            self.cycle = 0
            self.frame += 1
        if self.frame >= len(self.current_sprite_list):
            self.frame = 0
        if self.face == "back":
            self.current_sprite_list = m1blist
        if self.face == "forward":
            self.current_sprite_list = m1flist
        if self.face == "right":
            self.current_sprite_list = m1rlist
        if self.face == "left":
            self.current_sprite_list = m1llist
        if self.face == "idle":
            self.current_sprite_list = m1ilist
        self.current_sprite = self.current_sprite_list[self.frame]

    def draw(self,surface):
        self.update()
        surface.blit(self.current_sprite,(self.x,self.y))
    
    # going to need another method for movement on its own, just a simple algorithm that
    # moves it across the screen and then teleports it to a specific place so it looks like
    # theres more of them on the screen at once than there really are
    