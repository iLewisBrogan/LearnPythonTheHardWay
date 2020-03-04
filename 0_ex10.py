#  Exercise 10: What Was That?
#  \t creates a tab
tabby_cat = "\tI'm tabbed in."
#  \n creates a new line
persian_cat = "I'm split\non a line."
#  only one of \\'s get shown
backslash_cat = "I'm \\ a \\ cat."

#  \n\t creates a new line, and indents with a tab
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)