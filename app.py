import pygame
import math
import random
from src.game import Game
from src.player import Player

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
liste_of_colours = (blue, green, purple, pink, orange, yellow)

#initialize dimensions
screen_width = screen.get_width() 
screen_height = screen.get_height()

#initialize text
smallfont = pygame.font.SysFont('Corbel',35)
middlefont = pygame.font.SysFont('Corbel',100)
bigfont = pygame.font.SysFont('Corbel',200)
text_start = smallfont.render('Start' , True , black)
text_game_choice=bigfont.render('Choose your game', True, black)
text_solo = smallfont.render('Solo' , True , black)
text_multiplayer = smallfont.render('Multiplayer', True, black)
title = bigfont.render('Triv-IA-pursuit', True, black)
sub_title=middlefont.render('Triv-IA-pursuit', True, black)
screen.blit(title, (screen_width/2-100, screen_height/2))

#initialize the circle grids
def pursuit_board():
    center = (screen_width/2-450, screen_height/2)
    radius = 400
    radius_50 = 340
    radius_100 = 280
    radius_150= 220
    radius_200 = 160
    radius_250 = 100
    
    player1= Player("toto")
    game = Game(36)
    cases= Game.create_board(game)

    for i in range(len(cases)):
        angle = (2 * math.pi / len(cases)) * i
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))

        if i % 6 == 0:
            if cases[i]== "Bases de données":
                pygame.draw.circle(screen, blue, (x, y), 30)
            if cases[i]== "Langages de programmation":
                pygame.draw.circle(screen, green, (x, y), 30)
            if cases[i]== "Ligne de commandes":
                pygame.draw.circle(screen, pink, (x, y), 30)
            if cases[i]== "Actualités IA":
                pygame.draw.circle(screen, orange, (x, y), 30)
            if cases[i]== "Autres catégories":
                pygame.draw.circle(screen, yellow, (x, y), 30)
            if cases[i]== "DevOps":
                pygame.draw.circle(screen, purple, (x, y), 30)
            
            # #initialize picture
            cheese = pygame.image.load("media/cheese_slice.png")
            cheese = pygame.transform.scale(cheese, (30,30))
            screen.blit(cheese, (x-15,y-15)) #a rescale et décaler

            
            angle = (2 * math.pi / len(cases)) * i
            x1 = center[0] + int(radius_250 * math.cos(angle))
            y1 = center[1] + int(radius_250 * math.sin(angle))
            pygame.draw.circle(screen, light_grey, (x1, y1), 28)
            x2 = center[0] + int(radius_200 * math.cos(angle))
            y2 = center[1] + int(radius_200 * math.sin(angle))
            pygame.draw.circle(screen, light_grey, (x2, y2), 26)
            x3 = center[0] + int(radius_150 * math.cos(angle))
            y3 = center[1] + int(radius_150 * math.sin(angle))
            pygame.draw.circle(screen, light_grey, (x3, y3), 24)
            x4 = center[0] + int(radius_100 * math.cos(angle))
            y4 = center[1] + int(radius_100 * math.sin(angle))
            pygame.draw.circle(screen, light_grey, (x4, y4), 22)
            x5 = center[0] + int(radius_50 * math.cos(angle))
            y5 = center[1] + int(radius_50 * math.sin(angle))
            pygame.draw.circle(screen, light_grey, (x5, y5), 20)
                
            # if cases[i] == 'Bases de données':
            #     pygame.draw.circle(screen, blue, (x, y), 20)
        else:

            if cases[i]== "Bases de données":
                pygame.draw.circle(screen, blue, (x, y), 20)
            if cases[i]== "Langages de programmation":
                pygame.draw.circle(screen, green, (x, y), 20)
            if cases[i]== "Ligne de commandes":
                pygame.draw.circle(screen, pink, (x, y), 20)
            if cases[i]== "Actualités IA":
                pygame.draw.circle(screen, orange, (x, y), 20)
            if cases[i]== "Autres catégories":
                pygame.draw.circle(screen, yellow, (x, y), 20)
            if cases[i]== "DevOps":
                pygame.draw.circle(screen, purple, (x, y), 20)

    pygame.draw.circle(screen, black, center, 60)
    pygame.draw.circle(screen, light_grey, center, 58)
    screen.blit(sub_title, (screen_width/2-100, screen_height/2-500))


#start the display
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
    screen.fill(white)
    pursuit_board()
    pygame.display.flip()


