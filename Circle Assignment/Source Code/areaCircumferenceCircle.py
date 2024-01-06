# Afraz Akram
# March 23, 2023
# ICS4U
# Mr. Manyanga
# Version 1.0
# This program will prompt the user to enter the radius of
# a circle. It will be processed using math and the output
# will be the circumference and area of the circle. The
# user can use the program again until they do not want
# to anymore.

# Import the math function to use pi.

import math

print("\nHello user, welcome to the area and circumference calculator!")

# Everything in this loop will be executed back to back until the user does not want to.

while True:

    # Prompt the user to enter the radius of the circle.

    radius = input("\nEnter the radius of the circle: ")
    
    # If the value is not valid.

    try:
        radius = float(radius)
        
    except ValueError:
        
        print("\nPlease enter a valid value: ")
        
        continue
    
    # If the value is not valid.
    
    if radius <= 0:
        
        print("\nRadius must be greater than 0.")
        
        continue
        
    else:
        
        pass
    
    # Calculate area and circumference.
    
    circumference = round((2 * math.pi * radius), 2)
    
    area = round((math.pi * radius * radius), 2)
    
    # Print output.
    
    print(f"\nThe circumference of the circle is {circumference} units.")
    
    print(f"\nThe area of the circle is {area} square units.")
    
    while True:
        
    # This loop is when the user enters a selection.

        userSelection2 = input("\nWould you like to use the calculator again?\n\n\tY) Yes\n\tN) No\n\nEnter here: ")
        
        # We prompt the user if they want to use the calculator again.
  
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
        print("\nThank you for using the program!")
        break
    
    # If the selection is no, we thank the user and exit the main loop.