# Budget Percentage Calculator

# TODO: Prompt the user for their total budget
total_budget = float(input("Please enter your total budget: $"))

# TODO: Prompt the user for the amount spent in each category
housing = float(input("Enter the amount spent on Housing (rent or mortgage): $"))
utilities = float(input("Enter the amount spent on Utilities: $"))
groceries = float(input("Enter the amount spent on Groceries: $"))
transportation = float(input("Enter the amount spent on Transportation: $"))
health_care = float(input("Enter the amount spent on Health Care: $"))
personal_care = float(input("Enter the amount spent on Personal Care: $"))
clothing = float(input("Enter the amount spent on Clothing: $"))
debt = float(input("Enter the amount spent on Debt: $"))

# TODO: Calculate the percentage of the total budget spent in each category
housing_percentage = (housing / total_budget) * 100
utilities_percentage = (utilities / total_budget) * 100
groceries_percentage = (groceries / total_budget) * 100
transportation_percentage = (transportation / total_budget) * 100
health_care_percentage = (health_care / total_budget) * 100
personal_care_percentage = (personal_care / total_budget) * 100
clothing_percentage = (clothing / total_budget) * 100
debt_percentage = (debt / total_budget) * 100

# TODO: Display the results in a user-friendly format
print("\n--- Budget Breakdown ---")
print(f"Housing: ${housing:.2f} ({housing_percentage:.2f}%)")
print(f"Utilities: ${utilities:.2f} ({utilities_percentage:.2f}%)")
print(f"Groceries: ${groceries:.2f} ({groceries_percentage:.2f}%)")
print(f"Transportation: ${transportation:.2f} ({transportation_percentage:.2f}%)")
print(f"Health Care: ${health_care:.2f} ({health_care_percentage:.2f}%)")
print(f"Personal Care: ${personal_care:.2f} ({personal_care_percentage:.2f}%)")
print(f"Clothing: ${clothing:.2f} ({clothing_percentage:.2f}%)")
print(f"Debt: ${debt:.2f} ({debt_percentage:.2f}%)")

# TODO: Check if total budget is valid and not zero
if total_budget == 0:
    print("\nWarning: Total budget cannot be zero.")