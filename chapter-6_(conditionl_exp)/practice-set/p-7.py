# Write a program to find out whether a given post is talking about "Sachin"  or not 

post=input("Enter the post ")
if("Sachin".lower() in post.lower()):
    print("this post is talkng about Sachin")
else:
    print("This post is Not talking about Sachin")