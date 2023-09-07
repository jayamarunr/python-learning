#assign a variable 10 to types_of_people
types_of_people = 10

#add string to a format and assign it under a new variable X
x = f"There are {types_of_people} types of people."

#add string binary and do_not as a variable
binary = "binary"
do_not = "don't"

#add string to format and assign it under Y variable
y = f"Those who know {binary} and those who {do_not}."

#print x
print(x)

#print y
print(y)

#print x and y under format
print(f"I said: {x}")
print(f"I also said: '{y}'")

#add a boolean False to a variable called Hilarious
hilarious = False

#assign a string under joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"

#evaluate the expression with hilarious value assigned in previous step.
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)