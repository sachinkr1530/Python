# write a progrm to print the following star pattern 
'''
     *
    ***
   *****
'''

n=int(input("Enter any number "))
for i in range (1,n+1):
    
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")