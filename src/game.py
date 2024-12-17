import json, random
from src.player import Player
from src.dice import rolling_dice

class Game():

    def __init__(self, players):
        self.players = players
        self.board = self.create_board()
        self.current_player_idx = 0
        self.questions = self.load_questions()

    def load_questions(self):
        with open('data/questions.json', 'r') as file:
            return json.load(file)
        
    def create_board(self):
        categories_per_quarter = [
    ["Bases de données", "Langages de programmation", "Ligne de commandes", "Actualités IA", "DevOps", "Autres catégories"],
    ["DevOps", "Langages de programmation", "Ligne de commandes", "Actualités IA", "Bases de données", "Autres catégories"],
    ["Autres catégories", "DevOps", "Ligne de commandes", "Actualités IA", "Bases de données", "Langages de programmation"],
    ["Bases de données", "Autres catégories", "Ligne de commandes", "Actualités IA", "DevOps", "Langages de programmation"],
    ["Actualités IA", "Langages de programmation", "Bases de données", "DevOps", "Ligne de commandes", "Autres catégories"],
    ["Ligne de commandes", "DevOps", "Bases de données", "Langages de programmation", "Autres catégories", "Actualités IA"] 
]
        plateau = []
        for i in range(6):
            plateau.extend(categories_per_quarter[i])
        return plateau
    

    def get_question_by_category(self, category):
        questions = self.load_questions()
        if category in questions:
            category_questions = questions[category]
            if category_questions:
                return random.choice(category_questions)
            else: None
        return None

    def play_turn(self):
        player = self.players[self.current_player_idx]
        roll = rolling_dice()
        print(f"{player.name} lance le dé et obtient {roll}")
        player.move(roll, len(self.board))
        current_category = self.board[player.position]
        print(f"{player.name} se trouve sur la case {player.position + 1} (Catégorie: {current_category})")
        
        question_data = self.get_question_by_category(current_category)
        if question_data:
            print(f"Question: {question_data['question']}")
            print("Choix:")
            for i, choix in enumerate(question_data['choix'], 1):
                print(f"{i}. {choix}")
            
            player_answer = input(f"Votre réponse : ")
            
            if player_answer.strip().lower() == question_data['reponse'].lower():
                print("Bonne réponse !")
                score= player.count_score()
                print(f"Score = {score}")
            else:
                print(f"Mauvaise réponse. La bonne réponse était : {question_data['reponse']}")
        else:
            print("Aucune question disponible dans cette catégorie.")
        
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
