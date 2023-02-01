#Why and when to use while loop in python
#give a detailed description with example

# A while loop in Python is used to repeatedly execute a block of code
# as long as a certain condition is met.
# The loop will keep running as long as the condition is True,
# and will exit when the condition becomes False.

# Here's the general syntax for a while loop in Python:
# while condition:
#     # Code to be executed

# Here's an example that demonstrates the use of a while loop:
# Print the numbers from 1 to 10
counter = 1

while counter <= 10:
    print(counter)
    counter += 1

# In this example, the while loop will run as long as
# the value of counter is less than or equal to 10.
# On each iteration of the loop, the value of counter is printed,
# and then incremented by 1.
# The loop will exit when the value of counter becomes greater than 10.

# The while loop is useful when you don't know in advance how many times
# you need to loop, and you want to keep looping until a certain condition is met.
# For example, you can use a while loop to read data from a file until the end of the file is reached,
# or to keep asking the user for input until a valid response is given.
