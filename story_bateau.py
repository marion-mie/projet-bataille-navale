# User story "chevauchement"
from bateau import Bateau

# Jeu 1 : deux bateaux qui se chevauchent
# 1. créer un bateau b1
b1 = Bateau(2, 3, longueur=3)
# 2. créer un bateau b2
b2 = Bateau(1, 4, longueur=3, vertical=True)
# 3. vérifier si les deux bateaux se chevauchent
print("b1 :", b1.positions())
print("b2 :", b2.positions())
print("Chevauchement :", b1.chevauche(b2))

print()

# Jeu 2 : deux bateaux qui ne se chevauchent pas
b1 = Bateau(2, 3, longueur=3)
b2 = Bateau(0, 0, longueur=2, vertical=True)
print("b1 :", b1.positions())
print("b2 :", b2.positions())
print("Chevauchement :", b1.chevauche(b2))
