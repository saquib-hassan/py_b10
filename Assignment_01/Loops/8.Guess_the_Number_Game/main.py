"""Consider a random number between 1 
and 10. Let user guess until correct. Give hints: “Too high” or “Too low”."""
# use while loop

import random

secret_num = random.randint(1,10)
print(secret_num)

attempts = 0

while attempts < 4:
    pick_a_number = int(input("Enter a number between 1 to 10: "))
    if pick_a_number > secret_num:
        print("Too high")
    elif pick_a_number < secret_num:
        print("Too low")
    elif pick_a_number == secret_num:
        print("YAY! you guessed right!")
        break
