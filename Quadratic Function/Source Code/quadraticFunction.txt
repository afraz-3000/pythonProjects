# Afraz Akram
# April 1 2023
# ICS4U
# Mr Manyanga
# Version 1.0
# This program will find the roots of a quadratic equation. It will first
# prompt the user to enter the a, b, and c values. Then, a function will be
# defined with parameters of a, b, and c to find the roots. The output will
# be the values of the roots and the type of quadtratic.

# Need square root function

import math

# Define the function

def quadroots(a, b, c):
    
    dis = (b ** 2) - (4 * a * c)
    
    # If 2 solutions
    
    if dis > 0:
        
        r1 = round((((-1 * b) + (math.sqrt(dis))) / (2 * a)), 2)
        
        r2 = round((((-1 * b) - (math.sqrt(dis))) / (2 * a)), 2)
        
        print(f"\nThere are two real roots to this function: {r1} and {r2}")
    
    # If 1 solution
    
    elif dis == 0:
        
        r = round(((-1 * b) / (2 * a)), 2)
        
        print(f"\nThere is one real root to this function: {r}")
    
    # If no solutions
    
    else:
        
        print("\nThere are no real roots to this function.")

print("\nHello user, welcome to the quadratic formula calculator!")

while True:
    
    # Prompt for a value
    
    aVal = input("\nEnter the a value of the quadratic equation: ")
    
    try:
        
        aVal = float(aVal)
    
    except ValueError:
        
        print("\nPlease enter a valid value.")
        
        continue
    
    if aVal == 0:
        
        print("\nYour a value can not be 0, as this is not a quadratic.")
        
        continue
    
    # Prompt for b value
    
    bVal = 0
    
    while True:
        
        bVal = input("\nEnter the b value of the quadratic equation: ")
        
        try:
            
            bVal = float(bVal)
        
        except ValueError:
            
            print("\nPlease enter a valid value.")
            
            continue
        
        else:
            
            break
    
    # Prompt for c value
    
    cVal = 0
    
    while True:
        
        cVal = input("\nEnter the c value of the quadratic equation: ")
        
        try:
            
            cVal = float(cVal)
        
        except ValueError:
            
            print("\nPlease enter a valid value.")
            
            continue
        
        else:
            
            break
        
    quadroots(aVal, bVal, cVal)
    
    while True:
        
    # This loop is when the user enters a selection.

        userSelection2 = input("\nWould you like to use the calculator again?\n\n\tY) Yes\n\tN) No\n\nEnter here: ")
        
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
        print("\nThank you for using the quadratic formula calculator!")
        break
    
    # If the selection is no, we thank the user and exit the main loop.