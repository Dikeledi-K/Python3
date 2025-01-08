name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")
# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")


"""
Try to write some variables that convert the inches and pounds to centimeters and kilograms.
Do not just type in the measurements. Work out the math in Python.
"""

# Conversion factors

# 1 inch equals 2.54 centimeters
inches_to_cm = 2.54  

# 1 pound equals 0.453592 kilograms
pounds_to_kg = 0.453592  

# Example variables
height_in_inches = 68 

 # Example: height in inches
# Example: weight in pounds
weight_in_pounds = 150  

# Convert to metric units
height_in_cm = height_in_inches * inches_to_cm
weight_in_kg = weight_in_pounds * pounds_to_kg

# Print the results
print(f"Height in centimeters: {height_in_cm:.2f} cm")
print(f"Weight in kilograms: {weight_in_kg:.2f} kg")
