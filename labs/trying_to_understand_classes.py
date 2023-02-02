class Data:
    def __init__(self, value):
        self.value = value
        
    def __mul__(self, other):
        return Data(self.value * other.value)
a = Data(21)
b = Data(2)
c = a * b
print(c.value)

# 42


# class MyVector:
#     def __init__(self, name, values) -> None:
#         self.name = name
#         self.values = values

#     def get_values(self):
#         return self.values
    
#     def increase_values(self, x):
#         result = []
#         for v in self.values:
#             result.append(v + x)
#         return result


# v1: MyVector = MyVector("Eugene", [1,2,3])
# v2 = MyVector("Matvei", [3,2,1])

# print(v1.name)
# print(v2.name)

# print(v1.get_values())
# print(v2.get_values())

# print(v1.increase_values(5))
# print(v2.increase_values(10))

