# parens.py
# 
# Created by: Tran Tran
# Date: 2/9/2016
#
# The program checks the proper pairing of parentheses in a simple mathematical equation entered by the user.

# Prompt and extract a string from the user that contains a simple 
# mathematical equation.
userInput = input("Please enter a simple mathematical equation: ")

# Initialize the variables.
error = False
count = 0 # Count the number of parenthesis.
i = 0

# Examine the equation and determine if it contains a proper paring of 
# parenthesis.
while i < len(userInput) and not error :     
    letter = userInput[i] 
    
    # Determine the number of proper paring of parenthesis.
    if letter == "(" :      
        count = count + 1
    elif letter == ")" :
        count = count - 1
    
    # Stop processing the string and print a question mark at that point 
    # if there are too many right parentheses.
    if count < 0 :
        error = True
        print("?")
    else :
        # Print every letter in the equation to the terminal.
        print(letter, end="")
    i = i + 1

# Print the results.  
if error :
    print("ERROR: Unexpected parenthesis.")    
elif count == 0 :
    print()
    print("Valid equation.")
else :
    print()
    print("ERROR: Missing right parentheses:", ")" * count)

    