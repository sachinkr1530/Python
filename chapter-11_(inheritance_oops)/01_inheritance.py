class Employee:
    comapany="TCS"
    def show(self):
        print(f"The name is {self.name} and the salary {self.salary}")
        
# class Programmer:
#     comapany="Salsforce"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
        
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
        
class Programmer(Employee):
    comapany="TCS inforsis"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a=Employee()
b=Programmer()
print(a.comapany,b.comapany)