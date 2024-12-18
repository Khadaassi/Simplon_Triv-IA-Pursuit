def play_turn(self):
    player = self.players[self.current_player_idx]
    roll = rolling_dice()
    print(f"{player.name} lance le dé et obtient {roll}")
    
    direction = input("Vers où souhaitez-vous vous déplacer ( < ou >) ? ").strip()
    player.move(roll, len(self.board), direction)
    
    current_category = self.board[player.position]
    print(f"{player.name} se trouve sur la case {player.position + 1} (Catégorie: {current_category})")
    
    if current_category == "Dice":
        print(f"Case spéciale: {current_category}. Vous relancez le dé.")
        self.play_turn()  
        return

    # Récupération de la question
    question_data = self.get_question_by_category(current_category)
    if question_data:
        print(f"Question: {question_data['question']}")
        print("Choix:")
        for i, choix in enumerate(question_data['choix'], 1):
            print(f"{i}. {choix}")

        player_answer = input("Votre réponse : ")

        if player_answer.strip().lower() == question_data['reponse'].lower():
            print("Bonne réponse !")
            player.count_score()
            player.score_by_theme[current_category] += 1
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {question_data['reponse']}")
    else:
        print("Aucune question disponible dans cette catégorie.")
