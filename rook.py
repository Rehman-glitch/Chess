def move_rook(list, p1, p2, direction, player, black, white, n):
    
    P1 = p1
    P2 = p2
    
    if player == "white" and n != 0:
        if direction == "up" and p1 > 0:
            if p1 == 1 or n == 1:
                if list[p1-1][p2] in white:
                    return list
                else:
                    list[p1-1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1-1][p2] == "":
                    p1 -= 1
                    if p1-1 == 0 or p1-1 == P1-n:
                        if list[p1-1][p2] not in white:
                            list[p1-1][p2] = "x"
                
                if list[p1-1][p2] in white:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1-1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            
        elif direction == "down" and p1 < 7:
            if p1 == 6 or n == 1:
                if list[p1+1][p2] in white:
                    return list
                else:
                    list[p1+1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1+1][p2] == "":
                    p1 += 1
                    if p1+1 == 7 or p1+1 == P1+n:
                        if list[p1+1][p2] not in white:
                            list[p1+1][p2] = "x"
                
                if list[p1+1][p2] in white:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1+1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list

        elif direction == "left" and p2 > 0:
            if p2 == 1 or n == 1:
                if list[p1][p2-1] in white:
                    return list
                else:
                    list[p1][p2-1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1][p2-1] == "":
                    p2 -= 1
                    if p2-1 == 0 or p2-1 == P2-n:
                        if list[p1][p2-1] not in white:
                            list[p1][p2-1] = "x"
                
                if list[p1][p2-1] in white:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1][p2-1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                
        elif direction == "right" and p2 < 7:
            if p2 == 6 or n == 1:
                if list[p1][p2+1] in white:
                    return list
                else:
                    list[p1][p2+1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1][p2+1] == "":
                    p2 += 1
                    if p2+1 == 7 or p2+1 == P2+n:
                        if list[p1][p2+1] not in white:
                            list[p1][p2+1] = "x"
                
                if list[p1][p2+1] in white:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1][p2+1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
        else:
            return list

    elif player == "black" and n != 0:

        if direction == "up" and p1 > 0:
            if p1 == 1 or n == 1:
                if list[p1-1][p2] in black:
                    return list
                else:
                    list[p1-1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1-1][p2] == "":
                    p1 -= 1
                    if p1-1 == 0 or p1-1 == P1-n:
                        if list[p1-1][p2] not in black:
                            list[p1-1][p2] = "y"
                
                if list[p1-1][p2] in black:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1-1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list

        elif direction == "down" and p1 < 7:
            if p1 == 6 or n == 1:
                if list[p1+1][p2] in black:
                    return list
                else:
                    list[p1+1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1+1][p2] == "":
                    p1 += 1
                    if p1+1 == 7 or p1+1 == P1+n:
                        if list[p1+1][p2] not in black:
                            list[p1+1][p2] = "y"
                
                if list[p1+1][p2] in black:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1+1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list

        elif direction == "left" and p2 > 0:
            if p2 == 1 or n == 1:
                if list[p1][p2-1] in black:
                    return list
                else:
                    list[p1][p2-1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1][p2-1] == "":
                    p2 -= 1
                    if p2-1 == 0 or p2-1 == P2-n:
                        if list[p1][p2-1] not in black:
                            list[p1][p2-1] = "y"
                
                if list[p1][p2-1] in black:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1][p2-1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                
        elif direction == "right" and p2 < 7:
            if p2 == 6 or n == 1:
                if list[p1][p2+1] in black:
                    return list
                else:
                    list[p1][p2+1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1][p2+1] == "":
                    p2 += 1
                    if p2+1 == 7 or p2+1 == P2+n:
                        if list[p1][p2+1] not in black:
                            list[p1][p2+1] = "y"
                
                if list[p1][p2+1] in black:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1][p2+1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                
        else:
            return list
    
    else:
        return list