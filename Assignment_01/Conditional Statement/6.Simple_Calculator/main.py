
"""Input two numbers and an operator (+, -, *, /).Use 
if-elif to perform the operation and print the result. Handle division by zero 
using conditions."""

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

operation = input("Choose operator among these +, -, *, /")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("division by zero is not allowed")
    else:
        print(num1 / num2)
else:
    print("Invalid operator")