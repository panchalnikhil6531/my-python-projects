basic_salary = float(input("Enter the basic salary: "))
employee_grade = input("Enter the employee grade (A/B/C): ")
compute_salary=int()
gross_salary = compute_salary(basic_salary, employee_grade)
hra = 0.2 * basic_salary
da = 0.5 * basic_salary
pf = 0.11 * basic_salary
if employee_grade == 'A':
    allowance = 1700.0
elif employee_grade == 'B':
    allowance = 1500.0
else:
    allowance = 1300.0

gross = round(basic_salary + hra + da + allowance - pf, 2)

print("Final Salary:" ,gross_salary)
