# This is my first Python program
# I am just checking the syntax and testing stuff as an introduction

# variables
fullName = "dear reader"
age = 35
gpa = 3.2
isStudent = False # need to be capitalized

# user f string to insert the variable
print(f'Hello {fullName}')
print(f'Your are {age} years old')
print(f'Your GPA is {gpa}')

# if statement
if isStudent:
    print('You are a student')
else:
    print('You are NOT a student')

# get the type of variable
print(type(gpa)) # return <class 'float'>

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)
