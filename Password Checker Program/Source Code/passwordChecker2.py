# Afraz Akram
# February 28 2023
# ICS4U
# Mr. Manyanga
# Version 2.0

''' This program will check if an entered  password is, very strong,
strong, weak or very weak. It will first prompt the user to enter a
password. The input will be processed through the use of string methods,
loops, and logical operators. The output will be the strength of the password.'''

print("Hello user, welcome to the password checker program!")

print("\nA very strong password has no spaces, uppercase letters, lowercase letters, digits, and special characters [%, #, $, @, !, *, &].")

# We give our greetings to the user and tell them what the program is.

lettersUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lettersLower = "abcdefghijklmnopqrstuvwxyz"

specialCharacters = ["%", "#", "$", "@", "!", "*", "&"] 

# Create the data of letters and special characters for later use.

while True:
    
# Every process inside this loop will happen until the user decides to stop using the program.
    
    score = 0
    
    # The score depends if certian conditions are met.
    
    userData = input("\nEnter a password you would like to check the strength of: ")
    
    # Prompt the user to enter a password.
    
    countDigits = 0
    
    for digit in range(10):
        
        countDigits = countDigits + userData.count(str(digit))
    
    # Count the number of digits in the password.
    
    countLettersUpper = 0
    
    for letterUpper in lettersUpper:
        
        countLettersUpper = countLettersUpper + userData.count(letterUpper)
    
    # Count the number of upper case letters in the password.
    
    countLettersLower = 0
    
    for letterLower in lettersLower:
        
        countLettersLower = countLettersLower + userData.count(letterLower)
    
    # Count the number of lower case letters in the password.
    
    countSpecialCharacters = 0
    
    for specialCharacter in specialCharacters:
        
        countSpecialCharacters = countSpecialCharacters + userData.count(specialCharacter)
    
    # Count the number of special characters in the password.
    
    countSpaces = userData.count(" ")
    
    # Count the number of spaces in the password.
    
    userLength = len(userData)
    
    # Get the length of the password.
    
    if countDigits > 0:
        
        score = score + 1
    
    # Score increased if there are digits.
    
    if countLettersUpper > 0 and countLettersLower > 0:
        
        score = score + 1
    
    # Score increased if there are both uppercase and lowercase letters.
    
    if countSpecialCharacters > 0:
        
        score = score + 1
    
    # Score increased if there are special characters.
    
    if countSpaces == 0:
        
        score = score + 1
    
    # Score increased if there are no spaces.
    
    if userLength < 8 or userLength > 15:
        
        print("\nThe length should be between 8 and 15 characters.")
        
        continue
    
    # Prompt the user to enter another password 
    
    elif score == 0:
        print("\nThe password is VERY WEAK.")
        print("\nNONE of the conditions are met:\n\tNo Spaces\n\tDigits\n\tUpper Case Letters AND Lower Case Letters\n\tSpecial characters [%, #, $, @, !, *, &]")

    elif score == 1:
        print("\nThe password is VERY WEAK.")
        print("\nONE of the conditions are met:\n\tNo Spaces\n\tDigits\n\tUpper Case Letters AND Lower Case Letters\n\tSpecial characters [%, #, $, @, !, *, &]")

    # A score of 0 or 1 is very weak.
        
    elif score == 2:
        print("\nThe password is WEAK.")
        print("\nTWO of the conditions are met:\n\tNo Spaces\n\tDigits\n\tUpper Case Letters AND Lower Case Letters\n\tSpecial characters [%, #, $, @, !, *, &]")
    
    # A score of 2 is weak.
    
    elif score == 3:
        print("\nThe password is STRONG.")
        print("\nTHREE of the conditions are met:\n\tNo Spaces\n\tDigits\n\tUpper Case Letters AND Lower Case Letters\n\tSpecial characters [%, #, $, @, !, *, &]")
        
    # A score of 3 is strong.

    elif score == 4:
        print("\nThe password is VERY STRONG.")
        print("\nFOUR of the conditions are met:\n\tNo Spaces\n\tDigits\n\tUpper Case Letters AND Lower Case Letters\n\tSpecial characters [%, #, $, @, !, *, &]")
        
    # A score of 4 is very strong.
    
    while True:
        
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
        print("\nThank you for using the password checker program!")
        break
    
    # If the selection is no, we thank the user and exit the main loop.