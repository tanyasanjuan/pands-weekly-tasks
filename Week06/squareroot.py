# This program defines a function takes a positive floating-point number as input 
# and returns the square root of that number using the Newton-Raphson method.
# Author: Tanya San Juan

# The Newton-Raphson method is an iterative numerical method used to find the roots of a function.
# Source: https://en.wikipedia.org/wiki/Newton%27s_method

# The function starts with an initial guess for the square root, which is half of the input number.
# It then iteratively refines this guess using the formula:
# x = (x + n / x) / 2

def square_root(num):
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

        # return prev_guess: This line was deleted, to reach the presition required in the task.
        

#main program
number = float(input("Enter a positive number to find its square root: "))
# Check if the number is negative, if the user enter a negative number, the program will ask for a positive number.
if number < 0:  
        print("Please enter a positive floating number:")
else:
    result = square_root(number)
    print(f"The square root of {number} is approx {round(result,1)}.")


# Added 'round' to the print statement to limit the number of decimal places displayed.
# The result is rounded to one decimal place for better readability.

#Sources:
#https://www.geeksforgeeks.org/newton-raphson-method/
#https://calcworkshop.com/derivatives/newtons-method/
#https://www.datacamp.com/tutorial/python-square
#https://www.w3resource.com/python-exercises/python-functions-exercises.php
#https://docs.python.org/3/library/math.html#math.sqrt