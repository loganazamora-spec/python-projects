import pandas as pd

# Here is a standard dictionary, very similar to the ones you've been building
patient_data = {
    "Name": ["Erik", "Maria", "Lars", "Anna"],
    "Group": ["drug", "placebo", "drug", "placebo"],
    "Starting_Score": [52, 48, 61, 55]
}

# Now, we use the Pandas library to transform that dictionary into a "DataFrame"
df = pd.DataFrame(patient_data)

print(df)
print(df["Starting_Score"].mean())
print(df[df["Group"] == "drug"])



