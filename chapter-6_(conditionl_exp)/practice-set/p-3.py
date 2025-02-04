# A spam comment is defined as a text containing following keyword:
# "make a lot of Money ","buy now","subscribe this","click this ".Write a program to detect these spams.

p1="make a lot of Money "
p2="buy now"
p3="subscribe this"
p4="click this"
message=input("Enter your comment")

if((p1 in message) or(p2 in message) or(p3 in message)or (p4 in message)):
   print("This message is a spam") 

else:
    print("this message is not spam")