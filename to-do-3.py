tasks = []

def main_screen():
    options_1 = ["1", "Add".lower()]
    options_2 = ["2", "View".lower()]
    options_3 = ["3", "Quit".lower()]

    print("Welcome to your task tracker!")
    print("[1] Add a new task")
    print("[2] View existing tasks")
    print("[3] Quit")
    response = input("What would you like to do? ")

    if response in options_1:
        add()
    elif response in options_2:
        view()
    elif response in options_3 :
        quit_program()
    else:
        print("Please enter a valid response")
        main_screen()

def add():
    def confirmation():
        confirmation_prompt = input(f"Would you like to add the following task to your to do list {new_task}? [1] Yes [2] No ")

        if confirmation_prompt.strip().lower() in ["yes", "1"]:
            tasks.append(new_task)
            print(f"'{new_task}' has been added")
        elif confirmation_prompt.strip().lower() in ["no", "2"]:
            print(f"'{new_task}' has not been added.")
        else:
            print("Please choose '1' or '2'.")
            confirmation()

    new_task = input("New task: ")

    confirmation()

    response_2 = input("Would you like to: [1] Add another task [2] Return to homescreen. ")

    if response_2.strip().lower() in ["add", "1"]:
        add()
    else:
        main_screen()

def view():
    if len(tasks) == 0:
        print("There are currently no tasks to do")
    else:
        print("Current tasks: ")
        for task in tasks:
            print(f"- {task}")

    def choice():
        response = input("Would you like to: [1] Return to homescreen [2] Add a new task. ")

        if response.lower().strip() in ["1", "return", "home"]:
            main_screen()
        elif response.lower().strip() in ["2", "add"]:
            add()
        else:
            print("Please choose '1' or '2'")
            choice()
    
    choice()

def quit_program():
    print("See you next time!")
    quit()

main_screen()