# Reading Files

# From a module sys I am importing arguments
from sys import argv

# Import the argv module from the sys library to handle command-line arguments
script, filename = argv  

# Open the file specified by the 'filename' variable and assign the file object to 'txt'
txt = open(filename)

# Print a message showing the name of the file being read
print(f"Here's your file {filename}:")

# Read the contents of the file object 'txt' and print it to the console
print(txt.read())

# Prompt the user to type the filename again for a second access
print("Type the filename again:")

# Take input from the user for the file name and assign it to 'file_again'
file_again = input("> ")

# Open the file specified by 'file_again' and assign the file object to 'txt_again'
txt_again = open(file_again)

# Read the contents of 'txt_again' and print it to the console
print(txt_again.read())
