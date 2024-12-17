class Player():
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.score = 0

    def move(self, steps, board_size):
        self.position = (self.position + steps) % board_size
    
    def count_score(self):
        self.score += 1
        return self.score