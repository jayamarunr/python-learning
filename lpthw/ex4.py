#assigning a variable called cars with value 100
cars = 100
#assign space as 4 inside a car
space_in_a_car = 4.0
#assign 30 as available drivers with a variable called drivers
drivers = 30
#assign 90 as total passengers with a variable called passengers
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

