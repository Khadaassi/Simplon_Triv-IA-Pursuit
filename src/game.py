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
        self.current_player_idx = 0
        self.categories_per_quarter = [
            ["Bases de données", "Langages de programmation", "Ligne de commandes", "Actualités IA", "DevOps", "Agile"],
            ["DevOps", "Langages de programmation", "Ligne de commandes", "Actualités IA", "Bases de données", "Agile"],
            ["DevOps", "Agile", "Ligne de commandes", "Actualités IA", "Bases de données", "Langages de programmation"],
            ["Bases de données", "Agile", "Ligne de commandes", "Actualités IA", "DevOps", "Langages de programmation"],
            ["Actualités IA", "Langages de programmation", "Bases de données", "DevOps", "Ligne de commandes", "Agile"],
            ["Ligne de commandes", "DevOps", "Bases de données", "Langages de programmation", "Agile", "Actualités IA"] 
            ]
        self.questions = self.load_questions()
        self.board = self.create_board()

    def load_questions(self):
        with open('data/questions.json', 'r') as file:
            return json.load(file)
        
    def create_board(self):
        board = []
        for i in range(6):
            board.extend(self.categories_per_quarter[i])
        return board
    

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
        is_correct = True

        while is_correct == True:
            print(f"{RESET}{player.name} lances le dé et obtiens {roll}")
            while True:
                direction = input(f"{RESET}Vers où souhaitez vous vous déplacer (< ou >)?")
                if direction == ">" or direction == "<":
                    player.move(roll, len(self.board), direction)
                    break
                else:
                    print(f"{RED}Entrée invalide! Choisissez parmi ces deux choix : < ou > ")
            current_category = self.board[player.position]
            print(f"{player.name} se trouve sur la case {player.position + 1} {BOLD}{BLUE}(Catégorie: {current_category})")
            
            question_data = self.get_question_by_category(current_category)
            if question_data:
                print(f"{BOLD}{BLUE}Question: {RESET}{question_data['question']}")
                print(f"{BOLD}{BLUE}Choix:")
                for choix in question_data['choix']:
                    print(f"{RESET} {choix}")
                
                while True:
                    player_answer = input(f"{RESET}Votre réponse (numéro): ")
                    time.sleep(1)
                    score_by_categorie = player.score_by_theme.get(current_category, 0)
                    try:
                        player_answer_index = int(player_answer)
                        if player_answer_index == question_data['reponse'][1]:
                            print(f"{GREEN}Bonne réponse !")
                            score_total = player.count_score()

                            for category_list in enumerate(self.categories_per_quarter):
                                if category_list[0] == current_category:
                                    print(f"\033[4m"+ "CASE SPÉCIALE: Vous avez gagner un Δ!"+"\033[4m")
                                    if player.score_by_theme.get(current_category, 0) < 1:
                                        player.score_by_theme[current_category] = player.score_by_theme.get(current_category, 0) + 1

                            print(f"{RESET}Score pour le thème {current_category} = {score_by_categorie}")
                            print(f"Score = {score_total}")
                            break
            
                        else:
                            print(f"{RED}Mauvaise réponse. La bonne réponse était : {question_data['reponse']}")
                            is_correct = False
                            break
                    except ValueError:
                        print(f"{RED}Entrée invalide. Veuillez entrer un numéro correspondant à l'un des choix.")
                        time.sleep(1)
            # elif:
            #     print(f"{RED}Mauvaise réponse. La bonne réponse était : {question_data['reponse']}")
            #     is_correct = False
            #     break   

            else:
                print("Aucune question disponible dans cette catégorie.")
            
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
