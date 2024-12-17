from src.game import Game
from src.player import Player

def main():
    player1 = Player("A")
    
    game = Game([player1])
    
    num_turns = 10
    
    print("            Le jeu commence !")
    print("-"* 50)
    for turn in range(num_turns):
        print(f"--- Tour {turn + 1} ---")


if __name__ == "__main__":
    main()
