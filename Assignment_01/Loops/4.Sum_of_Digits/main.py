"""Write a Python program that takes an integer input from the 
user and calculates the sum of its digits using a while loop."""

user_input = int(input("Enter a number: "))

sum = 0

while user_input > 0:
    digit = user_input %10 #getting the last digit
    sum = sum + digit
    user_input = user_input // 10 #removing the last digit 
print(sum)

