#Write a program to accept the cost price of a bike and display
#the road tax to be paid according to the following criteria

#user input
costPriceOfBike = float(input("Enter the cost price of a bike: "))
#criteria
if(costPriceOfBike>100000):
    print("15%")
elif costPriceOfBike>50000 and costPriceOfBike<=100000:
    print("10%")
else:
    print("5%")
