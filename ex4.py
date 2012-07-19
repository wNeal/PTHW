# Number of cars
cars = 100
# The amount of space inside each car
space_in_a_car = 4.0
# Number of total available drivers
drivers = 30
# Number of total passengers
passengers = 90
# Number of extra cars
cars_not_driven = cars - drivers
# Number of cars that are assigned to a driver
cars_driven = drivers
# Max number of passengers
carpool_capacity = cars_driven * space_in_a_car
# Average number of passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

"""
Extra Credit 1.
The reason a NameError was thrown, was because the variable name used on line 8 was not defined before it was used in the code.
The solution is to change the name reference on line * to carpool_capacity or change the variable name on line 7 to car_pool_capacity

Extra Credit 1.2: I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
The use of floating point numbers effects the results on line 7 when it is used in the arthmetic. In this example the only difference is
that the number output will be followed by .0 when the float is used or it will be followed by nothing when an integer is used

Extra Credit 2: Remember that 4.0 is a "floating point" number. Find out what that means.
A floating point number is a more precise number than an integer. It allows the programmer to use numbers with decimal points in the code
instead of having to rely soley on whole numbers

Extra Credit 3: Write comments above each of the variable assignments.

Extra Credit 4: Make sure you know what = is called (equals) and that it's making names for things.

Extra Credit 5: Remember _ is an underscore character.

Extra Credit 6: Try running python as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.
"""
