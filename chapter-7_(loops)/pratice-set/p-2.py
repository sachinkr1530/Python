# write a program to greet all the person names stored in a list 'L' and which starts with 'S'.
# l=["Harry","Sohan","Sachin","Rahul"]

l=["Harry","Sohan","Sachin","Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"Name {name}")