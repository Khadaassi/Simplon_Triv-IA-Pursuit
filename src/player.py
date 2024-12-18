class Player():
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.score = 0
        self.score_by_theme =  {"Bases de données":0,"Langages de programmation":0,"Ligne de commandes":0, "Actualités IA":0,"DevOps":0,"AGIL":0}

    def move(self, roll, board_length, direction):
        if direction == ">":  # Déplacement vers l'avant
            self.position = (self.position + roll) % board_length
        elif direction == "<":  # Déplacement vers l'arrière
            self.position = (self.position - roll) % board_length
        else:
            print("Direction invalide, pas de déplacement effectué.")
    
    def count_score(self):
        self.score += 1
        return self.score 
    
    @property 
    def sum_of_count_by_theme(self):
        return sum(self.score_by_theme.values())
    
    