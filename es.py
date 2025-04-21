# This program reads in a text file and outputs the number of e's it contains.
# The program should take the file name from an argument on the command line.
# Author: Tanya San Juan

# Introduction:
# Command line in python is a way to pass arguments to the script when it's run.
# Sys is a module in Python that provides functions and variables in the system.
# The sys.argv list contains the command line arguments passed to the script.

# Sources: 
# https://docs.python.org/3/using/cmdline.html
# https://docs.python.org/3/library/sys.html#sys.argv
# https://docs.python.org/3/library/fileinput.html#module-fileinput
# https://docs.python.org/3/library/functions.html#open


# Promgram:
# The first step of the program is to import the sys module. 
# Sys module provides access to some variables used or maintained by the interpreter 
# and to functions that interact with the interpreter. 

import sys
#filename = "moby-dick.txt"

# The second step is to check if the user has provided a filename as a command line argument.
# If the user has provided a filename, the program will proceed to the next step.
# The first argument is the file name and the second argument is the mode in which the file is opened.
# If the user didn't provide a filename, the program will print a usage message and exit.
# The sys.exit() function is used to exit the program with a specified exit status.

if len(sys.argv) != 2:
    sys.exit("Usage: python script.py <filename>")

filename = sys.argv[1]
# The third step is to open the file in read mode.

try:
    with open(filename, 'r') as f:
        # The program will read the contents of the file and count the number of e's in it.
        # The read() method reads the entire contents of the file into a string.
        contents = f.read()
        # The program will print the number of e's in the file.
        print(contents)
except FileNotFoundError:
    # If the file does not exist, the program will print an error message and exit.
    sys.stderr.write(f"Error: {filename} not found.")

    sys.exit(1)
# The program will print the number of e's in the file.



