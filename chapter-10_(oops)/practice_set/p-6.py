# can you change the self-parameter inside a class to somethings else(say "sachin").Try changing self to "slf" or "sachin" and see the effects.


from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo
    def book(sachin,fro,to):
        print(f"Ticket is booked in Train No {sachin.trainNo} from {fro} to {to}")
    def getstatus(self):
       print(f"Train no {self.trainNo} is running on time") 
    def getfare(self,fro,to):
        print(f"Ticket fare in train no {self.trainNo} from {fro} to {to} is {randint(222,555)}")
        
t=Train(13453)
t.book(" Motihari","cheenai")
t.getstatus()
t.getfare(" Motihari"," Cheenai ")


# Ans=> No 