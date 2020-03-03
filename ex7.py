#  using the .format the strings will get printed in the format "{} {} {} {}"
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
#  this prints the formatter variable {} {} {} {} 4 times on the same line
print(formatter.format(formatter, formatter, formatter, formatter))
#  prints each string inside "" in each {}
print(formatter.format(
    "try your",
    "own text here",
    "maybe a poem",
    "or a song about fear"
))

#  takes the formatter string defined in line 1,
#  calls its .format function
#  pass to .format four arugments, which match up to the four {} in the formatter variable
#  result of calling format on formatter is a new string has the {} replaced with the four variable
#  prints