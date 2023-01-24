import random
from random import randint

los = random.randint(1, 100)
result = -1
x = 0

while result != los:
    try:
        x += 1
        result = int(input("Hi user, guess the number from 0 to 100: "))
    except ValueError:
        print("It's not a number!")
        continue
    if result > los:
        print("To big!")
    elif result < los:
        print("To small!")
    if result == los:
        print("You win!")

