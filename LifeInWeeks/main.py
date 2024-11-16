# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

current_age = int(input("What is your current age?: "))
max_age = 90

remaining_age = max_age - current_age

remaining_days = 365 * remaining_age
remaining_weeks = 52 * remaining_age
remaining_months = 12 * remaining_age

result = f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left."
print(result);
