import json
from lanceDe import lancer_de 

class Game:

    def __init__(self, size):
        self.size = size
        self.count_total = 0
        self.create_board
        self.load_Json_questions
        self.get_question_by_category
        self.player_position

    def create_board(self):
        board = [
            "Bases de données",
            "Langages de programmation",
            "Ligne de commandes",
            "Actualités IA",
            "DevOps",
            [
                "AGIL",
                "Actualités IA",
                "DevOps",
                "Ligne de commandes",
                "Bases de données",
                "Langages de programmation",
            ],
            "Ligne de commandes",
            "Actualités IA",
            "DevOps",
            "AGIL",
            "Bases de données",
            [
                "Langages de programmation",
                "Actualités IA",
                "DevOps",
                "Ligne de commandes",
                "Bases de données",
                "AGIL",
            ],
            "Actualités IA",
            "DevOps",
            "AGIL",
            "Bases de données",
            "Langages de programmation",
            [
                "Ligne de commandes",
                "Actualités IA",
                "DevOps",
                "AGIL",
                "Bases de données",
                "Langages de programmation",
            ],
            "DevOps",
            "AGIL",
            "Bases de données",
            "Langages de programmation",
            "Ligne de commandes",
            [
                "Actualités IA",
                "AGIL",
                "DevOps",
                "Ligne de commandes",
                "Bases de données",
                "Langages de programmation",
            ],
            "AGIL",
            "Bases de données",
            "Langages de programmation",
            "Ligne de commandes",
            "Actualités IA",
            [
                "DevOps",
                "Actualités IA",
                "AGIL",
                "Ligne de commandes",
                "Bases de données",
                "Langages de programmation",
            ],
            "Langages de programmation",
            "Ligne de commandes",
            "Actualités IA",
            "DevOps",
            "AGIL",
            [
                "Bases de données",
                "Actualités IA",
                "DevOps",
                "Ligne de commandes",
                "AGIL",
                "Langages de programmation",
            ],
        ]

    def player_position():
        pass

    def load_Json_questions(self):
        chemin_fichier = r"C:\Users\leoga\Downloads\questions.JSON"
        with open(chemin_fichier, "r", encoding="utf-8") as fichier:
            data = json.load
            return data
        
    def ask_question (self, theme ): 
        available_questions = [
            q for q in self.questions_data[theme] if q not in self.used_questions[theme]
        ]
        if not available_questions:
            print("Toutes les questions de ce thème ont été utilisées.")

    def get_question_by_category(self, category):
        questions = self.load_questions()
        if category in questions:
            category_questions = questions[category]
            if category_questions:
                return random.choice(category_questions)
            else:
                None
        return None


    def read_player_answer(self, player_answer, correct_answer):
        """
        Compare la réponse du joueur à la réponse correcte.
        """
        if player_answer.lower() == correct_answer.lower():
            print("Bonne réponse !")
            return True
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {correct_answer}")
            return False


    def lance_de(self):
        return random.randint(1,6)

    def update_player_position(self, steps, direction):
            """
            Met à jour la position du joueur selon le lancer de dé.
            """
            if direction == "front":
                self.player_position = (self.player_position + steps) % len(self.board)
            elif direction == "back":
                self.player_position = (self.player_position - steps) % len(self.board)
            print(f"Position actuelle du joueur : {self.player_position}")


    def start_game(self):
        print("Bienvenue dans le jeu !")
        while True:
                if not self.play_turn():
                    break
        print("Partie terminée !")
        print(f"Score final : {self.count_total} bonne(s) réponse(s).")
        print("Score par thème :")
        for theme, score in self.count_by_theme.items():
                print(f"{theme} : {score}")        