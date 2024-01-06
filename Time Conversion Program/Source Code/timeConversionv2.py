# Afraz Akram
# February 18 2023
# ICS4U
# Mr. Manyanga
# Version 2.0

''' This program will prompt the user to enter a value of time, as
well as the unit of time in either seconds, minutes, or hours. The
input will be processed by being multiplied by conversion factors. 
Whatever unit the user decided, the output will display the value in the
other two values. The program can be used again until the user decides
not to.'''

print("Hello user, welcome to the time conversion program!")

# We give our greetings to the user and tell them what the program is.

i = 0

# We set a variable, i, to 0 so that the while loop can be ran.

while i == 0:

# Every process inside this loop will happen until the user decides to stop using the program.
  
    userSelection1 = input("\nEnter the units of your time that you will like to convert:\n\n\tA) Seconds\n\tB) Minutes\n\tC) Hours\n\nEnter here: ")

    # The user can decide the units of their time, by entering a letter for their selection.
  
    if userSelection1.upper() != "A" and userSelection1.upper() != "B" and userSelection1.upper() != "C":
        print ("\nPlease enter a valid selection.")
        continue

    # Even if the user enters a lower case letter, the .upper() function will take care of it. If the selection is not valid, the user will be prompted again.

    userValueFloat = 0
    
    # We create a float variable that the user's value can be stored in. 

    while i == 0:
        
    # This loop is when the user enters a value.

        userValueString = input("\nEnter the value of time: ")
        
        # The user enters their value in a string variable.

        try:
            userValueFloat = float(userValueString)
            break
        
        # If the conversion from string to float is successful, we exit the inner loop.

        except ValueError:
            print("\nPlease enter a valid value.")
            continue
        
        # If the conversion from string to float is not successful, we prompt the user to reenter a valid value.
          
    if userSelection1 == "A" or userSelection1 == "a":
        print("\nYour time in minutes is: ", round((userValueFloat / 60), 3))
        print("Your time in hours is: ", round((userValueFloat / 3600), 3))
      
    # If the units of the user's value is in seconds, then the value will be converted and displayed in minutes and hours.

    elif userSelection1 == "B" or userSelection1 == "b":
        print("\nYour time in seconds is: ", round((userValueFloat * 60), 3))
        print("Your time in hours is: ", round((userValueFloat / 60), 3))
      
    # If the units of the user's value is in minutes, then the value will be converted and displayed in seconds and hours.

    elif userSelection1 == "C" or userSelection1 == "c":
        print("\nYour time in seconds is: ", round((userValueFloat * 3600), 3))
        print("Your time in minutes is: ", round((userValueFloat * 60), 3))
    
    # If the units of the user's value is in hours, then the value will be converted and displayed in seconds and minutes.

    userSelection2 = ""
    
    # We make a string variable in which the user's selection can be stored in.

    while i == 0:
        
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
        print("\nThank you for using the time conversion program!")
        break
    
    # If the selection is no, we thank the user and exit the main loop.