# This program reads 10 character account number 
# and outputs the account number with only the last 4 digits showing 
# and the first 6 digits replaced with Xs
# Author: Tanya San Juan

account_number = input ('Please enter an 10 digit account number: ')

print (f'XXXXXX{account_number[6:]}')