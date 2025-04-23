# This program asks the user to input any positive integer 
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one.
# Have the program end if the current value is 1.
# Author: Tanya San Juan

# Ask the user to input any positive integer
# input() returns a string
# int() convert the string in a integer
# i, is the variable that stores the number.
i = int(input("Please enter a positive integer: "))

# With the while loop we can execute a set of statements as long as a condition is true.
# While loop, will be repated until 'i' is different to 1 

while i != 1:
    # print the actual value of i.
    # (end = ''), makes the numbers to be in the same line, separate by spaces ( )
    print (i , end = ' ')
    # check if the number is even.
    # if 'i' can divided by 2m then is even. 
    # '%' is the remainder of the division, if the remainder is 0 then 'i' is even.
    # if the number is even, the number is divided by 2 using // 
    if i % 2 == 0:
        i = i // 2
    # if the number is odd, then take the number multiply it by 3 abd then sum + 1.    
    else:
        i = i * 3 + 1
 
# Sources:
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.datacamp.com/tutorial/loops-python-tutorial