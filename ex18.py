#  Exercise 18. Names, Variables, Code, Function

#  this one is like the scripts with argv
#  First we tell Python we want to make a func using def for "define"
#  on the same line as def, we give the func a name "print_two"
#  we tell it we want *args (like argv parameter but for funcs)

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#  *args is pointless, we can just do this:
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#  this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#  this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Lewis","Brogan")
print_two_again("Lewis","Brogan")
print_one("First!")
print_none()