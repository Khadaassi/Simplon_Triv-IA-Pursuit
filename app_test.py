import pygame
import math
import random
from pygame.locals import *

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
line_color = (255, 50, 50)

#initialize dimensions
screen_width = screen.get_width() 
screen_height = screen.get_height()

#initialize text
smallfont = pygame.font.SysFont('Corbel',20)
middlefont = pygame.font.SysFont('Corbel',50)
bigfont = pygame.font.SysFont('Corbel',100)
text_exit = smallfont.render('Exit' , True , black)
text_game_choice=middlefont.render('Choose your game', True, black)
text_solo = smallfont.render('Solo' , True , black)
text_multiplayer = smallfont.render('Multiplayer', True, black)
title = bigfont.render('Triv-IA-pursuite', True, black)
LEFT = 1


def menu():
    screen.blit(title, (screen_width/2, screen_height/2-500))
    screen.blit(text_game_choice, (screen_width/2+500, screen_height/2))
    screen.blit(text_solo, (screen_width/2+500, screen_height/2+50))
    screen.blit(text_multiplayer, (screen_width/2+500, screen_height/2+100))

    perso = pygame.image.load("media/jeton.png").convert_alpha()
    





#Start the graphic display and the simulation
while True:
    screen.fill(white)
    menu()
    perso = pygame.image.load("media/jeton.png").convert_alpha()
    persoRect = perso.get_rect()
    persoRect.topleft = (270,380)
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT: 
            pygame.quit()     

        if ev.type == KEYDOWN  :
            if ev.key == K_LEFT :
                if persoRect.left>=10 :
                    persoRect = persoRect.move(-10,0)
            if ev.key == K_RIGHT :
                if persoRect.right<=630 :
                    persoRect = persoRect.move(10,0)
        # #check if a mouse is clicked
        # if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == LEFT:
            # select multiplayer game
            # if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40:
    screen.blit(perso, persoRect)
    pygame.display.update()

    #store the (x,y) coordinates into the variable as a tuple 
    mouse = pygame.mouse.get_pos()


    pygame.display.flip()


#########################################################################"
# 
# 
# import pygame
import math
import random
import time
from src.game import Game
from lanceDe import lancer_de
import sys

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
line_color = (255, 50, 50)

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
rect = pygame.Rect(100, 100, 200, 150)
player_name = smallfont.render('Player : ', True, black)
score = smallfont.render('score : ', True, black)
legend = smallfont.render('Legend : ', True, black)
theme1 = smallfont.render("Actualités IA", True, black)
theme2 = smallfont.render("DevOps", True, black)
theme3 = smallfont.render("Ligne de commandes", True, black)
theme4 = smallfont.render("Bases de données", True, black)
theme5 = smallfont.render("Langages de programmation", True, black)
theme6 = smallfont.render("AGIL", True, black)
theme7 = smallfont.render("DevOps", True, black)
LEFT = 1

#initialize the circle grids
def pursuit_board():
    center = (screen_width/2 -450, screen_height/2)
    radius = 400
    cases = 48


    for i in range(cases):
        angle = (2 * math.pi / cases) * i
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))

        if i % 8 == 0:
            list_of_colours = [blue, green, purple, pink, orange, yellow]
            color_choice = random.choice(list_of_colours)
            pygame.draw.circle(screen, color_choice, (x, y), 30)
            list_of_colours.remove(color_choice)

            
        elif i % 8 == 1:
            #case_color = random.choice(liste_of_colours)
            pygame.draw.circle(screen, light_grey, (x, y), 20)
            imp = pygame.image.load("media/00.png")
            imp = pygame.transform.scale(imp, (35,35))
            screen.blit(imp,(x-18, y-18))
        else:
            pygame.draw.circle(screen, pink, (x, y), 20)
    
    screen.blit(title, (screen_width/2 -200, screen_height/2-500))
    screen.blit(scoring, (screen_width/2+450, screen_height/2 - 250))
    pygame.draw.rect(screen, black, [1140, 340, 620, 320])
    pygame.draw.rect(screen, light_grey, [1150, 350, 600, 300])

    screen.blit(player_name, (screen_width/2+210, screen_height/2 - 180))
    screen.blit(score, (screen_width/2+210, screen_height/2 - 160))

    screen.blit(legend, (screen_width/2+180, screen_height/2 +200))
    pygame.draw.circle(screen, pink, (screen_width/2+180, screen_height/2 +250), 20)
    pygame.draw.circle(screen, green, (screen_width/2+180, screen_height/2 +300), 20)
    pygame.draw.circle(screen, orange, (screen_width/2+180, screen_height/2 +350), 20)
    pygame.draw.circle(screen, purple, (screen_width/2+180, screen_height/2 +400), 20)
    pygame.draw.circle(screen, blue, (screen_width/2+550, screen_height/2 +250), 20)
    pygame.draw.circle(screen, yellow, (screen_width/2+550, screen_height/2 +300), 20)
    pygame.draw.circle(screen, pink, (screen_width/2+550, screen_height/2 +350), 20)

    screen.blit(theme1, (screen_width/2+210, screen_height/2 +240))
    screen.blit(theme2, (screen_width/2+210, screen_height/2 +290))
    screen.blit(theme3, (screen_width/2+210, screen_height/2 +340))
    screen.blit(theme4, (screen_width/2+210, screen_height/2 +390))
    screen.blit(theme5, (screen_width/2+580, screen_height/2 +240))
    screen.blit(theme6, (screen_width/2+580, screen_height/2 +290))
    screen.blit(theme7, (screen_width/2+580, screen_height/2 +340))
    
    screen.blit(text_solo, (screen_width/2, screen_height/2))
    pygame.draw.circle(screen, black, center, 50)
    pygame.draw.circle(screen, light_grey, center, 45)

    # Display questions


#start the graphic display
while True:
    screen.fill(white)
    
    #events as in button clicks
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
    
    # check if a mouse is clicked
    if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == LEFT: 
        # select SOLO mode
        if screen_width/2 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40:

    #store de (x,y) coordinates into a Tuple
    mouse = pygame.mouse.get_pos() 




# text_start = smallfont.render('Start' , True , black)
# text_game_choice=bigfont.render('Choose your game', True, black)
# text_solo = smallfont.render('Solo' , True , black)
# text_multiplayer = smallfont.render('Multiplayer', True, black)


        # select MULTIPLAYER mode

    # input_rect = pygame.Rect(200, 200, 140, 32) 

    # number_players = int(input("Nombre de joueurs?"))

    # while not isinstance(number_players, int) or number_players < 1 or number_players > 4:
    #     try:
    #         number_players = int(input("Entrez un nombre de joueurs (entre 1 et 4) : "))
    #     except ValueError:
    #         print("Veuillez entrer un nombre entier valide.")

    # player_list = []
    # for player in range(number_players):
    #     player_names = str(input(f"nom du joueur {player+1}?")).lower()
    #     player_list.append(player_names)

    pursuit_board()
    time.sleep(1)
    pygame.display.flip()


"


    
