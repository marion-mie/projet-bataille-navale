class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = "⛵"
        self.message = "Bateau coulé !"

    def positions(self):
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        return [(self.ligne, self.colonne + i) for i in range(self.longueur)]

    def chevauche(self, autre):   #vérifie si 2 bateaux se chevauchent
        for position in self.positions():
            if position in autre.positions():
                return True
        return False

    def coule(self, grille, touche="x"):
        for ligne, colonne in self.positions():
            if grille.matrice[ligne * grille.nb_colonnes + colonne] != touche:
                return False
        return True


class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 4, vertical)
        self.marque = "🚢"
        self.message = "Le porte-avion est coulé !"


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 3, vertical)
        self.marque = "⛴"
        self.message = "Le croiseur est coulé !"


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
        self.marque = "🚣"
        self.message = "Le torpilleur est coulé !"


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
        self.marque = "🐟"
        self.message = "Le sous-marin est coulé !"
