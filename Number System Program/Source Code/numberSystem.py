# Afraz Akram
# March 24, 2023
# ICS4U
# Version 2.0
# Mr. Manyanga
# This program involves four number systems: decimal, binary,
# octal, and hexadecimal. It will prompt the user to enter a
# value in ONE number system. By making everything in terms
# of the decimal value, python conversions, and other methods,
# the input will be processed to produce an output of the
# REMAINING THREE number systems.

# Greet the user

print("Hello user, welcome to the number system conversion program.")

# Everything in the loop will run until the user says not to

while True:
    
    # User selects the number system to convert from
    
    userSelection1 = input("\nEnter the system you would like to convert FROM.\n\n\tD) Decimal\n\tB) Binary\n\tO) Octal\n\tH) Hexadecimal\n\nEnter here: ")
    
    # For when user does invalid selection
    
    if userSelection1.upper() != "D" and userSelection1.upper() != "B" and userSelection1.upper() != "O" and userSelection1.upper() != "H":
        print("\nPlease enter a valid selection.")
        continue
    
    else:
        pass
    
    # From decimal to others
    
    if userSelection1.upper() == "D":
        
        userValue = 0
        
        # Get valid decimal value
        
        while True:
        
            userValue = input("\nEnter the decimal value: ")
        
            try:
                
                userValue = int(userValue)
                
            except ValueError:
                
                print("\nPlease enter a valid value.")
                
                continue
            
            else:
                
                break
        
        # Convert
        
        binValue = str(bin(userValue))[2:]
        
        octValue = str(oct(userValue))[2:]
        
        hexValue = str(hex(userValue))[2:]
        
        # Output
        
        print(f"\nThe binary value is: {binValue}")
        
        print(f"\nThe octal value is: {octValue}")
        
        print(f"\nThe hexadecimal value is: {hexValue}")
    
    # From binary to others
    
    elif userSelection1.upper() == "B":
        
        decValue = 0
        
        # Get valid decimal value
        
        while True:
        
            userValue = input("\nEnter the binary value: ")
        
            try:
            
                decValue = int(userValue, 2)
            
            except ValueError:
                
                print("\nPlease enter a valid value.")
                
                continue
            
            else:
                
                break
        
        # Convert
        
        octValue = str(oct(decValue))[2:]
        
        hexValue = str(hex(decValue))[2:]
        
        # Output
        
        print(f"\nThe decimal value is: {decValue}")
        
        print(f"\nThe octal value is: {octValue}")
        
        print(f"\nThe hexadecimal value is: {hexValue}")
    
    # From octal to others
    
    elif userSelection1.upper() == "O":
        
        decValue = 0
        
        # Get valid decimal value
        
        while True:
        
            userValue = input("\nEnter the octal value: ")
        
            try:
            
                decValue = int(userValue, 8)
            
            except ValueError:
                
                print("\nPlease enter a valid value.")
                
                continue
            
            else:
                
                break
        
        # Convert
        
        binValue = str(bin(decValue))[2:]
        
        hexValue = str(hex(decValue))[2:]
        
        # Output
        
        print(f"\nThe decimal value is: {decValue}")
        
        print(f"\nThe binary value is: {binValue}")
        
        print(f"\nThe hexadecimal value is: {hexValue}")
        
    # From hexadecimal to others
        
    elif userSelection1.upper() == "H":
        
        decValue = 0
        
        # Get valid decimal value
        
        while True:
        
            userValue = input("\nEnter the hexadecimal value: ")
        
            try:
            
                decValue = int(userValue, 16)
            
            except ValueError:
                
                print("\nPlease enter a valid value.")
                
                continue
            
            else:
                
                break
        
        # Convert
        
        binValue = str(bin(decValue))[2:]
        
        octValue = str(oct(decValue))[2:]
        
        # Output
        
        print(f"\nThe decimal value is: {decValue}")
        
        print(f"\nThe binary value is: {binValue}")
        
        print(f"\nThe octal value is: {octValue}")
        
    while True:
        
    # This loop is when the user enters a selection.

        userSelection2 = input("\nWould you like to use the converter again?\n\n\tY) Yes\n\tN) No\n\nEnter here: ")
        
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
        print("\nThank you for using the number system conversion program!")
        break
    
    # If the selection is no, we thank the user and exit the main loop.