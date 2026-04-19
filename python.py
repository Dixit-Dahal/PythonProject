age = 50

print(id(age))

EmptyDict = {}    # Empty Dictionary

EmptySet = {*()} # Empty Set

EmptyTuple = tuple()    # Empty Tuple
EmptyTuple2 = ()

print("Dixit\tRabeen")

# String Methods

student_results = ['A+','B+','A+']
print(len(student_results))             # Used to get the length of all items
print(student_results.count('A+'))      # Used to get the count of specific item/items

print('ram'.maketrans('r', 'R'))        # maketrans() method is used to transform a character within a string

num1 = 30
num2 = 40

print('The total sum of {0} and {1} is {result}'.format(num1, num2, result = num1+num2))
print(F'The total sum of {num1} and {num2} is {num1+num2}')