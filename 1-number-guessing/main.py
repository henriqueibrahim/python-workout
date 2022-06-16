# Number guessing game
import random

def guessing_game():
    number = random.randint(1, 100)

    while True:
        userNumber = int(input("Guess a number between 1 and 100: "))
        if userNumber == number:
            print("Just right!")
            break
        if userNumber > number:
            print("Too high!")
        else:
            print("Too low!")


guessing_game()
