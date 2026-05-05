balance = 5000
amount = int(input("Withdraw amount: "))

# without if-else:
balance -= amount
print(f"New balance: {balance}")

# with if-else:
balance = 5000

if amount <= 0:
    print("Enter a valid amount")

elif amount > balance:
    print("Insufficient Funds!")

else:
    balance -= amount
    print(f"New balance: {balance}")


# Authentication:

# Without if-else
correct_password = "gurkhas123"
entered = "pass123"

print("Login Successful!")
print("Welcome!!!")


# With if-else
username = "admin"
password = "gurkhas123"

enteredUser = "administrator"
enteredPass = "pass123"

if enteredUser == username and enteredPass == password:
    print("Login Succesful\nWelcome!!")

elif enteredUser != username:
    print("Username not Found!")

else:
    print("Passowrd Incorrect")

# Grading System:

# without if-else:

marks = 45

print("Grade: A+")
print("Grade: A")
print("Grade: B")
print("Grade: F")

# with if-else

marks = 45

if marks >= 90:
    print("Grade: A+")

elif marks >= 75:
    print("Grade: A")

elif marks >= 60:
    print("Grade: B")

elif marks >= 50:
    print("Grade: C")

else:
    print("Grade: F")


# Voting Registration System Authentication:

# Without if-else:

name = "Ram"
age = 14

print(f"{name} registered to vote")
print("Voter id issued")

# With if-else:

name = "Ram"
age = 14

if age >= 18:
    print(f"{name} registered")
    print("Voter id issued")

else:
    print(f"Must be 18+. You are {age}")
    print("Registration denied")