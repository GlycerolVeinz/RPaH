from copy import copy
import random

line = [0, 1]
collum = [1, 0]
l_diag = [1, -1]
r_diag = [1, 1]
directions = [line, collum, l_diag, r_diag]

positional_strat_arr = [
    [99, -8, 8, 6, 6, 8, -8, 99],
    [-8, -24, -4, -3, -3, -4, -24, -8],
    [8, -4, 7, 4, 4, 7, -4, 8],
    [6, -3, 4, 0, 0, 4, -3, 6],
    [6, -3, 4, 0, 0, 4, -3, 6],
    [8, -4, 7, 4, 4, 7, -4, 8],
    [-8, -24, -4, -3, -3, -4, -24, -8],
    [99, -8, 8, 6, 6, 8, -8, 99],
] # taken from https://samsoft.org.uk/reversi/strategy.htm#position, still sick can't think of anythink better sorry


class MyPlayer:
    """
    Player that gives back move based on positional strategy
    """

    def __init__(self, my_color, oponent_color):
        self.my_color = my_color
        self.oponent_color = oponent_color

    def is_on_board(self, nums_arr):

        for num in nums_arr:
            if (num <= 7) and (num >= 0):
                continue
            else:
                return False
        return True

    # def is_on_board(self, pos):
    #     return 0<=pos[0]<=7 and 0<=pos[1]<=7 


    def line_position(self, board, stone_color, y_coordinate, x_coordinate,
                      direction):
        #stores all positions of one stone color in a line
        num = stone_color

        #set values as to not change the original ones
        ycord, xcord = copy(y_coordinate), copy(x_coordinate)

        #create an empty list for all positions
        line_positions = list()

        while self.is_on_board([ycord, xcord]):
            #check one side
            if board[ycord][xcord] == num:
                line_positions.append([ycord,
                                       xcord])  #put on the end of a list
            else:
                break
            ycord += direction[0]
            xcord += direction[1]

        if len(line_positions) > 0:
            #take out starting position, will be there in second side
            line_positions.pop(0)

        # reset values
        ycord, xcord = copy(y_coordinate), copy(x_coordinate)

        while self.is_on_board([ycord, xcord]):
            #check other side
            if board[ycord][xcord] == num:
                #put at the strat of a list
                line_positions.insert(0, [ycord, xcord])
            else:
                break
            ycord -= direction[0]
            xcord -= direction[1]

        return line_positions

    def move(self, board):
        # selects a random move from possible
        possible_moves = list()

        # thru the whole board
        for row in range(len(board)):
            for coll in range(len(board)):
                for dir in directions:
                    # make list of enemy stones that are in line, reset before use
                    current_line = list()
                    current_line = self.line_position(board,
                                                      self.oponent_color, row,
                                                      coll, dir)

                    # if there is a line
                    if (len(current_line) >= 1):
                        # check if on board
                        before_y = current_line[0][0] - dir[0]
                        before_x = current_line[0][1] - dir[1]
                        after_y = current_line[-1][0] + dir[0]
                        after_x = current_line[-1][1] + dir[1]

                        to_check = [before_y, before_x, after_y, after_x]
                        if self.is_on_board(to_check):

                            if ((board[before_y][before_x])
                                    == self.my_color) and (
                                        (board[after_y][after_x]) == -1):
                                possible_moves.append((after_y, after_x))
                            elif ((board[after_y][after_x])
                                  == self.my_color) and (
                                      (board[before_y][before_x]) == -1):
                                possible_moves.append((before_y, before_x))
                            else:
                                continue

        if len(possible_moves) == 0:
            return None
        else:
            my_move = possible_moves[0] 
            for pos in possible_moves:
                if board[pos[0]][pos[1]] > board[my_move[0]][my_move[1]]:
                    my_move = pos
            return my_move

if __name__ == "__main__":

    def pretty_print(one_line_matrix: list):
        for i in one_line_matrix:
            for j in i:
                if j < 0:
                    print(j, end=" ")
                else:
                    print(j, end="  ")
            print()

    def generate_data(rows: int, cols: int):
        new_matrix = list()
        helping_matrix = list()

        for i in range(rows):
            for j in range(cols):
                helping_matrix.append(random.randint(-1, 1))
            new_matrix.append(helping_matrix)
            helping_matrix = list()

        return new_matrix

    player = MyPlayer(0, 1)

    desk = generate_data(8, 8)

    pretty_print(desk)

    print(player.move(desk))