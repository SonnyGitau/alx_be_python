# Prompt the user for their financial detail
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expense: "))
# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
# Project annual savings with 5% interest
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest
print(f"\nYour monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected savings after one year, including 5% interest, are: ${projected_savings:.2f}")
