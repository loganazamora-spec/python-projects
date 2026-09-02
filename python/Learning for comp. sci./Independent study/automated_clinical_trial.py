# Situation: Your lab is testing a new cognitive medication. 
# You have a cohort of patients. Some are receiving the actual drug, and some are receiving a placebo.
# The trial is scheduled to run for exactly two months. 
# Every patient comes into the clinic once a week to take a cognitive test and record their score.

import random 

trial_patients = {    
    "P001": {"name": "Erik", "treatment_group": "drug", "weekly_scores": [52]},    
    "P002": {"name": "Maria", "treatment_group": "placebo", "weekly_scores": [48]},    
    "P003": {"name": "Lars", "treatment_group": "drug", "weekly_scores": [61]},
    "P004": {"name": "Anna", "treatment_group": "placebo", "weekly_scores": [55]}
}

current_week = 1

while current_week < 8: 
    removed_patients = []
    weekly_score_drug = []
    weekly_score_placebo = []
    # Test patients' cognition weekly 
    for patient in trial_patients:
        data = trial_patients[patient]

        # Defining variables
        treatment_group = data["treatment_group"]
        score_patient = data["weekly_scores"]
        
        
        # Producing random test scores

        test_score_drug = random.randint(score_patient[-1]-1, score_patient[-1]+3)
        test_score_placebo = random.randint(score_patient[-1]-3, score_patient[-1]+1)


        # Adding test scores to list
        if treatment_group == "drug":
            score_patient.append(test_score_drug)
            weekly_score_drug.append(test_score_drug)
        else:
            # If a patient experiences a severe cognitive drop and their weekly test score falls below 40, 
            # they must be immediately withdrawn from the trial to receive emergency care  
            if test_score_placebo < 40:
                print(f"{patient}: This patient must be withdrawn from the trial.")
                print(f"Patient: {patient} {data['name']}; Scores: {score_patient}; Withdrawn after week {current_week} due to a score of {test_score_placebo}")
                removed_patients.append(patient)
            else:
                score_patient.append(test_score_placebo)
                weekly_score_placebo.append(test_score_placebo)

        # At the end of every single week, they expect a status report. 
        # They want to see the current average score of the active drug group 
        # side-by-side with the current average score of the active placebo group.
    average_drug = sum(weekly_score_drug)/len(weekly_score_drug)
    
    if len(weekly_score_placebo) == 0:
        print("There are no participants left in the placebo group")
        print(f"Average score this week (week {current_week}) for drug group: {average_drug}")
    else:
        average_placebo = sum(weekly_score_placebo)/len(weekly_score_placebo)
        print(f"Average score this week (week {current_week}) for placebo group: {average_placebo}")
        print(f"Average score this week (week {current_week}) for drug group: {average_drug}")
                
    current_week += 1       

    for i in removed_patients:
        trial_patients.pop(i)    

        
    if current_week == 8:
        print("Trial has ended.")

for patient in trial_patients:
    data = trial_patients[patient]  

    print(f"Total scores throughout trial: {patient} {data['name']}: {data['weekly_scores']}")

all_drug_scores = []
all_placebo_scores = []

for patient in trial_patients:
    data = trial_patients[patient]
    if data["treatment_group"] == "drug":
        all_drug_scores.extend(data["weekly_scores"])
    else:
        all_placebo_scores.extend(data["weekly_scores"])

print(f"The total score of the drug group was: {sum(all_drug_scores)}")
print(f"The total score of the placebo group was: {sum(all_placebo_scores)}")

total_average_drug = (round(sum(all_drug_scores)/len(all_drug_scores)))
total_average_placebo = round(sum(all_placebo_scores)/len(all_placebo_scores))
numerator = total_average_drug - total_average_placebo

print(f"The drug group had a {round(numerator/total_average_drug*100)}% higher total score than the placebo group")
