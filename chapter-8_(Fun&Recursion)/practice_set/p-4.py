# write a recursion function to calculate the sum of first n natural number 
'''
 sum(1)=1
 sum(4)=1+2+3+4
 sum(n)=sum(n-1)+n
'''
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

n=int(input("enter a number "))
print(f"Sum of the inputed number {sum(n)}")