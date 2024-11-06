# Decides the player turn:
def player_turn(sign1, sign2, count):
    for n in count:
        if n % 2 == 1:
            player = sign1
        elif n % 2 == 0:
            player = sign2
    print(f"{player} c'est ton tour de jouer.")
    return player