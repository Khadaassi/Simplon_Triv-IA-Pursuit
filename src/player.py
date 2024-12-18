class Player():
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.score = 0
        self.count_by_theme = 0
        self.score_by_theme =  {"Bases de données":0,"Langages de programmation":0,"Ligne de commandes":0, "Actualités IA":0,"DevOps":0,"AGIL":0}
        self.sum_of_count_by_theme = sum(self.score_by_theme.values())

    def move(self, steps, board_size):
        self.position = (self.position + steps) % board_size
    
    def count_score(self):
        self.score += 1
        return self.score 
    
    