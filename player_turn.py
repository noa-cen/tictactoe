# Print the sign of the payer :
def player_turn(board, coordonate, player):
    if is_box_empty(board, coordonate) == True:
        coordonate = player
        return board
    else:
        print("Case déjà occupée, choisis une autre case.")
        return choose_box()