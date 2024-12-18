import json
import random
import os
import time
from src.player import Player
from src.dice import rolling_dice


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[34m"
RESET = "\033[0m"
BOLD = "\033[1m"

class Game:
    def __init__(self, players):
        self.players = players
        self.current_player_idx = 0
        self.current_question = 0
        self.categories_per_quarter = [
            ["Bases de données", "🎲", "Langages de programmation", "Ligne de commandes", "Actualités IA", "Agile", "DevOps"],
            ["Agile", "🎲", "DevOps", "Ligne de commandes", "Actualités IA", "Bases de données", "Langages de programmation"],
            ["DevOps", "🎲", "Langages de programmation", "Ligne de commandes", "Actualités IA", "Bases de données", "Agile"],
            ["Langages de programmation", "🎲", "Agile", "Base de données", "Actualités IA", "DevOps", "Ligne de commandes"],
            ["Actualités IA", "🎲", "Langages de programmation", "Agile", "DevOps", "Ligne de commandes", "Bases de données"],
            ["Ligne de commandes", "🎲", "DevOps", "Bases de données", "Langages de programmation", "Agile", "Actualités IA"],
        ]
        self.board = self.create_board()
        self.special_case_indices = [0, 7, 14, 21, 28, 35, 42] 
        self.questions = self.load_questions()

    def load_questions(self):
        with open("data/questions.json", "r") as file:
            return json.load(file)

    def create_board(self):
        board = []
        for i in range(6):
            board.extend(self.categories_per_quarter[i])
        return board

    def get_question_by_category(self, category):
        self.current_question += 1
        if category in self.questions:
            category_questions = self.questions[category]
            if category_questions:
                return random.choice(category_questions)
        return None

    def is_special_case(self, position):
        """Vérifie si la position actuelle est une case spéciale."""
        return position in self.special_case_indices

    def get_possible_categories(self, current_position, steps, board_size):
        """Retourne les catégories des cases accessibles après un lancer de dé."""
        forward_position = (current_position + steps) % board_size
        backward_position = (current_position - steps) % board_size
        forward_category = self.board[forward_position]
        backward_category = self.board[backward_position]
        return forward_position, forward_category, backward_position, backward_category
    
    def is_game_over(self):
        for player in self.players:
            if player.final_score == 6:
                return player
        return None
    
    def display_scores(self):
        print(f"\n{BOLD}{YELLOW}Récapitulatif des scores :{RESET}")
        for player in self.players:
            print(f"\n{BOLD}{BLUE}{player.name}{RESET} :")
            for category, score in player.score_by_theme.items():
                print(f"  {category}: {score} Δ")
            print(f"{BOLD}Score total : {player.final_score} Δ{RESET}")

    def play_turn(self):
        player = self.players[self.current_player_idx]

        while player.final_score < 6:
            roll = rolling_dice()
            print(f"{RESET}{player.name} lances le dé et obtiens {roll}\n")

            forward_pos, forward_cat, backward_pos, backward_cat = self.get_possible_categories(
            player.position, roll, len(self.board)
            )
            print(f"Options possibles :")
            print(f"{BOLD}{BLUE}> (Avancer) : Case {forward_pos + 1} - {forward_cat}{RESET}")
            print(f"{BOLD}{BLUE}< (Reculer) : Case {backward_pos + 1} - {backward_cat}{RESET}\n")

            while True:
                direction = input(f"{RESET}Vers où souhaitez-vous vous déplacer (< ou >)? ")
                if direction in (">", "<"):
                    player.move(roll, len(self.board), direction)
                    break
                else:
                    print(f"{RED}Entrée invalide! Choisissez parmi ces deux choix : < ou >")

            current_category = self.board[player.position]
            print(f"{player.name} se trouve sur la case {player.position + 1} {BOLD}{BLUE}(Catégorie: {current_category})\n")

            question_data = self.get_question_by_category(current_category)
            if question_data:
                print(f"{BOLD}{BLUE}Question: {RESET}{question_data['question']}\n")
                print(f"{BOLD}{BLUE}Choix:")
                for choix in question_data["choix"]:
                    print(f"{RESET} {choix}")

                while True:
                    try:
                        player_answer = int(input(f"\n{RESET}Votre réponse (numéro): "))
                        time.sleep(1)
                        if 1 <= player_answer <= len(question_data["choix"]):
                            break
                        else:
                            print(f"{RED}Veuillez entrer un numéro valide.")
                    except ValueError:
                        print(f"{RED}Entrée invalide. Veuillez entrer un numéro.")

                if player_answer == question_data["reponse"][1]:
                    print(f"\n{GREEN}Bonne réponse !\n")
                    if self.is_special_case(player.position):
                        print(f"\033[4mCASE SPÉCIALE: Vous avez gagné un Δ!\033[0m\n")
                        if player.score_by_theme.get(current_category, 0) < 1:
                            player.score_by_theme[current_category] = 1

                    score_total = player.count_score()
                    score_by_categorie = player.score_by_theme.get(current_category, 0)
                    print(f"{RESET}Score pour le thème {current_category} = {score_by_categorie}")
                    print(f"Score total = {score_total}")
                    print(f"Nombre de {GREEN}Δ {RESET}gagné = {player.final_score}\n\n")
                else:
                    print(f"{RED}Mauvaise réponse. La bonne réponse était : {question_data['reponse'][1]}.")
                    time.sleep(1)
                    break
            else:
                print(f"{YELLOW}Relancez le dé!")
                time.sleep(1)

        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)