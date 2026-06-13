number = int(input("What is your favorite number? "))

if number % 2 == 0:
    print(f"{number} is even!")
elif number % 2 != 0 and number > 0:
    print(f"{number} is odd and positive!")
elif number == 0:
    print("You entered 0!")
elif number % 2 != 0 and number < 0:
    print(f"{number} is negative!")

