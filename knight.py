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