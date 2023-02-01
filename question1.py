#Write a program to accept percentage from the user and display the grade according to the following criteria:
#input marks here
Marks = int(input("Please enter your percentage: "))
#checking for criteria
if Marks > 90:
    print("A")
elif Marks>80 and Marks<=90:
    print("B")
elif Marks>=60 and Marks<=80:
    print("C")
else:
    print("D")
