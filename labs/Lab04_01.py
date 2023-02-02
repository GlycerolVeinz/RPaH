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

def line_size(y_coordinate: int, x_coordinate: int, data_matrix: list):
    x_coordinate -= 1
    y_coordinate -= 1
    num = data_matrix[y_coordinate][x_coordinate]
    line_length = 0

    for j_plus in range(x_coordinate, len(data_matrix[y_coordinate]), +1):
        if data_matrix[y_coordinate][j_plus] == num:
            line_length += 1
        else:
            break

    for j_minus in range(x_coordinate, 0, -1):
        if j_minus == x_coordinate:
            continue
        else:
            if data_matrix[y_coordinate][j_minus] == num:
                line_length += 1
            else:
                break
    return line_length

def collum_size(y_coordinate: int, x_coordinate: int, data_matrix: list):
    x_coordinate -= 1
    y_coordinate -= 1
    num = data_matrix[y_coordinate][x_coordinate]
    coll_lenght = 0

    for j_plus in range(x_coordinate, len(data_matrix), +1):
        if data_matrix[j_plus][x_coordinate] == num:
            coll_lenght += 1
        else:
            break

    for j_minus in range(x_coordinate, 0, -1):
        if j_minus == x_coordinate:
            continue
        else:
            if data_matrix[j_minus][x_coordinate] == num:
                coll_lenght += 1
            else:
                break
    return coll_lenght

def r_diagonal_size(y_coordinate: int, x_coordinate: int, data_matrix: list):
    x_coordinate -= 1
    y_coordinate -= 1
    num = data_matrix[y_coordinate][x_coordinate]
    rdiagonal_lenght = 0
    xcord = copy(x_coordinate)
    ycord = copy(y_coordinate)
    
    while ycord != 0:
        if data_matrix[ycord][xcord] == num:
            rdiagonal_lenght += 1
        else:
            break
        ycord -= 1
        xcord += 1         


    xcord = copy(x_coordinate)
    ycord = copy(y_coordinate)
    
    while xcord != 0:
        if data_matrix[ycord+1][xcord-1] == num:
            rdiagonal_lenght += 1
        else:
            break
        ycord += 1
        xcord -= 1 
        
    return rdiagonal_lenght

def l_diagonal_size(y_coordinate: int, x_coordinate: int, data_matrix: list):
    x_coordinate -= 1
    y_coordinate -= 1
    num = data_matrix[y_coordinate][x_coordinate]
    ldiagonal_lenght = 0
    xcord = copy(x_coordinate)
    ycord = copy(y_coordinate)
    
    while ycord != 0:
        if data_matrix[ycord][xcord] == num:
            ldiagonal_lenght += 1
        else:
            break
        ycord += 1
        xcord += 1         


    xcord = copy(x_coordinate)
    ycord = copy(y_coordinate)
    
    while xcord != 0 or ycord != 0:
        if data_matrix[ycord-1][xcord-1] == num:
            ldiagonal_lenght += 1
        else:
            break
        ycord -= 1
        xcord -= 1 
        
    return ldiagonal_lenght

arr = generate_data(10, 15)
pretty_print(arr)
print(line_size(4, 3, arr))
print(collum_size(4, 3, arr))
print(r_diagonal_size(4, 3, arr))
