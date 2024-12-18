import json
import random
import os
import time
from src.player import Player
from src.dice import rolling_dice

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

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
            ["Bases de données", "Dice", "Langages de programmation", "Ligne de commandes", "Actualités IA", "DevOps", "Agile"],
            ["DevOps", "Dice", "Langages de programmation", "Ligne de commandes", "Actualités IA", "Bases de données", "Agile"],
            ["DevOps", "Dice", "Agile", "Ligne de commandes", "Actualités IA", "Bases de données", "Langages de programmation"],
            ["Bases de données", "Dice", "Agile", "Ligne de commandes", "Actualités IA", "DevOps", "Langages de programmation"],
            ["Actualités IA", "Dice", "Langages de programmation", "Bases de données", "DevOps", "Ligne de commandes", "Agile"],
            ["Ligne de commandes", "Dice", "DevOps", "Bases de données", "Langages de programmation", "Agile", "Actualités IA"],
        ]
        self.board = self.create_board()
        self.special_case_indices = [0, 6, 13, 20, 27, 34, 41] 
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

    def play_turn(self):
        player = self.players[self.current_player_idx]

        while player.final_score < 6:
            roll = rolling_dice()
            print(f"{RESET}{player.name} lances le dé et obtiens {roll}\n")

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
                for idx, choix in enumerate(question_data["choix"], start=1):
                    print(f"{RESET} {idx}. {choix}")

                while True:
                    try:
                        player_answer = int(input(f"\n{RESET}Votre réponse (numéro): "))
                        if 1 <= player_answer <= len(question_data["choix"]):
                            break
                        else:
                            print(f"{RED}Veuillez entrer un numéro valide.")
                    except ValueError:
                        print(f"{RED}Entrée invalide. Veuillez entrer un numéro.")

                if player_answer == question_data["reponse"]:
                    print(f"\n{GREEN}Bonne réponse !\n")
                    player.score_by_theme[current_category] += 1

                    if self.is_special_case(player.position):
                        print(f"\033[4mCASE SPÉCIALE: Vous avez gagné un Δ!\033[0m\n")

                    print(f"{RESET}Score pour le thème {current_category} = {player.score_by_theme[current_category]}")
                    print(f"Score total = {player.score}")
                    print(f"Nombre de {GREEN}Δ {RESET}gagné = {player.final_score}\n\n")
                else:
                    print(f"{RED}Mauvaise réponse. La bonne réponse était : {question_data['reponse']}.")
                    break
            else:
                print(f"{YELLOW}Aucune question disponible pour cette catégorie. Relancez le dé!\n")


            self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
