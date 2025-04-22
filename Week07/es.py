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

# The second step is to check if the user has provided a filename as a command line argument.
# If the user has provided a filename, the program will proceed to the next step.
# If the user didn't provide a filename, the program will print a usage message and exit.
# The sys.exit() function is used to exit the program with a specified exit status.

if len(sys.argv) != 2:
    sys.exit("Usage: python moby-dick.txt <filename>")

filename = sys.argv[1]

# The third step is to open the file in read mode.
# The function will read the contents of the file and count the number of 'e' s in it.
try:
    with open(filename, 'r') as f:
        contents = f.read()
        e_count = contents.count('e')
        print (f'The number of "e"s in this file is: {e_count}')
except FileNotFoundError:
    print(f"File {filename} not found.")
    sys.exit(1)

# To excecute the program in the terminal, should be the next way: python es.py moby-dick.txt