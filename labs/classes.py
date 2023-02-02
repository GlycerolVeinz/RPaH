class complex_number:

    def __init__ (self,re,im):
        self.re = re
        self.im = im

    
    def plus(self, other_number):
        return complex_number(self.re + other_number.re, self.im + other_number.im)

    def minus(self,other_number):
        return complex_number(self.re - other_number.re, self.im - other_number.im)
    
    def multiply(self, other_number):
        return complex_number(self.re * other_number.re - self.im * other_number.im, self.re * other_number.im + other_number.re * self.im)    
   
    def size(self):
        return ( ((self.re ** 2) + (self.im ** 2)) ** (1/2))
    
    def inc_parts(self, inc_re, inc_im):
        self.re += inc_re
        self.im += inc_im

    def as_string(self):
        if self.im >= 0:
            return f"{str(self.re)}+{str(self.im)}i"
        else:
            return f"{str(self.re)}{str(self.im)}i"
    
    def __str__(self):
        return self.as_string()
    def __mul__(self,other_number):
        return self.multiply(other_number)
    def __add__(self,other_number):
        return self.plus(other_number)
    def __sub__(self,other_number):
        return self.minus(other_number)



z1 = complex_number(5,5)
z2 = complex_number(3,-1)

print(z1)
print(z2)
print(z1.plus(z2))
print(z1.multiply(z2))
print(z1.size())
print(z1.inc_parts(4,9))
print(z1 * z2)
print(z1 + z2)
print(z1 - z2)
print(z1)