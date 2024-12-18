from src.game import Game
from src.player import Player
import time

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BLUE = "\033[34m"

def main():
    player1 = Player("Antoine")
    player2 = Player("Ludivine")
    
    game = Game([player1, player2])
    
    num_turns = 10
    
    print(f"{YELLOW}            Le jeu commence !")
    print(f"{YELLOW}-"* 50)

    for turn in range(num_turns):
        print(f"{BLUE}--- Tour {turn + 1} ---")
        game.play_turn()
        time.sleep(2)
        print(f"{YELLOW}-"* 50)
    
    print(f"{YELLOW}Le jeu est terminé !")

if __name__ == "__main__":
    main()

