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