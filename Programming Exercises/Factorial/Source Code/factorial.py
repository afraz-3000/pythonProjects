# Afraz Akram
# April 8, 2023
# ICS4U
# Mr Manyanga

# This program will prompt the user to enter a number.
# It will be computed, and the factorial will be the output.

print("Hello user, welcome to the factorial program!")
while True:
    userInput = input("Enter the integer you would like to find the factorial of: ")
    try:
        userInput = int(userInput)
    except ValueError:
        print("Please enter a valid value.")
        continue
    if userInput < 0:
        print("Factorials can not be done with negative integers.")
        continue
    elif userInput == 0:
        print(f"The factorial of {userInput} is 1.")
    else:
        fact = 1
        for i in range(1, userInput + 1):
            fact = fact * i
        print(f"The factorial of {userInput} is {fact}.")
    while True: # If user wants to use again
        userSelection2 = input("\nWould you like to use the factorial program again?\n\n\tY) Yes\n\tN) No\n\nEnter here: ")  
        if userSelection2.upper() != "Y" and userSelection2.upper() != "N":
            print("\nPlease enter a valid selection.")
            continue
        elif userSelection2.upper() == "Y" or userSelection2.upper() == "N":
            break
    if userSelection2.upper() == "Y":
        continue
    elif userSelection2.upper() == "N":
        print("\nThank you for using the factorial program!")
        break