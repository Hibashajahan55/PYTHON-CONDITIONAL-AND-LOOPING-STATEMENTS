# Exercise 1
# Name your file: MonthNames.py
# Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
month_number = int(input("Enter the month: "))
if 1 <= month_number <= 12:
    print(f"Month {month_number} is {months[month_number - 1]}")
else:
    print("Error: Please enter a number between 1 and 12.")



# Exercise 2
# A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price to people
# who are less than 16 years old, and for a third of the price for people who are 60 years old or more.


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October","November", "December"]
month_number = int(input("Enter the month: "))
if 1 <= month_number <= 12:
        print(f"Month {month_number} is {months[month_number - 1]}")
else:
        print("Error: Please enter a number between 1 and 12.")

full_price = 6.0

Age = int(input("Enter your age: "))

  # Determine ticket cost based on age
if Age < 16:
        cost = full_price / 2
elif Age >= 60:
        cost = full_price / 3
else:
        cost = full_price

print(f"Your ticket costs £{cost:.2f}")


# Exercise 3
# Name your file: BodyMassIndex.py
# Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement
# to check if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters:
# BMI= weight(kg)/height2(m2)
# BMI Weight Status Categories table
# BMI range - kg/m2   Category
# Below 18.5 Underweight
# 18.5 -24.9 Normal
# 25 - 29.9 Overweight
# 30 & Above Obese


weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight/(height*2)

if bmi < 18.5:
            category = "Underweight"
elif 18.5 <= bmi < 24.9:
            category = "Normal"
elif 25 <= bmi < 29.9:
            category = "Overweight"
else:
            category = "Obese"

#result
print(f"\nYour BMI is: {bmi:.2f}")
print(f"You are in the \"{category}\" range.")

# Exercise 4
# Write a Python program to receive 3 numbers from the user and print the greatest among them


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
            greatest_num = num1
elif num2 >= num1 and num2 >= num3:
            greatest_num = num2
else:
            greatest_num = num3

print(f"The greatest number is: {greatest_num}")


# Exercise 5
# Find the factorial of a given number using loops(note the number is received from the user)

number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
            factorial *= i

print(f"The factorial of {number} is: {factorial}")


# Exercise 6
# Reverse a number using while loop

num = int(input("Enter a number: "))
reversed_number = 0

while num != 0:
    reminder = num % 10
    reversed_number = reversed_number * 10 + reminder
    num //= 10

print("The Reversed Number is : " + str(reversed_number))


# Exercise 7
# Finding the multiples of a number using loop

number = int(input("Enter a number to find its multiples: "))
count = int(input("Enter how many multiples to display: "))

print(f"The first 10 multiples of {number} are:")
for i in range(1, count + 1):
        print(f"{number} x {i} = {number * i}")

# Exercise 8
# Write a program to print the inputted value as it is and break the loop if the value is 'done'.
# Example run of the program
# :hello there
# hello there
# :finished
# finished
# :done
# Done

while True:
    user_input = input(":")
    print(user_input)
    if user_input.lower() == 'done':
        break


# Exercise 9
# Write a program that prints the numbers from 1 to 10.But for multiples of three print "Fizz" instead of the number
# and for the multiple of five print "Buzz".For numbers which are multiples of both three and five print "FizzBuzz"


limit = int(input("Enter the range up to which numbers displayed: "))
for number in range(1, limit + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Exercise 10
# Write a program to print the following pattern:
#
# 54321
# 4321
# 321
# 21
# 1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
