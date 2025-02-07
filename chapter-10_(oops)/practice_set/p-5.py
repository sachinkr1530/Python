# Write a class Train which has method to book a ticket,get status (no of seats) and get fare information of train running under indian Railways
from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in Train No {self.trainNo} from {fro} to {to}")
    def getstatus(self):
       print(f"Train no {self.trainNo} is running on time") 
    def getfare(self,fro,to):
        print(f"Ticket fare in train no {self.trainNo} from {fro} to {to} is {randint(222,555)}")
        
t=Train(13453)
t.book(" Motihari","cheenai")
t.getstatus()
t.getfare(" Motihari"," Cheenai ")