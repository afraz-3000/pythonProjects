# Afraz Akram
# April 8, 2023
# ICS4U
# Mr Manyanga
''' This program will ask the user to enter 10 test scores. It will
(a) Print out the highest and lowest scores.
(b) Print out the average of the scores.
(c) Print out the second largest score.
(d) If any of the scores is greater than 100, then after all the scores
have been entered, print a message warning the user that a value over 100
has been entered.
(e) Drop the two lowest scores and print out the average of the rest of them.'''

print("Welcome to the test score calcuator program!") # Greeting

while True: # So the program can run again
    testscores = [] # Make a list of test scores
    over100 = False # Initialize the over 100 score variable
    i = 1 # Make i = 1
    while i <= 10: # So 10 scores can ebe entered
        score = input(f"Enter test score {i}: ")
        try:        
            score = float(score)        
        except ValueError:        
            print("Please enter a valid value.") # If input not valid        
            continue
        if score < 0:
            print("Please enter a non-negative score.") # if Score negative
            continue
        if score > 100:
            over100 = True # If score over 100
        testscores.append(score)
        i = i + 1
    if over100 == True:
        print("Warning! A test score of over 100 has been entered.") # If score over 100
    testscores.sort()
    print(f"The highest score is {testscores[9]}") # Highest score
    print(f"The lowest score is {testscores[0]}") # Lowest score
    print(f"The second highest score is {testscores[8]}") # Second highest score
    k = 0
    for l in testscores:
        k = k + l
    average = round((k / 10), 1) # Calculate average
    print(f"The average of all 10 scores is {average}")
    testscores = testscores[2:10]
    m = 0
    for n in testscores:
        m = m + n
    average = round((m / 8), 1) # Calculate top 8 average
    print(f"The average of the top 8 scores is {average}")
    
    while True: # If user wants to use again
        userSelection2 = input("\nWould you like to use the program again?\n\n\tY) Yes\n\tN) No\n\nEnter here: ")  
        if userSelection2.upper() != "Y" and userSelection2.upper() != "N":
            print("\nPlease enter a valid selection.")
            continue
        elif userSelection2.upper() == "Y" or userSelection2.upper() == "N":
            break
    if userSelection2.upper() == "Y":
        continue
    elif userSelection2.upper() == "N":
        print("\nThank you for using the program!")
        break