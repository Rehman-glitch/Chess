def move_king(list, p1, p2, direction, player, black, white):

    if player == "white":
        if direction == "left":
            if p2 == 0 or list[p1][p2-1] in white:
                return list
            else:
                list[p1][p2-1] = list[p1][p2]
                list[p1][p2] = ""

        elif direction == "right":
            if p2 == 7 or list[p1][p2+1] in white:
                return list
            else:
                list[p1][p2+1] = list[p1][p2]
                list[p1][p2] = ""
        
        elif direction == "up":
            if p1 == 0 or list[p1-1][p2] in white:
                return list
            else:
                list[p1-1][p2] = list[p1][p2]
                list[p1][p2] = ""

        elif direction == "down":
            if p1 == 7 or list[p1+1][p2] in white :
                return list
            else:
                list[p1+1][p2] = list[p1][p2]
                list[p1][p2] = ""
        else:
            return list
    
    elif player == "black":
        if direction == "left":
            if p2 == 0 or list[p1][p2-1] in black:
                return list
            else:
                list[p1][p2-1] = list[p1][p2]
                list[p1][p2] = ""

        elif direction == "right":
            if p2 == 7 or list[p1][p2+1] in black:
                return list
            else:
                list[p1][p2+1] = list[p1][p2]
                list[p1][p2] = ""
        
        elif direction == "up":
            if p1 == 0 or list[p1-1][p2] in black:
                return list
            else:
                list[p1-1][p2] = list[p1][p2]
                list[p1][p2] = ""

        elif direction == "down":
            if p1 == 7 or list[p1+1][p2] in black:
                return list
            else:
                list[p1+1][p2] = list[p1][p2]
                list[p1][p2] = ""
        else:
            return list
    
    else:
        return list

    return list