#  Exercise 15. Reading Files
#  Line 1-3 use argv to get a filename
from sys import argv

script, filename = argv
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

#  close the opened file
txt.close()

# print("Type the filename again:")
# # file_again = input("> ")
# #
# # txt_again = open(file_again)
# #
# # print(txt_again.read())