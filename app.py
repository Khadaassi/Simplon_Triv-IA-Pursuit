import pygame
import math
import random
from src.game import Game
from src.player import Player
from src.dice import rolling_dice
import json

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
red= (227, 44, 54)
light_grey = (211,224,227)
very_light_grey = (240, 243, 247)
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
xsfont = pygame.font.SysFont('Corbel',20)
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
text_forward = smallfont.render('Forward', True, black)
clockwise= xsfont.render('(Clockwise)', True, black)
text_backward = smallfont.render('Backward ', True, black)
counterclockewise = xsfont.render('(Counterclockwise)', True, black)
# points = smallfont.render('Points : ', True, black)
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
points = 0      # initialise le score du joueur


# Load images
cheese = pygame.image.load("media/cheese_slice.png")
cheese = pygame.transform.scale(cheese, (30, 30))
star = pygame.image.load("media/Stars_mario.png")
star = pygame.transform.scale(star, (30, 30))


def draw_board():
    screen.fill(white)
    pygame.draw.circle(screen, dark_grey, center, 60)
    pygame.draw.circle(screen, light_grey, center, 58)
    pygame.draw.rect(screen, very_light_grey, [screen_width - 400, screen_height -1000, 350, 250])
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
     
    # screen.blit(scoring, (screen_width/2+450, screen_height/2 - 250))
    # pygame.draw.rect(screen, black, [1140, 340, 620, 320])
    # pygame.draw.rect(screen, light_grey, [1150, 350, 600, 300])

    # screen.blit(player_name, (screen_width/2+210, screen_height/2 - 180))
    # screen.blit(score, (screen_width/2+210, screen_height/2 - 160))

    # screen.blit(legend, (screen_width/2+180, screen_height/2 +200))
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

def draw_buttons():
    """Draw directional buttons"""
    pygame.draw.rect(screen, light_grey, [screen_width - 300, screen_height-880, 140, 40])  # Bouton Avancer
    pygame.draw.rect(screen, light_grey, [screen_width - 300, screen_height-830, 140, 40])  # Bouton Reculer

    screen.blit(text_forward, (screen_width - 290, screen_height-875))
    screen.blit(clockwise, (screen_width - 290, screen_height-855))
    screen.blit(text_backward, (screen_width - 290, screen_height-830))
    screen.blit(counterclockewise, (screen_width - 290, screen_height-810))


def dice_result(move_path):
    texte = f"Result : {move_path}"
    move_number = smallfont.render(texte, True, black)
    screen.blit(move_number, (screen_width - 300, screen_height -920))

def get_case_category(position,cases):
    global cat
    cat = cases[position]
    return cat

current_question = None
current__choices = None
current_answer   = None

def load_question(cat):

    """Charge une nouvelle question pour une catégorie donnée."""
    global current_question, current_choices, current_answer,questions
    with open("media/questions.JSON", 'r', encoding='utf-8') as file:
        data = json.load(file)
    questions = data[cat]
    question_dict = random.choice(questions)
    
    current_question = question_dict['question']
    current_choices = question_dict['choix']
    current_answer = question_dict['reponse']

def draw_question():
    """Affiche la question actuelle à l'écran."""
    global current_question, current_choices, current_answer, answer_buttons, cat
    answer_buttons = []


        # # Afficher la question
        # if cat == "Bases de données": 
        #     question_surface = smallfont.render(current_question, True, blue)
        #     screen.blit(question_surface, (screen_width / 2 + 210, screen_height / 2 - 130))
        # elif cat == "Langages de programmation":
        #     question_surface = smallfont.render(current_question, True, green)
        #     screen.blit(question_surface, (screen_width / 2 + 210, screen_height / 2 - 130))           
        # elif cat == "Ligne de commandes":
        #     question_surface = smallfont.render(current_question, True, pink)
        #     screen.blit(question_surface, (screen_width / 2 + 210, screen_height / 2 - 130)) 
        # elif cat == "Actualités IA":
        #     question_surface = smallfont.render(current_question, True, orange)
        #     screen.blit(question_surface, (screen_width / 2 + 210, screen_height / 2 - 130))
        # elif cat == "Agile":
        #     question_surface = smallfont.render(current_question, True, yellow)
        #     screen.blit(question_surface, (screen_width / 2 + 210, screen_height / 2 - 130)) 
        # elif cat == "DevOps":
        #     question_surface = smallfont.render(current_question, True, purple)
        #     screen.blit(question_surface, (screen_width / 2 + 210, screen_height / 2 - 130))    


        # Afficher la question
        
    question_surface = smallfont.render(current_question, True, black)
    screen.blit(question_surface, (screen_width / 2 + 210, screen_height / 2 - 130))
        
          # Liste des rectangles des boutons pour les choix
        # Afficher les choix
    if current_choices:
        for i, choice in enumerate(current_choices):
            choice_surface = smallfont.render(f"{i+1}. {choice}", True, black)
            screen.blit(choice_surface, (screen_width / 2 + 210, screen_height / 2 - 90 + i * 30))
            button_rect = pygame.draw.rect(screen, light_grey, [screen_width / 2 + 180, screen_height / 2 - 88 + i * 30, 20, 20])
            button_rect = pygame.Rect(screen_width / 2 + 180, screen_height / 2 - 88 + i * 30, 20, 20)
            answer_buttons.append(button_rect)
            screen.blit(text_dice, (screen_width -250, screen_height -980 + 10))


            #store the (x,y) coordinates into the variable as a tuple 
            mouse = pygame.mouse.get_pos() 
            #create buttons with text on them and change colour if mouse hovers over them

            # Affiche le carré en noir si la souris passe dessus 
            if screen_width / 2 + 180<= mouse[0] <= screen_width / 2 + 180 +20 and screen_height/ 2 - 88 + i * 30 <= mouse[1] <= screen_height/ 2 - 88+20 + i * 30: 
                pygame.draw.rect(screen, black, [screen_width / 2 + 180, screen_height / 2 - 88 + i * 30, 20, 20])
            
            

def check_answer(selected_index):
    """Vérifie si l'index sélectionné correspond à la bonne réponse."""
    global current_choices, current_answer, points
    
    if current_choices[selected_index] == current_answer:
        print("Bonne réponse!")
        # Indiquer la bonne réponse en vert
        pygame.draw.rect(screen, green, [screen_width / 2 + 180, screen_height / 2 - 88 + selected_index * 30, 20, 20])
        points += 1

    else:
        print("Mauvaise réponse!")
        # Indiquer la réponse incorrecte en rouge
        pygame.draw.rect(screen, red, [screen_width / 2 + 180, screen_height / 2 - 88 + selected_index * 30, 20, 20])

    scoring_surface = smallfont.render(str(points), True, black)
    screen.blit(scoring_surface, (screen_width / 2 , screen_height / 2 ))
    # clock    
    # pygame.display.update()
        


# def draw_question(cat):
#     with open("media/questions.JSON", 'r', encoding='utf-8') as file:
#             data = json.load(file)
#     questions = data[cat]
#     question_dict = random.choice(questions)
#     question = question_dict['question']
#     choice = question_dict['choix']
#     answers = question_dict['reponse']

#     display_question = smallfont.render(question, True, black)
#     screen.blit(display_question, (screen_width/2+210, screen_height/2 - 130))

    
#     return question, choice #, answers

#
#  def move(move_path, direction, cases):
#     if direction == ">":
#         player_position = (player_position + move_path) % len(cases)
#     if direction == "<":
#             player_position = (player_position + move_path) % len(cases)
#     return player_position

current_question = None
current_choices = None

def main():
    global player_position, current_question, current_choices, player_position, answer_buttons
    direction = None
    move_path = None
    
    running = True
    while running:
                # Draw the board and the player
        draw_board()
        pursuit_board()
        draw_player(player_position)
        
         # Afficher le score du dé
        if move_path is not None:
            dice_result(move_path)

        # Dessiner les boutons de direction
        if move_path is not None: #and not question_displayed:
            draw_buttons()

        # Get new question if the player moves
        if direction is not None and current_question is None:
            cat = get_case_category(player_position,cases)
            load_question(cat)
            # current_question, current_question=draw_question()
            direction =None
        draw_question()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()

                                # Vérifier si on clique sur les boutons de réponses
                for i, rect in enumerate(answer_buttons):
                    if rect.collidepoint(mouse):  # Vérifie si le clic est dans le bouton
                        check_answer(i)  # Vérifie si la réponse est correcte ou non


                if screen_width - 300 <= mouse[0] <= screen_width - 160 and screen_height-980 <= mouse[1] <= screen_height-940:
                    # Roll dice and update position
                    move_path = rolling_dice()
                    direction =None
                    #current_question, current_choices = None, None
                                    # Vérifier si on clique sur les boutons de réponses
                for i, rect in enumerate(answer_buttons):
                    if rect.collidepoint(mouse):  # Vérifie si le clic est dans le bouton
                        check_answer(i)  # Vérifie si la réponse est correcte ou non

                if move_path is not None:
                    if screen_width -300 <=mouse[0]<=screen_width-160 and screen_height-880<=mouse[1]<=screen_height-840:
                        player_position = (player_position + move_path) % len(cases)
                        direction = 1
                        

                    if screen_width -300 <=mouse[0]<=screen_width-160 and screen_height-830<=mouse[1]<=screen_height-790:
                        player_position = (player_position - move_path) % len(cases)
                        direction = -1
                    
                    # Check answers
                    # if direction is not None:
                    # fonction clique sur une reponse
                    #################################################################
                    # for i in range(4):
                    #     if screen_width / 2 + 180 <= mouse[0] <= screen_width / 2 + 180 +20 and screen_height / 2 - 88 + i+1 * 30 <= mouse[1] <=  screen_height / 2 - 68 + i+1 * 30:
                    #         answer = i+1
                    #         screen.blit(legend, (screen_width/2 -250, screen_height/2 -10))
                    #         print(f'mouse : {mouse[0]}')
                    #         print(screen_width / 2 + 180)
                    #         print(screen_width / 2 + 180 +20)
                    #         print(current_choices[i])
                    #         print(i)
                    #         mouse = pygame.mouse.get_pos()
                            # if current_choices[i] == current_answer:
                            #     print('you re the goat')
                            #     pygame.draw.rect(screen, green, [screen_width / 2 + 180, screen_height / 2 - 88 + i * 30, 20, 20])

                    if current__choices is not None:
                        for i in range(len(current_choices)):
                            if screen_width / 2 + 180 <= mouse[0] <= screen_width / 2 + 200 and screen_height / 2 - 88 + i * 30 <= mouse[1] <= screen_height / 2 - 68 + i * 30:
                                check_answer(i)
                                print(f'mouse : {mouse[0]}')
                                print(screen_width / 2 + 180)
                                print(screen_width / 2 + 180 +20)
                                

                                #function compare(answer)

                        #screen_width / 2 + 180, screen_height / 2 - 88 + i+1 * 30
                            
                        

        
        # event propose reponse

            




        
        if current_question is not None and current_choices is not None:
            display_question = smallfont.render(current_question, True, black)
            screen.blit(display_question, (screen_width / 2 + 210, screen_height / 2 - 130))
            direction =None

        # Draw the dice button
        pygame.draw.rect(screen, light_grey, [screen_width - 300, screen_height -980, 140, 40])
        screen.blit(text_dice, (screen_width -250, screen_height -980 + 10))

        # Print the last result of dice to the player
        # if last_dice_result is not None:
        #     texte=f"Résultat : {last_dice_result}"
        #     move_number = smallfont.render(texte, True, black)
        #     screen.blit(move_number, (screen_width - 200, screen_height / 2 + 50, 140, 40))
        # pygame.display.update()
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()

