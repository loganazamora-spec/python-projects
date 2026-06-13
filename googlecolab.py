bill_amount = int(input(("What is the bill amount? ")))
tip_prompt = int(input(("What is the tip percentage? ")))

tip_percentage = tip_prompt/100

tip = bill_amount * tip_percentage

print(f"Tip: {tip}%")

print(f"Total bill = ${bill_amount + tip}")
