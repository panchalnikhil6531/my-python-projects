salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))
bonus_percentage = 0.05
bonus_threshold = 5

if years_of_service > bonus_threshold:
    bonus = salary * bonus_percentage
    print(bonus)
else:
    bonus = 0

net_bonus = (salary, years_of_service)
print("Net bonus amount:" ,net_bonus)
