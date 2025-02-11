#write a program to filter a list of number which are divisible by 5.


def divisible5(n):
    if(n%5==0):
        return True
    return False
a=[1,2,3,588,668,1485,7856]
f=list(filter(divisible5,a))
print(f)