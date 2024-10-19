age = int(input('Enter your age: '))

if age >= 18:
    print('You are an adult')
elif age < 0:
    print("You haven't been born yet")
elif age == 0:
    print("You were just born")
else:
    print('You are a child')
