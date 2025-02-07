# create a class "programmer" for storing information of few programmers working at Microsoft.

class programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
        
p=programmer("Sachin",120000,245001)
print(p.name,p.salary,p.pin,p.company)
r=programmer("Rohan",140000,23456)
print(r.name,r.salary,r.pin,r.company)