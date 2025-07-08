# I want to create a program, where the user provides a number and the output is if the number provided 
# is odd or even...

# First: I need a variable to store the input
# Second: I need to ask for the input
# Third: I need to check if the input is odd or even
# Fourth: I need to show the answer to the user

my_variable = int(input("Provide an integer: ")) # first and second step

if my_variable % 2 == 0: # third step
    print(f"{my_variable} is even.") # fourth step
else: # third step
    print(f"{my_variable} is odd.") # fourth step

# DONE! (first version)
