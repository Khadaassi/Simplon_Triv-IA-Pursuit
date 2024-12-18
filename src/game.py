import json, random

from src.dice import rolling_dice
from src.player import Player

class Game():

    def __init__(self, players):
        self.players = players
        self.categories_per_quarter = [
            ["Bases de données","Dice", "Langages de programmation", "Ligne de commandes", "Actualités IA", "DevOps", "Agile"],
            ["DevOps","Dice", "Langages de programmation", "Ligne de commandes", "Actualités IA", "Bases de données", "Agile"],
            ["DevOps","Dice", "Agile", "Ligne de commandes", "Actualités IA", "Bases de données", "Langages de programmation"],
            ["Bases de données","Dice", "Agile", "Ligne de commandes", "Actualités IA", "DevOps", "Langages de programmation"],
            ["Actualités IA","Dice", "Langages de programmation", "Bases de données", "DevOps", "Ligne de commandes", "Agile"],
            ["Ligne de commandes","Dice", "DevOps", "Bases de données", "Langages de programmation", "Agile", "Actualités IA"] 
            ]
        self.board = self.create_board()
        self.current_player_idx = 0
        self.questions = self.load_questions()
        self.current_question = 0 
    

    def load_questions(self):
        with open('data/questions.json', 'r') as file:
            return json.load(file)
        
        
    def create_board(self):
        board = []
        for i in range(6):
            board.extend(self.categories_per_quarter[i])
        return board
    
    
    def get_question_by_category(self, category):
        if category in self.questions:
            category_questions = self.questions[category]
            if category_questions:
                return random.choice(category_questions)
            else: None
        return None

    current_category = 0

    def play_turn(self):
        player = self.players[self.current_player_idx]
        roll = rolling_dice()
        print(f"{player.name} lance le dé et obtient {roll}")
        
        direction = input("Vers où souhaitez-vous vous déplacer ( < ou >) ? ")
        player.move(roll, len(self.board), direction)
        
        current_category = self.board[player.position]
        print(f"{player.name} se trouve sur la case {player.position + 1} (Catégorie: {current_category})")
        
        if current_category == "Dice":
            print(f"Case spéciale: {current_category}. Vous relancez le dé.")
            self.play_turn()  
            return

        question_data = self.get_question_by_category(current_category)
        if question_data:
            print(f"Question: {question_data['question']}")
            print("Choix:")
            for i, choix in enumerate(question_data['choix'], 1):
                print(f"{i}. {choix}")

            player_answer = input("Votre réponse : ")

            if player_answer.strip().lower() == question_data['reponse'][1]:
                print("Bonne réponse !")
                player.count_score()
                player.score_by_theme[current_category] += 1
                print(f"Score total = {player.score}")
                print(f"Score par thème = {player.score_by_theme[current_category]}")
            else:
                print(f"Mauvaise réponse. La bonne réponse était : {question_data['reponse']}")
        

        if player.sum_of_count_by_theme == 6:
            print("Bravo ! Vous avez atteint un score par thème de 6.")
            response = input("Voulez-vous entrer dans la passerelle pour gagner ? (Y/N) : ").strip().lower()
            if response == "y":
                print(f"Félicitations {player.name}, vous avez gagné le trivial pursuit !")
                exit()  
        else:
            print(f"Votre score par thème total est de {player.sum_of_count_by_theme} sur 6.")

        # Passer au joueur suivant
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
