import pygame, sys
from pygame.locals import *
pygame.init()
SCREEN = pygame.display.set_mode((640, 480))
CLOCK = pygame.time.Clock()
FPS = 30
MOVEMENT_SPEED = 2
ARCADE_MODE = False

dt = 0
c1ilist,c1blist,c1flist,c1llist,c1rlist,c2ilist,c2blist,c2flist,c2llist,c2rlist,c3ilist,c3blist,c3flist,c3llist,c3rlist,c4ilist,c4blist,c4flist,c4llist,c4rlist,c5ilist,c5blist,c5flist,c5llist,c5rlist,c6ilist,c6blist,c6flist,c6llist,c6rlist = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

for i in range(4):
    c1ilist.append(pygame.image.load("c1\c1b" + str(0) + ".png").convert_alpha())
    c1blist.append(pygame.image.load("c1\c1b" + str(i) + ".png").convert_alpha())
    c1flist.append(pygame.image.load("c1\c1f" + str(i) + ".png").convert_alpha())
    c1llist.append(pygame.image.load("c1\c1l" + str(i) + ".png").convert_alpha())
    c1rlist.append(pygame.image.load("c1\c1r" + str(i) + ".png").convert_alpha())
for i in range(4):
    c2ilist.append(pygame.image.load("c2\c2b" + str(0) + ".png").convert_alpha())
    c2blist.append(pygame.image.load("c2\c2b" + str(i) + ".png").convert_alpha())
    c2flist.append(pygame.image.load("c2\c2f" + str(i) + ".png").convert_alpha())
    c2llist.append(pygame.image.load("c2\c2l" + str(i) + ".png").convert_alpha())
    c2rlist.append(pygame.image.load("c2\c2r" + str(i) + ".png").convert_alpha())
for i in range(4):
    c3ilist.append(pygame.image.load("c3\c3b" + str(0) + ".png").convert_alpha())
    c3blist.append(pygame.image.load("c3\c3b" + str(i) + ".png").convert_alpha())
    c3flist.append(pygame.image.load("c3\c3f" + str(i) + ".png").convert_alpha())
    c3llist.append(pygame.image.load("c3\c3l" + str(i) + ".png").convert_alpha())
    c3rlist.append(pygame.image.load("c3\c3r" + str(i) + ".png").convert_alpha())
for i in range(4):
    c4ilist.append(pygame.image.load("c4\c4b" + str(0) + ".png").convert_alpha())
    c4blist.append(pygame.image.load("c4\c4b" + str(i) + ".png").convert_alpha())
    c4flist.append(pygame.image.load("c4\c4f" + str(i) + ".png").convert_alpha())
    c4llist.append(pygame.image.load("c4\c4l" + str(i) + ".png").convert_alpha())
    c4rlist.append(pygame.image.load("c4\c4r" + str(i) + ".png").convert_alpha())
for i in range(4):
    c5ilist.append(pygame.image.load("c5\c5b" + str(0) + ".png").convert_alpha())
    c5blist.append(pygame.image.load("c5\c5b" + str(i) + ".png").convert_alpha())
    c5flist.append(pygame.image.load("c5\c5f" + str(i) + ".png").convert_alpha())
    c5llist.append(pygame.image.load("c5\c5l" + str(i) + ".png").convert_alpha())
    c5rlist.append(pygame.image.load("c5\c5r" + str(i) + ".png").convert_alpha())
for i in range(4):
    c6ilist.append(pygame.image.load("c6\c6b" + str(0) + ".png").convert_alpha())
    c6blist.append(pygame.image.load("c6\c6b" + str(i) + ".png").convert_alpha())
    c6flist.append(pygame.image.load("c6\c6f" + str(i) + ".png").convert_alpha())
    c6llist.append(pygame.image.load("c6\c6l" + str(i) + ".png").convert_alpha())
    c6rlist.append(pygame.image.load("c6\c6r" + str(i) + ".png").convert_alpha())

class Player:
    global MOVEMENT_SPEED
    def __init__(self, x, y, framerate):
        self.x = x
        self.y = y
        self.face = "back"
        self.frame = 0
        self.cycle = 0
        self.current_sprite_list = c1blist
        self.current_sprite = self.current_sprite_list[self.frame]
        self.interval = int(1000/framerate)

    def update(self):
        # increase frame when appropriate
        self.cycle += dt
        if self.cycle >= self.interval:
            self.cycle = 0
            self.frame += 1
        # reset frame w. a.
        if self.frame >= len(self.current_sprite_list):
            self.frame = 0
        # change current_sprite_list based on face
        if self.face == "back":
            self.current_sprite_list = c1blist
        if self.face == "forward":
            self.current_sprite_list = c1flist
        if self.face == "right":
            self.current_sprite_list = c1rlist
        if self.face == "left":
            self.current_sprite_list = c1llist
        if self.face == "idle":
            self.current_sprite_list = c1ilist
        # update current_sprite w. a.
        self.current_sprite = self.current_sprite_list[self.frame]

    def draw(self,surface):
        self.update()
        surface.blit(self.current_sprite,(self.x,self.y))

player_1 = Player(250,250,6)
                     
while True:
    SCREEN.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pressed = pygame.key.get_pressed()
    if ARCADE_MODE == False:      
        if pressed[K_w]:
            player_1.face = "forward"
            player_1.y -= MOVEMENT_SPEED
        if pressed[K_s]:
            player_1.face = "back"
            player_1.y += MOVEMENT_SPEED
        if pressed[K_a]:
            player_1.face = "left"
            player_1.x -= MOVEMENT_SPEED
        if pressed[K_d]:
            player_1.face = "right"
            player_1.x += MOVEMENT_SPEED
        elif pressed[K_w] == False and pressed[K_s] == False and pressed[K_a] == False and pressed[K_d] == False:
            player_1.face = "idle"
    #print(player_1.current_sprite_list[0])        
    player_1.draw(SCREEN)
    pygame.display.update()
    dt = CLOCK.tick(FPS)
        