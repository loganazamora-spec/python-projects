# manages a simple patient registry as a dictionary. 
# The keys are patient names, the values 
# are dictionaries containing their age and diagnosis.

patients = {
    "Erik andersson": {"age": 45, "diagnosis": "Parkinson's"},
    "Maria lindqvist": {"age": 45, "diagnosis": "Alzheimer's"},
}
    

def details_of_patients():
    name = input("Please enter the full name of the patient you would like to view: ").capitalize().strip()
    if name in patients:
        print(f"Details: {patients[name]}")
    else:
        print("Patient not found. ")
# Problem: Automatically returns to main screen after details viewed. 
def add_patient():
    added_name = input("Please enter the full name of the patient you would like to add: ").capitalize().strip()
    added_age = int(input("Please enter the age of the patient you would like to add: "))
    added_diagnosis = input("Please enter the diagnosis of the patient you would like to add: ").capitalize().strip()
    # Problem: With ALS, .capitalize() only capitalized the A, and had lower-case ls. 

    patients[added_name] = {"Age":added_age, "Diagnosis":added_diagnosis}

def view_all_patients():
    print(patients)

def main_screen():
    while True:
        print("Welcome to your patient registry program! ")
        print("[1] View details of a patient")
        print("[2] Add patient information to database")
        print("[3] View information of all patients")
        print("[4] Leave patient registry program")

        user_response = input("Please enter your choice: ").lower().strip()

        if user_response in ["1", "view"]:
            details_of_patients()
            
        elif user_response in ["2", "add"]:
            add_patient()
        elif user_response in ["3", "view all"]:
            view_all_patients()
        elif user_response in ["4", "leave", "exit"]:
            print("Thank you for using the patient registry program. Goodbye!")
            break  

main_screen()