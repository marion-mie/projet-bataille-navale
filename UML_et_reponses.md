# Projet bataille navale : UML et réponses aux questions

## 1. UML de la grille

```
+--------------------------------------+
|               Grille                 |
+--------------------------------------+
| nb_lignes : int                      |
| nb_colonnes : int                    |
| vide : str = "∿"                     |
| matrice : list[str]                  |
+--------------------------------------+
| Grille(nb_lignes, nb_colonnes)       |
| tirer(ligne, colonne, touche="x")    |
| __str__() : str                      |
+--------------------------------------+  (mise en forme du diagramme UML fait par IA)
```

## 2. Simuler une matrice de L lignes et C colonnes avec une liste

On crée une liste à L * C cases. L'élément placé à la ligne l et colonne c sera à la position l * C +c


## 3. Attributs nécessaires

Il faut stocker, en plus de la grille, le nombre de colonnes de la grille.

