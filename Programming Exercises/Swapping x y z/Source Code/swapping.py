# Afraz Akram
# April 8, 2023
# ICS4U
# Mr Manyanga
# This program will prompt the user to enter variables named x, y, and z.
# The input will be processed such that x gets the value of y, y gets the
# value of z, and z gets the value of x. These new variables will be printed.

x = input("Enter value of x: ") # Input x
y = input("Enter value of y: ") # Input y
z = input("Enter value of z: ") # Input z

print(f"The original value of x is {x}") # Print x
print(f"The original value of y is {y}") # Print y
print(f"The original value of z is {z}") # Print z

tempx = x # Store x in temporary variable
tempy = y # Store y in temporary variable
tempz = z # Store z in temporary variable

x = tempy # x gets y value
y = tempz # y gets z value
z = tempx # z gets x value

print(f"The new value of x is {x}")
print(f"The new value of y is {y}")
print(f"The new value of z is {z}")