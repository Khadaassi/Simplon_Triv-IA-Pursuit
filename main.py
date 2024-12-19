from src.game import Game
from src.player import Player
import time


YELLOW = "\033[93m"
BLUE = "\033[34m"
GREEN = "\033[92m"

def main():
    player1 = Player("Antoine")
    player2 = Player("Ludivine")
    
    game = Game([player1, player2])
    
    print(f"{YELLOW}            Le jeu commence !")
    print(f"{YELLOW}-"* 50)

    while True:
        print(f"{YELLOW}--- Nouveau tour ---")
        game.play_turn()
        
        winner = game.is_game_over()
        if winner:
            print(f"{GREEN}🎉 Félicitations {winner.name} ! Vous avez gagné le jeu avec {winner.final_score} Δ ! 🎉")
            time.sleep(1)
            break
        
    
    game.display_scores()

    time.sleep(1)
    print(f"{YELLOW}-"* 50)
    print(f"{YELLOW}Le jeu est terminé !\n")

if __name__ == "__main__":
    main()

