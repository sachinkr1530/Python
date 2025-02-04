# write a program using funtion to find greatest of three number

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a=int(input("enter a number " ))
b=int(input("enter b number " ))
c=int(input("enter c number " ))
print(f"the greatest number=:{greatest(a,b,c)}")