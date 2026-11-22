from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin


# test init
b = Bateau(2, 3)
assert b.ligne == 2
assert b.colonne == 3
assert b.longueur == 1
assert b.vertical is False


#test positions
assert Bateau(2, 3, longueur=3).positions() == [(2, 3), (2, 4), (2, 5)]
assert Bateau(2, 3, longueur=3, vertical=True).positions() == [(2, 3), (3, 3), (4, 3)]


#test chevauche
b1 = Bateau(2, 3, longueur=3)
assert b1.chevauche(Bateau(1, 4, longueur=3, vertical=True))
assert not b1.chevauche(Bateau(0, 0, longueur=2, vertical=True))


#test coule
g = Grille(3, 4)
b = Bateau(1, 1, longueur=2)
assert not b.coule(g)
g.tirer(1, 1)
assert not b.coule(g)
g.tirer(1, 2)
assert b.coule(g)


#test types
assert (PorteAvion(0, 0).longueur, PorteAvion(0, 0).marque) == (4, "🚢")
assert (Croiseur(0, 0).longueur, Croiseur(0, 0).marque) == (3, "⛴")
assert (Torpilleur(0, 0).longueur, Torpilleur(0, 0).marque) == (2, "🚣")
assert (SousMarin(0, 0).longueur, SousMarin(0, 0).marque) == (2, "🐟")
assert Croiseur(1, 2, vertical=True).positions() == [(1, 2), (2, 2), (3, 2)]
