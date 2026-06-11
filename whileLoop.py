# i = 0
# while i < 5:
#     print(i)
#     i += 1

# i = 0
# while i in range(5):
#     print(i)
#     i += 1

# i = 0
# while True:
#     if i == 5:
#         break
#     print(i)
#     i += 1  


# password = 'password'
# while True:
#     u_password = input("Enter your password:")
#     if u_password == password:
#         print("Access Granted")
#         break

# while (password := input("Enter your password:")) != "password":    # Walrus operator allows us to assign a value to a variable in the same line as the condition
#     print("Access Denied")

# # 1

# total = 0
# while (num := int(input("Enter a positive number:"))) > 0:
#     total = total + num

# print(total) 

# # 2

# n = int(input("Enter a positive integer: "))

# while n != 1:
#     print(n)
#     n -= 1

# else:
#     print("Lower Threshold Reached")

# # Class Question

# lst = [1,2,3,4,5]

# odd = []
# even = []
# i = 0

# while i in range(len(lst)):
#     if lst[i] % 2 != 0:
#         odd.append(lst[i])
#     else:
#         even.append(lst[i])
#     i += 1

# print(odd)
# print(even) 

# # 3

# import random

# num = random.randint(1, 100)

# attempt = 1

# while True:
#     guess = int(input("Guess the number between 1 and 100: "))
#     if guess > num:
#         print("Too High!")
#         attempt += 1
    
#     elif guess < num:
#         print("Too Low!")
#         attempt += 1
    
#     else:
#         print("You found the number in attempt no. ", attempt)
#         break

# # 4

while (password := input("Enter your password: ")).len() <= 8:
    print("Password must be 8+ characters")

