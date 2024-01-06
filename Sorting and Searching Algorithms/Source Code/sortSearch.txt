# Afraz Akram
# March 16 2023
# ICS4U
# Version 1.0
# This program will generate a random array using the random function.
# It will use sort the array using insertion sort, then find a certain
# item using linear search. The outputs will be each pass, the indices
# of the elements found, and the runtimes. 

# Import the random function to create a random array.

import random

# Import time to calculate runtime. 

import time

# Name of the array.

myArray = []

# Randomize the size of the array.

arraySize = random.randint(10, 21)

# So the while loop can run.

j = 0

# Randomize the elements in the array.

while j < arraySize:
    
    myArray.append(random.randint(-10, 50))
    
    j = j + 1

# Display this array.

print(f"This is a randomly generated array: \n{myArray}")

print("\nWe will use insertion sort to sort this array.")

# Timestamp start of insertion sort. 

timestamp1 = time.time()

for k in range(1, len(myArray)):
    
    # The elements that are greater than key will be moved one positon ahead of the current position. 
    
    key = myArray[k]
    
    l = k - 1
    
    while l >= 0 and key < myArray[l]:
        
        myArray[l + 1] = myArray[l]
        
        l -= 1
    
    myArray[l + 1] = key
    
    print(f"\nPass: {myArray}")

# Timestamp end of insertion sort.

timestamp2 = time.time()

# Display sorted array. 

print(f"\nNow we have the sorted array, thanks to insertion sort:\n{myArray}")

# Display runtime of insertion sort.

print(f"\nThe runtime for the insertion sort was {timestamp2 - timestamp1}.")

# Select a random element from the list to find using linear search. 

findElement = myArray[random.randint(0, (len(myArray)) - 1)]

print(f"\nLet's now find the element {findElement} using linear search.")

# Timestamp start of linear search.

timestamp3 = time.time()

for m in range(0, (len(myArray))):
    
    if myArray[m] == findElement:
        
        print(f"\nElement found at index {m}!")
    
    else:
        
        print(f"\nElement not found at index {m}.")
        
# Timestamp end of linear search.

timestamp4 = time.time()

# Display runtime of linear search.

print(f"\nThe runtime for the linear search was {timestamp4 - timestamp3}.")