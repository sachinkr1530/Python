# Write a __str__() method to print the vector as follows: 7i+8k+10k  Assume vector of dimension 3 for this problem.

# Write a class vector representing a vector of n dimensions.Overload the + and * operator which calculates the sum and the dot(.) product of them.

class vector:
    def __init__(self,x,y,z):
        self.x=x 
        self.y=y 
        self.z=z
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y,self.z+other.z) 
        return result 
    
    def __mul__(self,other):
        return self.x*other.x+self.y*other.y+self.z*other.z
        return result
    
    def __str__(self):
        return f" {self.x}i+{self.y}j+{self.z}k"
v1=vector(1,2,3)
v2=vector(4,5,6)
v3=vector(7,8,9)
print(v1+v2)
print(v1*v2)

print(v1+v3)
print(v1*v3)