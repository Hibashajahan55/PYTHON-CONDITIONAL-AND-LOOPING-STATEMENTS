# Exercise 1
# Name your file: MonthNames.py
# Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
month_number = int(input("Enter the month: "))
if 1 <= month_number <= 12:
    print(f"Month {month_number} is {months[month_number - 1]}")
else:
    print("Error: Please enter a number between 1 and 12.")

7