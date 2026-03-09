board = [["BRo", "BKn", "BBi", "BQu", "BKi", "BBi", "BKn", "BRo"],
          ["BPn", "BPn", "BPn", "BPn", "BPn", "BPn", "BPn", "BPn"],
          ["", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", ""],
          ["WPn", "WPn", "WPn", "WPn", "WPn", "WPn", "WPn", "WPn"],
          ["WRo", "WKn", "WBi", "WQu", "WKi", "WBi", "WKn", "WRo"]]

black = ["BRo", "BKn", "BBi", "BQu", "BKi", "BPn", "x"]
white = ["WRo", "WKn", "WBi", "WQu", "WKi", "WPn", "y"]
RnB = ["WRo", "BRo", "WBi", "BBi", "WQu", "BQu"]
d_rook = ["up", "down", "left", "right"]
d_bishop = ["up left", "up right", "down left", "down right"]

def create_board(l):
    table = "+-----------------------------------------------+\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 0\n" \
            .format(l[0][0], l[0][1], l[0][2], l[0][3],
                    l[0][4], l[0][5], l[0][6], l[0][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 1\n" \
            .format(l[1][0], l[1][1], l[1][2], l[1][3],
                    l[1][4], l[1][5], l[1][6], l[1][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 2\n" \
            .format(l[2][0], l[2][1], l[2][2], l[2][3],
                    l[2][4], l[2][5], l[2][6], l[2][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 3\n" \
            .format(l[3][0], l[3][1], l[3][2], l[3][3],
                    l[3][4], l[3][5], l[3][6], l[3][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 4\n" \
            .format(l[4][0], l[4][1], l[4][2], l[4][3],
                    l[4][4], l[4][5], l[4][6], l[4][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 5\n" \
            .format(l[5][0], l[5][1], l[5][2], l[5][3],
                    l[5][4], l[5][5], l[5][6], l[5][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 6\n" \
            .format(l[6][0], l[6][1], l[6][2], l[6][3],
                    l[6][4], l[6][5], l[6][6], l[6][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 7\n" \
            .format(l[7][0], l[7][1], l[7][2], l[7][3],
                    l[7][4], l[7][5], l[7][6], l[7][7])
    table += "+-----------------------------------------------+\n"
    table += "   0     1     2     3     4     5     6     7   \n"

    return table

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

def move_bishop(list, p1, p2, direction, player, black, white, n):
    
    P1 = p1
    P2 = p2

    if player == "white" and n != 0:
        if direction == "up left" and p1 > 0 and p2 > 0:
            if p1 == 1 or p2 == 1 or n == 1:
                if list[p1-1][p2-1] in white:
                    return list
                else:
                    list[p1-1][p2-1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1-1][p2-1] == "":
                    p1 -= 1
                    p2 -= 1
                    if p1-1 == 0 or p2-1 == 0 or p1-1 == P1-n:
                        if list[p1-1][p2-1] not in white:
                            list[p1-1][p2-1] = "x"
                
                if list[p1-1][p2-1] in white:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1-1][p2-1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list

        elif direction == "down left" and p1 < 7 and p2 > 0:
            if p1 == 6 or p2 == 1 or n == 1:
                if list[p1+1][p2-1] in white:
                    return list
                else:
                    list[p1+1][p2-1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1+1][p2-1] == "":
                    p1 += 1
                    p2 -= 1
                    if p1+1 == 7 or p2-1 == 0 or p1+1 == P1+n:
                        if list[p1+1][p2-1] not in white:
                            list[p1+1][p2-1] = "x"
                
                if list[p1+1][p2-1] in white:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1+1][p2-1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list

        elif direction == "up right" and p1 > 0 and p2 < 7:
            if p1 == 1 or p2 == 6 or n == 1:
                if list[p1-1][p2+1] in white:
                    return list
                else:
                    list[p1-1][p2+1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1-1][p2+1] == "":
                    p1 -= 1
                    p2 += 1
                    if p1-1 == 0 or p2+1 == 7 or p2+1 == P2+n:
                        if list[p1-1][p2+1] not in white:
                            list[p1-1][p2+1] = "x"
                
                if list[p1-1][p2+1] in white:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1-1][p2+1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                
        elif direction == "down right" and p1 < 7 and p2 < 7:
            if p2 == 6 or n == 1:
                if list[p1+1][p2+1] in white:
                    return list
                else:
                    list[p1+1][p2+1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1+1][p2+1] == "":
                    p1 += 1
                    p2 += 1
                    if p1+1 == 7 or p2+1 == 7 or p2+1 == P2+n:
                        if list[p1+1][p2+1] not in white:
                            list[p1][p2+1] = "x"
                
                if list[p1+1][p2+1] in white:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1+1][p2+1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
        else:
            return list
            
    elif player == "black" and n != 0:
        if direction == "up left" and p1 > 0 and p2 > 0:
            if p1 == 1 or p2 == 1 or n == 1:
                if list[p1-1][p2-1] in black:
                    return list
                else:
                    list[p1-1][p2-1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1-1][p2-1] == "":
                    p1 -= 1
                    p2 -= 1
                    if p1-1 == 0 or p2-1 == 0 or p1-1 == P1-n:
                        if list[p1-1][p2-1] not in black:
                            list[p1-1][p2-1] = "y"
                
                if list[p1-1][p2-1] in black:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1-1][p2-1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list

        elif direction == "down left" and p1 < 7 and p2 > 0:
            if p1 == 6 or p2 == 1 or n == 1:
                if list[p1+1][p2-1] in black:
                    return list
                else:
                    list[p1+1][p2-1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1+1][p2-1] == "":
                    p1 += 1
                    p2 -= 1
                    if p1+1 == 7 or p2-1 == 0 or p1+1 == P1+n:
                        if list[p1+1][p2-1] not in black:
                            list[p1+1][p2-1] = "y"
                
                if list[p1+1][p2-1] in black:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1+1][p2-1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list

        elif direction == "up right" and p1 > 0 and p2 < 7:
            if p1 == 1 or p2 == 6 or n == 1:
                if list[p1-1][p2+1] in black:
                    return list
                else:
                    list[p1-1][p2+1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1-1][p2+1] == "":
                    p1 -= 1
                    p2 += 1
                    if p1-1 == 0 or p2+1 == 7 or p2+1 == P2+n:
                        if list[p1-1][p2+1] not in black:
                            list[p1-1][p2+1] = "y"
                
                if list[p1-1][p2+1] in black:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1-1][p2+1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                
        elif direction == "down right" and p1 < 7 and p2 < 7:
            if p2 == 6 or n == 1:
                if list[p1+1][p2+1] in black:
                    return list
                else:
                    list[p1+1][p2+1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
            else:
                while list[p1+1][p2+1] == "":
                    p1 += 1
                    p2 += 1
                    if p1+1 == 7 or p2+1 == 7 or p2+1 == P2+n:
                        if list[p1+1][p2+1] not in black:
                            list[p1+1][p2+1] = "y"
                
                if list[p1+1][p2+1] in black:
                    list[p1][p2] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
                else:   
                    list[p1+1][p2+1] = list[P1][P2]
                    list[P1][P2] = ""
                    return list
        else:
            return list

    else:
        return list

def move_knight(list, p1, p2, direction, player, black, white):

    if player == "white":
        if direction == 1 and p1 >= 2 and p2 <= 6:
            if list[p1-2][p2+1] not in white:
                list[p1-2][p2+1] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 2 and p1 >= 1 and p2 <= 5:
            if list[p1-1][p2+2] not in white:
                list[p1-1][p2+2] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 3 and p1 <= 6 and p2 <= 5:
            if list[p1+1][p2+2] not in white:
                list[p1+1][p2+2] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 4 and p1 <= 5 and p2 <= 6:
            if list[p1+2][p2+1] not in white:
                list[p1+2][p2+1] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 8 and p1 >= 2 and p2 >= 1:
            if list[p1-2][p2-1] not in white:
                list[p1-2][p2-1] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 7 and p1 >= 1 and p2 >= 2:
            if list[p1-1][p2-2] not in white:
                list[p1-1][p2-2] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 6 and p1 <= 6 and p2 >= 2:
            if list[p1+1][p2-2] not in white:
                list[p1+1][p2-2] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 5 and p1 <= 5 and p2 >= 1:
            if list[p1+2][p2-1] not in white:
                list[p1+2][p2-1] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list
        else:
            return list
            
    elif player == "black":
        if direction == 1 and p1 >= 2 and p2 <= 6:
            if list[p1-2][p2+1] not in black:
                list[p1-2][p2+1] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 2 and p1 >= 1 and p2 <= 5:
            if list[p1-1][p2+2] not in black:
                list[p1-1][p2+2] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 3 and p1 <= 6 and p2 <= 5:
            if list[p1+1][p2+2] not in black:
                list[p1+1][p2+2] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 4 and p1 <= 5 and p2 <= 6:
            if list[p1+2][p2+1] not in black:
                list[p1+2][p2+1] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 5 and p1 >= 2 and p2 >= 1:
            if list[p1-2][p2-1] not in black:
                list[p1-2][p2-1] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 6 and p1 >= 1 and p2 >= 2:
            if list[p1-1][p2-2] not in black:
                list[p1-1][p2-2] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 7 and p1 <= 6 and p2 >= 2:
            if list[p1+1][p2-2] not in black:
                list[p1+1][p2-2] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        elif direction == 8 and p1 <= 5 and p2 >= 1:
            if list[p1+2][p2-1] not in black:
                list[p1+2][p2-1] = list[p1][p2]
                list[p1][p2] = ""
                return list
            else:
                return list

        else:
            return list
    else:
        return list

def game_over(list):

    m = 0
    msg = ""
    while m < 8:
        n = 0
        while n < 8:
            if list[m][n] == "WKi" or list[m][n] == "BKi":
                msg += list[m][n]
            n += 1
        m +=1
    if msg == "WKi":
        print ("White Won!")
        return True
    elif msg == "BKi":
        print ("Black Won!")
        return True
    else:
        return False

def move(list, p1, p2, direction, player, black, white, n):
    if list[p1][p2] == "WKi" or list[p1][p2] == "BKi":
        move_king(list, p1, p2, direction, player, black, white)
    elif list[p1][p2] == "WPn" or list[p1][p2] == "BPn":
        move_pawn(list, p1, p2, direction, player, black, white)
    elif list[p1][p2] == "WRo" or list[p1][p2] == "BRo":
        move_rook(list, p1, p2, direction, player, black, white, n)
    elif list[p1][p2] == "WBi" or list[p1][p2] == "BBi":
        move_bishop(list, p1, p2, direction, player, black, white, n)
    elif list[p1][p2] == "WQu" or list[p1][p2] == "BQu":
        if direction in d_rook:
            move_rook(list, p1, p2, direction, player, black, white, n)
        elif direction in d_bishop:
            move_bishop(list, p1, p2, direction, player, black, white, n)
        else:
            return list
    elif list[p1][p2] == "WKn" or list[p1][p2] == "BKn":
        move_knight(list, p1, p2, direction, player, black, white)
    else:
        return list

def game(list):
    game_over(list)
    print(create_board(list))
    while game_over(list) == False:
        player = input("player? ")
        p2 = int(input("P2? "))
        p1 = int(input("P1? "))
        if list[p1][p2] == "WKn" or list[p1][p2] == "BKn":
            direction = int(input("direction? "))
        else:
            direction = input("direction? ")
        if list[p1][p2] in RnB:
            n = int(input("n? "))
        else:
            n = int(0)
        move(list, p1, p2, direction, player, black, white, n)
        print(create_board(list))
        print("")
        game_over(list)

game(board)