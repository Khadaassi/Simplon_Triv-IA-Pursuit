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
red= (227, 44, 54)
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
    cat = cases[position]
    return cat

current_question = None
current_choices = None
current_answer   = None

def load_question(cat):
    """Charge une nouvelle question pour une catégorie donnée."""
    global current_question, current_choices, current_answer
    with open("media/questions.JSON", 'r', encoding='utf-8') as file:
        data = json.load(file)
    questions = data[cat]
    question_dict = random.choice(questions)
    current_question = question_dict['question']
    current_choices = question_dict['choix']
    current_answer = question_dict['reponse']

# def draw_question():
#     """Affiche la question actuelle et ses choix à l'écran."""
#     global current_question, current_choices
    
#     if current_question is not None:
#         # Afficher la question
#         question_surface = smallfont.render(current_question, True, black)
#         screen.blit(question_surface, (screen_width / 2 + 210, screen_height / 2 - 130))
        
#         # Afficher les choix
#         if current_choices:
#             for i, choice in enumerate(current_choices):
#                 # Position des choix
#                 x = screen_width / 2 + 180
#                 y = screen_height / 2 - 88 + i * 40
#                 choice_surface = smallfont.render(f"{i+1}. {choice}", True, black)
#                 pygame.draw.rect(screen, light_grey, [x, y, 20, 20])  # Rectangle du choix
#                 screen.blit(choice_surface, (x + 10, y + 5))

verification_done = False

# def check_answer(selected_index):
#     """Vérifie si l'index sélectionné correspond à la bonne réponse et affiche le résultat."""
#     global current_choices, current_answer, verification_done

#     x = screen_width / 2 + 180
#     y = screen_height / 2 - 88 + selected_index * 40

#     # Comparer la réponse sélectionnée avec la réponse correcte
#     if current_choices[selected_index] == current_answer:
#         # Bonne réponse : dessiner un rectangle vert
#         pygame.draw.rect(screen, green, [x, y, 20, 20])
#         verification_done = True  # Valider la réponse
#     else:
#         # Mauvaise réponse : dessiner un rectangle rouge pour la sélection et indiquer la bonne réponse
#         pygame.draw.rect(screen, red, [x, y, 20, 20])
#         correct_index = current_choices.index(current_answer)
#         correct_y = screen_height / 2 - 88 + correct_index * 40
#         pygame.draw.rect(screen, green, [x, correct_y, 20, 20])
#         verification_done = True

validated_answers = [None, None, None, None]  # Permet de garder l'état de chaque réponse (None, True, False)

def check_answer(selected_index):
    """Vérifie si l'index sélectionné correspond à la bonne réponse et marque le résultat."""
    global validated_answers, current_choices, current_answer, verification_done

    # Comparer la réponse sélectionnée avec la bonne réponse
    if current_choices[selected_index] == current_answer:
        validated_answers[selected_index] = True  # Marquer comme bonne réponse
        verification_done = True  # Valider la question
    else:
        validated_answers[selected_index] = False  # Marquer comme mauvaise réponse
        # Marquer également la bonne réponse en vert
        correct_index = current_choices.index(current_answer)
        validated_answers[correct_index] = True
        verification_done = True  # Valider la question

def draw_question():
    """Dessine la question et ses choix sur l'écran."""
    global current_question, current_choices, validated_answers

    if current_question:
        # Dessiner la question
        question_text = smallfont.render(current_question, True, black)
        screen.blit(question_text, (screen_width / 2 + 200, screen_height / 2 - 180))

        # Dessiner les choix
        for i, choice in enumerate(current_choices):
            choice_text = smallfont.render(choice, True, black)

            # Déterminer la couleur de l'arrière-plan en fonction de la validation
            if validated_answers[i] is None:  # Pas encore validé
                bg_color = light_grey
            elif validated_answers[i]:  # Bonne réponse
                bg_color = green
            else:  # Mauvaise réponse
                bg_color = red

            # Dessiner le rectangle coloré et le texte du choix
            x = screen_width / 2 + 200
            y = screen_height / 2 - 88 + i * 40
            pygame.draw.rect(screen, bg_color, [x - 10, y, 20, 20])
            screen.blit(choice_text, (x +40, y))
def main():
    global player_position, current_question, current_choices, player_position, verification_done
    direction = None
    move_path = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()

                # Action : lancer le dé uniquement si aucune question n'est en attente de validation
                if (
                    screen_width - 300 <= mouse[0] <= screen_width - 160
                    and screen_height - 980 <= mouse[1] <= screen_height - 940
                    and not verification_done
                ):
                    move_path = rolling_dice()
                    direction = None

                # Action : traiter les réponses
                if current_choices is not None and not verification_done:
                    for i in range(len(current_choices)):
                        x = screen_width / 2 + 180
                        y = screen_height / 2 - 88 + i * 40
                        if x <= mouse[0] <= x + 20 and y <= mouse[1] <= y + 20:
                            check_answer(i)

                # Action : gérer les boutons avancer/reculer
                if move_path is not None and not verification_done:
                    if screen_width - 300 <= mouse[0] <= screen_width - 160 and screen_height - 880 <= mouse[1] <= screen_height - 840:
                        player_position = (player_position + move_path) % len(cases)
                        direction = 1

                    if screen_width - 300 <= mouse[0] <= screen_width - 160 and screen_height - 830 <= mouse[1] <= screen_height - 790:
                        player_position = (player_position - move_path) % len(cases)
                        direction = -1

        # Dessiner le plateau, le joueur et les autres éléments
        draw_board()
        pursuit_board()
        draw_player(player_position)

        # Afficher le score du dé
        if move_path is not None and not verification_done:
            dice_result(move_path)

        # Dessiner les boutons de direction uniquement si le joueur peut encore bouger
        if move_path is not None and not verification_done:
            draw_buttons()

        # Charger une nouvelle question si nécessaire
        if direction is not None and current_question is None and not verification_done:
            cat = get_case_category(player_position, cases)
            load_question(cat)
            direction = None

        # Afficher la question actuelle
        draw_question()

        # Dessiner le bouton de dé
        pygame.draw.rect(screen, light_grey, [screen_width - 300, screen_height - 980, 140, 40])
        screen.blit(text_dice, (screen_width - 250, screen_height - 980 + 10))

        # Rafraîchir l'écran
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()

# def main():
#     global player_position, current_question, current_choices, player_position,verification_done
#     direction = None
#     move_path = None
   
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 mouse = pygame.mouse.get_pos()
#                 if screen_width - 300 <= mouse[0] <= screen_width - 160 and screen_height-980 <= mouse[1] <= screen_height-940:
#                     # Roll dice and update position
#                     move_path = rolling_dice()
#                     direction =None
#                     #current_question, current_choices = None, None
#                 if current_choices is not None:
#                     for i in range(len(current_choices)):
#                         x = screen_width / 2 + 180
#                         y = screen_height / 2 - 88 + i * 40
#                         if x <= mouse[0] <= x + 20 and y <= mouse[1] <= y + 20:
#                             check_answer(i)

#                 if move_path is not None:
#                     if screen_width -300 <=mouse[0]<=screen_width-160 and screen_height-880<=mouse[1]<=screen_height-840:
#                         player_position = (player_position + move_path) % len(cases)
#                         direction = 1
                        

#                     if screen_width -300 <=mouse[0]<=screen_width-160 and screen_height-830<=mouse[1]<=screen_height-790:
#                         player_position = (player_position - move_path) % len(cases)
#                         direction = -1
                    
#                     # Check answers
#                     # if direction is not None:
#                     # fonction clique sur une reponse
#                     #################################################################
#                     # for i in range(4):
#                     #     if screen_width / 2 + 180 <= mouse[0] <= screen_width / 2 + 180 +20 and screen_height / 2 - 88 + i+1 * 30 <= mouse[1] <=  screen_height / 2 - 68 + i+1 * 30:
#                     #         answer = i+1
#                     #         screen.blit(legend, (screen_width/2 -250, screen_height/2 -10))
#                     #         print(f'mouse : {mouse[0]}')
#                     #         print(screen_width / 2 + 180)
#                     #         print(screen_width / 2 + 180 +20)
#                     #         print(current_choices[i])
#                     #         print(i)
#                     #         mouse = pygame.mouse.get_pos()
#                             # if current_choices[i] == current_answer:
#                             #     print('you re the goat')
#                             #     pygame.draw.rect(screen, green, [screen_width / 2 + 180, screen_height / 2 - 88 + i * 30, 20, 20])

#                     if current_choices is not None and not verification_state:
#                         for i in range(len(current_choices)):
#                             if screen_width / 2 + 180 <= mouse[0] <= screen_width / 2 + 200 and screen_height / 2 - 88 + i * 30 <= mouse[1] <= screen_height / 2 - 68 + i * 30:
#                                 verification_state = True
#                                 if verification_state:
#                                     check_answer(i)
#                     if verification_state:
#                         for i, choice in enumerate(current_choices):
#                             x = screen_width / 2 + 180
#                             y = screen_height / 2 - 88 + i * 40
#                             color = green if choice == current_answer else red
#                             pygame.draw.rect(screen, color, [x, y, 200, 30])

#                                 #function compare(answer)

#                         #screen_width / 2 + 180, screen_height / 2 - 88 + i+1 * 30
                            
                        
#         # Draw the board and the player
#         draw_board()
#         pursuit_board()
#         draw_player(player_position)
        
#          # Afficher le score du dé
#         if move_path is not None and verification_state == False:
#             dice_result(move_path)

#         # Dessiner les boutons de direction
#         if move_path is not None and verification_state == False: #and not question_displayed:
#             draw_buttons()

#         # Get new question if the player moves
#         if direction is not None and current_question is None and verification_state==False:
#             cat = get_case_category(player_position,cases)
#             load_question(cat)
#             # current_question, current_question=draw_question()
#             direction =None
#         draw_question()
        
#         # event propose reponse





        
#         if current_question is not None and current_choices is not None:
#             display_question = smallfont.render(current_question, True, black)
#             screen.blit(display_question, (screen_width / 2 + 210, screen_height / 2 - 130))
#             direction =None

#         # Draw the dice button
#         pygame.draw.rect(screen, light_grey, [screen_width - 300, screen_height -980, 140, 40])
#         screen.blit(text_dice, (screen_width -250, screen_height -980 + 10))

#         # Print the last result of dice to the player
#         # if last_dice_result is not None:
#         #     texte=f"Résultat : {last_dice_result}"
#         #     move_number = smallfont.render(texte, True, black)
#         #     screen.blit(move_number, (screen_width - 200, screen_height / 2 + 50, 140, 40))

#         pygame.display.flip()
#         clock.tick(10)

#     pygame.quit()


# if __name__ == "__main__":
#     main()