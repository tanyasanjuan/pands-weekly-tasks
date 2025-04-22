# This program asks the user to input any positive integer 
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.
# Author: Tanya San Juan

# Ask the user to input any positive integer
i = int(input("Please enter a positive integer: "))

# Output the successive values of the following calculation
while i != 1:
    print (i , end = ' ')
    if i % 2 == 0:
        i = i // 2
    else:
        i = i * 3 + 1

# the end parameter in the print() function specifies what should be printed 
# at the end of the output instead of the default newline.