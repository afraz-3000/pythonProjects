# Afraz Akram
# April 8, 2023
# ICS4U
# Mr Manyanga

# This is a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.

end1 = 0 # Initialize the counter

for i in range(1, 101):
    j = i ** 2 # Square the numbers
    j = str(j) # Convert to string
    j = j[-1] # Get the last character
    j = int(j) # Convert to integer
    if j == 1: # Adds 1 to the counter if ends in 1
        end1 = end1 + 1
        
print(f"There are {end1} numbers between 1 and 100 whose squares end in 1.") # Print statement