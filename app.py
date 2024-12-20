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
text_dice = smallfont.render('Dé', True, black)
title = bigfont.render('Triv-IA-pursuit', True, black)
sub_title=middlefont.render('Triv-IA-pursuit', True, black)
screen.blit(title, (screen_width/2-100, screen_height/2))
text_forward = smallfont.render('Avancer', True, black)
clockwise= xsfont.render('(horaire)', True, black)
text_backward = smallfont.render('Reculer ', True, black)
counterclockewise = xsfont.render('(antihoraire)', True, black)
scoring = smallfont.render('Scoring', True, black)
rect = pygame.Rect(100, 100, 200, 150)
player_name = smallfont.render('Player : ', True, black)
score = smallfont.render('score : ', True, black)
legend = smallfont.render('Légende : ', True, black)
ia = smallfont.render("Actualités IA", True, black)
devops = smallfont.render("DevOps", True, black)
ligne_commande = smallfont.render("Ligne de commandes", True, black)
db = smallfont.render("Bases de données", True, black)
langage_progra = smallfont.render("Langages de programmation", True, black)
agile = smallfont.render("AGILE", True, black)


LEFT = 1

# center positions
center = (screen_width / 2 - 450, screen_height / 2)
radius = 400

# initialize game state
player_position = 0  # Current position of the player
cases = Game.create_board(Game(36))  # Initialize board
score = 0
total_questions = 0
cheese_score = 0
yellow_cheese =0
green_cheese=0
pink_cheese=0
blue_cheese=0
purple_cheese=0
orange_cheese=0

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

    screen.blit(legend, (screen_width/2, screen_height/2 +280))
    pygame.draw.circle(screen, blue, (screen_width/2+180, screen_height/2 +290), 20)
    pygame.draw.circle(screen, green, (screen_width/2+180, screen_height/2 +340), 20)
    pygame.draw.circle(screen, pink, (screen_width/2+180, screen_height/2 +390), 20)
    pygame.draw.circle(screen, orange, (screen_width/2+600, screen_height/2 +290), 20)
    pygame.draw.circle(screen, yellow, (screen_width/2+600, screen_height/2 +340), 20)
    pygame.draw.circle(screen, purple, (screen_width/2+600, screen_height/2 +390), 20)


    screen.blit(db, (screen_width/2+210, screen_height/2 +280))
    screen.blit(langage_progra, (screen_width/2+210, screen_height/2 +330))
    screen.blit(ligne_commande, (screen_width/2+210, screen_height/2 +380))
    screen.blit(ia, (screen_width/2+630, screen_height/2 +280))
    screen.blit(agile, (screen_width/2+630, screen_height/2 +330))
    screen.blit(devops, (screen_width/2+630, screen_height/2 +380))

            
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


verification_done = False


validated_answers = [None, None, None, None]  # Permet de garder l'état de chaque réponse (None, True, False)

def check_answer(selected_index):
    """Vérifie si l'index sélectionné correspond à la bonne réponse et marque le résultat."""
    global validated_answers, current_choices, current_answer, verification_done, total_questions, score, cheese_score, yellow_cheese, green_cheese, pink_cheese, blue_cheese, purple_cheese, orange_cheese
   
    total_questions+=1
    # Comparer la réponse sélectionnée avec la bonne réponse
    if current_choices[selected_index] == current_answer:
        validated_answers[selected_index] = True  # Marquer comme bonne réponse
        verification_done = True  # Valider la question
        score+=1

        if player_position % 6 == 0:
            cheese_score += 1

            cat = get_case_category(player_position,cases)
            if cat == "Bases de données":
                blue_cheese = 1
            if cat == "Langages de programmation":
                green_cheese = 1
            if cat == "Ligne de commandes":
                pink_cheese = 1
            if cat == "Actualités IA":
                orange_cheese = 1
            if cat == "Agile":
                yellow_cheese = 1
            if cat == "DevOps":
                purple_cheese = 1
       
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

        draw_score()

def draw_button_reroll():
    """Dessine un bouton pour relancer le dé."""
    button_color = light_grey  # Bleu
    button_text_color = black
    button_rect = pygame.Rect(screen_width/2+200, screen_height-2 - 450, 200, 50)  # Position du bouton

    # Dessiner le bouton
    pygame.draw.rect(screen, button_color, button_rect)

    # Ajouter le texte "Relancer le dé"
    button_text = smallfont.render("Relancer le dé", True, button_text_color)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    return button_rect  # Retourner le rectangle pour détecter les clics

def reroll_dice():
    """Relance le dé et met à jour la position du joueur."""
    global player_position, verification_done, validated_answers, current_question, current_choices

    # Simuler un lancer de dé (1 à 6)
    verification_done = False
    validated_answers = [None] * 4
    current_question = None
    current_choices = None

    # Simuler un nouveau lancer de dé
    move_path = rolling_dice()
    return move_path

def draw_score():
    """Affiche le score actuel sur l'écran."""
    global score, total_questions, cheese_score, blue_cheese, orange_cheese, yellow_cheese, green_cheese, purple_cheese, pink_cheese
    score_text = smallfont.render(f"Score : {score}/{total_questions}", True, red)
    screen.blit(score_text, (screen_width/2+200, screen_height-2 - 380))
    cheese_text = smallfont.render(f"Camemberts : {cheese_score}", True, red)
    screen.blit(cheese_text, (screen_width/2 + 200, screen_height-2 - 340))
    
    if blue_cheese == 1:
        blue_text = xsfont.render("Camembert bleu validé", True, red)
        screen.blit(blue_text, (screen_width/2 + 600, screen_height-2 - 400))
    if green_cheese == 1:
        green_text = xsfont.render("Camembert vert validé", True, red)
        screen.blit(green_text, (screen_width/2 + 600, screen_height-2 - 380))
    if pink_cheese == 1:
        pink_text = xsfont.render("Camembert rose validé", True, red)
        screen.blit(pink_text, (screen_width/2 + 600, screen_height-2 - 360))
    if orange_cheese == 1:
        orange_text = xsfont.render("Camembert orange validé", True, red)
        screen.blit(orange_text, (screen_width/2 + 600, screen_height-2 - 340))
    if yellow_cheese == 1:
        yellow_text = xsfont.render("Camembert jaune validé", True, red)
        screen.blit(yellow_text, (screen_width/2 + 600, screen_height-2 - 320))
    if purple_cheese == 1:
        purple_text = xsfont.render("Camembert violet validé", True, red)
        screen.blit(purple_text, (screen_width/2 + 600, screen_height-2 - 300))
            

def main():
    global player_position, verification_done, current_question, current_choices
    direction = None
    move_path = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()

                # Détection du clic sur le bouton "Relancer le dé"
                if verification_done:
                    reroll_button_rect = draw_button_reroll()
                    if reroll_button_rect.collidepoint(mouse):
                        move_path = reroll_dice()
                        direction = None

                # Lancer le dé initialement
                if not verification_done:
                    if screen_width - 300 <= mouse[0] <= screen_width - 160 and screen_height - 980 <= mouse[1] <= screen_height - 940:
                        move_path = rolling_dice()
                        direction = None

                # Gestion des réponses
                if current_choices is not None and not verification_done:
                    for i in range(len(current_choices)):
                        x = screen_width / 2 + 200
                        y = screen_height / 2 - 88 + i * 40
                        if x <= mouse[0] <= x + 20 and y <= mouse[1] <= y + 20:
                            check_answer(i)

                # Gestion des boutons de direction
                if move_path is not None and not verification_done:
                    if screen_width - 300 <= mouse[0] <= screen_width - 160 and screen_height - 880 <= mouse[1] <= screen_height - 840:
                        player_position = (player_position + move_path) % len(cases)
                        direction = 1

                    if screen_width - 300 <= mouse[0] <= screen_width - 160 and screen_height - 830 <= mouse[1] <= screen_height - 790:
                        player_position = (player_position - move_path) % len(cases)
                        direction = -1

        # Dessiner le plateau et les autres éléments
        draw_board()
        pursuit_board()
        draw_player(player_position)
        draw_score

        # Dessiner les boutons et afficher les résultats
        if move_path is not None and not verification_done:
            dice_result(move_path)
            draw_buttons()

        # Charger une question si le déplacement est terminé
        if direction is not None and current_question is None and not verification_done:
            cat = get_case_category(player_position, cases)
            load_question(cat)
            direction = None

        # Dessiner la question et les choix
        draw_question()
        
        # Dessiner le bouton de dé
        pygame.draw.rect(screen, light_grey, [screen_width - 300, screen_height - 980, 140, 40])
        screen.blit(text_dice, (screen_width - 250, screen_height - 980 + 10))

        # Bouton "Relancer le dé" si la vérification est terminée
        if verification_done:
            draw_button_reroll()

        # Rafraîchir l'écran
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()