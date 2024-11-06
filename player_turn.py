# Print the sign of the payer :
def player_turn(board, coordonate, sign1, sign2):
    if is_box_empty(board, coordonate) == True:
        for n in range(10):
            if n % 2 == 1:
                player = sign1
            elif n % 2 == 0:
                player = sign2
        coordonate = player
    else:
        print("Case déjà occupée, choisis une autre case.")
        return choose_box()