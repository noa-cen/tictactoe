#Check if the box is empty using the coordonate from choose_box function.
def is_box_empty(board, coordonate):
    if board[coordonate["row"]][coordonate["column"]] == " ":
        return True
    else:
        return False