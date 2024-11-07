def choose_sign(): 
    sign1 = input("Choix du signe. ")
    if sign1 == "X" or sign1 == "x":
        sign1 = "X"
        sign2 = "O"
    else: 
        sign1 = "O"
        sign2 = "X"
    print("Joueur 1 est ",sign1)
    print("Joueur 2 est ",sign2)
choose_sign()

def is_victory(sign,board):
    if board[1][1] == sign and board[2][1] == sign and board[3][1] == sign:
        winner = True
    elif board[1][2] == sign and board[2][2] == sign and board[3][2] == sign:
        winner = True
    elif board[1][3] == sign and board[2][3] == sign and board[3][3] == sign:
        winner = True
    elif board[1][1] == sign and board[2][1] == sign and board[3][1] == sign:
        winner = True
    elif board[1][2] == sign and board[2][2] == sign and board[3][2] == sign:
        winner = True
    elif board[1][3] == sign and board[2][3] == sign and board[3][3] == sign:
        winner = True
    elif board[1][1] == sign and board[2][2] == sign and board[3][3] == sign:
        winner = True
    elif board[3][1] == sign and board[2][2] == sign and board[1][3] == sign:
        winner = True
    
    else:
        winner =  False
    return winner

def Match_nul(board):

    for i in range(1,4):
        for j in range(1,4):
            if board[i][j] == " ":
                full = False
            else:
                full = True
        return full