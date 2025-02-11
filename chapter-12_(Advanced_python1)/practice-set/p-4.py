# Write a program to display a/b are integers. if b=0, display infinite by handling the 'ZeroDivisionError'.

try:
    a=int(input("enter a: "))
    b=int(input("enter a: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")
