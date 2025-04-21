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
FILENAME = sys.argv[1]
