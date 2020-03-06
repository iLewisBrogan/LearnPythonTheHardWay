#  Weekly Recap 06/03/2020
#  Trying to write as much of the code i've learned through the week without looking at my notes

date = '06/03/2020'
name = 'Lewis'
recap_week = '01'

print(f"My name is {name}, the date is: {date} and this is week {recap_week} of the recap.")

#  Next i will show knowledge of input()
#  end= ' ' puts the answer on the same line from the input()
print("What is your name?", end=' ')
nameInput = input()
print("Date?", end=' ')
dateInput = input()
print("Recap week?", end=' ')
recap_week_input = input()

print(f"Your name is: {nameInput}, the date is: {dateInput} and the week of the recap is: {recap_week_input}")