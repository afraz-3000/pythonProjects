# Afraz Akram
# February 25 2023
# ICS4U
# Mr. Manyanga
# Version 1.0

''' This program will count the number letters, spaces, digits, and special
characters (%, #, $, @, !, *, &). It will first prompt the user to enter a
string. The input will be processed through the use of string methods. The
output will be the number of each character type. The program can be used
again until the user decides not to.'''

print("Hello user, welcome to the character counter program!")

# We give our greetings to the user and tell them what the program is.

i = 0

# We set a variable, i, to 0 so that the while loop can be ran.

letters = "abcdefghijklmnopqrstuvwxyz"

specialCharacters = ["%", "#", "$", "@", "!", "*", "&"]

# We have a collection of letters and special characters for later use.

while i == 0:

# Every process inside this loop will happen until the user decides to stop using the program.
  
    userString = input("\nEnter a string you would like to count the characters of: ")
    
    # Prompt the user to enter the string.
    
    countLetters = 0
    
    # Variable containing the number of letters.
    
    lowerUserString = userString.lower()
    
    for letter in letters:
        
        countLetters = countLetters + lowerUserString.count(letter)
        
    # The for loop will count the number of letters in the string.
    
    countSpaces = userString.count(" ")
    
    # Variable containing the number of spaces.
    
    countDigits = 0
    
    # Variable containing the number of digits.
    
    for digit in range(10):
        
        countDigits = countDigits + userString.count(str(digit))
        
    # The for loop will count the number of digits in the string.
    
    countSpecial = 0
    
    # Variable containing the number of special characters.
    
    for special in specialCharacters:
        
        countSpecial = countSpecial + userString.count(special)
        
    # The for loop will count the number of special characters in the string.
    
    countOther = len(userString) - (countLetters + countSpaces + countDigits + countSpecial)
    
    # Variable containing the number of other characters that were not counted for before.

    print(f"\nThere are {countLetters} letters, {countSpaces} spaces, {countDigits} digits, {countSpecial} special characters (%, #, $, @, !, *, &), and {countOther} other characters in your string.")
    
    # Print the final statement displaying the amount of characters!

    while i == 0:
        
    # This loop is when the user enters a selection.

        userSelection2 = input("\nWould you like to use the program again?\n\n\tY) Yes\n\tN) No\n\nEnter here: ")
        
        # We prompt the user if they want to use the converter again.
  
        if userSelection2.upper() != "Y" and userSelection2.upper() != "N":
            print("\nPlease enter a valid selection.")
            continue
        
        # If the selection is neither yes or no, we prompt the user to enter a valid value again.

        elif userSelection2.upper() == "Y" or userSelection2.upper() == "N":
            break
        
        # If the selection is either yes or no, we break out of the inner loop so a decision can be made.

    if userSelection2.upper() == "Y":
        continue
    
    # If the selection is yes, we go back to the top of the main loop.

    elif userSelection2.upper() == "N":
        print("\nThank you for using the character counter program!")
        break
    
    # If the selection is no, we thank the user and exit the main loop.