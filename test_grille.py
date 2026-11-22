from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin


#test init
g = Grille(5, 8)
assert g.nb_lignes == 5
assert g.nb_colonnes == 8
assert g.vide == "∿"
assert g.matrice == ["∿"] * 40


#test tirer
g = Grille(5, 8)
g.tirer(2, 3)
assert g.matrice[2 * 8 + 3] == "x"
assert g.matrice.count("x") == 1


#test tirer hors grille
g = Grille(3, 4)
g.tirer(5, 1)
g.tirer(1, 9)
g.tirer(-1, 0)
assert g.matrice == ["∿"] * 12


#test tirer touche
g = Grille(2, 3)
g.tirer(1, 2, "💣")
assert g.matrice[5] == "💣"


#test str
g = Grille(5, 8)
assert str(g) == "\n".join(["∿∿∿∿∿∿∿∿"] * 5)
g.tirer(2, 3)
assert str(g) == ("∿∿∿∿∿∿∿∿\n"
                  "∿∿∿∿∿∿∿∿\n"
                  "∿∿∿x∿∿∿∿\n"
                  "∿∿∿∿∿∿∿∿\n"
                  "∿∿∿∿∿∿∿∿")


#test ajoute
g = Grille(2, 3)
g.ajoute(Bateau(1, 0, longueur=2, vertical=False))
assert g.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]


# test ajoute depasse
g = Grille(2, 3)
g.ajoute(Bateau(1, 0, longueur=2, vertical=True))
g.ajoute(Bateau(1, 0, longueur=4, vertical=True))
assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "∿"]


#test types
g = Grille(4, 4)
g.ajoute(PorteAvion(0, 0))
g.ajoute(Croiseur(1, 0))
g.ajoute(Torpilleur(2, 0))
g.ajoute(SousMarin(3, 0))
assert str(g) == "🚢🚢🚢🚢\n⛴⛴⛴∿\n🚣🚣∿∿\n🐟🐟∿∿"
