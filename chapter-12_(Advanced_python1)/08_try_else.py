try:
    a=int(input("hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")