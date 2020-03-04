types_of_people = 10
#  prints out {types_of_people} in the {} which in this case is 10
x = f"There are {types_of_people} types of people."

#  binary variable is the string "binary" do_not is the string "don't"
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#  prints x
print(x)
#  prints y
print(y)

#  prints x in {x}
print(f"I said: {x}")
#  prints y in {y}
print(f"I also said: {y}")

#  boolean value hilarious is False
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#  prints hilarious inside {}
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

#  this makes a longer string because it prints w + e into a single line of string
print(w + e)
