class Employee:
    
    language="Py"
    salary=120000
    
    
    def __init__(self,name,salary,language):   # dunder method which is automacally called 
        self.name=name
        self.salary=salary
        self.language=language
    
        print("I am creating an object")
        
    
    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    
    
    @staticmethod # static method work 
    def greet():
        print(f"Good morning")  
    
sachin=Employee("sachin",13000,"Javascript")
# sachin.name="sachin"
print(sachin.name,sachin.salary,sachin.language)
# rohan=Employee()