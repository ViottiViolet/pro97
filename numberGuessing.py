import random

int = random.randint(1, 9)
chances = 0

while chances < 5:
    guess = input("guess a number from 1 to 9")
    if guess == int:
        print("correct")
        print("congradulations")
        break
    else:
        print("wrong")
    chances += 1

if not chances < 5:
    print("you lost. the number was " + int)