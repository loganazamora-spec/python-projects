raw_input = input("List of ages: ")

age_list = [int(x) for x in raw_input.split(",")]

elig_ages = []
inelig_ages = []

for age in age_list:
    if age >= 30:
        elig_ages.append(age)
    elif age < 30:
        inelig_ages.append(age)


avg_elig = round(sum(elig_ages)/len(elig_ages), 1)
avg_inelig = round(sum(inelig_ages)/len(inelig_ages), 1)

print(f"Eligible ages: {elig_ages} | Average age: {avg_elig}")
print(f"Ineligible ages: {inelig_ages} | Average age: {avg_inelig}")


#35, 24, 64, 15, 34, 3, 55, 21, 14, 84, 44, 52, 43, 64