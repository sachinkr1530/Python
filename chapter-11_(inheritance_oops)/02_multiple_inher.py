class Employee:
    comapany="TCS"
    name="Default name"
    salary=12344
    def show(self):
        print(f"The name is {self.name} and the salary {self.salary}")
        
        
class Coder:   
    language="python"
    def printlanguage(self):
        print(f"Out of all the language here is your language: {self.language}")

  
class Programmer(Employee,Coder):
    comapany="TCS inforsis"
    def showLanguage(self):
        print(f"The name is {self.comapany} and he is good with {self.language} language")

a=Employee()
b=Programmer()
b.show()
b.printlanguage()
b.showLanguage()
print(a.comapany,b.comapany)
