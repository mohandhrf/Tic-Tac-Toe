from game_logic import verifier_victoire, verifier_match_nul

def minimax(plateau, profondeur, maximisant):
    if verifier_victoire(plateau, "O"):
        return 1
    if verifier_victoire(plateau, "X"):
        return -1
    if verifier_match_nul(plateau):
        return 0

    if maximisant:
        meilleur_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if plateau[i][j] == " ":
                    plateau[i][j] = "O"
                    score = minimax(plateau, profondeur + 1, False)
                    plateau[i][j] = " "
                    meilleur_score = max(meilleur_score, score)
        return meilleur_score
    else:
        meilleur_score = float("inf")
        for i in range(3):
            for j in range(3):
                if plateau[i][j] == " ":
                    plateau[i][j] = "X"
                    score = minimax(plateau, profondeur + 1, True)
                    plateau[i][j] = " "
                    meilleur_score = min(meilleur_score, score)
        return meilleur_score

def meilleur_coup(plateau):
    meilleur_score = -float("inf")
    meilleur_mouvement = None
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == " ":
                plateau[i][j] = "O"
                score = minimax(plateau, 0, False)
                plateau[i][j] = " "
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_mouvement = (i, j)
    return meilleur_mouvement
