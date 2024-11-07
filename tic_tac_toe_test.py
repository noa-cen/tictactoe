# Introduction to the game and rules:
def intro():
    print("Bienvenue sur le Tic Tac Toe d'Adeline, Maéva et Noa !")
    print("\n")
    print("Règles du jeu: joueur 1 et joueur 2, représentés par X et O, "
          "choisissent une case à tour de rôle. "
          "Le premier qui réussit à aligner trois X ou trois O verticalement, "
          "horizontalement ou en diagonale, gagne la partie."
          "Le choix de la case se fait sous format 'A3', 'B1', 'C2'...")
    print("\n")
    print("Let's play !")
    print("\n")
    input("Touche entrée pour continuer.")


# Ask player to choose their sign. Maeva's function
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
    return sign1, sign2

# Ask a player a box to play and map the index inside coordonate {} . Adeline's Function
def choose_box():
    box = input("choisir la case : ")
    
    coordonate = {
        "row": 0,
        "column":0
        }
    
    match box:
        case "A1" | "1A" | "a1" | "1a":
            box_choice_ok = True
            coordonate["row"] = 1
            coordonate["column"] = 1
        case "A2" | "2A" | "a2" | "2a":
            box_choice_ok = True
            coordonate["row"] = 2
            coordonate["column"] = 1
        case "A3" | "3A" | "a3" | "3a":
            box_choice_ok = True
            coordonate["row"] = 3
            coordonate["column"] = 1
        case "B1" | "1B" | "b1"  | "1b":
            box_choice_ok = True
            coordonate["row"] = 1
            coordonate["column"] = 2
        case "B2" | "2B" | "b2" | "2b":
            box_choice_ok = True
            coordonate["row"] = 2
            coordonate["column"] = 2
        case "B3" | "3B" | "b3" | "3b":
            box_choice_ok = True
            coordonate["row"] = 3
            coordonate["column"] = 2
        case "C1" | "1C" | "c1" | "1c":
            box_choice_ok = True
            coordonate["row"] = 1
            coordonate["column"] = 3
        case "C2" | "2C" | "c2" | "2c":
            box_choice_ok = True
            coordonate["row"] = 2
            coordonate["column"] = 3
        case "C3" | "3C" | "c3" | "3c":
            box_choice_ok = True
            coordonate["row"] = 3
            coordonate["column"] = 3
        case _:
            print("Les coordonnées ne sont pas bonnes, veuillez les entrer à nouveau.")
            box_choice_ok = False
            while box_choice_ok == False:
                return choose_box()
    return coordonate

#Check if the box is empty using the coordonate from choose_box function. Adeline's Function
def is_box_empty(board, coordonate):
    if board[coordonate["row"]][coordonate["column"]] == " ":
        return True
    else:
        return False

''' 
# This function return if the board is full. Noa's Function
def is_board_full():
    count = 1
    while count < 10:
        if count == 9:
            full = True
            print("Match nul !")
        else:
            full = False
        count += 1
    return full
'''  
# Creation of a 'pretty' board game. Noa's Function
def display_board(board):
    rows = len(board)
    for n in range(rows):
        print(board[n][0], "|", board[n][1], "|", board[n][2], "|", board[n][3], "|")
        print("--+---+---+---+")
    return board

# Print the sign of the payer :
def player_turn(board, sign):
    coordonate = choose_box()
    if is_box_empty(board, coordonate) == True:
        board[coordonate["row"]][coordonate["column"]] = sign
    else:
        print("Case déjà occupée, choisis une autre case.")
        return player_turn(board,sign)

# Check 8 possibilities of victory and return true or false. Maeva's Function
def is_victory(sign,board):
    if board[1][1] == sign and board[2][1] == sign and board[3][1] == sign:
        winner = True
    elif board[1][2] == sign and board[2][2] == sign and board[3][2] == sign:
        winner = True
    elif board[1][3] == sign and board[2][3] == sign and board[3][3] == sign:
        winner = True
    elif board[1][1] == sign and board[1][2] == sign and board[1][3] == sign:
        winner = True
    elif board[2][1] == sign and board[2][2] == sign and board[2][3] == sign:
        winner = True
    elif board[3][1] == sign and board[3][2] == sign and board[3][3] == sign:
        winner = True
    elif board[1][1] == sign and board[2][2] == sign and board[3][3] == sign:
        winner = True
    elif board[3][1] == sign and board[2][2] == sign and board[1][3] == sign:
        winner = True
    else:
        winner =  False
    return winner
 
'''def who_won(board,sign):
    winner = is_victory(sign, board)
    if winner == True:
        return f"Le joueur du symbole {sign} a gagné"
'''
def game_on():
    board = [[" ", "A", "B", "C"], 
         ["1", " ", " ", " "], 
         ["2", " ", " ", " "], 
         ["3", " ", " ", " "]]
    
    intro()
    print("Voici le plateau de jeu : ")
    display_board(board)
    sign1,sign2 = choose_sign()
    
    
    winner = False
    count = 0
    while winner == False and count < 9:
        print()
        print("Tour du joueur 1")
        player_turn(board, sign1)
        count += 1
        display_board(board)
        winner = is_victory(sign1, board)
        who_won = f"Le joueur 1 du symbole {sign1} a gagné !"
        # victor = who_won(board,sign1)
        if winner == False and count < 9:
            print()
            print("Tour du joueur 2")
            player_turn(board, sign2)
            count +=1
            display_board(board)
            winner = is_victory(sign2, board)
            who_won = f"Le joueur 2 du symbole {sign2} a gagné !"
            # victor = who_won(board,sign2)
    if winner == True:
        print(who_won)
    elif count == 9:
        print()
        print("Match Nul")

game_on()