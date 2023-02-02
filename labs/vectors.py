class MyVector:

    def __init__(self, vector_list):
        self.vector_list = vector_list

    def get_vector(self):
        return (self.vector_list)

    def plus(self, other):
        longer = 0
        if len(self.get_vector()) >= len(other.get_vector()):
            longer = len(self.get_vector())
        else:
            longer = len(other.getvector())

        new_vector = list()
        for i in range(longer):
            new_vector.append((self.get_vector()[i]) + (other.get_vector()[i]))

        return MyVector(new_vector)

    def __add__(self, other):
        return self.plus(other)

    def norm(self):
        summ = 0
        for i in range(len(self.get_vector())):

            summ += (self.get_vector()[i])**2

        return (summ**(1 / 2))
