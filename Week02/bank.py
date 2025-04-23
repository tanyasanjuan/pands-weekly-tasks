# This program prompts the user and read in two money amounts (in cent) 
# adds the two amounts, and prints out the amount with a euro sign
# and decimal point between the euro and cents. 
# author: Tanya San Juan


# The program have to create two variables to assign a value (ammount 1 and 2)
# "int()" function is used to convet an specified value to an integer 'int'
# https://www.w3schools.com/python/ref_func_int.asp
# https://www.w3schools.com/python/python_numbers.asp

# Request the user to enter the two ammounts that have to be sum
# Specify to the user must include amounts including cents.
amount1 = int(input("Enter amount 1 (in cents): "))
amount2 = int(input("Enter amount 2 (in cents): "))

# Convert amount in euros. 
# I guide myself with ChatGPT (to get the number in decimals and not get 65.00 and 180.00).
# https://www.w3schools.com/python/python_operators.asp
amount1euros = amount1 / 100
amount2euros = amount2 /100


# This part of the program sum the two amounts and display the result with decimal.

# The "f-strings" is a way to embed expressions and variables into a string. 
# To round the two decimal places we can use the 2f, that f is the float value and 2 specify the decimals.
# Sum the two values and display in euros. 
print (f"The sum of these is: €{amount1euros + amount2euros:.2f}")


#Sources: 
# https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
# https://www.datacamp.com/es/tutorial/python-round-to-two-decimal-places
# https://www.w3schools.com/python/trypython.asp?filename=demo_fstring_operation2