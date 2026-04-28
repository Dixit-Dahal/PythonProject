fullName = 'Laxman Kunwar'
age = 29
Class = "10th"
College = 'Softwarica College'
bloodGroup = 'O+'

print('STUDENT ID CARD'.center(20))
print(f'FullName{' ' * 5}: {fullName}')
print(f'Age{' ' * 10}: {age}')
print(f'Class{' ' * 8}: {Class}')
print(f'College{' ' * 6}: {College}')
print(f'Blood Group{' ' * 2}: {bloodGroup}')

# print(fullName.center(10, ' ')) # can't leave empty string '', but can use ' '