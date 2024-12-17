import pygame
import math
import random
import time
from src.game import Game

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
# liste_of_colours = (blue, green, purple, pink, orange, yellow)

#initialize dimensions
screen_width = screen.get_width() 
screen_height = screen.get_height()

#initialize text
smallfont = pygame.font.SysFont('Corbel',35)
middlefont = pygame.font.SysFont('Corbel',120)
bigfont = pygame.font.SysFont('Corbel',200)
text_start = smallfont.render('Start' , True , black)
text_game_choice=bigfont.render('Choose your game', True, black)
text_solo = smallfont.render('Solo' , True , black)
text_multiplayer = smallfont.render('Multiplayer', True, black)

title = middlefont.render('Triv-IA-pursuite', True, black)
scoring = smallfont.render('Scoring', True, black)
screen.blit(title, (screen_width/2-100, screen_height/2))

#initialize the circle grids
def pursuit_board():
    center = (screen_width/2 -450, screen_height/2)
    radius = 400
    # cases = 48
    board = Game(6)
    print(board)

    # for i in range(cases):
    #     angle = (2 * math.pi / cases) * i
    #     x = center[0] + int(radius * math.cos(angle))
    #     y = center[1] + int(radius * math.sin(angle))

    #     if i % 8 == 0:
    #         list_of_colours = [blue, green, purple, pink, orange, yellow]
    #         #case_color = random.choice(liste_of_colours)
    #         color_choice = random.choice(list_of_colours)
    #         pygame.draw.circle(screen, color_choice, (x, y), 30)
    #         list_of_colours.remove(color_choice)

            
    #     elif i % 8 == 1:
    #         #case_color = random.choice(liste_of_colours)
    #         pygame.draw.circle(screen, light_grey, (x, y), 20)
    #     else:
    #         pygame.draw.circle(screen, pink, (x, y), 20)

    # screen.blit(title, (screen_width/2, screen_height/2-500))
    # screen.blit(scoring, (screen_width/2+350, screen_height/2 - 250))
    # pygame.draw.circle(screen, black, center, 50)
    # pygame.draw.circle(screen, light_grey, center, 45)


#start the display
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
    screen.fill(white)
    pursuit_board()
    time.sleep(1)
    pygame.display.flip()


