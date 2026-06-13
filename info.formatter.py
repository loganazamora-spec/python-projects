name = input("What's your name? ").strip().title()
favColor = input("What's your favorite color? ").lower()
favNumber = int(input("What's your favorite number? "))
birthYear = int(input("When were you born? "))

print(f"Hi {name}! Your favorite color is {favColor} and your favorite number is {favNumber}. In 2025 you are {2025 - birthYear}!")