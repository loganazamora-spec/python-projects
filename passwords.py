options_1 = ["1", "[1]", "Add".lower()]
options_2 = ["2", "[2]", "View".lower()]
options_3 = ["3", "[3]", "Delete".lower()]
options_4 = ["4", "[4]", "Quit".lower()]

login_password = {}

def add_new():
    # prompt for login and password
    print("Add a new login and password")
    login = input("Login: ")
    password = input("Password: ")

    # add login and password to dictionary
    login_password[login] = password

    print("Your login and password have been saved.")

    # prompt what to do now
    response = input("Would you like to quit, return to home page, or add another login and password? ")
    if "Return".lower() in response:
        main_screen()
    elif "Add".lower() in response:
        add_new()
    elif response == "Quit".lower():
        quit_program()
        
    
def view():
    # in case user hasnt added any passwords
    if login_password == {}:
        print("No saved passwords")
        return
    
    # show the current logins and passwords
    print("Here are your current logins and their corresponding passwords: ")
    for login, password in login_password.items():
        print(f"Login: {login}")
        print(f"Password: {password}")

    # prompt what to do now
    response = input("Would you like to quit or return to home page? ")
    if response == "Return".lower():
        main_screen()
    elif response == "Quit".lower():
        quit_program()

def delete():
    for i, (login, password) in enumerate(login_password.items(), start=1):
        print(f"{i}. {login} | {password}")

    try:
        choice = int(input("Enter the number of the login to delete: "))
    except:
        ()

        

def quit_program():
    print("See you next time!")
    quit()


def main_screen():
    # print main screen as long as user not made decision
    while True:
        print("===== PASSWORD VAULT =====")
        print("[1] Add new login")
        print("[2] View existing logins")
        print("[3] Delete an existing login")
        print("[4] Quit")

        choice = input("What do you want to do? ")
    # move to different pages depending on decision
        if choice in options_1:
            add_new()
            break
        elif choice in options_2:
            view()
            break
        elif choice in options_3:
            delete()
            break
        elif choice in options_4:
            quit_program()
            break

main_screen()

# ask dad about numbering of logins and passwords