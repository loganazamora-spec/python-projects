tasks = {}

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
    print("Enter the task you would like to add and its priority from 1 (high) to 3 (low)")
    task = input("Task: ")
    
    try:
        priority = int(input("Priority: "))

        confirmation()
    except:
        print("Please enter a number from 1-3 to establish the priority of the task")
        add()

def confirmation(task, priority):
    affirmative_responses = ["Yes".strip().lower(), "Yup".lower().strip(), "Affirmative".lower().strip()]

    response = input("Would you like to add this task to your to-do list?: Task: {task} | Priority: {priority}  ")

    if response in affirmative_responses:
        tasks.append({"Task":task, "Priority":priority})

        view()
    else:
        return_responses = ["Return".strip().lower(), "Back".strip().lower(), "Home".strip().lower()] 
        add_responses = ["Add".strip().lower(), "New".strip().lower()]

        choice = input("Would you like to add a different task or return to the home screen? ")

        if choice in return_responses:
             main_screen()
        elif choice in add_responses:
             add()
        else:
             print("Please choose to return to the home screen or add another task. ")
             # how do i run this particular part of the program? a new function entirely? 




def view():
    if tasks:
        print()

    print("Here are your current tasks and their corresponding priorities: ")

    for i, task, priority in tasks:
        print(enumerate(tasks, start=1))


def quit_program():
    print("quit")


main_screen()