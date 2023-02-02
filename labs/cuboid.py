class Cuboid:
    def __init__(self,a_side,b_side,c_side):
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side
    
    def compute_surface(self):
  
        return (2 * (self.a_side * self.b_side) + 2 * (self.a_side * self.c_side) + 2 * (self.b_side * self.c_side))
    
    def make_enlarged_copy(self, a_delta, b_delta, c_delta):
        
        return Cuboid(self.a_side + a_delta, self.b_side + b_delta, self.c_side + c_delta)

if __name__ == "__main__":
    c1 = Cuboid(1,2,3)
    print(c1.compute_surface())
    c3 = c1.make_enlarged_copy(1,2,1)
    print(c3.compute_surface())
    