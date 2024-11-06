# Ask a player a box to play and map the index inside coordonate {}
def choose_box():
    box = input("choisir la case : ")
    
    coordonate = {
        "row": 0,
        "column":0
        }
    
    match box:
        case "A1" | "1A" | "a1" | "1a":
            coordonate["row"] = 1
            coordonate["column"] = 1
        case "A2" | "2A" | "a2" | "2a":
            coordonate["row"] = 2
            coordonate["column"] = 1
        case "A3" | "3A" | "a3" | "3a":
            coordonate["row"] = 3
            coordonate["column"] = 1
        case "B1" | "1B" | "b1"  | "1b":
            coordonate["row"] = 1
            coordonate["column"] = 2
        case "B2" | "2B" | "b2" | "2b":
            coordonate["row"] = 2
            coordonate["column"] = 2
        case "B3" | "3B" | "b3" | "3b":
            coordonate["row"] = 3
            coordonate["column"] = 2
        case "C1" | "1C" | "c1" | "1c":
            coordonate["row"] = 1
            coordonate["column"] = 3
        case "C2" | "2C" | "c2" | "2c":
            coordonate["row"] = 2
            coordonate["column"] = 3
        case "C3" | "3C" | "c3" | "3c":
            coordonate["row"] = 3
            coordonate["column"] = 3
        case _:
            print("Les coordonnées ne sont pas bonne, veuillez les entrer à nouveau.")
            return choose_box()
    return coordonate