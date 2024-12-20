import json, random, time
from src.player import Player
from src.dice import rolling_dice


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[34m"
RESET = "\033[0m"
BOLD = "\033[1m"
class Game():

    def __init__(self, players):
        self.players = players
        self.board = self.create_board()
        self.current_player_idx = 0
        self.questions = self.load_questions()

    def load_questions(self):
        with open('media/questions.JSON', 'r') as file:
            return json.load(file)
        
    def create_board(self):
        categories_per_quarter = [
    ["Bases de données", "Langages de programmation", "Ligne de commandes", "Actualités IA", "DevOps", "Agile"],
    ["DevOps", "Langages de programmation",  "Actualités IA", "Ligne de commandes","Bases de données", "Agile"],
    ["Agile", "DevOps", "Ligne de commandes", "Actualités IA", "Bases de données", "Langages de programmation"],
    ["Langages de programmation","Bases de données", "Agile", "Ligne de commandes", "Actualités IA", "DevOps"],
    ["Actualités IA", "Langages de programmation", "Bases de données", "DevOps", "Ligne de commandes", "Agile"],
    ["Ligne de commandes", "DevOps", "Bases de données", "Langages de programmation", "Agile", "Actualités IA"] 
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
        print(f"{RESET}{player.name} lances le dé et obtiens {roll}")
        direction = input("Vers où souhaitez vous vous déplacer ( < ou >)?")
        player.move(roll, len(self.board), direction)
        current_category = self.board[player.position]
        print(f"{player.name} te trouve sur la case {player.position + 1} {BOLD}{BLUE}(Catégorie: {current_category})")
        
        question_data = self.get_question_by_category(current_category)
        if question_data:
            print(f"{BOLD}{BLUE}Question: {RESET}{question_data['question']}")
            print(f"{BOLD}{BLUE}Choix:")
            for i, choix in enumerate(question_data['choix'], 1):
                print(f"{RESET}{i}. {choix}")
            
            player_answer = input(f"Votre réponse : ")
            time.sleep(1)
            scoreByTheme = player.score_by_theme.get(current_category, 0)
            if player_answer.strip().lower() == question_data['reponse'].lower():
                print(f"{GREEN}Bonne réponse !")
                score= player.count_score()

                if player.score_by_theme[current_category] < 1 :
                    scoreByTheme  += 1
                print(f"Score pour le thème {current_category} = {scoreByTheme}")
                
                print(f"Score = {score}")
            else:
                print(f"{RED}Mauvaise réponse. La bonne réponse était : {question_data['reponse']}")
                print(f"{GREEN}Score pour le thème {current_category} = {scoreByTheme}")
                
        else:
            print("Aucune question disponible dans cette catégorie.")
        
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
