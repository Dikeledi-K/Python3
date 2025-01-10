# Reading and Writing Files

# Import the 'argv' module from the 'sys' library to handle command-line arguments
from sys import argv

# Unpack command-line arguments into 'script' and 'filename' variables
script, filename = argv

# Inform the user that the file specified by 'filename' will be erased
print(f"We're going to erase {filename}.")

# Warn the user about the option to cancel the operation using CTRL-C
print("If you don't want that, hit CTRL-C (^C).")

# Give the user the option to proceed by hitting RETURN
print("If you do want that, hit RETURN.")

# Wait for user input to proceed; this acts as a pause for confirmation
input("?")

# Inform the user that the file is being opened
print("Opening the file...")

# Open the file in write mode ('w'), which also truncates the file if it exists
target = open(filename, 'w')

# Announce that the file is being truncated (emptied of content)
print("Truncating the file.")
target.truncate()  # Optional, as opening in 'w' mode already truncates the file

# Say goodbye to the current content of the file
print("Goodbye!")

# Let the user know they will be prompted to enter three lines of text
print("Now I'm going to ask you for three lines.")

# Prompt the user for three lines of input and store them in variables
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Inform the user that the lines will be written to the file
print("I'm going to write these to the file.")

# Write the first line to the file followed by a newline character
target.write(line1)
target.write("\n")

# Write the second line to the file followed by a newline character
target.write(line2)
target.write("\n")

# Write the third line to the file followed by a newline character
target.write(line3)
target.write("\n")

# Inform the user that the file is being closed
print("And finally, we close it.")

# Close the file to ensure changes are saved and resources are released
target.close()
