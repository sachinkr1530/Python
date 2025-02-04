a=int(input("Enter your age: "))

# if statement-1
if(a%2==0):
    print("A is even")
    
# if statement-2
if(a>=18):
    print("Your are above age ")
elif(a<0):
    print("You are entring invalid age ")

elif(a==0):
    print("You are entring 0 which are not valid age ")

else:
    print("You are below the age of concent")
    
print("End of program")