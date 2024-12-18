import pygame
import math
import random
from src.game import Game
from src.player import Player
from src.dice import rolling_dice

#initialize the constructor 
pygame.init() 
  
#initialize screen
res = (1920,1080) 
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
fps = pygame.time.Clock()

#initialize colours
white = (255,255,255) 
black = (0,0,0)
light_grey = (211,224,227)
dark_grey =(184, 178, 178)
blue = (94,184,204)
green = (94,204,118)
purple = (151,94,204)
pink = (204,94,200)
orange = (204,141,73)
yellow = (204,193,73)
liste_of_colours = (blue, green, purple, pink, orange, yellow)
blue_light = (179, 222, 232)
green_light = (187, 240, 198)
purple_light = (197, 166, 227)
pink_light = (227, 166, 225)
orange_light = (217, 184, 150)
yellow_light = (217, 210, 132)
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
text_dice = smallfont.render('Dice', True, black)
title = bigfont.render('Triv-IA-pursuit', True, black)
sub_title=middlefont.render('Triv-IA-pursuit', True, black)
screen.blit(title, (screen_width/2-100, screen_height/2))
scoring = smallfont.render('Scoring', True, black)
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

# center positions
center = (screen_width / 2 - 450, screen_height / 2)
radius = 400

# initialize game state
player_position = 0  # Current position of the player
cases = Game.create_board(Game(36))  # Initialize board

# Load images
cheese = pygame.image.load("media/cheese_slice.png")
cheese = pygame.transform.scale(cheese, (30, 30))
star = pygame.image.load("media/Stars_mario.png")
star = pygame.transform.scale(star, (30, 30))


def draw_board():
    screen.fill(white)
    pygame.draw.circle(screen, dark_grey, center, 60)
    pygame.draw.circle(screen, light_grey, center, 58)
    screen.blit(sub_title, (screen_width/2-100, screen_height/2-500))


#initialize the circle grids
def pursuit_board():
    center = (screen_width/2-450, screen_height/2)
    radius = 400
    radius_50 = 340
    radius_100 = 280
    radius_150= 220
    radius_200 = 160
    radius_250 = 100
    
    for i, case in enumerate(cases):
        angle = (2 * math.pi / len(cases)) * i
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))

        color = {
            "Bases de données": blue,
            "Langages de programmation": green,
            "Ligne de commandes": pink,
            "Actualités IA": orange,
            "Agile": yellow,
            "DevOps": purple
        }.get(case, white)

        pygame.draw.circle(screen, color, (x, y), 20 if i % 6 != 0 else 30)

        if i % 6 == 0:
            screen.blit(cheese, (x - 15, y - 15))
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
    
    screen.blit(scoring, (screen_width/2+450, screen_height/2 - 250))
    pygame.draw.rect(screen, black, [1140, 340, 620, 320])
    pygame.draw.rect(screen, light_grey, [1150, 350, 600, 300])

    screen.blit(player_name, (screen_width/2+210, screen_height/2 - 180))
    screen.blit(score, (screen_width/2+210, screen_height/2 - 160))

    screen.blit(legend, (screen_width/2+180, screen_height/2 +200))
    pygame.draw.circle(screen, blue, (screen_width/2+180, screen_height/2 +250), 20)
    pygame.draw.circle(screen, green, (screen_width/2+180, screen_height/2 +300), 20)
    pygame.draw.circle(screen, pink, (screen_width/2+180, screen_height/2 +350), 20)
    pygame.draw.circle(screen, orange, (screen_width/2+550, screen_height/2 +250), 20)
    pygame.draw.circle(screen, yellow, (screen_width/2+550, screen_height/2 +300), 20)
    pygame.draw.circle(screen, purple, (screen_width/2+550, screen_height/2 +350), 20)


    screen.blit(theme1, (screen_width/2+210, screen_height/2 +240))
    screen.blit(theme2, (screen_width/2+210, screen_height/2 +290))
    screen.blit(theme3, (screen_width/2+210, screen_height/2 +340))
    screen.blit(theme4, (screen_width/2+580, screen_height/2 +240))
    screen.blit(theme5, (screen_width/2+580, screen_height/2 +290))
    screen.blit(theme6, (screen_width/2+580, screen_height/2 +340))

            
def draw_player(position):
    """Draw the player's token at the current position."""
    angle = (2 * math.pi / len(cases)) * position
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    screen.blit(star, (x - 15, y - 15))

def main():
    global player_position

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                if screen_width - 200 <= mouse[0] <= screen_width - 60 and screen_height / 2 <= mouse[1] <= screen_height / 2 + 40:
                    # Roll dice and update position
                    move_path = rolling_dice()
                    last_dice_result = move_path
                    # move_number = smallfont.render(f"Resultat : {move_path}", True, black)
                    # screen.blit(move_number, (screen_width-200,screen_height/2+50,140,40))
                    #player_position1 = (player_position - move_path) % len(cases)
                    player_position = (player_position + move_path) % len(cases)
                

        # Draw the board and the player
        draw_board()
        pursuit_board()
        draw_player(player_position)

        # Draw the dice button
        pygame.draw.rect(screen, light_grey, [screen_width - 200, screen_height / 2, 140, 40])
        screen.blit(text_dice, (screen_width - 150, screen_height / 2 + 10))

        # Print the last result of dice to the player
        # if last_dice_result is not None:
        #     texte=f"Résultat : {last_dice_result}"
        #     move_number = smallfont.render(texte, True, black)
        #     screen.blit(move_number, (screen_width - 200, screen_height / 2 + 50, 140, 40))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()

#     #store the x,y position of the mouse position
#     mouse = pygame.mouse.get_pos() 
#     #create buttons with text on them and change colour if mouse hovers over them
#     pygame.draw.rect(screen, light_grey,[screen_width-200,screen_height/2,140,40]) 
#     screen.blit(text_dice, (screen_width-150,screen_height/2+10,140,40))

#     if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40: 
#             pygame.draw.rect(screen,dark_grey,[screen_width-200,screen_height/2,140,40])
#             screen.blit(text_dice , (screen_width-150,screen_height/2+10,140,40))
#     #         # move_path = rolling_dice()
#             # move_number = smallfont.render(f"Resultat : {move_path}", True, black)
#             # screen.blit(move_number, (screen_width-200,screen_height/2+50,140,40))

#     for ev in pygame.event.get():
#         if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == LEFT:
#             if ev.type == pygame.QUIT:
#                 pygame.quit()

#             if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40:
#                 # pygame.draw.rect(screen,dark_grey,[screen_width-200,screen_height/2,140,40])
#                 # screen.blit(text_dice , (screen_width-150,screen_height/2+10,140,40))
#                 move_path = rolling_dice()
#                 move_number = smallfont.render(f"Result : {move_path}", True, black)
#                 screen.blit(move_number, (screen_width-200,screen_height/2+50,140,40))
#                 i = i+move_path
#                 angle = (2 * math.pi / len(cases)) * i
#                 x = center[0] + int(radius * math.cos(angle))
#                 y = center[1] + int(radius * math.sin(angle))
#                 star = pygame.image.load("media/Stars_mario.png")
#                 star = pygame.transform.scale(star, (30,30))
#                 screen.blit(star, (x-15,y-15))
#     pygame.display.update()
#     fps.tick(10)

# #Ce bloc ci permet d'afficher le pion dans la case, plus on augmente le pion, plus ca va loin dans le cercle

# # if i == 3:
# #     star = pygame.image.load("media/Stars_mario.png")
# #     star = pygame.transform.scale(star, (30,30))
# #     screen.blit(star, (x-15,y-15)

# #start the display
# while True:
#     for ev in pygame.event.get():
#         if ev.type == pygame.QUIT:
#             pygame.quit()
#      #store the (x,y) coordinates into the variable as a tuple 
#     mouse = pygame.mouse.get_pos() 
#     #create buttons with text on them and change colour if mouse hovers over them
#     pygame.draw.rect(screen, light_grey,[screen_width-200,screen_height/2,140,40]) 

#     screen.fill(white)
#     pursuit_board()
    
#     pygame.display.flip()


# #il faut créer un bouton pour lancer le dé
# #le joueur lance, on récupère le dé et on fait avancer le pion grâce au roulage de dé.