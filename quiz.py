# introduction
user_name = input("What is your name? ").strip().title()
quiz_prompt = input("Do you want to do the easy, medium or hard quiz? ").lower()

print(f"Hello {user_name}! You will be doing a quiz, you have 3 attempts for each question. Good luck!")

def easy_quiz():
    score = 0

    # question 1
    attempts = 3
    correct_answers_1e = ["1.5", "3/2"]

    while attempts > 0:
        user_guess_1e = input("1. Solve for x: 2x - 3 = 0 . x = ")
        if user_guess_1e not in correct_answers_1e:
            attempts -= 1

            if attempts > 0:
                print("Wrong! Try again.")
            else:
                print("Wrong! Next question.")
        elif user_guess_1e in correct_answers_1e:
            print("Correct! Next question.")
            score += 1
            break

    attempts = 3
    # question 2
    correct_answer_2e = "George Washington"

    while attempts > 0:
        user_guess_2e = input("2. Who was the first president of the USA? ").strip().title()
        if user_guess_2e != correct_answer_2e:
            attempts -= 1

            if attempts > 0:
                print("Wrong! Try again.")
            else:
                print("Wrong! Next question.")
        elif user_guess_2e == correct_answer_2e:
            print("Correct! Next question.")
            score += 1
            break
    
    attempts = 3
    # question 3
    correct_answers_3e = ["Hola", "Ciao", "Saludos"]

    while attempts > 0:
        user_guess_3e = input("3. How do you say 'Hello' in Spanish? ").strip().title()
        if user_guess_3e not in correct_answers_3e:
            attempts -= 1
            
            if attempts > 0:
                print("Wrong! Try again.")
            else:
                print("Wrong! Next question.")
        elif user_guess_3e in correct_answers_3e:
            print("Correct! You're done.")
            score += 1
            break

    answers_e = [user_guess_1e, user_guess_2e, user_guess_3e]

    if score >= 2:
        pass_fail = "pass"
    else:
        pass_fail = "fail"

    print("You answers were:")

    for answer in answers_e:
        print(f"{answer}")

    print(f"so your final score is {score} out of 3. You {pass_fail}ed!")


def medium_quiz():
    score = 0

    attempts = 3
    # question 1
    correct_answers_1m = ["(x + 3)(x - 3)", "(x - 3)(x + 3)"]

    while attempts > 0:
        user_guess_1m = input("1. Factorize x^2 - 9. ")
        if user_guess_1m not in correct_answers_1m:
            attempts -= 1

            if attempts > 0:
                print("Wrong! Try again.")
            else:
                print("Wrong! Next question.")
        elif user_guess_1m in correct_answers_1m:
            print("Correct! Next question.")
            score += 1
            break

    attempts = 3
    # question 2
    correct_answer_2m = "Bern"

    while attempts > 0:
        user_guess_2m = input("2. What is the capital of Switzerland? ").title()
        if user_guess_2m != correct_answer_2m:
            attempts -= 1

            if attempts > 0:
                print("Wrong! Try again.")
            else:
                print("Wrong! Next question.")
        elif user_guess_2m == correct_answer_2m:
            print("Correct! Next question.")
            score += 1
            break

    attempts = 3
    # question 3
    correct_answer_3m = "Nucleus"

    while attempts > 0:
        user_guess_3m = input("Where is DNA stored in a cell? ").title()
        if correct_answer_3m not in user_guess_3m:
            attempts -= 1

            if attempts > 0:
                print("Wrong! Try again.")
            else:
                print("Wrong! Next question")
        elif correct_answer_3m in user_guess_3m:
            print("Correct! You're done.")
            score += 1
            break

    if score >= 2:
        pass_fail = "pass"
    else:
        pass_fail = "fail"

    answers_m = [user_guess_1m, user_guess_2m, user_guess_3m]

    print("Your answers were:")
    for answer in answers_m:
        print(answer)

    print(f"Your final score is {score} out of 3. You {pass_fail}ed!")

def hard_quiz():
    score = 0

    attempts = 3
    # question 1
    correct_answers_1h = ["cos(x)", "cosx"]

    while attempts > 0:
        user_guess_1h = input("1. What is the derivative of sin(x)? ")
        if user_guess_1h not in correct_answers_1h:
            print("Wrong! Try again.")
            attempts -= 1
        elif user_guess_1h in correct_answers_1h:
            print("Correct! Next question.")
            score += 1
            break

    attempts = 3
    # question 2
    correct_answers_2h = ["2-methylpropan-2-ol", "2-methyl-2-propanol", "tert-butyl alcohol"]

    while attempts > 0:
        user_guess_2h = input("2. What is the name of the tertiary isomer of butanol? ")
        if user_guess_2h not in correct_answers_2h:
            print("Wrong! Try again.")
            attempts -= 1
        elif user_guess_2h in correct_answers_2h:
            print("Correct! Next question.")
            score += 1
            break
    
    attempts = 3
    # question 3
    correct_answers_3h = ["5' -> 3'", "5 prime to 3 prime", "5' to 3'", "Five prime to three prime"]

    while attempts > 0:
        user_guess_3h = input("3. In what direction does DNA transcription occur? ")
        if user_guess_3h not in correct_answers_3h:
            print("Wrong! Try again.")
            attempts -= 1
        elif user_guess_3h in correct_answers_3h:
            print("Correct! You're done.")
            score += 1
            break

    if score >= 2:
        pass_fail = "pass"
    else:
        pass_fail = "fail"

    answers_h = [user_guess_1h, user_guess_2h, user_guess_3h]
    print("Your answers were:")
    for answer in answers_h:
        print(answer)
    print(f"Your final score is {score} out of 3. You {pass_fail}ed!")

if "easy" in quiz_prompt:
    easy_quiz()
elif "medium" in quiz_prompt:
    medium_quiz()
elif "hard" in quiz_prompt:
    hard_quiz()

