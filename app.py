from flask import Flask, render_template, request, jsonify
from game_logic import verifier_victoire, verifier_match_nul
from ai_logic import meilleur_coup

app = Flask(__name__)

# Initialisation du plateau
plateau = [[" " for _ in range(3)] for _ in range(3)]
tour_joueur = True  # True = Joueur (X), False = IA (O)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jouer", methods=["POST"])
def jouer():
    global tour_joueur, plateau

    data = request.json
    ligne = data["ligne"]
    colonne = data["colonne"]

    # Vérifier si la case est vide
    if plateau[ligne][colonne] != " ":
        return jsonify({"erreur": "Case déjà prise"}), 400

    # Jouer le coup du joueur
    plateau[ligne][colonne] = "X"

    # Vérifier si le joueur a gagné ou si c'est un match nul
    if verifier_victoire(plateau, "X"):
        return jsonify({"etat": "victoire", "message": "Le joueur (X) a gagné !"})
    if verifier_match_nul(plateau):
        return jsonify({"etat": "match_nul", "message": "Match nul !"})

    # Tour de l'IA
    tour_joueur = False
    ligne_ia, colonne_ia = meilleur_coup(plateau)
    plateau[ligne_ia][colonne_ia] = "O"

    # Vérifier si l'IA a gagné ou si c'est un match nul
    if verifier_victoire(plateau, "O"):
        return jsonify({"etat": "victoire", "message": "L'IA (O) a gagné !"})
    if verifier_match_nul(plateau):
        return jsonify({"etat": "match_nul", "message": "Match nul !"})

    # Retourner le plateau mis à jour
    return jsonify({"etat": "continuer", "plateau": plateau})

if __name__ == "__main__":
    app.run(debug=True)
