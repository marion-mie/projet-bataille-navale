# User story "Plouf dans l'eau"
from grille import Grille

# 1. créer une grille à 5 lignes et 8 colonnes
grille = Grille(5, 8)

while True:
    # 2. afficher la grille à l'écran
    print(grille)

    # 3. demander à l'utilisateur de rentrer deux coordonnées x et y
    x = int(input("Sur quelle ligne ? "))
    y = int(input("Sur quelle colonne ? "))

    # 4. tirer à l'endroit indiqué sur la grille
    grille.tirer(x, y)
    # 5. retour en 2
