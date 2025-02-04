# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.

f=open("poem.txt")
cont=f.read()
if("twinkle"in cont):
    print("The word in present in the content")
else:
    print("The word twinkle is not present in the content ")
f.close()