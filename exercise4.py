# Assigning a variable cars to a value 100
cars = 100

# ASsigning a variable space_in_car to a value 4.0
space_in_a_car = 4.0

# Assigning a variable drivers to a value 30
drivers = 30

# Assigning a variable passngers to a value 90
passengers = 90

# Assigning a variable cars_not_deriven to the difference of cars and drivers
cars_not_driven = cars - drivers

# Equatig cars_driven to drivers
cars_driven = drivers

# Assigning a variable carpool_capacity to the product of cars driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car

# Assigning the variable avarage_passengers_per_car to passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven


# Displaying the number of cars that available
print("There are", cars, "cars available.")

# Displaying the number of drivers that are available
print("There are only", drivers, "drivers available.")

# Displaying the number of cars that will not be driven
print("There will be", cars_not_driven, "empty cars today.")

# Displaying the number of people that can be transported today
print("We can transport", carpool_capacity, "people today.")

# Displaying the current number of passengers to be transported today
print("We have", passengers, "to carpool today.")

#Displaying  the avarage number of passengers that should be put in each car
print("We need to put about", average_passengers_per_car, "in each car.")