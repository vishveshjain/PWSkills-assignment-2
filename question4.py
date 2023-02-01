#check how many times a given number can be divided by 3
#before it is less than or equal to 10

#user input
number = int(input("Enter a number: "))
#variable declaration
count = 0
#while loop will run until it is less than or equal to 10
while number > 10:
    #check for divide by 3
    number = number / 3
    #increment count
    count += 1
#print message
print("The number can be divided by 3 is", count, "times before it is less than or equal to 10.")
