'''
 A file contains a word "Donkey" multiple times. you need to write a program
 which replace this word with ##### by updating the same file.
'''

word="Donkey"
with open("file.txt","r") as f:
    cont=f.read()
contNew=cont.replace(word,"######")
with open("file.txt","w")as f:
    f.write(contNew)