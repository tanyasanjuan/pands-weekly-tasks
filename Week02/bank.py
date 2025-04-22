# bank.py
# This program prompts the user and read in two money amounts, in cent, 
# The second part of the program print the amount with a euro sign and decimal point between the euro and cent of the amount. 
# author: Tanya San Juan

# Promting the user for two money amounts in cent 
amount1 = int (input ("Enter amount1 (in cents): "))
amount2 = int (input ("Enter amount2 (in cents): "))

# Convert amount in euros. I guide myself with ChatGPT (to get the number in decimals and not get 65.00 and 180.00).
amount1euros = amount1 / 100
amount2euros = amount2 /100

# Printing the values 
print (f"Enter amount1 (in cents): €{amount1euros: .2f}")
print (f"Enter amount 2 (in cents): €{amount2euros: .2f}")

# Sum the two values, display in euros. Guide by https://www.w3schools.com/python/trypython.asp?filename=demo_fstring_operation2
print (f"The sum of these is: € {amount2euros + amount1euros: .2f}")
