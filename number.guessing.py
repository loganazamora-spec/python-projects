import random

number = random.randint(1, 10)
user_guess = int(input("Guess a number from 1-10: "))

while user_guess != number:
    if user_guess < number:
        print("Too low! Try again.")
    elif user_guess > number:
        print("Too high! Try again.")
    user_guess = int(input("Guess a number from 1-10: "))
print(f"You got it! The number was {number}!")

