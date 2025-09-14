"""Predefined password. Let user try until 
correct or after 3 failed attempts show "Account locked"."""

predifined_password = "100bdt"

attempts = 0
while attempts < 3:
    guessed_pass = input("Enter your password => You can try only 3 times...")
    if guessed_pass == predifined_password:
        print("Access granted.")
        break
    elif guessed_pass != predifined_password:
        print("Please try again...")
        attempts += 1
else:
    print("Account locked")

    
   


