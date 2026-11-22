import random

from termcolor import colored
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

grille = Grille(8, 10)



def afficher(grille):
    for i in range(grille.nb_lignes):
        ligne = ""
        for j in range(grille.nb_colonnes):
            case = grille.matrice[i * grille.nb_colonnes + j]
            if case == grille.vide:
                ligne += colored(case, "blue", attrs=["bold"])
            elif case == "x":
                ligne += colored(case, "yellow")
            elif case == "💣":
                ligne += colored(case, on_color="on_red")
            else:
                ligne += case
        print(ligne)   #Affiche la grille en couleur : l'eau en bleu, les tirs ratés en jaune, les touchés sur fond rouge.



# placement aléatoire des bateaux
bateaux = []
for type_bateau in [PorteAvion, Croiseur, Torpilleur, SousMarin]:
    possibles = []
    for ligne in range(grille.nb_lignes):
        for colonne in range(grille.nb_colonnes):
            for vertical in [False, True]:
                bateau = type_bateau(ligne, colonne, vertical)
                dedans = True
                for l, c in bateau.positions():
                    if l >= grille.nb_lignes or c >= grille.nb_colonnes:
                        dedans = False
                libre = True
                for autre in bateaux:
                    if bateau.chevauche(autre):
                        libre = False
                if dedans and libre:
                    possibles.append(bateau)
    bateaux.append(random.choice(possibles))

# boucle de jeu
restants = list(bateaux)
nb_coups = 0
while len(restants) > 0:
    afficher(grille)
    ligne = int(input("Quelle ligne (entre 0 et 7) ? "))
    colonne = int(input("Quelle colonne (entre 0 et 9) ? "))
    nb_coups += 1

    bateau_touche = None
    for bateau in restants:
        if (ligne, colonne) in bateau.positions():
            bateau_touche = bateau

    if bateau_touche is None:
        grille.tirer(ligne, colonne)
        print("À l'eau.")
    else:
        grille.tirer(ligne, colonne, "💣")
        if bateau_touche.coule(grille, "💣"):
            grille.ajoute(bateau_touche)
            restants.remove(bateau_touche)
            print(bateau_touche.message)
        else:
            print("Touché !")

afficher(grille)
print("Tous les bateaux sont coulés en", nb_coups, "coups !")
