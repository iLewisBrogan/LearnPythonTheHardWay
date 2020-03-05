#  Exercise 13. Parameters, Unpacking, Variables
#  import, this is how you add features to your script from the Python feature set
#  argv is the "argument variable."
from sys import argv
#  read the WYSS section for how to run this
#  "unpacks" argv so that, rather than holding all the arguments, it gets assigned to four variables.
#  "Take whatever is in 'Argv' unpack it, and assign it to all of these variables on the left in order"
#  correct name for argv is the "import the argv modules"
script, first, second, third = argv

print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#  python ex13.py, putting fewer than free arguments causes an error because theres not enough values
#  to unpack (need 4, got 3 values)