# Create a class with a class attribute a; create an object from it and set 'a' directly using object.a=0.does this change the class attribute?

class Demo:
    a=4
o=Demo()
o.a=0  # instrance attributes is set
print(o.a) # print the class attribute because instrance attributes is not present
print(Demo.a) # prints class attributes 

# Ans=> No 