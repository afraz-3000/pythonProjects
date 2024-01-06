# Afraz Akram
# March 3 2023
# ICS4U
# Mr. Manyanga
# Version 1.0

''' This program will prompt the user to enter a value of the mass of a
letter to be mailed. The input will be processed by using conditional
statements and logical operations. The output will display the price of
mailing the letter. The program can be used again until the user decides
not to.'''

print("Welcome to Rahmania! Here, the cost of mailing a letter depends on the mass.")

# We give our greetings to the user and tell them what the program is.

while True:

# Every process inside this loop will happen until the user decides to stop using the program.

    mass = 0

    while True:
        
    # This loop is when the user enters a value.

        mass = input("\nEnter the mass of your letter (g): ")
        
        # The user enters their value in a string variable.

        try:
            
            mass = float(mass)
            
            break
        
        # If the conversion from string to float is successful, we exit the inner loop.

        except ValueError:
            
            print("\nPlease enter a valid mass.")
            
            continue
        
        # If the conversion from string to float is not successful, we prompt the user to reenter a valid value.
        
    if mass <= 0:
        
        print("\nPlease enter a valid mass.")
        
        continue
    
    # Mass needs to be non-negative, so if it is not, the user has to reenter the value. 
    
    elif mass > 0 and mass <= 30:
        
        print("\nThe cost of mailing your letter is 40 sinas.")
        
    # It costs 40 sinas for up to 30 g.
        
    elif mass > 30 and mass <= 50:
        
        print("\nThe cost of mailing your letter is 55 sinas.")
    
    # It costs 55 sinas over 30 g up to 50 g.
    
    elif mass > 50 and mass <= 100:
        
        print("\nThe cost of mailing your letter is 70 sinas.")
    
    # It costs 70 sinas over 50 g up to 100 g.
    
    elif mass > 100:
        
        massAdd = mass - 100
        
        i = (massAdd // 50) + 1

        if massAdd < 50:
            
            i = 1

        elif massAdd % 50 == 0:
            
            i = i - 1
    
        else:
            
            pass

        price = int((25 * i) + 70)
        
        print(f"\nThe cost of mailing your letter is {price} sinas.")
    
    # If the letter is over 100 g, it costs 70 sinas plus an additional 25 sinas for each additional 50 g (or part thereof).
    
    while True:
        
    # This loop is when the user enters a selection.

        userSelection2 = input("\nWould you like to use the program again?\n\n\tY) Yes\n\tN) No\n\nEnter here: ")
        
        # We prompt the user if they want to use the program again.
  
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
        
        print("\nThank you for using the mailing program!")
        
        break
    
    # If the selection is no, we thank the user and exit the main loop.