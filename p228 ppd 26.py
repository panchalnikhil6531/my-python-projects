years_of_service=int(input("enter service year "))
salary=int(input("enter salary"))
if years_of_service > 5:
        bonus = 0.05 * salary
        print("bonus = 5%",bonus)
        total_salary = bonus +salary
        print("total salary is =>",total_salary)
else:
        print("bonus = 0 ")