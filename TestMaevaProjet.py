def is_victory(sign,board):
    if board[1][1] == sign and board[2][1] == sign and board[3][1] == sign:
        winner = True
    elif board[1][2] == sign and board[2][2] == sign and board[3][2] == sign:
        winner = True
    elif board[1][3] == sign and board[2][3] == sign and board[3][3] == sign:
        winner = True
    elif board[1][1] == sign and board[2][1] == sign and board[3][1] == sign:
        winner = True
    elif board[1][2] == sign and board[2][2] and board[3][2] == sign:
        winner = True
    elif board[1][3] and board[2][3] and board[3][3] == sign:
        winner = True
    elif board[1][1] and board[2][2] and board[3][3] == sign:
        winner = True
    elif board[3][1] and board[2][2] and board[1][3] == sign:
        winner = True
    
    else:
        winner =  False
    return winner

def Match_nul(board):
    full = True
    for i in range(1, 4):
        for j in range(1, 4):
            if board[i][j] == " ":
                full = False
                break
        if not full:
            break
    return full