month = int(input("Input a month number (1-12): "))
year = int(input("Input a year: "))
days = (month, year)
if days:
    print(month,year,days)
else:
    print("Invalid month number. Please enter a value between 1 and 12.")
    if month==1:
        print("31 days ")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("29 days")
    else:
        print("28 days ")
    if month==3:
        print("31 days")
    if month==4:
        print("30days ")
    if month==5:
        print("31 days ")
    if month==6:
        print("30 days")
    if month==7:
        print("31 days")
    if month==8:
        print("30 days ")
    days_per_month = {
        1: 31,  # January
        2: 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,  # February
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # Julya        8: 31,  # August
        9: 30,  # September
        10: 31,  # October
        11: 30,  # November
        12: 31,  # December
    }