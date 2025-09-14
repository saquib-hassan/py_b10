
""" Write a Python program that takes a person's height (in 
meters) and weight (in kilograms) as input and calculates their Body Mass 
Index (BMI). Print out their BMI and a message indicating whether they are 
underweight (<18.5), normal (18.5-24.9), overweight (25-29.9), or obese 
(>=30). 
"""

height = float(input("Please enter your height: "))
weight = float(input("pleaes enter your weight: "))

bmi = weight/(height ** 2)
print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("You're underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You're normal")
elif bmi >= 25 and bmi <=29.9:
    print("You're overweight")
else:
    print("You're obese")