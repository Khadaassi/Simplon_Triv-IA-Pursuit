import json, random, time
from src.player import Player
from src.dice import rolling_dice



RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[34m"
RESET = "\033[0m"
BOLD = "\033[1m"
class Game:
    """
    Represents the interactive trivia game.
    """

class Game:
    def __init__(self, players):
        """
        Initializes the game with the given players and board setup.

        Args:
            players (list): List of Player objects participating in the game.
        """
        self.players = players
        self.current_player_idx = 0
        self.current_question = 0
        self.categories_per_quarter = [
            ["Bases de données", "🎲", "Langages de programmation", "Ligne de commandes", "Actualités IA", "Agile", "DevOps"],
            ["Agile", "🎲", "DevOps", "Ligne de commandes", "Actualités IA", "Bases de données", "Langages de programmation"],
            ["DevOps", "🎲", "Langages de programmation", "Ligne de commandes", "Actualités IA", "Bases de données", "Agile"],
            ["Langages de programmation", "🎲", "Agile", "Bases de données", "Actualités IA", "DevOps", "Ligne de commandes"],
            ["Actualités IA", "🎲", "Langages de programmation", "Agile", "DevOps", "Ligne de commandes", "Bases de données"],
            ["Ligne de commandes", "🎲", "DevOps", "Bases de données", "Langages de programmation", "Agile", "Actualités IA"],
        ]
        self.board = self.create_board()
        self.special_case_indices = [0, 7, 14, 21, 28, 35, 42]
        self.questions = self.load_questions()

    def load_questions(self):
        """
        Loads the questions from a JSON file.

        Returns:
            dict: Dictionary containing questions categorized by themes.
        """
        with open("data/questions.json", "r") as file:
            return json.load(file)


    def load_question_finale():
        
        with open('date/questions.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        question_data = data['question_finale']
        
        print(f"\n{question_data['question']}")
        
        for choix in question_data['choix']:
            print(choix)
        return question_data


    def get_question_win():
        question_data = load_question_finale()
        
        player_answer = int(input(f"\nVotre réponse (numéro) : "))
        
        if player_answer == question_data['reponse'][1]:
            print("Bonne réponse !")
        else:
            print("Mauvaise réponse. La bonne réponse est :")
            print(f"{question_data['reponse'][1]}")
        return None


    def create_board(self):
        """
        Creates the game board with a predefined sequence of categories.

        Returns:
            list: The complete game board as a list of categories.
        """
        board = []
        for i in range(6):
            board.extend(self.categories_per_quarter[i])
        return board

    def get_question_by_category(self, category):
        """
        Retrieves a random question from a given category.

        Args:
            category (str): The category to fetch the question from.

        Returns:
            dict or None: A question dictionary or None if no question is available.
        """
        if category in self.questions:
            category_questions = self.questions[category]
            remaining_questions = [q for q in category_questions if q not in self.question_already_posed]
        else:
            remaining_questions = []

        if remaining_questions:
            
            question = random.choice(remaining_questions)
            self.question_already_posed.append(question)

            return question
        else:
            print(f"Toutes les questions de la catégorie '{category}' ont déjà été posées.")
        return None

    def is_special_case(self, position):
        """
        Checks if the current board position is a special case.

        Args:
            position (int): The position on the board.

        Returns:
            bool: True if the position is special, False otherwise.
        """
        return position in self.special_case_indices

    def get_possible_categories(self, current_position, steps, board_size):
        """
        Calculates possible forward and backward categories from a position.

        Args:
            current_position (int): The current position of the player.
            steps (int): Number of steps the player rolls.
            board_size (int): Total size of the board.

        Returns:
            tuple: Forward and backward positions with their corresponding categories.
        """
        forward_position = (current_position + steps) % board_size
        backward_position = (current_position - steps) % board_size
        forward_category = self.board[forward_position]
        backward_category = self.board[backward_position]
        return forward_position, forward_category, backward_position, backward_category

    def is_game_over(self):
        """
        Checks if the game is over by verifying if any player has won.

        Returns:
            Player or None: The winning player or None if no one has won yet.
        """
        for player in self.players:
            if player.final_score == 6:
                return player
        return None

    def display_scores(self):
        """
        Displays the scores of all players.
        """
        print(f"\n{BOLD}{YELLOW}Récapitulatif des scores :{RESET}")
        for player in self.players:
            print(f"\n{BOLD}{BLUE}{player.name}{RESET} :")
            for category, score in player.score_by_theme.items():
                print(f"  {category}: {score} Δ")
            print(f"{BOLD}Score total : {player.final_score} Δ{RESET}")

    def play_turn(self):
        """
        Manages the logic for a single player's turn.
        """
        player = self.players[self.current_player_idx]

        while player.final_score < 6:
            roll = rolling_dice()
            print(f"{RESET}{player.name} lances le dé et obtiens {roll}\n")

            forward_pos, forward_cat, backward_pos, backward_cat = self.get_possible_categories(
                player.position, roll, len(self.board)
            )
            print(f"Options possibles :")
            print(f"{BOLD}{BLUE}> (Avancer) : Case {forward_pos + 1} - {forward_cat}{RESET}")
            print(f"{BOLD}{BLUE}< (Reculer) : Case {backward_pos + 1} - {backward_cat}{RESET}\n")

            while True:
                direction = input(f"{RESET}Vers où souhaitez-vous vous déplacer (< ou >)? ")
                if direction in (">", "<"):
                    player.move(roll, len(self.board), direction)
                    break
                else:
                    print(f"{RED}Entrée invalide! Choisissez parmi ces deux choix : < ou >")

            current_category = self.board[player.position]
            print(f"{player.name} se trouve sur la case {player.position + 1} {BOLD}{BLUE}(Catégorie: {current_category})\n")

            question_data = self.get_question_by_category(current_category)
            if question_data:
                print(f"{BOLD}{BLUE}Question: {RESET}{question_data['question']}\n")
                print(f"{BOLD}{BLUE}Choix:")
                for choix in question_data["choix"]:
                    print(f"{RESET} {choix}")

                while True:
                    try:
                        player_answer = int(input(f"\n{RESET}Votre réponse (numéro): "))
                        time.sleep(1)
                        if 1 <= player_answer <= len(question_data["choix"]):
                            break
                        else:
                            print(f"{RED}Veuillez entrer un numéro valide.")
                    except ValueError:
                        print(f"{RED}Entrée invalide. Veuillez entrer un numéro.")

                if player_answer == question_data["reponse"][1]:
                    print(f"\n{GREEN}Bonne réponse !\n")
                    if self.is_special_case(player.position):
                        print(f"\033[4mCASE SPÉCIALE: Vous avez gagné un Δ!\033[0m\n")
                        if player.score_by_theme.get(current_category, 0) < 1:
                            player.score_by_theme[current_category] = 1

                    score_total = player.count_score()
                    score_by_categorie = player.score_by_theme.get(current_category, 0)
                    print(f"{RESET}Score pour le thème {current_category} = {score_by_categorie}")
                    print(f"Score total = {score_total}")
                    print(f"Nombre de {GREEN}Δ {RESET}gagné = {player.final_score}\n\n")
                else:
                    print(f"{RED}Mauvaise réponse. La bonne réponse était : {question_data['reponse'][1]}.")
                    time.sleep(1)
                    break
            else:
                print(f"{YELLOW}Relancez le dé!")
                time.sleep(1)

        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
