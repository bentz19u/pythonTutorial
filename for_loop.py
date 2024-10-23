# first value is inclusive
# second value is exclusive
# third is just the number added at each loop

import time

for i in range(1, 11, 2):
    print(i)

name = "Toto"

for letter in name:
    # second parameter concat each letter with it
    print(letter, end=" ")

# iterate backward for a countdown
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print("Happy New Year!")

