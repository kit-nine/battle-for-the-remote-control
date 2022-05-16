import pygame, sys, random
from pygame.locals import *
pygame.init()
pygame.mixer.init(48000,-16,2,1024)
# constants
SCREEN = pygame.display.set_mode((640, 480))
CLOCK = pygame.time.Clock()
FPS = 30
MOVEMENT_SPEED = 5
ARCADE_MODE = False
MENU = pygame.image.load("Main Menu.png")
INSTRUCTIONS = pygame.image.load("Instructions.png").convert()
SPACE_PURPOSE = pygame.image.load("instructions_button_purposes/purpose_space.png").convert()
RETURN_PURPOSE = pygame.image.load("instructions_button_purposes/purpose_return.png").convert()
UP_PURPOSE = pygame.image.load("instructions_button_purposes/purpose_up.png").convert()
DOWN_PURPOSE = pygame.image.load("instructions_button_purposes/purpose_down.png").convert()
LEFT_PURPOSE = pygame.image.load("instructions_button_purposes/purpose_left.png").convert()
RIGHT_PURPOSE = pygame.image.load("instructions_button_purposes/purpose_right.png").convert()
TILE0 = pygame.image.load("tiling/tile0.png").convert()
TILE1 = pygame.image.load("tiling/tile1.png").convert()
SELECT = pygame.mixer.Sound("sounds/selection.wav")
STEP = pygame.mixer.Sound("sounds/footstep.wav")
OUTRO = pygame.mixer.Sound("sounds/outro.wav")
MINIGAME = pygame.image.load("minigame.png")
GAME = pygame.image.load("game.png")
# variables
left_click = False
mouse_x,mouse_y = 0,0
mouse_speed = 5
gamemode = "menu"
background_reset = True
dt = 0
c1ilist,c1blist,c1flist,c1llist,c1rlist,c2ilist,c2blist,c2flist,c2llist,c2rlist,c3ilist,c3blist,c3flist,c3llist,c3rlist,c4ilist,c4blist,c4flist,c4llist,c4rlist,c5ilist,c5blist,c5flist,c5llist,c5rlist,c6ilist,c6blist,c6flist,c6llist,c6rlist = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
m1ilist,m1blist,m1flist,m1llist,m1rlist,m2ilist,m2blist,m2flist,m2llist,m2rlist,m3ilist,m3blist,m3flist,m3llist,m3rlist,m4ilist,m4blist,m4flist,m4llist,m4rlist,m5ilist,m5blist,m5flist,m5llist,m5rlist,m6ilist,m6blist,m6flist,m6llist,m6rlist = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
p1_proj_list = []
p2_proj_list = []
playing_sound_select,playing_sound_step,playing_sound_outro = False, False, False
character = "default"
bg_y_pos = -4313
# loading sprites
for i in range(4):
    # characters
    c1ilist.append(pygame.image.load("c1\c1b" + str(0) + ".png").convert_alpha())
    c1blist.append(pygame.image.load("c1\c1b" + str(i) + ".png").convert_alpha())
    c1flist.append(pygame.image.load("c1\c1f" + str(i) + ".png").convert_alpha())
    c1llist.append(pygame.image.load("c1\c1l" + str(i) + ".png").convert_alpha())
    c1rlist.append(pygame.image.load("c1\c1r" + str(i) + ".png").convert_alpha())
    c2ilist.append(pygame.image.load("c2\c2b" + str(0) + ".png").convert_alpha())
    c2blist.append(pygame.image.load("c2\c2b" + str(i) + ".png").convert_alpha())
    c2flist.append(pygame.image.load("c2\c2f" + str(i) + ".png").convert_alpha())
    c2llist.append(pygame.image.load("c2\c2l" + str(i) + ".png").convert_alpha())
    c2rlist.append(pygame.image.load("c2\c2r" + str(i) + ".png").convert_alpha())
    c3ilist.append(pygame.image.load("c3\c3b" + str(0) + ".png").convert_alpha())
    c3blist.append(pygame.image.load("c3\c3b" + str(i) + ".png").convert_alpha())
    c3flist.append(pygame.image.load("c3\c3f" + str(i) + ".png").convert_alpha())
    c3llist.append(pygame.image.load("c3\c3l" + str(i) + ".png").convert_alpha())
    c3rlist.append(pygame.image.load("c3\c3r" + str(i) + ".png").convert_alpha())
    c4ilist.append(pygame.image.load("c4\c4b" + str(0) + ".png").convert_alpha())
    c4blist.append(pygame.image.load("c4\c4b" + str(i) + ".png").convert_alpha())
    c4flist.append(pygame.image.load("c4\c4f" + str(i) + ".png").convert_alpha())
    c4llist.append(pygame.image.load("c4\c4l" + str(i) + ".png").convert_alpha())
    c4rlist.append(pygame.image.load("c4\c4r" + str(i) + ".png").convert_alpha())
    c5ilist.append(pygame.image.load("c5\c5b" + str(0) + ".png").convert_alpha())
    c5blist.append(pygame.image.load("c5\c5b" + str(i) + ".png").convert_alpha())
    c5flist.append(pygame.image.load("c5\c5f" + str(i) + ".png").convert_alpha())
    c5llist.append(pygame.image.load("c5\c5l" + str(i) + ".png").convert_alpha())
    c5rlist.append(pygame.image.load("c5\c5r" + str(i) + ".png").convert_alpha())
    c6ilist.append(pygame.image.load("c6\c6b" + str(0) + ".png").convert_alpha())
    c6blist.append(pygame.image.load("c6\c6b" + str(i) + ".png").convert_alpha())
    c6flist.append(pygame.image.load("c6\c6f" + str(i) + ".png").convert_alpha())
    c6llist.append(pygame.image.load("c6\c6l" + str(i) + ".png").convert_alpha())
    c6rlist.append(pygame.image.load("c6\c6r" + str(i) + ".png").convert_alpha())
    # color monsters
    m1blist.append(pygame.image.load("m1\m1b" + str(i) + ".png").convert_alpha())
    m1flist.append(pygame.image.load("m1\m1f" + str(i) + ".png").convert_alpha())
    m1llist.append(pygame.image.load("m1\m1l" + str(i) + ".png").convert_alpha())
    m1rlist.append(pygame.image.load("m1\m1r" + str(i) + ".png").convert_alpha())
    m2blist.append(pygame.image.load("m2\m2b" + str(i) + ".png").convert_alpha())
    m2flist.append(pygame.image.load("m2\m2f" + str(i) + ".png").convert_alpha())
    m2llist.append(pygame.image.load("m2\m2l" + str(i) + ".png").convert_alpha())
    m2rlist.append(pygame.image.load("m2\m2r" + str(i) + ".png").convert_alpha())
    m3blist.append(pygame.image.load("m3\m3b" + str(i) + ".png").convert_alpha())
    m3flist.append(pygame.image.load("m3\m3f" + str(i) + ".png").convert_alpha())
    m3llist.append(pygame.image.load("m3\m3l" + str(i) + ".png").convert_alpha())
    m3rlist.append(pygame.image.load("m3\m3r" + str(i) + ".png").convert_alpha())
    m4blist.append(pygame.image.load("m4\m4b" + str(i) + ".png").convert_alpha())
    m4flist.append(pygame.image.load("m4\m4f" + str(i) + ".png").convert_alpha())
    m4llist.append(pygame.image.load("m4\m4l" + str(i) + ".png").convert_alpha())
    m4rlist.append(pygame.image.load("m4\m4r" + str(i) + ".png").convert_alpha())
    m5blist.append(pygame.image.load("m5\m5b" + str(i) + ".png").convert_alpha())
    m5flist.append(pygame.image.load("m5\m5f" + str(i) + ".png").convert_alpha())
    m5llist.append(pygame.image.load("m5\m5l" + str(i) + ".png").convert_alpha())
    m5rlist.append(pygame.image.load("m5\m5r" + str(i) + ".png").convert_alpha())
    m6blist.append(pygame.image.load("m6\m6b" + str(i) + ".png").convert_alpha())
    m6flist.append(pygame.image.load("m6\m6f" + str(i) + ".png").convert_alpha())
    m6llist.append(pygame.image.load("m6\m6l" + str(i) + ".png").convert_alpha())
    m6rlist.append(pygame.image.load("m6\m6r" + str(i) + ".png").convert_alpha())
# player class
class Player:
    global MOVEMENT_SPEED
    def __init__(self, x, y, framerate, proj_list, character):
        self.x = x
        self.y = y
        self.proj_list = proj_list
        self.character = character
        self.face = "back"
        self.frame = 0
        self.cycle = 0
        if self.character == 1 or self.character == "default": self.current_sprite_list = c1ilist
        if self.character == 2: self.current_sprite_list = c2ilist
        if self.character == 3: self.current_sprite_list = c3ilist
        if self.character == 4: self.current_sprite_list = c4ilist
        if self.character == 5: self.current_sprite_list = c5ilist
        if self.character == 6: self.current_sprite_list = c6ilist
        self.current_sprite = self.current_sprite_list[self.frame]
        self.interval = int(1000/framerate)

    def update(self):
        self.cycle += dt
        if self.cycle >= self.interval:
            self.cycle = 0
            self.frame += 1
        if self.frame >= len(self.current_sprite_list):
            self.frame = 0
        if self.face == "back":
            if self.character == 1 or self.character == "default": self.current_sprite_list = c1blist
            if self.character == 2: self.current_sprite_list = c2blist
            if self.character == 3: self.current_sprite_list = c3blist
            if self.character == 4: self.current_sprite_list = c4blist
            if self.character == 5: self.current_sprite_list = c5blist
            if self.character == 6: self.current_sprite_list = c6blist
        if self.face == "forward":
            if self.character == 1 or self.character == "default": self.current_sprite_list = c1flist
            if self.character == 2: self.current_sprite_list = c2flist
            if self.character == 3: self.current_sprite_list = c3flist
            if self.character == 4: self.current_sprite_list = c4flist
            if self.character == 5: self.current_sprite_list = c5flist
            if self.character == 6: self.current_sprite_list = c6flist
        if self.face == "right":
            if self.character == 1 or self.character == "default": self.current_sprite_list = c1rlist
            if self.character == 2: self.current_sprite_list = c2rlist
            if self.character == 3: self.current_sprite_list = c3rlist
            if self.character == 4: self.current_sprite_list = c4rlist
            if self.character == 5: self.current_sprite_list = c5rlist
            if self.character == 6: self.current_sprite_list = c6rlist
        if self.face == "left":
            if self.character == 1 or self.character == "default": self.current_sprite_list = c1llist
            if self.character == 2: self.current_sprite_list = c2llist
            if self.character == 3: self.current_sprite_list = c3llist
            if self.character == 4: self.current_sprite_list = c4llist
            if self.character == 5: self.current_sprite_list = c5llist
            if self.character == 6: self.current_sprite_list = c6llist
        if self.face == "idle":
            if self.character == 1 or self.character == "default": self.current_sprite_list = c1ilist
            if self.character == 2: self.current_sprite_list = c2ilist
            if self.character == 3: self.current_sprite_list = c3ilist
            if self.character == 4: self.current_sprite_list = c4ilist
            if self.character == 5: self.current_sprite_list = c5ilist
            if self.character == 6: self.current_sprite_list = c6ilist
        self.current_sprite = self.current_sprite_list[self.frame]

    def draw(self,surface):
        self.update()
        surface.blit(self.current_sprite,(self.x,self.y))
    
    def shoot(self):
        pass
    
    def block(self):
        pass
# make the players
player_1 = Player(250,250,6,p1_proj_list,character)
player_2 = Player(250,250,6,p2_proj_list,character)
# color monster class
class ColorMonster:
    def __init__(self,x,y,framerate,monster):
        self.x = x
        self.y = y
        self.face = "back"
        self.frame = 0
        self.cycle = 0
        self.monster = monster
        if self.monster == 1:self.current_sprite_list = m1blist
        if self.monster == 2:self.current_sprite_list = m2blist
        if self.monster == 3:self.current_sprite_list = m3blist
        if self.monster == 4:self.current_sprite_list = m4blist
        if self.monster == 5:self.current_sprite_list = m5blist
        if self.monster == 6:self.current_sprite_list = m6blist
        self.current_sprite = self.current_sprite_list[self.frame]
        self.interval = int(1000/framerate)
        self.direction = random.randint(0,3)
        self.x_change = 0
        self.y_change = 0

    def update(self):
        self.cycle += dt
        if self.cycle >= self.interval:
            self.cycle = 0
            self.frame += 1
        if self.frame >= len(self.current_sprite_list):
            self.frame = 0
        if self.face == "back":
            if self.monster == 1:self.current_sprite_list = m1blist
            if self.monster == 2:self.current_sprite_list = m2blist
            if self.monster == 3:self.current_sprite_list = m3blist
            if self.monster == 4:self.current_sprite_list = m4blist
            if self.monster == 5:self.current_sprite_list = m5blist
            if self.monster == 6:self.current_sprite_list = m6blist
        if self.face == "forward":
            if self.monster == 1:self.current_sprite_list = m1flist
            if self.monster == 2:self.current_sprite_list = m2flist
            if self.monster == 3:self.current_sprite_list = m3flist
            if self.monster == 4:self.current_sprite_list = m4flist
            if self.monster == 5:self.current_sprite_list = m5flist
            if self.monster == 6:self.current_sprite_list = m6flist
        if self.face == "right":
            if self.monster == 1:self.current_sprite_list = m1rlist
            if self.monster == 2:self.current_sprite_list = m2rlist
            if self.monster == 3:self.current_sprite_list = m3rlist
            if self.monster == 4:self.current_sprite_list = m4rlist
            if self.monster == 5:self.current_sprite_list = m5rlist
            if self.monster == 6:self.current_sprite_list = m6rlist
        if self.face == "left":
            if self.monster == 1:self.current_sprite_list = m1llist
            if self.monster == 2:self.current_sprite_list = m2llist
            if self.monster == 3:self.current_sprite_list = m3llist
            if self.monster == 4:self.current_sprite_list = m4llist
            if self.monster == 5:self.current_sprite_list = m5llist
            if self.monster == 6:self.current_sprite_list = m6llist
        if self.face == "idle":
            if self.monster == 1:self.current_sprite_list = m1ilist
            if self.monster == 2:self.current_sprite_list = m2ilist
            if self.monster == 3:self.current_sprite_list = m3ilist
            if self.monster == 4:self.current_sprite_list = m4ilist
            if self.monster == 5:self.current_sprite_list = m5ilist
            if self.monster == 6:self.current_sprite_list = m6ilist
        self.current_sprite = self.current_sprite_list[self.frame]

    def attack(self):
        if self.x <= 0 or self.x >= 640 or self.y <= 0 or self.y >= 480:
            if self.direction == 0:
                self.direction = random.choice("123")
            if self.direction == 1:
                self.direction = random.choice("023")
            if self.direction == 2:
                self.direction = random.choice("013")
            if self.direction == 3:
                self.direction = random.choice("012")
            if self.x <= 0:
                self.x = 17
            if self.x >= 640:
                self.x = 623
            if self.y <= 0:
                self.y = 19
            if self.y >= 480:
                self.y = 471
        if self.direction == 0:
            self.face = "forward"
            self.y -= MOVEMENT_SPEED
        if self.direction == 1:
            self.face = "back"
            self.y += MOVEMENT_SPEED
        if self.direction == 2:
            self.face = "left"
            self.x -= MOVEMENT_SPEED
        if self.direction == 3:
            self.face = "right"
            self.x += MOVEMENT_SPEED
                
    def draw(self,surface):
        self.attack()
        self.update()
        self.collision(player_1.x, player_1.y, 19, 20)
        surface.blit(self.current_sprite,(self.x,self.y))
        
    def collision(self,player_x,player_y,player_w,player_h):
        global gamemode
        self.player_rect = pygame.Rect(player_x,player_y,player_w,player_h)
        self.monster_rect = pygame.Rect(self.x,self.y,17,19)
        if self.monster_rect.colliderect(self.player_rect) and gamemode == "singleplayer":
            gamemode = "s_minigame"
        elif gamemode == "multiplayer":
            gamemode = "m_minigame"
# make the monsters
monster_0 = ColorMonster(50,50,6,1)
# list of monsters
monster_list = [monster_0]
# projectile class
class Projectile:
    pass
# cursor class
class Cursor:
    def __init__(self,player,x,y,speed):
        self.player = player
        self.x,self.y = (x,y)
        self.speed = speed
        self.clicked = False
        self.cursor = pygame.Surface((7,12),pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(self.x,self.y,7,12)
    def update(self):
        self.rect = pygame.Rect(self.x,self.y,7,12)
    def draw(self,surface):
        self.update()
        pygame.draw.polygon(self.cursor,(255,255,255),[(0,0),(7,7),(5,9),(7,11),(5,12),(3,9),(0,11)])
        pygame.draw.polygon(self.cursor,(0,0,0),[(0,0),(7,7),(5,9),(7,11),(5,12),(3,9),(0,11)],1)
        surface.blit(self.cursor,(self.x,self.y))
# make the cursor
P1C = Cursor(1,400,300,mouse_speed)
# button profile class
class ButtonProfile:
    def __init__(self, button_color, outline_color, outline_width, text_color, hover_color, font_type, font_size):
        self.button_color = button_color
        self.outline_color = outline_color
        self.outline_width = outline_width
        self.text_color = text_color
        self.hover_color = hover_color
        self.font_type = font_type
        self.font_size = font_size
        self.hover_outline = outline_color
        self.hover_text = text_color
        self.antialias = False
        self.font = pygame.font.Font(self.font_type, self.font_size)
# button class
class Button:
    def __init__(self, xpos, ypos, width, height, label, value, button_profile):
        self.rect = pygame.Rect(xpos, ypos, width, height)
        self.label = label
        self.value = value
        self.button_profile = button_profile
        self.button_color = button_profile.button_color
    
    def draw(self, screen):
        self.mouse_over(P1C.x,P1C.y)
        label_surface = self.button_profile.font.render(self.label, self.button_profile.antialias, self.button_profile.text_color)
        label_rect = label_surface.get_rect()
        x_offset = abs(self.rect.width - label_rect.width)/2
        y_offset = abs(self.rect.height - label_rect.height)/2
        pygame.draw.rect(screen, self.button_color, self.rect, 0)#, self.button_profile.border_radius) #rect border_radius only works for newest pygame distributions 
        pygame.draw.rect(screen, self.button_profile.outline_color, self.rect, self.button_profile.outline_width)#, self.button_profile.border_radius) #rect border_radius only works for newest pygame distributions
        screen.blit(label_surface, (self.rect.x+x_offset, self.rect.y+y_offset))
    
    def mouse_over(self,mouse_x,mouse_y):
        global gamemode
        if self.rect.collidepoint(mouse_x,mouse_y):
            self.button_color = self.button_profile.hover_color
        else:
            self.button_color = self.button_profile.button_color
# make the button profile
profile_0 = ButtonProfile((198,198,198), (20,20,20), 10, (20,20,20), (255,0,0), None, 18)
# make all the buttons
singleplayer = Button(86, 209, 155, 60, "Singleplayer", 0, profile_0)
multiplayer = Button(391, 210, 155, 60, "Multiplayer", 1, profile_0)
introduction = Button(162, 309, 150, 49, "Introduction", 2, profile_0)
credits_ = Button(347, 308, 99, 48, "Credits", 3, profile_0)
instructions = Button(240, 395, 162, 38, "Instructions", 4, profile_0)
# temporary outro button so I can show off the outro
outro = Button(240, 438, 162, 38, "Outro", 5, profile_0)
# put all the buttons in a list
button_list = [singleplayer,multiplayer,introduction,credits_,instructions,outro]

# MAIN GAME LOOP

while True:
    if gamemode == "menu": SCREEN.blit(MENU,(0,0))
    P1C.clicked = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if gamemode == "menu":
                if event.key == K_SPACE:
                    if singleplayer.rect.collidepoint(P1C.x,P1C.y):
                        playing_sound_select = True
                        gamemode = "singleplayer"                        
                    elif multiplayer.rect.collidepoint(P1C.x,P1C.y):
                        playing_sound_select = True
                        gamemode = "multiplayer"
                    elif introduction.rect.collidepoint(P1C.x,P1C.y):
                        playing_sound_select = True
                        gamemode = "introduction"                        
                    elif credits_.rect.collidepoint(P1C.x,P1C.y):
                        playing_sound_select = True
                        gamemode = "credits"
                    elif instructions.rect.collidepoint(P1C.x,P1C.y):
                        playing_sound_select = True
                        gamemode = "instructions"
                    elif outro.rect.collidepoint(P1C.x,P1C.y):
                        playing_sound_select = True
                        gamemode = "outro"
                    if playing_sound_select == True:
                        pygame.mixer.Sound.play(SELECT)
                        playing_sound_select = False
            else:
                if event.key == K_ESCAPE:
                    gamemode = "menu"
            if gamemode == "instructions":
                SCREEN.blit(INSTRUCTIONS,(0,0))
                if event.key == K_SPACE or event.key == K_q: SCREEN.blit(SPACE_PURPOSE,(270,430))
                if event.key == K_RETURN or event.key == K_j: SCREEN.blit(RETURN_PURPOSE,(270,430))
                if event.key == K_UP or event.key == K_r: SCREEN.blit(UP_PURPOSE,(270,430))
                if event.key == K_DOWN or event.key == K_f: SCREEN.blit(DOWN_PURPOSE,(270,430))
                if event.key == K_LEFT or event.key == K_d: SCREEN.blit(LEFT_PURPOSE,(270,430))
                if event.key == K_RIGHT or event.key == K_g: SCREEN.blit(RIGHT_PURPOSE,(270,430))
            if gamemode == "s_minigame":
                if event.key == K_SPACE:
                    player_1.shoot()
                if event.key == K_RETURN:
                    player_1.block()
            if gamemode == "m_minigame":
                if event.key == K_SPACE:
                    player_1.shoot()
                if event.key == K_RETURN:
                    player_1.block()
                if event.key == K_q:
                    player_2.shoot()
                if event.key == K_j:
                    player_2.block()
    check = pygame.key.get_pressed()
    if gamemode == "menu":
        if check[K_UP]:
            P1C.y -= P1C.speed
        elif check[K_DOWN]:
            P1C.y += P1C.speed
        if check[K_LEFT]:
            P1C.x -= P1C.speed
        elif check[K_RIGHT]:
            P1C.x += P1C.speed
        for each_button in button_list:
            each_button.draw(SCREEN)
        P1C.draw(SCREEN)
    if gamemode == "singleplayer":
        SCREEN.blit(GAME,(0,bg_y_pos))
        if check[K_UP]:
            player_1.face = "forward"
            if player_1.y > 240:
                player_1.y -= MOVEMENT_SPEED
            else:
                bg_y_pos += MOVEMENT_SPEED
                for i in monster_list:
                    if i.face == "forward":
                        i.y += MOVEMENT_SPEED
                    if i.face == "back":
                        i.y += MOVEMENT_SPEED
                    if i.face == "left" or i.face == "right":
                        i.y += MOVEMENT_SPEED
        if check[K_DOWN]:
            player_1.face = "back"
            if player_1.y < 460:
                player_1.y += MOVEMENT_SPEED
        if check[K_LEFT]:
            player_1.face = "left"
            if player_1.x > 0:
                player_1.x -= MOVEMENT_SPEED
        if check[K_RIGHT]:
            player_1.face = "right"
            if player_1.x < 620:
                player_1.x += MOVEMENT_SPEED
        elif check[K_UP] == False and check[K_DOWN] == False and check[K_LEFT] == False and check[K_RIGHT] == False:
            player_1.face = "idle"
        player_1.draw(SCREEN)
        monster_0.draw(SCREEN)
    if gamemode == "multiplayer":
        SCREEN.blit(GAME,(0,bg_y_pos))
        if check[K_UP]:
            player_1.face = "forward"
            player_1.y -= MOVEMENT_SPEED
        if check[K_DOWN]:
            player_1.face = "back"
            player_1.y += MOVEMENT_SPEED
        if check[K_LEFT]:
            player_1.face = "left"
            player_1.x -= MOVEMENT_SPEED
        if check[K_RIGHT]:
            player_1.face = "right"
            player_1.x += MOVEMENT_SPEED
        elif check[K_UP] == False and check[K_DOWN] == False and check[K_LEFT] == False and check[K_RIGHT] == False:
            player_1.face = "idle"
        if check[K_r]:
            player_2.face = "forward"
            player_2.y -= MOVEMENT_SPEED
        if check[K_f]:
            player_2.face = "back"
            player_2.y += MOVEMENT_SPEED
        if check[K_d]:
            player_2.face = "left"
            player_2.x -= MOVEMENT_SPEED
        if check[K_g]:
            player_2.face = "right"
            player_2.x += MOVEMENT_SPEED
        elif check[K_r] == False and check[K_f] == False and check[K_d] == False and check[K_g] == False:
            player_2.face = "idle"
        player_1.draw(SCREEN)
        player_2.draw(SCREEN)
        monster_0.draw(SCREEN)
    if gamemode == "s_minigame":
        SCREEN.blit(MINIGAME,(0,0))
        if check[K_UP]:
            player_1.face = "forward"
            if player_1.x > 0 and player_1.x < 640 and player_1.y > 0 and player_1.y < 480:
                player_1.y -= MOVEMENT_SPEED
        if check[K_DOWN]:
            player_1.face = "back"
            if player_1.x > 0 and player_1.x < 640 and player_1.y > 0 and player_1.y < 480:
                player_1.y += MOVEMENT_SPEED
        if check[K_LEFT]:
            player_1.face = "left"
            if player_1.x > 0 and player_1.x < 640 and player_1.y > 0 and player_1.y < 480:
                player_1.x -= MOVEMENT_SPEED
        if check[K_RIGHT]:
            player_1.face = "right"
            if player_1.x > 0 and player_1.x < 640 and player_1.y > 0 and player_1.y < 480:
                player_1.x += MOVEMENT_SPEED
        elif check[K_UP] == False and check[K_DOWN] == False and check[K_LEFT] == False and check[K_RIGHT] == False:
            player_1.face = "idle"
        player_1.draw(SCREEN)
    if gamemode == "m_minigame":
        SCREEN.blit(MINIGAME,(0,0))
        if check[K_UP]:
            player_1.face = "forward"
            if player_1.x > 0 and player_1.x < 640 and player_1.y > 0 and player_1.y < 480:
                player_1.y -= MOVEMENT_SPEED
        if check[K_DOWN]:
            player_1.face = "back"
            if player_1.x > 0 and player_1.x < 640 and player_1.y > 0 and player_1.y < 480:
                player_1.y += MOVEMENT_SPEED
        if check[K_LEFT]:
            player_1.face = "left"
            if player_1.x > 0 and player_1.x < 640 and player_1.y > 0 and player_1.y < 480:
                player_1.x -= MOVEMENT_SPEED
        if check[K_RIGHT]:
            player_1.face = "right"
            if player_1.x > 0 and player_1.x < 640 and player_1.y > 0 and player_1.y < 480:
                player_1.x += MOVEMENT_SPEED
        if check[K_r]:
            player_2.face = "forward"
            if player_2.x > 0 and player_2.x < 640 and player_2.y > 0 and player_2.y < 480:
                player_2.y -= MOVEMENT_SPEED
        if check[K_f]:
            player_2.face = "back"
            if player_2.x > 0 and player_2.x < 640 and player_2.y > 0 and player_2.y < 480:
                player_2.y += MOVEMENT_SPEED
        if check[K_d]:
            player_2.face = "left"
            if player_2.x > 0 and player_2.x < 640 and player_2.y > 0 and player_2.y < 480:
                player_2.x -= MOVEMENT_SPEED
        if check[K_g]:
            player_2.face = "right"
            if player_2.x > 0 and player_2.x < 640 and player_2.y > 0 and player_2.y < 480:
                player_2.x += MOVEMENT_SPEED
        elif check[K_r] == False and check[K_f] == False and check[K_d] == False and check[K_g] == False:
            player_2.face = "idle"
        player_1.draw(SCREEN)
        player_2.draw(SCREEN)
    if gamemode == "outro":
        SCREEN.fill((0,0,0))
        pygame.mixer.Sound.play(OUTRO)
        gamemode = "menu"
    pygame.display.update()
    dt = CLOCK.tick(FPS)