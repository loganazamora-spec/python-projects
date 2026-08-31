lab_supplies = {
    #equipment:quantity,int
    "Beakers":50,
    "Microscopes":2,
}

print(f"Current lab supplies: {lab_supplies}")

lab_supplies["Test tubes"] = 200

print(f"Updated lab supplies: {lab_supplies}")

lab_supplies["Beakers"] = 75

print(f"Updated lab supplies: {lab_supplies}")

print(f"Current number of microscopes: {lab_supplies['Microscopes']}")

lab_supplies.pop("Test tubes")

print(f"Updated lab supplies: {lab_supplies}")


