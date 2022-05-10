import pygame, sys
from pygame.locals import *
pygame.init()
SCREEN = pygame.display.set_mode((640, 480))
CLOCK = pygame.time.Clock()
FPS = 30
MOVEMENT_SPEED = 5
ARCADE_MODE = False
MENU = pygame.image.load("Main Menu.png")
left_click = False
mouse_x,mouse_y = 0,0
mouse_speed = 5
gamemode = "menu"

class Player:
    pass

class ColorMonster:
    pass

class Projectile:
    pass

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

P1C = Cursor(1,400,300,mouse_speed)

class ButtonProfile:
    def __init__(self, button_color, outline_color, outline_width, text_color, hover_color, font_type, font_size):
        self.button_color = button_color
        self.outline_color = outline_color
        self.outline_width = outline_width
        self.text_color = text_color
        self.hover_color = hover_color
        # self.border_radius = border_radius
        self.font_type = font_type
        self.font_size = font_size
        # may manually change
        self.hover_outline = outline_color
        self.hover_text = text_color
        self.antialias = False
        self.font = pygame.font.Font(self.font_type, self.font_size)

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
        if self.rect.collidepoint(mouse_x,mouse_y):
            self.button_color = self.button_profile.hover_color
            if self.value == 0:
                gamemode = "singleplayer"
            elif self.value == 1:
                gamemode = "multiplayer"
            elif self.value == 2:
                gamemode = "introduction"
            elif self.value == 3:
                gamemode = "credits"
            elif self.value == 4:
                gamemode = "instructions"
        else:
            self.button_color = self.button_profile.button_color

profile_0 = ButtonProfile((198,198,198), (20,20,20), 10, (20,20,20), (255,0,0), None, 18)

singleplayer = Button(86, 209, 155, 60, "Singleplayer", 0, profile_0)
multiplayer = Button(391, 210, 155, 60, "Multiplayer", 1, profile_0)
introduction = Button(162, 309, 150, 49, "Introduction", 2, profile_0)
credits_ = Button(347, 308, 99, 48, "Credits", 3, profile_0)
instructions = Button(240, 395, 162, 38, "Instructions", 4, profile_0)

button_list = [singleplayer,multiplayer,introduction,credits_,instructions]

while True:
    SCREEN.blit(MENU,(0,0))
    #left_click = False
    P1C.clicked = False
    # EVENT HANDLER
    check = pygame.key.get_pressed() # Press & Hold
    if check[K_UP]:
        P1C.y -= P1C.speed
    elif check[K_DOWN]:
        P1C.y += P1C.speed
    if check[K_LEFT]:
        P1C.x -= P1C.speed
    elif check[K_RIGHT]:
        P1C.x += P1C.speed
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #pressed = pygame.key.get_pressed()
    #if ARCADE_MODE == False:
    #  if pressed[K_w]:
    #      # move back
    #  if pressed[K_s]:
    #      # move forward
    #  if pressed[K_a]:
    #      # move left
    #  if pressed[K_d]:
    #      # move right
    #elif ARCADE_MODE == True:
    #  if pressed[K_UP]:
    #      # move back
    #  if pressed[K_DOWN]:
    #      # move forward
    #  if pressed[K_LEFT]:
    #      # move left
    #  if pressed[K_RIGHT]:
    #      # move right
    for each_button in button_list:
        each_button.draw(SCREEN)
        if each_button.button_color == profile_0.hover_color and left_click == True:
            value = each_button.value
            print("button clicked!", value)
    P1C.draw(SCREEN)
    pygame.display.update()
    CLOCK.tick(FPS)