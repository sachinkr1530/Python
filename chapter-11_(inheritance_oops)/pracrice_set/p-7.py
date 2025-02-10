# Write a class vector representing a vector of n dimensions.Overload the + and * operator which calculates the sum and the dot(.) product of them.

class vector:
    def __init__(self,l):
        self.l=l
        
    def __len__(self):
        return len(self.l)
v1=vector([1,2,5])
print(len(v1))