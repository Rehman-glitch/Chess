def move_pawn(list, p1, p2, direction, player, black, white):

    piece = ""

    if player == "white":

        if direction == "double up":
            if p1 == 6 and list[5][p2] == "" and list[4][p2] == "":
                list[p1-2][p2] = list[p1][p2]
                list[p1][p2] = ""
            else:
                return list

        elif direction == "up":    
            if list[p1-1][p2] == "":
                list[p1-1][p2] = list[p1][p2]
                list[p1][p2] = ""
                if p1-1 == 0:
                    piece = input("change ?")
                    list[p1-1][p2] = piece
            else:
                return list

        elif direction == "capture left" and p2 > 0:
            if list[p1-1][p2-1] in black:
                list[p1-1][p2-1] = list[p1][p2]
                list[p1][p2] = ""
                if p1-1 == 0:
                    piece = input("change ?")
                    list[p1-1][p2-1] = piece
            else:
                return list
        
        elif direction == "capture right" and p2 < 7:
            if list[p1-1][p2+1] in black:
                list[p1-1][p2+1] = list[p1][p2]
                list[p1][p2] = ""
                if p1-1 == 0:
                    piece = input("change ?")
                    list[p1-1][p2+1] = piece
            else:
                return list
        else:
            return list
    
    elif player == "black":

        if direction == "double down":
            if p1 == 1 and list[2][p2] == "" and list[3][p2] == "":
                list[p1+2][p2] = list[p1][p2]
                list[p1][p2] = ""
            else:
                return list

        elif direction == "down":
            if list[p1+1][p2] == "":   
                list[p1+1][p2] = list[p1][p2]
                list[p1][p2] = ""
                if p1+1 == 7:
                    piece = input("change ?")
                    list[p1+1][p2] = piece
            else:
                return list

        elif direction == "capture left":
            if list[p1+1][p2-1] in white:
                list[p1+1][p2-1] = list[p1][p2]
                list[p1][p2] = ""
                if p1+1 == 0:
                    piece = input("change ?")
                    list[p1+1][p2-1] = piece
            else:
                return list

        elif direction == "capture right":
            if list[p1+1][p2+1] in white:
                list[p1+1][p2+1] = list[p1][p2]
                list[p1][p2] = ""
                if p1+1 == 0:
                    piece = input("change ?")
                    list[p1+1][p2+1] = piece
            else:
                return list
        else:
            return list

    else:
        return list
    
    return list
