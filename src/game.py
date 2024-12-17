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
    "Bases de données", "Langages de programmation", "Ligne de commandes", "Actualités IA", "DevOps", ['AGIL', 'Actualités IA', 'DevOps', 'Ligne de commandes', 'Bases de données', 'Langages de programmation'],
    "Ligne de commandes", "Actualités IA", "DevOps", "AGIL", "Bases de données", ['Langages de programmation', 'Actualités IA', 'DevOps', 'Ligne de commandes', 'Bases de données', 'AGIL'],
    "Actualités IA", "DevOps", "AGIL", "Bases de données", "Langages de programmation", ['Ligne de commandes', 'Actualités IA', 'DevOps', 'AGIL', 'Bases de données', 'Langages de programmation'],
    "DevOps", "AGIL", "Bases de données", "Langages de programmation", "Ligne de commandes", ['Actualités IA', 'AGIL', 'DevOps', 'Ligne de commandes', 'Bases de données', 'Langages de programmation'],
    "AGIL", "Bases de données", "Langages de programmation", "Ligne de commandes", "Actualités IA", ['DevOps', 'Actualités IA', 'AGIL', 'Ligne de commandes', 'Bases de données', 'Langages de programmation'],
    "Langages de programmation", "Ligne de commandes", "Actualités IA", "DevOps", "AGIL", ['Bases de données', 'Actualités IA', 'DevOps', 'Ligne de commandes', 'AGIL', 'Langages de programmation']
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

    current_category = 0

    def play_turn(self):
        player = self.players[self.current_player_idx]
        roll = rolling_dice()
        print(f"{player.name} lance le dé et obtient {roll}")
        player.move(roll, len(self.board))
        current_category = self.board[player.position]

    sum_of_count_by_theme = sum(player.score_by_theme.values())
    

    if player.sum_of_count_by_theme == 6 :
        
        print(f"{player.name} se trouve sur la case {player.position + 1} (Catégorie: {current_category})")

        question_data = self.get_question_by_category(current_category)
        if question_data:
            print(f"Question: {question_data['question']}")
            print("Choix:")
            for i, choix in enumerate(question_data['choix'], 1):
                print(f"{i}. {choix}")
            
            scoreByTheme = player.score_by_theme[current_category] + 1

            if player_answer.strip().lower() == question_data['reponse'].lower():
                print("Bonne réponse !")
                score= player.count_score()
               
                if isinstance(current_category, list) :
                 if player.score_by_theme[current_category] < 1 :
                    scoreByTheme += 1
                print(f"Score = {score}")
                print(f"Score par thème = {scoreByTheme}")
                if player.sum_of_count_by_theme == 6: 
                     print("Do you want to enter the gateway ? (Y/N)")
                else : current_category=current_category[0]

            else:
                print(f"Mauvaise réponse. La bonne réponse était : {question_data['reponse']}")
        else:
            print("Aucune question disponible dans cette catégorie.")
        
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
