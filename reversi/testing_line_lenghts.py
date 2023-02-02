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


def line_size(game_desk, y_coordinate, x_coordinate, direction):
    num = game_desk[y_coordinate][x_coordinate]

    ycord, xcord = copy(y_coordinate), copy(x_coordinate)

    line_lenght = -1

    while ycord <= 7 and xcord <= 7:
        if game_desk[ycord][xcord] == num:
            line_lenght += 1
        else:
            break
        ycord += direction[0]
        xcord += direction[1]
    ycord, xcord = copy(y_coordinate), copy(x_coordinate)

    while ycord >= 0 and xcord >= 0:
        if game_desk[ycord][xcord] == num:
            line_lenght += 1
        else:
            break
        ycord -= direction[0]
        xcord -= direction[1]
    return line_lenght


line = [0, 1]
collum = [1, 0]
l_diag = [1, -1]
r_diag = [1, 1]


for i in range (1000):
    desk = generate_data(8, 8)
    pretty_print(desk)
    print(line_size(desk, 0, 0, r_diag))
