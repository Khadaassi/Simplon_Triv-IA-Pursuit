class Player:
    """
    Represents a player in the game.
    """

    def __init__(self, name):
        """
        Initializes a new player with a name, position, and scores.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.position = 0
        self.score = 0
        self.count_by_theme = 0
        self.score_by_theme = {
            "Bases de données": 0,
            "Langages de programmation": 0,
            "Ligne de commandes": 0,
            "Actualités IA": 0,
            "DevOps": 0,
            "Agile": 0
        }

    @property
    def final_score(self):
        """
        Calculates the player's total score by summing scores across all themes.

        Returns:
            int: The total score across all themes.
        """
        return sum(self.score_by_theme.values())
    
    def move(self, steps, board_size, direction):
        """
        Updates the player's position on the board based on the dice roll and direction.

        Args:
            steps (int): Number of steps to move.
            board_size (int): The total size of the game board.
            direction (str): The direction to move ('>' for forward, '<' for backward).
        """
        if direction == ">":
            self.position = (self.position + steps) % board_size
        if direction == "<":
            self.position = (self.position - steps) % board_size

    def count_score(self):
        """
        Increases the player's score by 1 and returns the updated score.

        Returns:
            int: The updated score of the player.
        """
        self.score += 1
        return self.score
