print("Welcome to BMI Calculator!")

height = float(input("Please enter your height in meters (m): "))
weight = float(input("Please enter your weight in kilogrmas (kg): "))
bmi = round(weight / (height ** 2))
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30:
    print(f"Your BMI is {bmi}, you are obese.")
