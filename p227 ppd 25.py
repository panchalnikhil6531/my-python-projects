age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of"))

if 18 <= age < 30:
    if gender == 'M':
        wage_per_day = 700
    elif gender == 'F':
        wage_per_day = 750

elif 30 <= age <= 40:
    if gender == 'M':
        wage_per_day = 800
    elif gender == 'F':
        wage_per_day = 850

total_wages = wage_per_day * days
print( f"Total wages: {total_wages}")


