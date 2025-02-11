#  we are to write a progrsm that generates a random number and asks the user to guess it. If the player's guess is higher than the actual number, 
# the program should display "Lower number please". Similarly, if the user's guess is too low, the program should display "Higher number please"
# .When the user guesses the correct number, the program should display the number of guesses the player used to arrive at the number. 

import random
n=random.randint(1,100)
a=-1
guesses=1

while(a!=n):
      
    a=int(input("Guess a number: "))
    if(a>n):
        print("Lower number please ")   
        guesses+=1       
    elif(a<n):
        print(f"Higher Number please ")
        guesses+=1  
print(f"You have guessed the correctly {n} in {guesses} attempts")