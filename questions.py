# 1. 

student_records = {'Ram' : 'ramkomail@gmail.com',
                   'Sam' : 'samkomail@gmail.com',
                   'Hari' : 'harikomail@gmail.com'}

user = input("Enter the name of a student: ").title()

print(student_records.get(user, 'Student Not Found!'))

# 2.

shopping_list = {"Milk", "Bread", "Eggs"}
bought = {"Bread", "Eggs"}

if shopping_list.difference():
    unbought = shopping_list ^ bought
    print('Remaining items: ', unbought)

else: 
    print("Shopping Complete!")

# 3.

class_list = ['ram', 'sita', 'laxman']

user = input("Enter the name of the student to be added: ")

if user not in class_list:
    class_list.extend(user)
    print(f"{user} successfully added to the class.")

else:
    print("The student is already present in the class.")



# 4.

votes = ["Blue", "Red", "Blue", "Green", "Blue"]

if votes.count("Blue") >= 3:
    print("Blue Wins!")

else:
    print("Blue did not win!")


# 5.

grades = {"Ram": 92, "Sita": 88}

user = input("Enter a students name: ").title()

print(grades.get(user, "Student Not Found!"))



# 6.

applicant = {}

requiredSkills = {"Python", "Java"}

applicant["name"] = input("Enter your Name: ").title()
applicant["skills"] = input("Enter your skills separated by commas: ").title().split(', ')
applicant["experience_years"] = int(input("Enter how many years of experience you have: "))

if (set(applicant['skills']) & requiredSkills) and applicant["experience_years"] >= 2:
        print(f"{applicant['name']} Qualifies!")

else:
    print(f"{applicant['name']} Does Not Qualify!")

# 7. 

banned_items = {"scissors", "knife", "lighter"}

weight = float(input("Enter the weight of your baggage: "))
items = []
items = input("Enter the items in your baggage (Separate using comma): ").lower().split(', ')
print(items)
if (set(items) & banned_items) or weight > 7:
     print("Bag not allowed!")

else:
     print("Bag allowed!")


# 8.

salary_sheet = {
     'emp1' : {'name' : "John", 'salary' : 7500},
     'emp2' : {'name' : "Emma", 'salary' : 8000},
     'emp3' : {'name' : "Shyam", 'salary' : 500},
}

salary_sheet['emp3']['salary'] = 8500

print(salary_sheet['emp3'])


# 9.

items_Ram = []
items_Laxman = []

items_Ram = input("Enter the items that Ram picked(separate with a comma): ").lower().split(', ')
items_Laxman = input("Enter the items that Laxman picked(separate with a comma): ").lower().split(', ')

if set(items_Ram) & set(items_Laxman):
     print("They have some common items")

else:
     print("They picked completely different items")


# 10.

myList = [10, 20, 30]
myTuple = (10, 20, 30)
mySet = {10, 20, 30}
myDict = {
     'a' : 10,
     'b' : 20,
     'c' : 30
     }

val = int(input("Enter token value: "))

if (val in myList) and (val in myTuple):
     if ('b' in myDict) and (val not in mySet):
          print("Path A")
     else:
          print("Path B")
else:
     print("Path C")


# 11.   The value for a becomes 30

# 12.   [1,2,3]

# 13.   Not Found

# 14.   2

# 15.   my_set.add(40)

# 16.

menu = {
     'Pizza' : 15,
     'Burger' : 10,
     'Salad' : 8
     }

order = input("Enter your order: ").title()

if order in menu:
     print(f'Price = {menu[order]}')

else:
     print("Item not Found!")


# 17.

student_data = {}

student_data["name"] = input("Enter the name of the student: ").title()
student_data["score"] = int(input("Enter the score: "))

if student_data["score"] >= 80:
     student_data['status'] = "Pass"

else:
     student_data['status'] = "Review"

print(student_data)


# 18.

database = {"admin" : "1234", "user" : "abcd"}

user_input = input("Enter your username: ").lower()
user_pass = input("Enter your password: ")

if (user_input in database) and user_pass in database[user_input]:
     print("Login Successful")

else:
     print("Login Failed")


# 19.

emails = ['ram123@gmail.com', 'hari77@gmail.com']
blacklisted_emails = {'hari77@test.com'}

current_email = input("Enter the email: ")

if (current_email in emails) and (current_email not in blacklisted_emails):
     print("Email sent")

else:
     print("Blocked")


# 20.

inventory = {'A1': 50, 'B2': 0, 'C3': 10}
restricted_zones = {'B2', 'Z9'}

target = input("Enter the target zone: ")

if target in inventory:
     if (target not in restricted_zones) and (inventory[target] > 0):
          print("Dispatch them")
     else:
          print("Stock Error")

else:
     print("Invalid Zone")


# 21. 

valid_courses = {'python', 'robotics', 'java'}
hs_grades = [9, 10, 11, 12]
studentData = {}

studentData["name"] = input("Enter your name: ")
studentData["course"] = input("Enter the course: ").lower()
studentData["grade"] = int(input("Enter the grade: "))

if studentData["course"] in valid_courses:
     if studentData["grade"] in hs_grades:
          if (studentData["course"] == 'robotics') and studentData["grade"] == 9:
               print(f"{studentData['name']} is ineligible for {studentData['course']}")
          else:
                print(f"{studentData['name']} is approved for {studentData['course']}")
     elif studentData["grade"] < 9:
          print("Grade is too low")
     elif studentData["grade"] > 12:
          print("Grade is too high")

else:
     print(f"{studentData['name']} selected an invalid course!")