# map example
from functools import reduce
l=[1,2,3,4,5]
square=lambda x: x*x
sqlist=map(square,l)
print(list(sqlist))


# filter 

def even(n):
    if(n%2==0):
        return True
    return False 
onlyEven=filter(even,l)
print(list(onlyEven))

#Reduce

def sum(a,b):
    return a+b
mul=lambda x,y:x*y
print(reduce(sum,l))
print(reduce(mul,l))