# Add a static method inproblem 2, to greet the user with hello



class calculator:
    def __init__(self,n):
        self.n=n
        
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The cube is {self.n**1/2}")
        
    @staticmethod
    def hello():
        print("HEllo i m sachin")
        

a=calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()
    