# Parameters, Unpacking and Variables

""" This is how you add features to your script from the Python feature set
This keeps your programs small, but it also acts as documentation for other programmers who read your
code later.
"""
from sys import argv
# read the WYSS section for how to run this

script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)