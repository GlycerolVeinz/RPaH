
class MyMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def save(self, file_name):
        with open(file_name, mode='w', encoding='utf-8') as a_file:
            for i in range(len(self.matrix)):
                a_file.write(str(self.matrix[i]))
                if i != len(self.matrix) - 1:
                    a_file.write(" ")
    
    def load(self, file_name):
        with open(file_name, mode='rt', encoding='utf-8') as a_file:
            mat = a_file.readline()
            new_mat = mat.split(" ")
        self.matrix = new_mat
    
    
if __name__ == "__main__":
    a = MyMatrix([[1,2,3],[7,8,9]])
    a.save("kek.txt")
    heh = MyMatrix([])
    
    print(a.matrix, heh.matrix)