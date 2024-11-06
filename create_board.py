# Creation of a plank board game:
def create_board():
    print("Voici le plateau de jeu : ")
    board = [[" ", "A", "B", "C"], 
         ["1", " ", " ", " "], 
         ["2", " ", " ", " "], 
         ["3", " ", " ", " "]]
    return board

# Creation of a 'pretty' board game:
def display_board(board):
    rows = len(board)
    columns = len(board)
    for n in range(rows):
        print(board[n][0], "|", board[n][1], "|", board[n][2], "|", board[n][3], "|")
        print("--+---+---+---+")
    return board