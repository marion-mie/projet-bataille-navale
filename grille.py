class Grille:
    def __init__(self, nb_lignes, nb_colonnes):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.vide = "∿"
        self.matrice = [self.vide] * (nb_lignes * nb_colonnes)

    def tirer(self, ligne, colonne, touche="x"):
        if 0 <= ligne < self.nb_lignes and 0 <= colonne < self.nb_colonnes:
            self.matrice[ligne * self.nb_colonnes + colonne] = touche

    def ajoute(self, bateau):
        for ligne, colonne in bateau.positions():
            if not (0 <= ligne < self.nb_lignes and 0 <= colonne < self.nb_colonnes):
                return False          #vérifie que le bateau rentre en entier dans la grille
        for ligne, colonne in bateau.positions():
            self.matrice[ligne * self.nb_colonnes + colonne] = bateau.marque
        return True

    def __str__(self):
        lignes = []
        for i in range(self.nb_lignes):
            debut = i * self.nb_colonnes
            fin = debut + self.nb_colonnes
            lignes.append("".join(self.matrice[debut:fin]))
        return "\n".join(lignes)
