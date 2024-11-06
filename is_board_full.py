# This function return if the board is full:
def is_board_full():
    count = 1
    while count < 10:
        if count == 9:
            full = True
            print("Match nul !")
        else:
            full = False
        count += 1
    return full, count