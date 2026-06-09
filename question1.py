# # 1.

# user = ['ram', 'hari']
# print('1. Add user')
# print('2. View user')
# print('3. Modify user')
# print('4. Delete user')
# print('5. Exit')
# for i in range(4):
#     u_input = int(input("Enter a number according to your requirement: "))

#     if u_input == 1:
#         user_name = input("Enter the name of the new user: ").lower
#         user.append(user_name)
#         print(f'{user_name} has been successfully added!')

#     elif u_input == 2:
#         index_num = input("enter the index number to view the data: ")

#         if index_num >= 0 and index_num < len(user):
#             for i,j in enumerate(user):
#                 print(i, ' ', j)
        
#         else:
#             print('Invalid index number!')


#     elif u_input == 3:
#         index_num = int(input("Enter the index number to modify user data: "))

#         if index_num >= 0 and index_num < len(user):
#             user[index_num] = input("Enter the modified name of the user: ")
#             print(f'{user[index_num]} has been successfully modified!')
        
#         else:
#             print("Invalid index number!")
    
#     elif u_input == 4:
#         index_num = int(input("Enter the index number to delete user data: "))

#         if index_num >= 0 and index_num < len(user):
#             user.pop(index_num)

#             print("Successfully deleted the user!")

#         else:
#             print("Invalid index number!")

#     elif u_input == 5:
#         break


# # 4.

sampleLists = [['Black', 'Red', 'Maroon', 'Yellow'], ['#000000', '#FF0000', '#800000', '#FFFF00']]

output = []

for i in zip(sampleLists[0], sampleLists[1]):       # Combines multiple lists together as a tuple and skips those for those without a pair
    output.append({'color_name': i[0], 'color_code': i[1]})

print(output)