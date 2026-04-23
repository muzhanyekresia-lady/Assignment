

import random


secret_number = random.randint(1, 100)
#  random.randint means selection of whole number(integers)
attempts = 0
guess = None

print(" Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print("Can you guess it?\n")


while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print("\n Congratulations! You guessed the number!")
        print(f"It took you {attempts} attempts.")

        