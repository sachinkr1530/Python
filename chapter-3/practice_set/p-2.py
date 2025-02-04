# Write a program to fill in a letter template given below with name and date
    # letter='''
    #         Dear <|NAme|>,
    #         You are Selected |
    #         <|Date|
    #         '''
            
letter='''
Dear <|Name|>,
You are Selected |
<|Date|'''
         
print(letter.replace ("<|Name|>","Sachin").replace("<|Date|","24 september 2025"))