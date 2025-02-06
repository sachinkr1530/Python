class Employee:
    name="Sachin"
    language="Py"
    salary=120000
    
    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    
    
    @staticmethod # static method work 
    def greet():
        print(f"Good morning")  
    
sachin=Employee()
#sachin.language="javascript"
# print(sachin.language,sachin.salary)
sachin.greet()
sachin.getInfo()
