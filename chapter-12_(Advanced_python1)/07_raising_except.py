a=int(input("Enter a number "))
b=int(input("Enter a number "))
if(b==0):
    raise ZeroDivisionError("Heey our program is not ment to division number by zero")
else:
    print(f"The Divion a/b is {a/b}")
