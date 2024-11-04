Développez une version en ligne du fameux Tic Tac Toe.
Dans ce jeu, deux joueurs s'affrontent. À tour de rôle, ils désignent une case et
y insèrent alternativement un signe (‘X’ et ‘O’). Le premier joueur qui arrive à
faire un alignement vertical, horizontal ou diagonal de trois signes gagne la
partie. Si le plateau de jeu est rempli de signes et qu’il n’y a pas d'alignement 
de trois, alors c’est un match nul.

Il est préférable d’être deux pour jouer à ce jeu, mais comme vos visiteurs
sont parfois seuls, vous devez également créer une Intelligence Artificielle.
Votre algorithme de décision doit être codé dans une fonction prototypée de 
la façon suivante :

def ia(board, signe).

Cette fonction prend en paramètre un tableau nommé “board” et un
caractère nommé “signe”. 
Elle retourne l’emplacement où l’IA souhaite jouer (0-8). 
“signe” contient le signe qui est joué par l’IA à savoir “X” ou “O”.

En cas d’erreur, la fonction retourne false.

Voici les différentes informations que peut contenir ce tableau :
➔ Personne n’a joué à cet emplacement
➔ Il y a une croix à cet emplacement
➔ Il y a un rond à cet emplacement