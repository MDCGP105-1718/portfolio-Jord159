total_cost = float(input('Cost of House: '))
portion_deposit = 0.20
current_savings = 0
annual_return = 0.04

annual_salary = float(input('Annual Salary: '))
portion_saved = float(input('Portion Saved (as decimal): '))
monthly_salary = annual_salary/12
months = 0

while current_savings < portion_deposit*total_cost:
    current_savings += current_savings * annual_return/12
    current_savings += monthly_salary * portion_saved
    months = months + 1

print('Number of months = ', months)
