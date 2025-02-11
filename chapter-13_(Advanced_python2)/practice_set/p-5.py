# Write a program to find the maximum of the number in a list using the reduce function.

from functools import reduce
a=[1,2,3,588,668,1485,7856,57855,14782]
def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,a))