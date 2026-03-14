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

import copy
from king import move_king
from pawn import move_pawn
from rook import move_rook
from bishop import move_bishop
from knight import move_knight

def create_board(l):
    table = "+-----------------------------------------------+\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 8\n" \
            .format(l[0][0], l[0][1], l[0][2], l[0][3],
                    l[0][4], l[0][5], l[0][6], l[0][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 7\n" \
            .format(l[1][0], l[1][1], l[1][2], l[1][3],
                    l[1][4], l[1][5], l[1][6], l[1][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 6\n" \
            .format(l[2][0], l[2][1], l[2][2], l[2][3],
                    l[2][4], l[2][5], l[2][6], l[2][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 5\n" \
            .format(l[3][0], l[3][1], l[3][2], l[3][3],
                    l[3][4], l[3][5], l[3][6], l[3][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 4\n" \
            .format(l[4][0], l[4][1], l[4][2], l[4][3],
                    l[4][4], l[4][5], l[4][6], l[4][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 3\n" \
            .format(l[5][0], l[5][1], l[5][2], l[5][3],
                    l[5][4], l[5][5], l[5][6], l[5][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 2\n" \
            .format(l[6][0], l[6][1], l[6][2], l[6][3],
                    l[6][4], l[6][5], l[6][6], l[6][7])
    table += "|-----------------------------------------------|\n"
    table += "| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | 1\n" \
            .format(l[7][0], l[7][1], l[7][2], l[7][3],
                    l[7][4], l[7][5], l[7][6], l[7][7])
    table += "+-----------------------------------------------+\n"
    table += "   1     2     3     4     5     6     7     8   \n"

    return table

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
    y = 0
    game_over(list)
    print(create_board(list))
    while game_over(list) == False:
        p1 = 0
        p2 = 0
        h = copy.deepcopy(list)
        if y%2 == 0:
            player = "white"
        else:
            player = "black"

        while p2 < 1 or p2 > 8:
            p2 = int(input("P2? "))
        while p1 < 1 or p1 > 8:
            p1 = int(input("P1? "))
        p2 -= 1
        p1 = 8 - p1
        if list[p1][p2] == "WKn" or list[p1][p2] == "BKn":
            direction = int(input("direction? "))
        else:
            direction = input("direction? ")
        if list[p1][p2] in RnB:
            n = int(input("n? "))
        else:
            n = int(0)
        move(list, p1, p2, direction, player, black, white, n)

        if list == h:
            print("Invalid!")
        else:
            print(create_board(list))
            print((y+1)/2)
            print("")
            game_over(list)
            y += 1

game(board)