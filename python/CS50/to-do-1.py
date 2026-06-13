tasks = [
    # {}   # task:priority
]



# main screen
def main_screen():
    options_1 = ["1", "Add".lower()]
    options_2 = ["2", "View".lower()]
    options_3 = ["3", "Quit".lower()]

    print("Welcome to your task tracker!")
    print("[1] Add a new task")
    print("[2] View existing tasks")
    print("[3] Quit")
    response = input("What would you like to do? ")

    try: 
        if response in options_1:
            add()
        elif response in options_2:
            view()
        elif response in options_3 :
            quit_program()
    except:
        print("Please enter a valid response")
        main_screen()
        
# view current
def view(): 
    ms_response = ["Return".lower(), "Main".lower()]
    mark_response = ["Mark".lower()]

    print("Here is your current to-do list: ")
    for i, task in enumerate(tasks):
        
        # print(f"{task}")

        # print(f"{i}. {task['task']};  Priority: {task['task']}") 
        print(task["Task"])
    
    # mark as done
    def mark():
        try:
            task_marked = input("Which task would you like to mark as done? ").lower().strip()
            
            
        except:
            ()


        # prompt what to mark as done
        # do I reprint the list of tasks?  
    

    response = input("Would you like to mark a task as done or return to the main screen? ")
    try:
        if response in ms_response:
            main_screen()
        elif response in mark_response:
            mark()
    except:
        print("Please enter a valid response")
        # then maybe run the program again to offer another attempt? 
# mark as done

# add
def add():

    print("Enter the task you would like to add and its priority from 1 (high) to 3 (low)")
    task = input("Task: ")
    try:
        priority = int(input("Priority: "))

        confirmation(task, priority)
    except:
        print("Please enter a number from 1-3 to establish the priority of the task")
        add()
    
    
def confirmation(task, priority):
    affirmative_responses = ["Yes".lower().strip(), "Yup".lower().strip(), "Affirmative".lower().strip()]

    response = input(f"Would you like to add this task to your to-do list?: {task}, priority: {priority} ")

    if response in affirmative_responses:
        tasks.append({"Task": {task}, "Priority": {priority}}) 
            
        view()
    else:
        print("Please answer yes or no. ")
        confirmation()


# quit
def quit_program():
    print("See you next time!")
    quit

main_screen()