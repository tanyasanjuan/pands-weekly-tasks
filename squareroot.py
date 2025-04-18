# This program defines a function takes a positive floating-point number as input 
# and returns the square root of that number using the Newton-Raphson method.
# Author: Tanya San Juan

# The Newton-Raphson method is an iterative numerical method used to find the roots of a function.
# Source: https://en.wikipedia.org/wiki/Newton%27s_method

# The function starts with an initial guess for the square root, which is half of the input number.
# It then iteratively refines this guess using the formula:
# x = (x + n / x) / 2

def square_root(num):
    # Check if the input is a positive number
    if num < 0:
        print("Please enter a positive floating number:")
    
    # Initialize the guess for the square root
    prev_guess = num / 2.0
    
    # Iterate until the guess converges to the actual square root
    while True:
        # Calculate the next guess using the Newton-Raphson formula
        new_num = (prev_guess + num / prev_guess) / 2.0
        
        # Check for convergence (if the difference is small enough)
        if abs(new_num - prev_guess) < 1e-10:  # Tolerance level
            return new_num
        # Update the previous guess for the next iteration
        prev_guess = new_num
        

#main program
number = float(input("Enter a positive number to find its square root: "))
if number < 0:  # Check if the number is negative
        print("Please enter a positive floating number:")
else:
    result = square_root(number)
    print(f"The square root of {number} is approx {round(result,1)}.")
    
# Deleted line, to reach the presition required in the task: return prev_guess  
# Added round to the print statement to limit the number of decimal places displayed.
# The result is rounded to one decimal place for better readability.