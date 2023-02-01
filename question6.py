#Use nested while loop to print 3 different pattern

#pattern 1 
print("Pattern 1")
#initialize variables 
i=1
j=1
#while loop
while i<5:
    #nested while
    while j<=i:
        #printed j without space
        print(j, end="")
        #increment j by 1
        j+=1
    #print new line
    print()
    #reset value of j
    j=1
    #increment value of i by 1
    i+=1

print("----------------------------------------------------------------")
print("Pattern 2")
#initialize variables 
i=1
j=1
#while loop
while i<5:
    #nested while
    while j<=i:
        #printed * without space
        print("*", end="")
        #increment j by 1
        j+=1
    #print new line
    print()
    #reset value of j
    j=1
    #increment value of i by 1
    i+=1

print("----------------------------------------------------------------")
print("Pattern 3")
#initialize variables 
i=1
j=1
#while loop
while i<10:
    #nested while
    while j<10:
        #printed smile with smile using Unicode associated with it
        print("\U0001f600\U0001f600", end="\U0001F606")
        #increment j by 1
        j+=1
    #print new line
    print()
    #reset value of j
    j=1
    #increment value of i by 1
    i+=1