# 52 weeks in a year
# 365 days in non-leap and 366 days in a leap year
# 12 months
# Write a prog to tell us how days, weeks, months we have left if we live until 90 years old.

age = int(input("Enter your current age?"))


years_remaining = int(90 - age)
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365 

message = f"You have Total {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months"
print(message)
