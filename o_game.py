import json
import random

def lancer_de():
    return random.randint(1, 6)

chemin_fichier = r"C:\Users\leoga\Downloads\data_test.JSON"
with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
    donnees = json.load(fichier)

questions_data = {
    'Bases de données': donnees['Bases de données'],
    'Langages de programmation': donnees['Langages de programmation'],
    'Ligne de commandes': donnees['Ligne de commandes'],
    'Actualités IA': donnees['Actualités IA'],
    'DevOps': donnees['DevOps'],
    'AGIL': donnees['AGIL']
}


player_position = 0
count_total = 0
count_by_theme = {theme: 0 for theme in questions_data.keys()}
used_questions = {theme: [] for theme in questions_data.keys()}


board = [
    "Bases de données", "Langages de programmation", "Ligne de commandes", "Actualités IA", "DevOps", ['AGIL', 'Actualités IA', 'DevOps', 'Ligne de commandes', 'Bases de données', 'Langages de programmation'],
    "Ligne de commandes", "Actualités IA", "DevOps", "AGIL", "Bases de données", ['Langages de programmation', 'Actualités IA', 'DevOps', 'Ligne de commandes', 'Bases de données', 'AGIL'],
    "Actualités IA", "DevOps", "AGIL", "Bases de données", "Langages de programmation", ['Ligne de commandes', 'Actualités IA', 'DevOps', 'AGIL', 'Bases de données', 'Langages de programmation'],
    "DevOps", "AGIL", "Bases de données", "Langages de programmation", "Ligne de commandes", ['Actualités IA', 'AGIL', 'DevOps', 'Ligne de commandes', 'Bases de données', 'Langages de programmation'],
    "AGIL", "Bases de données", "Langages de programmation", "Ligne de commandes", "Actualités IA", ['DevOps', 'Actualités IA', 'AGIL', 'Ligne de commandes', 'Bases de données', 'Langages de programmation'],
    "Langages de programmation", "Ligne de commandes", "Actualités IA", "DevOps", "AGIL", ['Bases de données', 'Actualités IA', 'DevOps', 'Ligne de commandes', 'AGIL', 'Langages de programmation']
]



print("Pour lancer le dé, tapez 'go'")
go = input("go ? ").lower()

if go == "go":
    dice_result = lancer_de()
    print(f"Le dé a donné : {dice_result}")
else:
    print("Ok, on ne joue pas.")
    exit()


print(f"Voulez-vous avancer de {dice_result} (tapez 'front') ou reculer de {dice_result} (tapez 'back') ?")
choix = ""

while choix not in ["back", "front"]:
    choix = input("Votre choix est 'back' ou 'front' ? ").lower()

if choix == "back":
    player_position = (player_position - dice_result) % len(board)
elif choix == "front":
    player_position = (player_position + dice_result) % len(board)


current_theme = board[player_position]

if isinstance(current_theme, list):  # Case avec plusieurs thèmes
    # Vérifier si toutes les questions des thèmes sont répondues
    if all(count_by_theme[theme.lower()] > 0 for theme in current_theme):
        print("Vous êtes tombé sur une case avec plusieurs thèmes :")
        for i, theme in enumerate(current_theme):
            print(f"{i}. {theme}")
        choix_theme = int(input("Choisissez un thème (numéro) : "))
        current_theme = current_theme[choix_theme]
    else:
        # Par défaut, prendre le premier thème si toutes les conditions ne sont pas remplies
        current_theme = current_theme[0]

print(f"Vous êtes tombé sur le thème : {current_theme}")


if current_theme.lower() in questions_data:  
    theme_questions = questions_data[current_theme.lower()]  
    
    available_questions = [q for q in theme_questions if q not in used_questions[current_theme.lower()]]
    if available_questions: 
        question = available_questions[0]  
        used_questions[current_theme.lower()].append(question)  
        
        # Affiche la question et les choix
        print(f"Question : {question['question']}")
        for i, choix in enumerate(question['choix'], 1):
            print(f"{i}. {choix}")
        
        # Récupère la réponse de l'utilisateur
        try:
            user_answer_index = int(input("Votre réponse (numéro) : ")) - 1
            user_answer = question['choix'][user_answer_index]
        except (ValueError, IndexError):
            print("Réponse invalide !")
            exit()
        
        # Vérifie la réponse
        if user_answer == question['reponse']:
            print("Bonne réponse !")
            count_total += 1
            if count_by_theme[current_theme.lower()] == 0:  
                count_by_theme[current_theme.lower()] += 1
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {question['reponse']}")
    else:
        print(f"Aucune question disponible pour le thème {current_theme}.")
else:
    print(f"Thème {current_theme} introuvable dans les données JSON.")
