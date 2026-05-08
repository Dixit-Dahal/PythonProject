# Q4. Student Resource Portal

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "ad123":
    print("Access Granted: Faculty Dashboard")

elif username == "student" and password == "st2026":
    print("Access Granted: Notes and Practice Questions")

else:
    print("Invalid Credentials. Please try again")

# Q5. Traffic Light System

light = {"red" : "Stop", "yellow" : "Slow Down", "green" : "Go"}

userInput = input("Enter a traffic light color: ").lower

if userInput in light:
    print(f"{light[userInput]}")

else:
    print("Invalid Color")

# Q6. Match Statement

seasonNum = int(input("Enter a season number: "))

match seasonNum:
    case 1:
            print("Spring")
        
    case 2:
        print("Summer")
        
    case 3:
        print("Autumn")

    case 4:
        print("Winter")

    case _:
        print("Unknown")

# Q7. Bank Loan Approval System

age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))
creditScore = int(input("Enter your credit score: "))

if 21 <= age <= 60:
    if income >= 30000:
        if creditScore >= 700:
            print("Approved!")
        
        else:
            print("Disapproved! Credit Score is less than 700")
    else:
        print("Disapproved! Income is less than 30k")
else:
    print("Age is not between 21 and 60")


# Q8. Ticket booking System

age = int("Enter you age: ")
membership = input("Do you have membership card? Yes or No: ").lower()
ticketCost = 200

if age < 12:
    print("Ticket is Free of Cost!")
    ticketCost = 0

elif 12 <= age <= 60 and membership != 'yes':
    print(f"Ticket Cost = {ticketCost}")

elif 12 <= age <= 60 and membership == 'yes':
    ticketCost = 150
    print(f"Ticket Cost = {ticketCost}")

else:
    ticketCost = 100
    print(f"You get a Senior citizen discount. Ticket Cost = {ticketCost}")


# Q9. Bonus for employees serving for more than 5 years

salary = int(input("Enter your salary: "))
service = float(input("Enter your year of service: "))

if service > 5:
    print(f"Net Bonus = {0.05 * salary}")

else:
    print("You don't have any bonus")


# Q10. Area of circle

radius = float(input("Enter the radius of a circle: "))

print(f"Area of circle = {3.14 * radius ** 2}")

# Q11. Wage per Day calculator

age = int(input("Enter your age: "))
gender = input("Enter your gender, M or F: ").capitalize()

if 30 > age >= 18:
    if gender == 'M':
        print("Your wage per day is 700")
    
    elif gender == 'F':
        print("Your wage per day is 750")

    else:
        print("Invalid Gender!")

elif 40 >= age >= 30:
    if gender == 'M':
        print("Your wage per day is 800")
    
    elif gender == 'F':
        print("Your wage per day is 850")

    else:
        print("Invalid Age!")


# Q12. Fizz Buzz 

num = int(input("Enter a number: "))

if num % 3 == 0:
    if num % 5 == 0:
        print("Fizz Buzz")
    else:
        print("Fizz")

else:
    if num % 5 == 0:
        print("Buzz")
    
    else:
        print(num)
    
# Q13. Electricity Bill

usage = float(input("Enter your electricity usage in units: "))

if usage < 100:
    print(f"Cost: Rs. {usage * 5}")

elif usage <= 300:
    print(f"Cost: Rs. {(100 * 5) + ((usage - 100) * 8)}")

elif usage > 300:
    print(f"Cost: Rs. {(100 * 5) + (200 * 8) + ((usage - 300) * 10)}")

# Q14. Rock paper scissors game

player1 = input("Enter your move, Rock, Paper or Scissors: ").lower()
player2 = input("Enter your move, Rock, Paper or Scissors: ").lower()

moves = ['rock', 'paper', 'scissors']

if player1 not in moves or player2 not in moves:
    print("Invalid Move")

else:
    if player1 == player2:
        print("It is a draw")
    
    elif player1 == 'rock' and player2 == 'scissors':
        print("Player 1 wins")
    
    elif player1 == 'paper' and player2 == 'rock':
        print("Player 1 wins")

    elif player1 == 'scissors' and player2 == 'paper':
        print("Player 1 wins")

    else:
        print("Player 2 wins")

# Q15. positive -> odd or even

num = int(input("Enter a number: "))

if num >= 0:
    if num % 2 == 0:
        print(f"{num} is positive and even")
    
    else:
        print(f"{num} is positive and odd")

else:
    print(f"{num} is negative")

# Q16. Sales Handler

totalAmount = float(input("Enter the total amount: "))
isMember = input("Are you a member? Yes or No: ").lower()

if totalAmount > 1000:
    if isMember == 'yes':
        print(f"Final Amount: {totalAmount - (totalAmount * 0.2)}")

    else:
        print(f"Final Amount: {totalAmount - (totalAmount * 0.1)}")

else:
    print(f"Final Amount: {totalAmount}")


# Q17. Weight in other planets

userWeight = float(input("Enter your Earth Weight: "))
planetNum = int(input("Enter a planet number, 1 to 7: "))

relativeGravity = {1 : 0.38, 2 : 0.91, 3 : 0.38, 4 : 2.53, 5 : 1.07, 6 : 0.89, 7 : 1.14}

if planetNum not in relativeGravity:
    print("invalid Planet Number")

else:
    print(f"Your weight on planet {planetNum} is {userWeight * relativeGravity[planetNum]} kg")


# Q18. Grade Calculator

mark1 = int(input("Enter the marks of the first subject: "))
mark2 = int(input("Enter the marks of the second subject: "))
mark3 = int(input("Enter the marks of the third subject: "))
mark4 = int(input("Enter the marks of the fourth subject: "))

totalMarks = mark1 + mark2 + mark3 + mark4
percentage = (totalMarks/400) * 100

print(f"Total Marks: {totalMarks}")
print(f"Percentage: {percentage}")

if percentage <= 40:
    print("Grade: Fail")

elif percentage > 70:
    print("Grade: Distinction")

elif percentage > 60:
    print("Grade: First Division")

elif percentage > 40:
    print("Grade: Pass")


# Q19. ATM logic

accountBalance = 5000

pin = input("Enter your pin: ")

if pin == '123':
    option = input("Select the appropriate option: 1. Withdraw  2. Check Balance  3. Exit: ")

    if option == 1:
        amount = int(input("Enter the amount to withdraw: "))
        
        if amount > accountBalance:
            print("Insufficient Funds!")

        else:
            accountBalance -= amount
            print(f"Successfully withdrawn Rs. {amount}! New balance is Rs. {accountBalance}")
    
    elif option == 2:
        print(f"Current balance: {accountBalance}")

    elif option == 3:
        print("Thank you for Visitng!")

    else:
        print("Invalid option!")

else:
    print("Invalid pin! Access Denied!")


# Q20. Magic Forest Game

print("Welcome to the Magic Forest!")

direction = input("Where do you want to go? North or South?: ").lower()

if direction == 'north':
    choice = input("Cross the River or follow the path? Cross or follow?: ").lower()

    if choice == 'cross':
        print("Game Over!")
    
    elif choice == 'follow':
        choice = input("Choose from Fairy, Ogre or Elf: ").lower()
        if choice == 'fairy' or choice == 'ogre':
            print("Game Over!")
        
        elif choice == 'elf':
            print("You Win!")

        else:
            print("Invalid Option!")

    else:
        print("Invalid Option!")

elif direction == 'south':
    print("Game Over!")

else:
    print("Invalid Option! Please choose the right direction")


# Q21. Smart Elevator

floorNum = int(input("Enter the floor number: "))

isDoorClosed = True
isRunning = False

if floorNum <= 10 and floorNum >= 0:
    weight = float(input("Enter the total weight: "))
    if weight <= 500:
        
        if isDoorClosed:
            isRunning = True
        else:
            print("Close the door!")
    
    else:
        print("Overweight! Lift Cannot Move!")

else:
    print("Invalid Floor Number!")