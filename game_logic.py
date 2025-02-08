def verifier_victoire(plateau, symbole):
    # Vérifie les lignes, colonnes et diagonales
    for i in range(3):
        if all([case == symbole for case in plateau[i]]):  # Lignes
            return True
        if all([plateau[j][i] == symbole for j in range(3)]):  # Colonnes
            return True
    if all([plateau[i][i] == symbole for i in range(3)]) or all([plateau[i][2 - i] == symbole for i in range(3)]):  # Diagonales
        return True
    return False

def verifier_match_nul(plateau):
    return all([case != " " for ligne in plateau for case in ligne])
