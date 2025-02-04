# Write a program too find out whether a student has passed or faiiled if it requires a total of 40% and at least 33% in 
#         each subject to pass.  Assume 3 subject and make marks as  an input from the user.

m1=int(input("Enter subject-1 marks  "))
m2=int(input("Enter subject-2 marks  "))
m3=int(input("Enter subject-3 marks  "))
total_percentage=(100*(m1+m2+m3))/300

if(total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("You are passed  ",total_percentage)
else:
    print("you are failed try again  next year ",total_percentage)