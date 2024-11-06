# Créer une grid pour pouvoir jouer
# Faire choisir par l'IA en fonction du symbole choisi par l'utilisateur 
# Surement avec un boolean ?
# Verifier si les symboles sont alignés
# Empêcher l'alignement

'''
On va devoir créer une grille qui sera en 4 x 4 (et un jeu qui se fait 3 x 3 )

__| A | B | C
1 | __| __| __
2 | __| __| __
3 | __| __| __

De cette façon on peut déterminer où se trouve les éléments

Les possibilités de victoires sont au nombre de 8 : 
les lignes
A1, B1, C1
A2, B2, C2
A3, B3, C3

les colonnes :
A1, A2, A3
B1, B2, B3
C1, C2, C3

les diagonales :
A1, B2, C3
A3, B2, C1
'''