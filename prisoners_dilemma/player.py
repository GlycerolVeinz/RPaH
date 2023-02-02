# quote: For all finitely repeated PDs,
# mutual defection in every period is the unique subgame perfect equilibrium.
# (source: https://www.youtube.com/watch?v=CO3-796fGv8&ab_channel=WilliamSpaniel)

class MyPlayer:
    '''Player that picks better variant, independetly of enemy's choice'''
    def __init__(self, payoff_matrix, number_of_iterations=1):
        # Inputs:
        #
        # payoff_matrix, number of iterations
        # number of iterations isnt used in this code,
        # but I need to store it due to asigments specifications.
        # 
        # Also need to check all inputs if they are the right type,
        # befor adding them in to my class.
        # 
        # Outputs:
        # 
        # in move() method - DEFECT(False) / COOPERATE(True)
        
        # quick input checks
        if not (isinstance(payoff_matrix, list) or isinstance(payoff_matrix, tuple)):
            raise TypeError("invalid argument, list or tuple expected")
        if not isinstance(number_of_iterations, int):
            raise TypeError("invalid argument, int expected")
        
        #finally self classes arguments
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations

    def move(self):
        # first I need to check where is the better profit,
        # regardless of an enemys move.
        #
        # I agree with the quete from the begining of this document,
        # so I wont be "evolving strategy, even if the enemy does so.
        
        payoff = self.payoff_matrix  #this one is added for clarity of code

        if (payoff[0][0][0] + payoff[0][1][0]) > (payoff[1][0][0] + payoff[1][1][0]):
            # if the payoff is different from the standart version -> COOPERATE
            return False

        else:
            # else -> DEFECT
            return True

    def record_last_moves(self, my_last_move, opponent_last_move):
        
        #checking if the enemys code is good enough and outputs bool hehe,
        #also mine, just to be sure        
        if not (isinstance(my_last_move, bool) or isinstance(opponent_last_move, bool)):
            raise TypeError("wrong argument, bool expected")
        
        last_moves_list = list()
        last_moves_list.append((my_last_move, opponent_last_move))


if __name__ == "__main__":
    original_payoff_matrix = (((4, 4), (1, 6)), ((6, 1), (2, 2)))
