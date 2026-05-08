# First Name validation

firstName = input("Enter your First Name: ")

if not firstName:
    print("First name cannot be empty")

elif not firstName.isalpha():
    print("Name must only contain letters")

else:
    print("Valid")

# Last Name validation

lastName = input("Enter your Last Name: ")

if not lastName:
    print("Last name cannot be empty")

elif not lastName.isalpha():
    print("Name must only contain letters")

else:
    print("Valid")

# Email validation:

email = input("Enter your email: ")

if not email:
    print("This feild cannot be empty")

elif '@' not in email:
    print("Email must contain '@'")

elif '.' not in email:
    print("Email must contain '.'")

else:
    print("Valid")

# Re-email Validation:

reEmail = input("Re enter your email: ")

if email == reEmail:
    print("Valid")

else:
    print("Email does not match")

# password validation:

password = input("Enter your password: ")

if not password:
    print("Password cannot be empty")

elif len(password) < 6:
    print("Password must contain at least 6 characters")

else:
    print("Valid")


# Recombining all the if else statements:

firstName = input("Enter your First Name: ")
lastName = input("Enter your Last Name: ")
email = input("Enter your email: ")
reEmail = input("Re enter your email: ")
password = input("Enter your password: ")

if not (firstName and lastName and email and reEmail and password):
    print("First name cannot be empty")

elif not (firstName.isalpha() and lastName.isalpha()):
    print("Name must only contain letters")

elif '@' not in email or '.' not in email:
    print("Invalid Email")

elif email != reEmail:
    print("Emails do not match")

elif len(password) < 6:
    print("Password must be longer than 6 characters")

else:
    print("Registration Succesful")