# Repeat program 4 for a list of such words to be censored

words=["Donkey","bad","ganda"]
with open("file.txt","r") as f:
    cont=f.read()
for word in words:  
    cont=cont.replace(word,"#"*len(word))
with open("file.txt","w")as f:
    f.write(cont)