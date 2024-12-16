import pygame
import math

#initialize the constructor 
pygame.init() 
  
#initialize screen
res = (1920,1080) 
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

#initialize colours
white = (255,255,255) 
black = (0,0,0)
light_grey = (211,224,227)
blue = (94,184,204)
green = (94,204,118)
purple = (151,94,204)
pink = (204,94,200)
orange = (204,141,73)
yellow = (204,193,73)

#initialize dimensions
screen_width = screen.get_width() 
screen_height = screen.get_height()

#initialize text
smallfont = pygame.font.SysFont('Corbel',35)
bigfont = pygame.font.SysFont('Corbel',200)
text_start = smallfont.render('Start' , True , black)
text_game_choice=bigfont.render('Choose your game', True, black)
text_solo = smallfont.render('Solo' , True , black)
text_multiplayer = smallfont.render('Multiplayer', True, black)
title = bigfont.render('Triv-IA-pursuite', True, black)
screen.blit(title, (screen_width/2-100, screen_height/2))

#initialize the circle grids
def pursuit_board():
    center = (screen_width/2, screen_height/2)
    radius = 400
    cases = 42

    for i in range(cases):
        angle = (2 * math.pi / cases) * i
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))

        if i % 6 == 0:
            pygame.draw.circle(screen, blue, (x, y), 20)
        else:
            pygame.draw.circle(screen, pink, (x, y), 20)

    pygame.draw.circle(screen, black, center, 50)
    pygame.draw.circle(screen, white, center, 45)


#start the display
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
    screen.fill(white)
    pursuit_board()
    pygame.display.flip()


