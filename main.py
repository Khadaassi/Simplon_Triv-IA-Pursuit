from src.game import Game
from src.player import Player

def main():
    print("Bienvenue au Trivial Pursuit !")
    print("Entrez les noms des joueurs séparés par '-'")
    player_names = input().strip().split("-")
    
    players = [Player(name.strip()) for name in player_names if name.strip()]
    
    game = Game(players)
    
    print("Le jeu commence !")
    print("-" * 50)

    while True:
        print(f"Tour du joueur {game.players[game.current_player_idx].name}  ")
        game.play_turn()
        print("-" * 50)  

if __name__ == "__main__":
    main()
