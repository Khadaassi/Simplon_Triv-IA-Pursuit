import json
import random
class Game():

    def __init__(self, size):
        self.size = size

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

