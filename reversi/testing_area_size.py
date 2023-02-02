
from copy import copy
import random

def pretty_print(one_line_matrix: list):
    for i in one_line_matrix:
        for j in i:
            print(j, end=" ")
        print()

def generate_data(rows: int, cols: int):
    new_matrix = list()
    helping_matrix = list()

    for i in range(rows):
        for j in range(cols):
            helping_matrix.append(random.randint(0, 1))
        new_matrix.append(helping_matrix)
        helping_matrix = list()

    return new_matrix

def area_size(y_coordinate, x_coordinate, game_desk):
    num = game_desk[y_coordinate][x_coordinate]
    xcord = copy(x_coordinate)
    ycord = copy(y_coordinate)
    
    def cord_reset(x_value,y_value):
        x_value = copy(x_coordinate)
        y_value = copy(y_coordinate)
        return x_value, y_value


    #line lenght
    line_lenght = 0
    while xcord != 7: #to the right
        if game_desk[ycord][xcord] == num:
            line_lenght += 1
        else:
            break
        xcord += 1

    cord_reset(xcord, ycord)  #reset xcord
    while xcord != 0: #to the left
        if game_desk[ycord][xcord - 1] == num:
            line_lenght += 1
        else:
            break
        xcord -= 1
    cord_reset(xcord, ycord)  #reset xcord


    #collum lenght
    coll_lenght = 0
    while ycord != 7:  #counting down
        if game_desk[ycord][xcord] == num:
            coll_lenght += 1
        else:
            break
        ycord += 1
    cord_reset(xcord, ycord)

    while ycord != 0:  #counting up
        if game_desk[ycord - 1][xcord] == num:
            coll_lenght += 1
        else:
            break
        ycord -= 1
    cord_reset(xcord, ycord)
    
    
    #from left to right diagonal lenght
    ldiag_lenght = 0
    while ycord != 7 or xcord != 7: #counting down
        if game_desk[ycord][xcord] == num:
            ldiag_lenght += 1
        else:
            break
        xcord += 1
        ycord += 1
    cord_reset(xcord, ycord)
    
    while ycord != 0 or xcord != 0: #counting up
        if game_desk[ycord-1][xcord-1] == num:
            ldiag_lenght += 1
        else:
            break
        xcord -= 1
        ycord -= 1
    cord_reset(xcord, ycord)
    
    
    #form right to left diagonal lenght
    rdiag_lenght = 0
    while ycord != 7 or xcord != 0: #counting down
        if game_desk[ycord][xcord] == num:
            rdiag_lenght += 1
        else:
            break
        xcord -= 1
        ycord += 1
    cord_reset(xcord, ycord)
    while ycord != 0 or xcord != 7: #counting up
        if game_desk[ycord - 1][xcord + 1] == num:
            rdiag_lenght += 1
        else:
            break
        xcord += 1
        ycord -= 1
    cord_reset(xcord, ycord)
    
    return ((line_lenght + coll_lenght + rdiag_lenght + ldiag_lenght) - 3)
    
    
    
    

arr = generate_data(8, 8)
pretty_print(arr)
print(area_size(2,1,arr))