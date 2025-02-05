# write a program to find out wheather a file is identical & matches the content of another file.

with open("this.txt")as f:
    content1=f.read()

with open("this_copy.txt")as f:
    content2=f.read()
    
if(content1==content2):
    print("yes these files are identical")
    
else:
    print("No these files are not identical")
    