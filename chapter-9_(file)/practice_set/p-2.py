'''
The game() function in a program let's a user play a game and return the score as an integer.you need to read a file'Hi-score.text()
which is either blank or contains the previous Hi-score.You need to write a program to update the Hi-score whenever the game() function 
breaks the Hi-score.'''


import random
def game():
    print("you are playing the game..")
    score=random.randint(1, 62)
    # fetch the hiscore
    with open("hiscore.txt")as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
        
    print(f"your score : {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("hiscore.txt","w")as f:
         f.write(str(score))
    return score

game()

