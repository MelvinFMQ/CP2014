#q04_determine_leap_year.py
year = int(input("Enter yar: " ))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 != 0):
    print("Leap")
else:
    print("Non-Leap")
