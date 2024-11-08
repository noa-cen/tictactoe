import random

def bot_turn(board, sign2):
    full_bot = True
    coordonate_bot = []
    coordonate_to_add = {}
    row = 1
    while row < 4 and full_bot == True:
        column = 1
        while column < 4 and full_bot == True:
            if board[row][column] == " ":
                coordonate_to_add = {"Row" : row, "Column" : column}
                coordonate_bot.append(coordonate_to_add)
            column +=1
        row +=1
    
    bot_box = random.choice(coordonate_bot)
    board[bot_box["Row"]][bot_box["Column"]] = sign2