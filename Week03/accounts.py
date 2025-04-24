# This program reads 10 character account number 
# and outputs the account number with only the last 4 digits showing 
# and the first 6 digits replaced with Xs
# Author: Tanya San Juan
'''
# Request the user to enter a 10 digit account number
# The variable account_number storage the infomation provided by the user as a string.
account_number = input ('Please enter a 10 digit account number: ')

# f-string is used to insert a variable in a string. 
# the text "XXXXXX" are the first 6 hidden numbers.
# To leave out the start index, we can 'slice strings'.  
# {account_number[6:]} Take from the initial number to the 6th and replace them with Xs
print (f'XXXXXX{account_number[6:]}')
'''
# Program modified to deal with account numbers of any length:
# The user can input a number longer than 10 digits. 
# The user can input a number smaller than 10 digits, for example only 1 digit
# To solve the problem we can use negative indexing, to start the slice from the end of the string
account_number = input ('Please enter a 10 digit account number: ')
print (f'XXXXXX{account_number[-4:]}')

# However if the user input a number of 4 digits or smaller, the program will show the number entered.

#Source: https://www.w3schools.com/python/python_strings_slicing.asp