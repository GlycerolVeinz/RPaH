class MyVector:
    def __init__(self, vector_list):
        if not isinstance(vector_list, list):
            raise TypeError("invalid argument, list expected")       
         
        for i in range(len(vector_list)):
            if not (isinstance(vector_list[i],int) or isinstance(vector_list[i], float)):
                raise TypeError(f"invalid list item at {i} position, int expected")
        self.vector_list = vector_list

    def get_vector(self):
        return (self.vector_list)        
    
    def dot_product(self, other_vector):
        other_list = other_vector.get_vector()
        if len(self.vector_list) != len(other_list):
            raise ValueError("different lenghts of vectors")
                        
        final_summ = 0
        for i in range(len(self.vector_list)):
            final_summ += self.vector_list[i] * other_list[i]
        return final_summ
    
    def __mul__(self, other_vector):
        return self.dot_product(other_vector)

    def is_perpendicular_to(self,other):
        if (self * other) == 0:
            return True
        else:
            return False
    
    def cross_product(self, other):
        if len(self.vector_list) == 3 and len(other.vector_list) == 3:
            frst = self.get_vector()
            scnd = other.get_vector()
            
            return MyVector([frst[1] * scnd[2] - frst[2] * scnd[1], frst[2] * scnd[0] - frst[0] * scnd[2], frst[0] * scnd[1] - frst[1] * scnd[0]])
            
        else:
            raise ValueError("cross product can be done only with 3 dimentional vectors")
        
            
            
if __name__ == "__main__":
    vec1 = MyVector([1,2,3])
    vec2 = MyVector([3,4,5])
    vec3 = MyVector([1,0,0])
    vec4 = MyVector([0,1,0])
    print(vec1 * vec2)
    print(bool(vec3.is_perpendicular_to(vec4)))
    vec_p = vec1.cross_product(vec2)
    print(vec_p.get_vector())
    print(vec_p.is_perpendicular_to(vec1))