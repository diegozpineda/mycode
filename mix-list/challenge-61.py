#!/usr/bin/env python3
#
#
import random

wordbank= ["indentation", "spaces"]
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

# Part 3
wordbank.append(4)

# Part 4
num = int(input("Please enter a number between 0 and 20: "))

# Part 5

student_name = tlgstudents[num]

# Part 6
print(f'{student_name} always uses {wordbank[2]} {wordbank[1]} to indent')

# Bonus 1

print(f'Using ranom.range to pick a random student name...')
random_number = random.randrange(0, len(tlgstudents))
student_name = tlgstudents[random_number]
print(f'{student_name} always uses {wordbank[2]} {wordbank[1]} to indent')

# Bonus 2
