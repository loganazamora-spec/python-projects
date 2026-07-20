# manages a simple patient registry as a dictionary. 
# The keys are patient names, the values 
# are dictionaries containing their age and diagnosis.

patients = {
    "Erik Andersson": {"age": 45, "diagnosis": "Parkinson's"},
    "Maria Lindqvist": {"age": 45, "diagnosis": "Alzheimer's"}
}
    

def details_of_patients():
    input_prompt = "Please enter the name of the patient: "

def add_patient():


def view_all_patients():

while True:
    print("Welcome to your patient registry program! ")
    print("[1] View details of a patient")
    print("[2] Add patient information to database")
    print("[3] View information of all patients")
    print("[4] Leave patient registry program")

    user_response = input("Please enter your choice: ").lower().strip()

    if user_response in ["1", "View"]:
        details_of_patients()
    elif user_response in ["2", "Add"]:
        add_patient()
    elif user_response in ["3", "View All"]:
        view_all_patients()
    elif user_response in ["4", "Leave"]:
        print("Thank you for using the patient registry program. Goodbye!")
        break  
    