# lst = [1,2,3,4,5]
# odd = []
# even = []

# for i in lst:
#     if i % 2 != 0:
#         odd.append(i)       # Using append instead of extend because extend only allows iterable parameters

#     else:
#         even.append(i)


# print(odd)
# print(even)

# items = ['apple', 'orange','grapes', 'milk']

# for i in items:
#     if (i.startswith('a') or i.startswith('g')):
#         print(i)


# sample = [1,2,3,4,'apple','orange',2+3j, 11.2, 45.3]
# integer = []
# string = []
# floatNum = []
# compNum = []

# for i in sample:
#     if type(i) == int:
#         integer.append(i)
    
#     elif type(i) == str:
#         string.append(i)
    
#     elif type(i) == complex:
#         compNum.append(i)

#     elif type(i) == float:
#         floatNum.append(i)

# print(f'{integer}\n{string}\n{floatNum}\n{compNum}')


# cart = {'apple':(2,210), 'orange':(3,145), 'banana':(4,335)}
# total = 0
# print(f"items\tquantity\tper Quantity price\t total price")

# for i, j in cart.items():
#     print(f"{i}\t {j[0]}\t\t  {j[1]}\t\t\t  {j[0]*j[1]}")
#     total += j[0] * j[1]

# print(f"Total Cost = {total}")

# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f'{num} * {i} = {num*i}')

# for i in range(1,4):
#     for j in range(i):
#         print(i, sep = '')


# get() method returns None type as a default value if the given condition is true.

# dictionary = {}
# items = ['milk','mango','milk']

# for i in items:
#     count = items.count(i)
#     if count > 1:
#         dictionary[i] = f'{count}'
#     elif count == 1:
#         dictionary[i] = f'{count}'

# print(dictionary)

# number = [2,3,4,5,6,7,8]

# for i in number:
#     if i == 2 or i == 7:
#         print(f'\nFor {i}')
#         for j in range(1,11):
#             print(f'{i} * {j} = {j * i}')



for row in range(6):
    for column in range(58):
        if column == 0 or column == 7 or column == 30 or column == 41 or column == 44 or column == 53:
            print('*', end=' ')
        
        elif (column == 35 or column == 39 or column == 47 or column == 51) and row != 0:
            print('*', end=' ')

        elif (column == 1 or column == 2 or column == 31 or column == 32) and (row == 0 or row == 5):
            print('*', end=' ')
        
        elif (column == 3 or column == 20 or column == 26 or column == 33)  and (row != 0 and row != 5):
            print('*', end=' ')

        elif (column == 5 or column == 6 or column == 8 or column == 9 or column == 11 or column == 16 or column == 18 or column == 19 or column == 20 or column == 21 or column == 22 or column == 26) and (row == 0 or row == 5):
            print('*', end=' ')
        
        elif (column == 12 or column == 15) and (row == 1 or row == 4):
            print('*', end=' ')

        elif (column == 13 or column == 14) and (row == 2 or row == 3):
            print('*', end=' ')
        
        elif (column == 36 or column == 37 or column == 38 or column == 48 or column == 49 or column == 50) and (row == 0 or row == 3):
            print('*', end=' ')
        
        elif (column == 24 or column == 25 or column == 27 or column == 28) and (row == 0):
            print('*', end=' ')

        elif (column == 42 or column == 43) and row == 2:
            print('*', end = ' ')

        elif (column == 54 or column == 55 or column == 56) and row == 5:
            print('*', end = ' ')
        else:
            print(end='  ')
    print()